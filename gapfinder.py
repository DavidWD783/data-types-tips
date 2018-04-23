# Import all packages
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy.io 

# Import dataset from url
from urllib.request import urlretrieve
url = 'https://assets.datacamp.com/production/course_2023/datasets/gapminder.csv'

# Create DataFrame
df = pd.read_csv(url, sep = ',', dtype=None, low_memory = False)
# df = df.drop('Unnamed: 0')
df = df.set_index('Life expectancy')
print(df.head())
# print(df.describe())
# print(df.columns)

# Create plot of 1800 vs. 1899 columns
df.plot(kind='scatter', x='1800', y='1899')

# Set the x and y axis limits
plt.xlim(20, 80)
plt.ylim(20, 80)

# Label the axes
plt.xlabel('Life expectancy 1800')
plt.ylabel('Life expectancy 1899')

# Plot scatter plot
# plt.show()

# # Create function to check null or valid for df
# def check_null_or_valid(row_data):
#     """Function that takes a row of data,
#     drops all missing values,
#     and checks if all remaining values are greater than or equal to 0
#     """
#     no_na = row_data.dropna()[1:-1]
#     numeric = pd.to_numeric(no_na)
#     ge0 = numeric >= 0
#     return ge0

# # Check whether the first column is 'Life expectancy'
# assert df.columns[0] == 'Life expectancy'

# # Check whether the values in the row are valid
# assert df.iloc[:, 1:].apply(check_null_or_valid, axis=1).all().all()

# # Check that there is only one instance of each country
# assert df['Life expectancy'].value_counts()[0] == 1

# Melt columns
df_melt = pd.melt(df, id_vars=['Life expectancy'], value_vars = ['1800', '1900'])
print(df_melt.head())
print(df_melt.tail())




