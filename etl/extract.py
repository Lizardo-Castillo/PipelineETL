import pandas as pd

def extract_web_orders(path):
    return pd.read_csv(path, sep=';', parse_dates=['DATE'], dayfirst=True)

def extract_catalog_orders(path):
    return pd.read_csv(path, parse_dates=['DATE'], dayfirst=True)

def extract_products(path):
    return pd.read_json(path)
