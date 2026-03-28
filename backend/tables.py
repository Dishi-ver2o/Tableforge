# backend/tables.py
import pandas as pd
from sqlalchemy import text, inspect

def get_tables(engine):
    """Return a list of table names in the database"""
    inspector = inspect(engine)
    return inspector.get_table_names()

def read_table(engine, table_name):
    """Read all rows from a table as a DataFrame"""
    return pd.read_sql(f"SELECT * FROM {table_name}", engine)

def save_table(engine, table_name, df):
    """Replace table contents with the edited DataFrame"""
    with engine.begin() as conn:
        conn.execute(text(f"DELETE FROM {table_name}"))
        df.to_sql(table_name, conn, if_exists="append", index=False)

from backend.utils import validate_columns

def create_table(engine, table_name, columns_text):
    columns = validate_columns(columns_text)
    cols_sql = ", ".join([f"{name} {dtype}" for name, dtype in columns])
    sql = f"CREATE TABLE {table_name} ({cols_sql})"
    with engine.begin() as conn:
        conn.execute(text(sql))