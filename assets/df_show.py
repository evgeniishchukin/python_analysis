import pandas as pd


class DFshow:
    '''Allows to display a data frame in various forms.'''

    def __init__(self):
        '''Define a list of class variables'''
        pass

    def full(self, df):
        '''Display in full'''

        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        print(df)

    def all_columns(self, df):
        '''Display max columns'''

        pd.set_option('display.max_columns', None)
        print(df)

    def all_rows(self, df):
        '''Display max rows'''

        pd.set_option('display.max_rows', None)
        print('\n\n', df)


df_show = DFshow()
