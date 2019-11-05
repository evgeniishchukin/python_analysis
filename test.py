from assets.wb_request import wb_request as wb_request
from assets.df_empty import df_empty as df_empty
from assets.xlsx_parse import xlsx_parse as xlsx_parse
from assets.df_show import df_show as df_show
import datetime

# indicator_names = [
#    'Births attended by skilled health staff (% of total)',
#    'Educational attainment, Doctoral or equivalent, population 25+, total (%) (cumulative)',
#    'Educational attainment, at least Bachelor\'s or equivalent, population 25+, total (%) (cumulative)'
# ]
#
# country_codes = ['DZA', 'TCD', 'EGY', 'LBY', 'MLI', 'MRT', 'MAR', 'NER', 'SDN', 'TUN']
# date_range = (datetime.datetime(2017, 1, 1), datetime.datetime(2017, 12, 31))
#
# df = wb_request.get_dataframe(indicator_names, date_range, country_codes)
# print(df)
# print('---'*60)
# print(df_empty.search(df))
# print('---'*60)
# print(df_empty.search(df, 9))
print('---'*60)
newDF = xlsx_parse.df_create('data/WDIW.xlsx', 0, 'Cool Name', 'Bumblebee')
print('---'*60)
df_show.full(newDF)
print(df_empty.search(newDF, 3))
