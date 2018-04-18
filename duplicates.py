# Import all packages
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy.io 

# Create DataFrame with duplicate data

dupes = {'name': ['Daniel', 'John', 'Jane', 'Daniel'],
		'sex': ['male', 'male', 'female', 'male'],
		'treat_a': ['-', 12, 24, '-'],
		'treat_b': [42, 31, 27, 42]}

df = pd.DataFrame(data=dupes)
print(df.head())

# Remove duplicate using .drop_duplicates() method

df = df.drop_duplicates()
print(df)

# Import tips dataset and practice missing data
# Import dataset from url
from urllib.request import urlretrieve
url = 'https://assets.datacamp.com/production/course_2023/datasets/tips.csv'

# Create DataFrame
df_tips = pd.read_csv(url, sep = ',', dtype=None, low_memory = False)
df_tips_sub = df_tips[:][0:5]
df_tips_sub['total_bill'][1] = np.nan
df_tips_sub['tip'][3] = np.nan
df_tips_sub['sex'][4] = np.nan
df_tips_sub['smoker'][4] = np.nan
df_tips_sub['time'][4] = np.nan
print(df_tips_sub.head())
# print(df_tips_sub.info())

# # Use .dropna() method to drop all ros with NaN
# df_tips_sub_drop = df_tips_sub.dropna()
# print(df_tips_sub_drop)

# Use .fillna() method to fill all missing values
df_tips_sub['tip'] = df_tips_sub['tip'].fillna(np.mean(df_tips_sub['tip']))
df_tips_sub['total_bill'] = df_tips_sub['total_bill'].fillna(np.mean(df_tips_sub['total_bill']))
df_tips_sub['sex'] = df_tips_sub['sex'].fillna('missing')
print(df_tips_sub)

# Write assert statement to check for missing data
assert df_tips_sub.day.notnull().all()









