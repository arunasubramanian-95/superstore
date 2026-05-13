import pandas as pd
from connection import get_connection
from cleaning import get_clean_data

def insert_data():
    conn = get_connection()
    cursor = conn.cursor()
    df = get_clean_data()

    try:
        customers = df[['customer_id', 'customer_name', 'segment']].drop_duplicates()
        for _, row in customers.iterrows():
            cursor.execute("""
                INSERT INTO customers(customer_id, customer_name, segment)
                VALUES(%s,%s,%s)
                ON CONFLICT (customer_id) DO NOTHING
            """, (row['customer_id'], row['customer_name'], row['segment']))

        shipping = df[['ship_mode']].drop_duplicates()
        for _, row in shipping.iterrows():
            cursor.execute("""
                INSERT INTO shipping(ship_mode)
                VALUES(%s)
                ON CONFLICT DO NOTHING
            """, (row['ship_mode'],))

        products = df[['product_id', 'product_name', 'category', 'sub_category']].drop_duplicates()
        for _, row in products.iterrows():
            cursor.execute("""
                INSERT INTO products(product_id, product_name, category, sub_category)
                VALUES(%s, %s, %s, %s)
                ON CONFLICT(product_id) DO NOTHING
            """, (row['product_id'], row['product_name'], row['category'], row['sub_category']))

        locations = df[['postal_code', 'city', 'state', 'country', 'region']]
        for _, row in locations.iterrows():
            cursor.execute("""
                INSERT INTO locations(postal_code, city, state, country, region)
                VALUES(%s, %s, %s, %s, %s)
                ON CONFLICT DO NOTHING
            """, (row['postal_code'], row['city'], row['state'], row['country'], row['region']))

        # Get shipping mapping
        cursor.execute("SELECT ship_mode, shipping_id FROM shipping")
        shipping_map = {row[0]: row[1] for row in cursor.fetchall()}

        # Get location mapping
        cursor.execute("SELECT postal_code, location_id FROM locations")
        location_map = {row[0]: row[1] for row in cursor.fetchall()}

        cursor.execute("SELECT postal_code, location_id FROM locations")
        location_map = {row[0]: row[1] for row in cursor.fetchall()}

        orders = df[['order_id', 'customer_id', 'product_id', 'postal_code', 'order_date', 'ship_date', 'ship_mode', 'sales', 'quantity', 'discount', 'profit']].drop_duplicates()
        for _, row in orders.iterrows():
            cursor.execute("""
                INSERT INTO orders(order_id, customer_id, product_id, location_id, order_date, ship_date, shipping_id, sales, quantity, discount, profit)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT DO NOTHING
            """, (row['order_id'], row['customer_id'], row['product_id'], location_map[str(row['postal_code'])], row['order_date'], row['ship_date'], shipping_map[row['ship_mode']], row['sales'], row['quantity'], row['discount'], row['profit']))
        conn.commit()

    except Exception as e:
        print(f"Unable to complete data insertion: {e}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    insert_data()