import pandas


def read_csv(path: str):
    return pandas.read_csv(path, sep=";", encoding='cp1252')

