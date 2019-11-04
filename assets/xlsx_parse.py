import pandas as pd
import os


class XLSXparse:
    '''Creates a data frame by reading an excel file'''

    def __init__(self):
        '''Define a list of class variables
            and determine the path to the root directory'''

        self.root_directory = os.path.dirname(os.path.abspath(
                                                __file__+'../../'))
        self.directory = None

    def df_create(
                  self, directory, sheet_number,
                  column_name_1=None, cell_data_1=None,
                  column_name_2=None, cell_data_2=None):
        '''Create a data frame on the basis of parsing a Excel file
        directory = String - path to file from root directory
        sheet_number = Integer - number of sheet in Excel File. Starts from 0
        column_name = String - Column for data sampling. None by default
        cell_data_# = String - Cell value for data sampling. None by default
        '''

        self.directory = os.path.join(self.root_directory, directory)
        xlsx = pd.ExcelFile(self.directory)
        df = xlsx.parse(xlsx.sheet_names[sheet_number], index_col=None)
        if column_name_1 is not None and cell_data_1 is not None \
                and column_name_2 is not None and cell_data_2 is not None:
            df = df.loc[(df[column_name_1] == cell_data_1)
                        | (df[column_name_2] == cell_data_2)]
        elif column_name_1 is not None and cell_data_1 is not None \
                and column_name_2 is None and cell_data_2 is None:
            df = df.loc[df[column_name_1] == cell_data_1]
        return df


xlsx_parse = XLSXparse()
