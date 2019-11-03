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

def show_all_columns(df):
    pd.set_option('display.max_columns', None)
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

print('\n\nMake a list of all column names, check wich is ALL empty and not')
emptynes_df = df.isnull().all()
print(emptynes_df)

print('\n\nMake a list of all empty columns and show them')
columns_empty = df.columns[emptynes_df].tolist()
showing_list(columns_empty)

print('\n\nMake a list of codes of given country codes')
country_codes = df['Country Code'].tolist()
showing_list(country_codes)

# print('\n\nMake a list of all indicators that we need to fill')
# indicators = []
# indicators_dict = {}
# for column in columns_empty:
#     searched_indicator = wbdata.search_indicators(column)[0]['id']
#     indicators.append(searched_indicator)
#     indicators_dict[searched_indicator] = column
# showing_list(indicators)
#
# print('\n\nGet data for each country')
# data_date = (datetime.datetime(2017, 1, 1), datetime.datetime(2017, 12, 31))
# newDF = wbdata.get_dataframe(indicators_dict, country=country_codes, data_date=data_date)
# print(newDF)
#
# print('\n\nMake a list of all column names, check wich is empty and not')
# newDF_empty = newDF.isnull().all()
# show_all_rows(newDF_empty)
#
# print('\n\nMake a list of all empty columns')
# newDF_columns_empty = newDF.columns[newDF_empty].tolist()
# showing_list(newDF_columns_empty)
#
# print('\n\nDelete empty columns from new DF')
# newDF = newDF.drop(newDF_columns_empty, axis=1)
# print(newDF)

print('\n\nDelete empty columns from new DF')
df = df.drop(columns_empty, axis=1)
print(df)

print('\n\nMake a list of all column names, check wich is ANY empty and not and amount of empty values')
any_empty_df = df.isnull().sum()
print(any_empty_df)

print('\n\nMake a list of all columns that have more than 3 empty values')
columns_empty = df.columns[any_empty_df > 3].tolist()
showing_list(columns_empty)

print('\n\nDelete empty columns and useles columns from new DF')
df = df.drop(columns_empty, axis=1)
df = df.drop(['Cool Name', 'Counter', 'Hult Region', 'Country Code'], axis=1)
print(df)

print('\n\nFill empty values by 0')
df_0 = df.fillna(0)
print(df_0)

print('\n\nDescribe the data')
print(df_0.describe())

print('\n\nFill empty values by mean')
df_mean = df.fillna(df.mean())
print(df_mean)

print('\n\nDescribe the data')
print(df_mean.describe())

print('\n\nSaving to Excel')
df.to_excel(r'data\DF.xlsx')
df_mean.to_excel(r'data\DF_mean.xlsx')
df_0.to_excel(r'data\DF_0.xlsx')
