class DFempty:
    '''Searches for columns with empty data and creates a list of titles'''

    def __init__(self):
        '''Allows to display a data frame in various forms'''

        self.df = None
        self.empty_columns = None
        self.condition = None

    def full(self):
        '''Finds completely empty columns'''

        self.empty_columns = self.df.columns[self.df.isnull().all()].tolist()

    def partially(self):
        '''Finds partially empty columns matching the condition'''

        self.empty_columns = self.df.columns[self.df.isnull().sum()
                                             > self.condition].tolist()

    def search(self, df, condition=None):
        '''Searches for empty columns
        df = pandas data data frame
        condition = integer - more than how many empty cells should be.
            Default - None
        '''

        self.df = df
        self.condition = condition
        if condition is None:
            self.full()
        else:
            self.partially()
        return self.empty_columns

df_empty = DFempty()
