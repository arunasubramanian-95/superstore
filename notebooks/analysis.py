import pandas as pd
from notebooks.cleaning import get_clean_data

df = get_clean_data()

def region_report():
    region_report = df.groupby('Region')[['Sales', 'Profit']].sum().sort_values(by='Profit', ascending=False)
    return region_report
def category_report():
    category_report = df.groupby('Category')[['Sales', 'Profit']].sum().sort_values(by='Profit', ascending = False)
    return category_report
def sub_category_report():
    sub_category_report = df.groupby('Sub-Category')[['Sales', 'Profit']].sum().sort_values(by='Profit', ascending = True)
    return sub_category_report
def yearly_report():
    yearly_report = df.groupby('Order Year')[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending = False)
    return yearly_report

correlation = df[['Discount', 'Profit']].corr()
print(correlation)