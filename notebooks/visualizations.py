import matplotlib.pyplot as plt
import seaborn as sns
from cleaning import get_clean_data
from analysis import region_report, category_report, sub_category_report, yearly_report

region_data = region_report()
sns.set_style('whitegrid')
region_data.plot(kind='bar', figsize=(10,6), color=['#2196F3','#4CAF50'])
plt.title('Sales and Profit by Region', fontsize=16)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Amount ($)', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

category_data = category_report()
sns.set_style('whitegrid')
category_data.plot(kind='bar', figsize=(10,6), color=['#2196F3','#4CAF50'])
plt.title('Sales and Profit by Product Category', fontsize=16)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Amount ($)', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

sub_category_data = sub_category_report()
sns.set_style('whitegrid')
sub_category_data.plot(kind='barh', figsize=(10,6), color=['#2196F3','#4CAF50'])
plt.title('Sales and Profit by Product Sub-Category (Loss vs Profit)', fontsize=16)
plt.axvline(x=0, color='red', linestyle='--')
plt.xlabel('Sub-Category', fontsize=12)
plt.ylabel('Amount ($)', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()