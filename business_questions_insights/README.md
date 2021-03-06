# Data Analysis 
### Business Questions.

_We want answers!_ 

**The company's business areas have some questions and challenges such as:**


- Can we give the same benefits to all shopkeepers (sellers)? Or is there one that deserves to be highlighted?


- Is there a difference in the amount of freight charged in different regions, cities? Or can we apply the shipping subsidy rules to any location?


- Is our product catalog comprehensive? Or does it focus on specific categories?



**Dashboard that analyzes the company's latest sales data that can be shared with Regional leads and their respective analysts:**

- Total Sales
- Sales per Region
- Top 5 selling categories for each Region

_delivered orders only_

## Results

### Dashboard
<p align="center">
    <img src="images/dashboard_1.PNG" width="850"/>
</p>

<br>

<p align="center">
    <img src="images/dashboard_2.PNG" width="850"/>
</p>

### Business Questions

- **Can we give the same benefits to all shopkeepers (sellers)? Or is there one that deserves to be highlighted?**

One form of evaluation is to give benefits based on productivity, using RFV (Recency, Frequency and Value) 
as main metrics.

So... Yes, **there are sellers who deserve to be highlighted:**

- **Super Productive:** High Value High Frequency! Top 10% of sales and frequency. 
- **Productive:** lots of sales, high revenue. 
- **High Value:** few sales, but great revenue values.
- **High Frequency:** low revenue value, but many sales.
- **Low Value Low Frequency:** low revenue value and few sales.

<p align="center">
    <img src="images/type_of_sellers.png" width="500"/>
</p>

[**Web App Visual Approach.**](https://share.streamlit.io/pauloreis-ds/olist_streamlit_rfv_seller_segmentation/main/main.py)
[Code.](https://github.com/pauloreis-ds/olist_streamlit_rfv_seller_segmentation)

<p align="center">
    <a href="https://share.streamlit.io/pauloreis-ds/olist_streamlit_rfv_seller_segmentation/main/main.py" target="_blank">
        <img src="images/question_2_streamlit.PNG" width="900"/>
    </a>
</p>

        ps: Inactive Sellers (sellers more than 10 months with no sales)
            New Sellers (sellers who have been in the database for a maximum of 2 months)

<br>

<br>

- **Is there a difference in the amount of freight charged in different regions, cities?<br> 
  Or can we apply the shipping subsidy rules to any location?**

Yes, there is a difference among cities and regions. Therefore, we must apply the shipping subsidy rules according to the location.

<p align="center">
    <img src="images/avg_freight_by_state.png" width="800"/>
</p>

<p align="center">
    <img src="images/avg_freight_by_region.png" width="800"/>
</p>

<br>

<br>

- **Is our product catalog comprehensive? Or does it focus on specific categories?**

Yes, it is, but there are a large number of purchases for some specific categories.

<p align="center">
    <img src="images/orders_by_category_2018.png" width="800"/>
</p>


[<img align="right" width="60" height="60" src="https://github.com/pauloreis-ds/Paulo-Reis-Data-Science/blob/master/Paulo%20Reis/Pauloreis01.png">](https://github.com/pauloreis-ds)

---