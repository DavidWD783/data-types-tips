# Import all packages
# export PATH="/usr/local/opt/python/libexec/bin:"
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy.io 

# # Import dataset from url
# from urllib.request import urlretrieve
# url = ''
# urlretrieve(url, '-.csv')
# file = '-.csv'

# # Use BeautifulSoup to print html of dataset
# from bs4 import BeautifulSoup
# import requests
# r = requests.get(url)
# text = r.text
# soup = BeautifulSoup(text, "lxml")
# print(soup.prettify())

# # Create DataFrame
# df = pd.read_csv(file, sep = ',', dtype=None, low_memory = False)
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())

# Create regex practice expression and import re
import re
pattern = re.compile('^\d{3}-\d{3}-\d{4}$')

# Check pattern against examples
result = pattern.match('123-456-78490')
print(bool(result))