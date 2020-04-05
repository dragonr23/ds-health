import os
import pandas as pd



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


# SEQN - Respondent sequence number
# SLQ300 - Usual sleep time on weekdays or workdays
# SLQ310 - Usual wake time on weekdays or workdays
# SLD012 - Sleep hours - weekdays or workdays
# SLQ320 - Usual sleep time on weekends
# SLQ330 - Usual wake time on weekends
# SLD013 - Sleep hours - weekends

def make_key(row):
    year = str(row['year'])
    key = str(row['ID'])

    key_made = year +'_'+key

    return key_made


dataframes = []


for y in years:
    processed_path = f'../data/{y}'
    for filename in os.listdir(processed_path):
        if filename == 'sleeping_disorders.csv': 

            df = pd.read_csv(f'{processed_path}/sleeping_disorders.csv')

            df = df.rename(columns={
                'SEQN': 'ID',
                'SLQ300': 'week_day_sleep_time',
                'SLQ310': 'week_day_wake_time',
                'SLD012': 'week_day_hours',
                'SLQ320':'weekend_sleep_time',
                'SLQ330':'weekend_wake_time',
                'SLD013': 'weekend_hours',
                'SLD010H': 'avg_hours'
            })

            df['year'] = y
            df['year_id'] = df.apply(make_key, axis=1)

            if 'avg_hours' not in df.columns:
                df['avg_hours'] = df[['week_day_hours']].mean(axis=1)

            dataframes.append(df)

            

            # need to add a year column

            #need to mush all of that dataframes together

            #need to join them correctly

            print(y)
            print(df.head())

print(dataframes)

df = dataframes[0]

print(len(df))
for d in range(1, len(dataframes)):
    print(dataframes[d].head())

    df = df.merge(dataframes[d], how='outer')




df = df[['year_id',
    'ID',
    'week_day_sleep_time',
    'week_day_wake_time',
    'week_day_hours',
    'weekend_sleep_time',
    'weekend_wake_time',
    'weekend_hours',
    'avg_hours',
    'years'

]]

df.to_csv('../data/cleaned_files/sleep.csv')
print(df.head())




        # with open(f'{processed_path}/{filename}', 'rb') as f:
        #     # code = filename[:-6]
        #     # if code in names:
        #     #     name = names[code]
        #         # print(name)
        #     os.rename(f'{processed_path}/{filename}', f'{processed_path}/{filename}.csv')
        #     print('file renamed')