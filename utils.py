import pandas as pd


def preprocess(f):
    processed = pd.read_table(f)[["Symbol", "FDR"]].drop_duplicates(subset="Symbol").dropna().set_index("Symbol")
    return processed
