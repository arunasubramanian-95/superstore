import psycopg2
from connection import get_connection

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers(
            customer_id VARCHAR(25) PRIMARY KEY,
            customer_name VARCHAR(100) NOT NULL,
            segment VARCHAR(15) NOT NULL
            )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS shipping(
            shipping_id SERIAL PRIMARY KEY,
            ship_mode VARCHAR(20)
            )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            product_id VARCHAR(25) NOT NULL PRIMARY KEY,
            product_name VARCHAR(100) NOT NULL,
            category VARCHAR(50) NOT NULL,
            sub_category VARCHAR(25) NOT NULL
            )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS locations(
            location_id SERIAL PRIMARY KEY,
            postal_code varchar(10),
            city VARCHAR(20),
            state VARCHAR(20),
            country VARCHAR(20),
            region VARCHAR(10)
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders(
        order_id VARCHAR(25),
        customer_id VARCHAR(25) REFERENCES customers(customer_id),
        product_id VARCHAR(25) REFERENCES products(product_id),
        location_id INT REFERENCES locations(location_id),
        order_date DATE,
        ship_date DATE,
        shipping_id INT REFERENCES shipping(shipping_id),
        sales NUMERIC(10,2) NOT NULL,
        quantity NUMERIC(10,2) NOT NULL,
        discount NUMERIC(10,2),
        profit NUMERIC(10,2) NOT NULL,
        PRIMARY KEY(order_id, product_id)
        )""")

    except Exception as e:
        conn.rollback()
        print(f"Tables creation failed. \n{e}")

    finally:
        conn.commit()
        cursor.close()
        conn.close()
        print("Tables Created successfully")

if __name__ == "__main__":
    setup_database()