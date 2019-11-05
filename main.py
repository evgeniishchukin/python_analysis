# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from assets.xlsx_parse import xlsx_parse as xlsx_parse
from assets.df_empty import df_empty as df_empty
# from assets.list_show import list_show as list_show
# from assets.df_show import df_show as df_show
# from assets.wb_request import wb_request as wb_request


# <codecell>
'''DATA PREPARATION'''
# <codecell>
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
df.to_excel(r'data\DF.xlsx')
df['GDP per Capita'] = df['GDP (current US$)']/df['Population, total']
df.set_index(df.columns[0])
df = df.reset_index(drop=True)

# <codecell>
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df

# <codecell>
df.dtypes

# <codecell>
df.describe()

# <codecell>
'''CORRELATIONS'''
# <codecell>
corr = df.corr()
corr.style.background_gradient(cmap='coolwarm')

# <codecell>
corr = df[[
    'Employment in agriculture (% of total employment) (modeled ILO estimate)',
    'Employment in industry (% of total employment) (modeled ILO estimate)',
    'Employment in services (% of total employment) (modeled ILO estimate)'
    ]].corr()
corr.style.background_gradient(cmap='coolwarm')

# <codecell>
corr = df[[
    'Agriculture, forestry, and fishing, value added (% of GDP)',
    'Industry (including construction), value added (% of GDP)',
    'Services, value added (% of GDP)'
    ]].corr()
corr.style.background_gradient(cmap='coolwarm')

# <codecell>
'''BAR PLOTS AND HISTOGRAMS'''
# <codecell>
df.plot.bar(x='Country Name',
            y='Birth rate, crude (per 1,000 people)',
            rot=0,
            figsize=(15, 10))

# <codecell>
df.plot.bar(x='Country Name',
            y='Urban population growth (annual %)',
            rot=0,
            figsize=(15, 10))

# <codecell>
df.plot.bar(x='Country Name',
            y=[
                'Agriculture, forestry, and fishing, value added (% of GDP)',
                'Industry (including construction), value added (% of GDP)',
                'Services, value added (% of GDP)'
                ],
            stacked=True,
            rot=0,
            figsize=(15, 10))

# <codecell>
df.plot.bar(x='Country Name',
            y=[
                'Population ages 0-14 (% of total population)',
                'Population ages 15-64 (% of total population)',
                'Population ages 65 and above (% of total population)'
                ],
            stacked=True,
            rot=0,
            figsize=(15, 10))

# <codecell>
y = [
    'Employment in agriculture (% of total employment) (modeled ILO estimate)',
    'Employment in industry (% of total employment) (modeled ILO estimate)',
    'Employment in services (% of total employment) (modeled ILO estimate)'
]
df.plot.bar(x='Country Name',
            y=y,
            stacked=True,
            rot=0,
            figsize=(15, 10))

# <codecell>
df.plot.bar(x='Country Name',
            y=[
                'Rural population (% of total population)',
                'Urban population (% of total population)',
                ],
            color=['r', 'b'],
            rot=0,
            figsize=(15, 10))

# <codecell>
'''BOX PLOTS'''
# <codecell>
value = 'Mobile cellular subscriptions (per 100 people)'
plt.figure(num=None, figsize=(10, 2))
plt.boxplot(df[value],
            vert=False)
plt.title(value)
plt.show()

# <codecell>
value = 'Prevalence of HIV, total (% of population ages 15-49)'
plt.figure(num=None, figsize=(10, 2))
plt.boxplot(df[value],
            vert=False)
plt.title(value)
plt.show()

# <codecell>
'''SCATTER PLOTS'''
# <codecell>
x = 'GDP per Capita'
y = 'Life expectancy at birth, total (years)'
plt.figure(num=None, figsize=(20, 10))
plt.scatter(
            df[x],
            df[y],
            c=df[y],
            s=df[x],
            cmap='viridis',
            alpha=0.5)
plt.xlabel(x)
plt.ylabel(y)
for i, txt in enumerate(df['Country Name']):
    plt.annotate(
                txt,
                (df.iloc[i][x],
                    df.iloc[i][y]))
plt.show()

# <codecell>
x = 'GDP per Capita'
y = 'Population ages 15-64 (% of total population)'
plt.figure(num=None, figsize=(20, 10))
plt.scatter(
            df[x],
            df[y],
            c=df[y],
            s=df[x],
            cmap='viridis',
            alpha=0.5)
plt.xlabel(x)
plt.ylabel(y)
for i, txt in enumerate(df['Country Name']):
    plt.annotate(
                txt,
                (df.iloc[i][x],
                    df.iloc[i][y]))
plt.show()

# <codecell>
x = 'GDP per Capita'
y = 'Age dependency ratio, young (% of working-age population)'
plt.figure(num=None, figsize=(20, 10))
plt.scatter(
            df[x],
            df[y],
            c=df[y],
            s=df[x],
            cmap='viridis',
            alpha=0.5)
plt.xlabel(x)
plt.ylabel(y)
for i, txt in enumerate(df['Country Name']):
    plt.annotate(
                txt,
                (df.iloc[i][x],
                    df.iloc[i][y]))
plt.show()

# <codecell>
'''ADDITIONAL ANALYSIS (GROUPING POOR AND REACH COUNTRIES)'''
# <codecell>
df_rich = df.iloc[:-1].\
    loc[df['Age dependency ratio, young (% of working-age population)'] < 65]
df_rich = df_rich.reset_index(drop=True)
df_rich

# <codecell>
df_rich.describe()

# <codecell>
df_poor = df.iloc[:-1].\
    loc[df['Age dependency ratio, young (% of working-age population)'] > 65]
df_poor = df_poor.reset_index(drop=True)
df_poor

# <codecell>
df_poor.describe()
