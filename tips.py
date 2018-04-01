# Import all packages
# export PATH="/usr/local/opt/python/libexec/bin:$PATH"
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy.io 

# Import dataset from url
from urllib.request import urlretrieve
url = 'https://assets.datacamp.com/production/course_2023/datasets/tips.csv'
urlretrieve(url, 'dob_job_application_filings_subset.csv')
file = 'dob_job_application_filings_subset.csv'
# # Use BeautifulSoup to print html of datacamp dataset
# from bs4 import BeautifulSoup
# import requests
# r = requests.get(url)
# text = r.text
# soup = BeautifulSoup(text, "lxml")
# print(soup.prettify())

# Create DataFrame
df = pd.read_csv(file, sep = ',', dtype=None, low_memory = False)
print(df.head())
print(df.tail())
print(df.info())
print(df['sex'].describe())

# Change datatype of sex to category for categorical variable
df['sex'] = df['sex'].astype('category')
print(df['sex'].describe())