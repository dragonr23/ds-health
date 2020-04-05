import os
import pandas as pd
import numpy as np
import xport



years = [
    '1999-2000',
    '2001-2002',
    '2003-2004',
    '2005-2006',
    '2007-2008',
    '2009-2010',
    '2011-2012',
    '2013-2014',
    '2015-2016',
    '2017-2018'

]

#TODO: Make it so a file is renamed properly


for y in years:
    processed_path = f'../data/{y}'
    for filename in os.listdir(processed_path):
        if filename.endswith(".XPT"): 
            print(filename[:-4])
            with open(f'{processed_path}/{filename}', 'rb') as f:
                df = xport.to_dataframe(f)
                print('df created')
                csv = df.to_csv(f'{processed_path}/{filename[:-4]}.csv', index=False)
                print(f'exported {filename} to csv')
                os.remove(f'{processed_path}/{filename}')
                print('xpt removed')
        else:
            print('try again becca')


