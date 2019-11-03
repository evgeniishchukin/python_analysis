import numpy as np
import pandas as pd
import wbdata
import datetime

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.reset_option('max_colwidth')


def showing_list(list_to_show):
    for i, name in enumerate(list_to_show):
        print(f'#{i+1}: {name}')


def show_all_rows(df):
    pd.set_option('display.max_rows', None)
    print(df)


print('\nCreating data frame from the Excel File')
xlsx = pd.ExcelFile('data/WDIW.xlsx')

print('\n\nGet list of all sheet list')
sheet_names = xlsx.sheet_names
showing_list(sheet_names)

print('\n\nParse an dataframe with needed sheet names, needed data')
df = xlsx.parse(sheet_names[0])
df = df.loc[df['Cool Name'] == 'Bumblebee']
print(df)

print('\n\nMake a list of all column names, check wich is empty and not')
emptynes_df = df.isnull().all()
show_all_rows(emptynes_df)

print('\n\nMake a list of all column names, check wich is empty and not')
emptynes_df = df.isnull().all()
print(emptynes_df)

print('\n\nMake a list of all empty columns and show them')
columns_empty = df.columns[emptynes_df].tolist()
showing_list(columns_empty)

print('\n\nMake a list of codes of given country codes')
country_codes = df['Country Code'].tolist()
showing_list(country_codes)

print('\n\nMake a list of all indicators that we need to fill')
indicators = []
indicators_dict = {}
for column in columns_empty:
    searched_indicator = wbdata.search_indicators(column)[0]['id']
    indicators.append(searched_indicator)
    indicators_dict[searched_indicator] = column
showing_list(indicators)

print('\n\nGet data for each country')
data_date = (datetime.datetime(2017, 1, 1), datetime.datetime(2017, 12, 31))
newDF = wbdata.get_dataframe(indicators_dict, country=country_codes, data_date=data_date)
print(newDF)


print('\n\nMake a list of all column names, check wich is empty and not')
newDF_empty = newDF.isnull().all()
show_all_rows(newDF_empty)

print('\n\nMake a list of all empty columns')
newDF_columns_empty = newDF.columns[newDF_empty].tolist()
showing_list(newDF_columns_empty)
