
import pandas as pd


def load_wide_cpd(fname):
    df = pd.read_excel(fname)
    df = df.set_index(df.columns[0], drop=True)
    df = df.transpose()
    return df

def load_tall_cpd(fname):
    df = pd.read_csv(fname)
    return df
