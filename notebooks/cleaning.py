import pandas as pd

def get_clean_data():
    df = pd.read_csv('../data/superstore.csv', encoding='latin-1')

    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])

    df['Order Year'] = df['Order Date'].dt.year
    df['Order Month'] = df['Order Date'].dt.month
    df['Order Month Name'] = df['Order Date'].dt.strftime('%b')

    return df

if __name__ == '__main__':
    df = get_clean_data()
    df.to_parquet('../data/superstore_cleaned.parquet', index=False)
