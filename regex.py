# Import all packages
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
result = pattern.match('123-456-8490')
print(bool(result))

# Create regex practice expression and match attempts
pattern2 = re.compile('^\$\d*\.\d{2}$')
result2 = pattern2.match('$24.41')
print(bool(result2))