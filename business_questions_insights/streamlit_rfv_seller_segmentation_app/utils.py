import os
import dotenv


def read_query(path):
    with open(f'{path}', 'r') as file:
        return file.read()


def set_dotenv():
    dotenv.load_dotenv(dotenv.find_dotenv(os.path.expanduser("-")))


def get_password():
    return os.getenv("POSTGRES_PASSWORD")


def map_month(month):
    months = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
              "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
    return months[month]


def classify_seller(value, frequency):
    if value <= .5 and frequency <= .5:
        seller_category = "LOW VALUE LOW FREQUENCY"
    elif value > .5 and frequency <= .5:
        seller_category = "HIGH VALUE"
    elif value <= .5 and frequency > .5:
        seller_category = "HIGH FREQUENCY"
    elif value > .9 and frequency > .9:
        seller_category = "SUPER PRODUCTIVE"
    else:
        seller_category = "PRODUCTIVE"

    return seller_category


def get_seller_status(months_since_enrollment, months_since_last_sale):
    if months_since_enrollment <= 2:
        status = "NEW SELLER"
    elif months_since_last_sale >= 10:
        status = "INACTIVE"
    else:
        status = "ACTIVE"

    return status
