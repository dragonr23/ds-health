import pandas as pd
import csv

c = pd.read_csv('./utilities/file_names.csv')

print(c.head())

d = c[['Code ', 'Name']]

print(d.head())

code = list(c.loc[:, 'Code '])
names = list(c.loc[:, 'Name'])

res = dict(zip(code, names)) 

print(res)