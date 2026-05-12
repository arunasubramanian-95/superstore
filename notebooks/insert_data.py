import pandas as pd
from connection import get_connection
from cleaning import get_clean_data

def insert_data():
    conn = get_connection()
    cursor = conn.cursor()
    df = get_clean_data()

    try:
        customers = df[['customer_id',
                         'customer_name',
                         'segment']]

        for customer,row in customers.iterrows():
            cursor.execute("""
            INSERT INTO customers(customer_id, customer_name, segment)
            VALUES(%s,%s,%s)
            ON CONFLICT (customer_id) DO NOTHING"""),(customer_id, customer_name, segment, ))