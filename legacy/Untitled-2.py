# backend/db/postgresql.py
from sqlalchemy import create_engine
from backend.config import DEFAULT_POSTGRESQL
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def connect_postgresql(
    user=DEFAULT_POSTGRESQL["user"],
    password=DEFAULT_POSTGRESQL["password"],
    host=DEFAULT_POSTGRESQL["host"],
    port=DEFAULT_POSTGRESQL["port"],
    database=DEFAULT_POSTGRESQL["database"]
):
    logging.info(f"Connecting to PostgreSQL at {host}:{port}, DB: {database}")
    conn_str = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(conn_str)
    with engine.connect():
        pass
    logging.info("PostgreSQL connection successful")
    return engine