import pandas as pd

def get_clean_data(filepath: str = '../data/superstore.csv') -> pd.DataFrame:
    try:
        df = pd.read_csv(filepath, encoding='latin-1')
    except FileNotFoundError:
        print(f"Error: File not found at path - {filepath}")
        raise

    # Column Name Standardization
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_', regex=False).str.replace('-', '_', regex=False)

    #Date Conversion
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce')

    #Clean String Columns
    str_cols = df.select_dtypes(include='str').columns
    df[str_cols] = df[str_cols].apply(lambda x: x.str.strip())

    #Convert numeric columns
    num_cols = ['sales', 'profit', 'quantity', 'discount']
    df[num_cols] = df[num_cols].apply(pd.to_numeric, errors='coerce')

    # Basic validation checks
    if df['sales'].isna().any():
        raise ValueError("Sales contains missing values")

    if not df['quantity'].gt(0).all():
        raise ValueError("Quantity must be greater than 0")

    df = df.drop_duplicates()

    # Shipping duration in days
    df['shipping_days'] = (df['ship_date'] - df['order_date']).dt.days

    # Profit margin
    df['profit_margin'] = df['profit'] / df['sales'].replace(0, float('nan'))

    df['order_year'] = df['order_date'].dt.year
    df['order_month'] = df['order_date'].dt.month
    df['order_quarter'] = df['order_date'].dt.quarter

    return df

if __name__ == '__main__':
    df = get_clean_data()
    df.to_csv('../data/superstore_cleaned.csv', index=False)