import wbdata


class WBrequest:
    '''Generates a dataframe based on a request from World Bank'''

    def __init__(self):
        '''Define a list of class variables'''

        self.indicators = dict()
        self.df = None
        self.i_names = None
        self.date = None
        self.codes = None

    def indicators_request(self):
        '''Request all necessary indicators from World Bank'''

        for i_name in self.i_names:
            indicator = wbdata.search_indicators(i_name)[0]['id']
            self.indicators[indicator] = i_name

    def df_request(self):
        '''Request dataframe from World Bank, based on indicators,
                    country codes and date period'''

        self.df = wbdata.get_dataframe(
            self.indicators, country=self.codes, data_date=self.date)

    def get_dataframe(self, indicator_names, date_range, country_codes):
        '''Return requested dataframe
        indicator_names = [List of indicators presented as text]
        date_range = (Tuple of datetime(year, month, day) to
                               datetime(year, month, day))
        country_codes = [List of country codes]
        '''

        self.i_names = indicator_names
        self.date = date_range
        self.codes = country_codes
        self.indicators_request()
        self.df_request()
        return self.df


wb_request = WBrequest()
