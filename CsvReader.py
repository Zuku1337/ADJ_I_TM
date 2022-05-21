import pandas


def read_csv(path: str):
    return pandas.read_csv(path, encoding='ISO-8859-1')
