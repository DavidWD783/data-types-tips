# Import all packages
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy.io 

# Create table using df of treatment dict
treatment = {'name': ['Daniel', 'John', 'Jane'],
 			'sex': ['male', 'male', 'female'],
 			'treat_a': ['18', 12, 24],
 			'treat_b': [42, 31, 27]}

treat_df = pd.DataFrame(data=treatment)
print(treat_df)

# Check the type of data in treat_df
# print(treat_df.dtypes)
treat_df['sex'] = treat_df['sex'].astype('category')
treat_df['treat_a'] = pd.to_numeric(treat_df['treat_a'], downcast = 'integer', errors='coerce')
treat_df.set_index('name')
# print(treat_df.dtypes)
# print(treat_df)

# Apply .apply method to df
new_treat_df = treat_df[['name', 'treat_a', 'treat_b']].set_index('name')
print(new_treat_df)
print(new_treat_df.apply(np.mean, axis=0)) # mean of col
print(new_treat_df.apply(np.mean, axis=1)) # mean of row