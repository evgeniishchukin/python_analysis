import numpy as np
import pandas as pd
import datetime
from assets.wb_request import wb_request as wb_request
from assets.df_empty import df_empty as df_empty
from assets.list_show import list_show as list_show
from assets.xlsx_parse import xlsx_parse as xlsx_parse
from assets.df_show import df_show as df_show

df = xlsx_parse.df_create(
                          'data/WDIW.xlsx', 0,
                          'Cool Name', 'Bumblebee',
                          'Country Name', 'World')

full_empty_columns = df_empty.search(df)
partially_empty_columns = df_empty.search(df, 3)
country_codes = df['Country Code'].tolist()
list_show.show(full_empty_columns)
list_show.show(partially_empty_columns)
list_show.show(country_codes)

#
#
#
# print('\n\nDelete empty columns from new DF')
# df = df.drop(columns_empty, axis=1)
# print(df)
#
# print('\n\nMake a list of all column names, check wich is ANY empty and not and amount of empty values')
# any_empty_df = df.isnull().sum()
# print(any_empty_df)
#
# print('\n\nMake a list of all columns that have more than 3 empty values')
# columns_empty = df.columns[any_empty_df > 3].tolist()
# showing_list(columns_empty)
#
# print('\n\nDelete empty columns and useles columns from new DF')
# df = df.drop(columns_empty, axis=1)
# df = df.drop(['Cool Name', 'Counter', 'Hult Region', 'Country Code'], axis=1)
# print(df)
#
# print('\n\nFill empty values by 0')
# df_0 = df.fillna(0)
# print(df_0)
#
# print('\n\nDescribe the data')
# print(df_0.describe())
#
# print('\n\nFill empty values by mean')
# df_mean = df.fillna(df.mean())
# print(df_mean)
#
# print('\n\nDescribe the data')
# print(df_mean.describe())
#
# print('\n\nSaving to Excel')
# df.to_excel(r'data\DF.xlsx')
# df_mean.to_excel(r'data\DF_mean.xlsx')
# df_0.to_excel(r'data\DF_0.xlsx')


# def showing_list(list_to_show):
#     for i, name in enumerate(list_to_show):
#         print(f'#{i+1}: {name}')
