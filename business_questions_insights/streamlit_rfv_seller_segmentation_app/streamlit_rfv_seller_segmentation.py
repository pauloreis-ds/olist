import streamlit as st
import pandas as pd
from datetime import date
from utils import *
from database import PostegreSQL
from functools import reduce
import graph

class SellerSegmentationPipeline:
    def __init__(self, data_frame):
        self.sellers_sales_df = data_frame
        self.sellers_sgmt_abt = None

    def create_sellers_sgmt_abt(self, analysis_date):
        # Value*
        total_revenue = self.sellers_sales_df.groupby("seller_id")["price"].sum()
        total_revenue.name = "total_revenue"

        # sales_quantity "False Frequency"
        orders_quantity = self.sellers_sales_df.groupby("seller_id")["order_id"].count()
        orders_quantity.name = "orders_quantity"

        distinct_products_sold = self.sellers_sales_df.groupby("seller_id")["order_id"].nunique()
        distinct_products_sold.name = "distinct_products_sold"

        # Recency*
        days_since_last_sale = pd.to_datetime(
            self.sellers_sales_df.groupby("seller_id")["order_approved_at"].max()).dt.date.apply(lambda x: analysis_date - x)
        days_since_last_sale.name = "days_since_last_sale"

        # days in the database "Enrollment"
        days_since_first_sale = pd.to_datetime(
            self.sellers_sales_df.groupby("seller_id")["order_approved_at"].min()).dt.date.apply(lambda x: analysis_date - x)
        days_since_first_sale.name = "days_since_first_sale"

        dfs = [total_revenue, orders_quantity, distinct_products_sold, days_since_last_sale, days_since_first_sale]
        self.sellers_sgmt_abt = reduce(lambda left, right: pd.merge(left, right, on='seller_id'), dfs)

        self.sellers_sgmt_abt['months_since_last_sale'] = days_since_last_sale.dt.days / 30
        self.sellers_sgmt_abt['months_since_first_sale'] = days_since_first_sale.dt.days / 30

        self.sellers_sgmt_abt['orders_per_month'] = self.sellers_sgmt_abt['orders_quantity'] / \
                                                    self.sellers_sgmt_abt['months_since_first_sale']
        self.sellers_sgmt_abt['revenue_per_month'] = self.sellers_sgmt_abt['total_revenue'] / \
                                                     self.sellers_sgmt_abt['months_since_first_sale']

        self.sellers_sgmt_abt['value_rank'] = self.sellers_sgmt_abt['revenue_per_month'].rank(pct=True)
        self.sellers_sgmt_abt['frequency_rank'] = self.sellers_sgmt_abt['orders_per_month'].rank(pct=True)

        return self

    def classify_sellers(self):
        self.sellers_sgmt_abt['value_frequency_segment'] = self.sellers_sgmt_abt. \
            apply(lambda df: classify_seller(df['value_rank'], df['frequency_rank']), axis=1)

        self.sellers_sgmt_abt['seller_status'] = self.sellers_sgmt_abt. \
            apply(lambda df: get_seller_status(df['months_since_first_sale'], df['months_since_last_sale']), axis=1)

        return self


# streamlit run business_questions_insights\streamlit_rfv_seller_segmentation_app\streamlit_rfv_seller_segmentation.py
if __name__ == "__main__":
    img = 'https://raw.githubusercontent.com/pauloreis-ds/Paulo-Reis-Data-Science/master/Paulo%20Reis/PRojects.png'
    st.set_page_config(page_title='Seller RFV Segmentation', page_icon=img)

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    QUERIES_DIR = os.path.join(os.path.join(BASE_DIR, 'business_questions_insights'), 'sql_queries')

    set_dotenv()
    db = PostegreSQL(password=get_password())

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    st.sidebar.title("Analysis Time Frame")
    st.sidebar.write("From:")
    initial_month = st.sidebar.selectbox('Month', months)
    inital_year = st.sidebar.selectbox('Year', [2018, 2017, 2016])
    st.sidebar.write("To:")
    final_month = st.sidebar.selectbox('Month ', months)
    final_year = st.sidebar.selectbox('Year ', [2019, 2018, 2017, 2016])

    initial_date = date(inital_year, map_month(initial_month), 1)   
    final_date = date(final_year, map_month(final_month), 1)     

    # check_date_range()
    # if initial_date > final_date or initial_date == final_date:
    #     st.error(f"Invalid Date Range From {initial_date} To {final_date}")

    approved_orders_only = st.checkbox("Include only Approved Orders", help='also includes delivered ones')
    if approved_orders_only:
        order_status_q = "AND order_status in ('approved', 'delivered', 'shipped', 'invoiced')"
    else:
        order_status_q = ""

    time_frame = f'''\nWHERE order_purchase_timestamp BETWEEN DATE('{initial_date}') AND DATE('{final_date}')
                             {order_status_q}'''
    sellers_pre_abt_query = read_query(os.path.join(QUERIES_DIR, "sellers_segment_pre_abt.sql")) + time_frame

    cols = ['order_id', 'order_approved_at', 'purchase_date', 'price', 'seller_id']
    sellers_sales_df = pd.DataFrame(db.execute(sellers_pre_abt_query), columns=cols).dropna()

    seller_abt_pipeline = SellerSegmentationPipeline(sellers_sales_df)

    seller_abt_pipeline.create_sellers_sgmt_abt(analysis_date=final_date).classify_sellers()
    sellers_sgmt_abt = seller_abt_pipeline.sellers_sgmt_abt

    seller_status_df = pd.concat([sellers_sgmt_abt['seller_status'].value_counts(),
                                  sellers_sgmt_abt['seller_status'].value_counts(normalize=True)],
                                 axis=1)
    seller_status_df.columns = ["quantity_of_sellers", "percentage"]
    st.write(seller_status_df)

    seller_rank_df = pd.concat([sellers_sgmt_abt['value_frequency_segment'].value_counts(),
                                sellers_sgmt_abt['value_frequency_segment'].value_counts(normalize=True)],
                               axis=1)

    seller_rank_df.columns = ["quantity_of_sellers", "percentage"]
    st.write(seller_rank_df)

    cmap = {
        'ACTIVE': "#1f77b4",
        'NEW SELLER': "#2ca02c",
        'INACTIVE': "#c1c0b9"
    }
    st.pyplot(graph.scatter(sellers_sgmt_abt['frequency_rank'], sellers_sgmt_abt['value_rank'],
                            c=sellers_sgmt_abt['seller_status'].map(cmap), s=5, l=sellers_sgmt_abt['seller_status'],
                            x_label="Frequency Rank", y_label="Value Rank", title="RFM Seller Segmentation"))

    cmap_ = {
        'HIGH VALUE': "#2ca02c",
        'SUPER PRODUCTIVE': "#ff7f0e",
        'PRODUCTIVE': "#1f77b4",
        'LOW VALUE LOW FREQUENCY': "#d62728",
        'HIGH FREQUENCY': "#9467bd"
    }

    st.pyplot(graph.scatter(sellers_sgmt_abt['frequency_rank'], sellers_sgmt_abt['value_rank'],
                            c=sellers_sgmt_abt['value_frequency_segment'].map(cmap_), s=5,
                            l=sellers_sgmt_abt['seller_status'],
                            x_label="Frequency Rank", y_label="Value Rank", title="RFM Seller Segmentation"))

# streamlit run business_questions_insights\streamlit_rfv_seller_segmentation_app\streamlit_rfv_seller_segmentation.py
