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

# SEQN - Respondent sequence number
# PAQ605 - Vigorous work activity
# PAQ610 - Number of days vigorous work
# PAD615 - Minutes vigorous-intensity work
# PAQ620 - Moderate work activity
# PAQ625 - Number of days moderate work
# PAD630 - Minutes moderate-intensity work
# PAQ635 - Walk or bicycle
# PAQ640 - Number of days walk or bicycle
# PAD645 - Minutes walk/bicycle for transportation
# PAQ650 - Vigorous recreational activities
# PAQ655 - Days vigorous recreational activities
# PAD660 - Minutes vigorous recreational activities
# PAQ665 - Moderate recreational activities
# PAQ670 - Days moderate recreational activities
# PAD675 - Minutes moderate recreational activities
# PAD680 - Minutes sedentary activity

def make_key(row):
    year = str(row['year'])
    key = str(row['ID'])

    key_made = year +'_'+key

    return key_made


dataframes = []


for y in years:
    processed_path = f'../data/{y}'
    for filename in os.listdir(processed_path):
        if filename == 'physical_activity.csv': 

            df = pd.read_csv(f'{processed_path}/physical_activity.csv')

            df = df.rename(columns={
        'SEQN':'ID',
        'PAQ605': 'vigorous_work',
        'PAQ610': 'days_vigorous_work',
        'PAD615': 'minutes_work',
        'PAQ620': 'moderate_work',
        'PAQ625': 'days_moderate_work',
        'PAD630': 'minutes_moderate_work',
        'PAQ635': 'walk_bike',
        'PAQ640': 'days_walk_bike',
        'PAQ650': 'vigorous_rec',
        'PAQ655': 'days_vigorous_rec',
        'PAD660': 'minutes_vigorous_rec',
        'PAQ665': 'moderate_rec',
        'PAQ670': 'days_moderate_rec',
        'PAD675': 'minutes_moderate_rec',
        'PAD680': 'minutes_sedentary'
            })





            df['year'] = y
            df['year_id'] = df.apply(make_key, axis=1)



            dataframes.append(df)

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
        'vigorous_work',
        'days_vigorous_work',
        'minutes_work',
        'moderate_work',
        'days_moderate_work',
        'minutes_moderate_work',
        'walk_bike',
        'days_walk_bike',
        'vigorous_rec',
        'days_vigorous_rec',
        'minutes_vigorous_rec',
        'moderate_rec',
        'days_moderate_rec',
        'minutes_moderate_rec',
        'minutes_sedentary',
        'year'

]]

print(df.head())

df.to_csv('../data/cleaned_files/physical.csv')
# print(df.head())