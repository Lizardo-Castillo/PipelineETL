from sqlalchemy import create_engine

def load_to_postgres(df, table_name, db_url):
    engine = create_engine(db_url)
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
