import os
from utilities import name_dict
# I need to rename the current files but this will not be used for dataprocessing all of the time


names = name_dict.names

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
        # if filename.endswith(".csv"): 
            # print(filename[:-6])
        with open(f'{processed_path}/{filename}', 'rb') as f:
            # code = filename[:-6]
            # if code in names:
            #     name = names[code]
                # print(name)
            os.rename(f'{processed_path}/{filename}', f'{processed_path}/{filename}.csv')
            print('file renamed')



        # else:
        #     print('try again becca')


