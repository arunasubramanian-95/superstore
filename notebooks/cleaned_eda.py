import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_parquet('../data/superstore_cleaned.parquet')

# ---- BASIC EXPLORATION ----

# See first 5 rows
print("First 5 rows:")
print(df.head())

# See shape of data (rows, columns)
print("\nShape of dataset:")
print(df.shape)

# See all column names
print("\nColumn Names:")
print(df.columns.tolist())

# See data types of each column
print("\nData Types:")
print(df.dtypes)

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Basic statistics
print("\nBasic Statistics:")
print(df.describe())