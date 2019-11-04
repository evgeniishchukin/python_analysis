import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from assets.wb_request import wb_request as wb_request
from assets.df_empty import df_empty as df_empty
from assets.list_show import list_show as list_show
from assets.xlsx_parse import xlsx_parse as xlsx_parse
from assets.df_show import df_show as df_show

date_range = (datetime.datetime(2017, 1, 1), datetime.datetime(2017, 12, 31))
useless_data = ['Cool Name', 'Counter', 'Hult Region', 'Country Code']

df = xlsx_parse.df_create(
                          'data/WDIW.xlsx', 0,
                          'Cool Name', 'Bumblebee',
                          'Country Name', 'World')

full_empty_columns = df_empty.search(df)
partially_empty_columns = df_empty.search(df, 3)
country_codes = df['Country Code'].tolist()
df = df.drop(full_empty_columns
             + partially_empty_columns
             + useless_data, axis=1)
df = df.fillna(0)
print(df)
df.to_excel(r'data\DF.xlsx')
df = xlsx_parse.df_create('data/DF.xlsx', 0)
df.iloc[:, 1:].describe()

df.plot.bar(x='Country Name',
            y=[
                'Agriculture, forestry, and fishing, value added (% of GDP)',
                'Industry (including construction), value added (% of GDP)',
                'Services, value added (% of GDP)'
                ],
            stacked=True,
            rot=0)

df.plot.bar(x='Country Name',
            y=[
                'Population ages 0-14 (% of total population)',
                'Population ages 15-64 (% of total population)',
                'Population ages 65 and above (% of total population)'
                ],
            stacked=True,
            rot=0)

df.plot.bar(x='Country Name',
            y=[
                'Employment in agriculture (% of total employment) (modeled ILO estimate)',
                'Employment in industry (% of total employment) (modeled ILO estimate)',
                'Employment in services (% of total employment) (modeled ILO estimate)'
                ],
            stacked=True,
            rot=0)

df.plot.bar(x='Country Name',
            y=[
                'Rural population (% of total population)',
                'Urban population (% of total population)',
                ],
            colors=['r', 'b'],
            rot=0)

df.boxplot('Mobile cellular subscriptions (per 100 people)')
df.boxplot('Prevalence of HIV, total (% of population ages 15-49)')

corr = df.iloc[:, 1:].corr()
corr.style.background_gradient(cmap='coolwarm')

corr = df[[
    'Employment in agriculture (% of total employment) (modeled ILO estimate)',
    'Employment in industry (% of total employment) (modeled ILO estimate)',
    'Employment in services (% of total employment) (modeled ILO estimate)'
    ]].corr()
corr.style.background_gradient(cmap='coolwarm')

corr = df[[
    'Agriculture, forestry, and fishing, value added (% of GDP)',
    'Industry (including construction), value added (% of GDP)',
    'Services, value added (% of GDP)'
    ]].corr()
corr.style.background_gradient(cmap='coolwarm')

#
# plt.hist(df.iloc[:-2])
# df.iloc[:-2].hist(column='Population, total')
# df.hist(column='Population ages 0-14 (% of total population)')
# df.hist(column='Population ages 15-64 (% of total population)')
# df.hist(column='Population ages 65 and above (% of total population)')
# np.histogram(df)

# rs = np.random.RandomState(0)
# df = pd.DataFrame(rs.rand(10, 10))
# corr = df.corr()
# corr.style.background_gradient(cmap='coolwarm')
# df = xlsx_parse.df_create(
#                           'data/WDIW.xlsx', 0,\
#                           'Cool Name', 'Bumblebee',
#                           'Country Name', 'World')
