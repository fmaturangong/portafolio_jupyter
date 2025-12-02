
import pandas as pd

class DataCleaner:
    def __init__(self, df):
        self.df = df.copy()

    def fill_missing(self, col, value):
        self.df.loc[:, col] = self.df[col].fillna(value)

    def drop_duplicates(self):
        self.df = self.df.drop_duplicates()

    def drop_na(self, columns=None):
        if columns is None:
            self.df = self.df.dropna()
        else:
            self.df = self.df.dropna(subset=columns)

    def summary(self):
        return self.df.describe(include='all')


# ===========================================================
# ===========================================================

def clean_peliculas(df):
    cleaner = DataCleaner(df)
    cleaner.drop_na(columns=['género', 'año'])
    cleaner.fill_missing('año', 0)
    cleaner.drop_duplicates()
    return cleaner.df


def clean_ventas(df):
    cleaner = DataCleaner(df)
    cleaner.drop_na()
    cleaner.drop_duplicates()
    return cleaner.df

def clean_peliculas_200(df):
    cleaner = DataCleaner(df)
    cleaner.drop_na(columns=['Titulo', 'Genero', 'Año'])
    cleaner.fill_missing('Recaudacion_USD', 0)
    cleaner.drop_duplicates()
    return cleaner.df
