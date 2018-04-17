# Import all packages
# export PATH="/usr/local/opt/python/libexec/bin:$PATH"
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy.io 

# Import dataset from url
from urllib.request import urlretrieve
url = 'https://assets.datacamp.com/production/course_2023/datasets/tips.csv'
# urlretrieve(url, 'dob_job_application_filings_subset.csv')
# file = 'dob_job_application_filings_subset.csv'
# # Use BeautifulSoup to print html of datacamp dataset
# from bs4 import BeautifulSoup
# import requests
# r = requests.get(url)
# text = r.text
# soup = BeautifulSoup(text, "lxml")
# print(soup.prettify())

# Create DataFrame
df = pd.read_csv(url, sep = ',', dtype=None, low_memory = False)
print(df.head())
print(df.tail())
print(df.info())
print(df['sex'].describe())

# Change datatype of sex to category for categorical variable
df['sex'] = df['sex'].astype('category')
print(df.head())
print(df.info())


# Your job is to write a function that will recode 
# 'Male' to 1, 'Female' to 0, and return np.nan for 
# all entries of 'sex' that are neither 'Male' nor 'Female'



def recode_resend(sex_value):
	""" Recodes Male to 1 and Female to 0, NaN for neither """
	if sex_value == 'Male':
		return 1
	elif sex_value == 'Female':
		return 0
	else:
		return np.nan


df['sex_recode'] = df['sex'].apply(recode_resend)
print(df.head())


















