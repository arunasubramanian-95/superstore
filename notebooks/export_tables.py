import pandas as pd
from connection import get_connection

def export_tables():
    conn = get_connection()

    tables = ['customers', 'shipping', 'products', 'locations', 'orders']

    for table in tables:
        df = pd.read_sql(f"SELECT * FROM {table}", conn)
        df.to_csv(f'../data/cleaned_dataset_tables/{table}.csv', index=False)
        print(f"{table}.csv exported successfully")

    conn.close()

if __name__ == '__main__':
    export_tables()