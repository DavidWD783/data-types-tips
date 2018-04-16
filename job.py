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
print(df.tail())
print(df.info())
print(df.describe())

# Check Initial Cost and Total Est Fee 
import re
from numpy import NaN
pattern = re.compile('\$\d*\.\d{2}')

def pattern_checker(df, key) :
	for key, value in df:
		if bool(pattern.match(value)):
			value = value.replace('$', '')
			df[key] = value
		else: 
			raise ValueError('Getting a non matching value')

	return df

pattern_checker(df, 'Initial Cost')
print(df['Initial Cost'].head())





