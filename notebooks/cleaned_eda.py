import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from cleaning import get_clean_data

df = get_clean_data()

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

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Basic statistics
print("\nBasic Statistics:")
print(df.describe())

