import pandas as pd

def clean_web_orders(df):
    df.columns = df.columns.str.strip().str.lower()
    df['custnum'] = df['custnum'].astype(str)
    df.dropna(inplace=True)
    return df

def clean_catalog_orders(df):
    df.columns = df.columns.str.strip().str.lower()
    df['custnum'] = df['custnum'].astype(str)
    df.dropna(inplace=True)
    return df

def clean_products(df):
    df.columns = df.columns.str.strip().str.lower()
    df.dropna(inplace=True)
    return df

def integrate_orders(web_df, catalog_df):
    return pd.concat([web_df, catalog_df], ignore_index=True)

def group_products(df):
    return df.groupby(['type', 'supplier']).agg({
        'price': 'mean',
        'cost': 'mean'
    }).reset_index()
