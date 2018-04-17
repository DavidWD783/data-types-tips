# Import all packages
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy.io 

# Import dataset from url
from urllib.request import urlretrieve
url = 'https://assets.datacamp.com/production/course_2023/datasets/dob_job_application_filings_subset.csv'
# urlretrieve(url, '-.csv')
# file = '-.csv'

# # Use BeautifulSoup to print html of dataset
# from bs4 import BeautifulSoup
# import requests
# r = requests.get(url)
# text = r.text
# soup = BeautifulSoup(text, "lxml")
# print(soup.prettify())

# Create DataFrame
df = pd.read_csv(url, sep = ',', dtype=None, low_memory = False)
df = df[['Job #', 'Doc #', 'Borough', 'Initial Cost', 'Total Est. Fee']]
print(df.head())
# print(df.tail())
print(df.info())
# print(df.describe())

# Create sub DataFrame
df_sub = df[:][0:15]

# Check Initial Cost and Total Est Fee 
import re
from numpy import NaN
pattern = re.compile('\$\d*\.\d{2}')

def diff_checker(row, pattern):
	icost = row['Initial Cost']
	tef = row['Total Est. Fee']

	if bool(pattern.match(icost)) and bool(pattern.match(tef)):
		icost = float(icost.replace('$', ''))
		tef = float(tef.replace('$', ''))
		return icost - tef
	else:
		return (NaN)

df_sub['diff'] = df_sub.apply(diff_checker, axis=1, pattern=pattern)
print(df_sub.head())









