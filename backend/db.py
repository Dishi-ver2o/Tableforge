# backend/db.py
import logging
from sqlalchemy import create_engine

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def connect_sqlite(db_path):
    logging.info(f"Connecting to SQLite database at {db_path}")
    engine = create_engine(f"sqlite:///{db_path}")
    with engine.connect():
        pass
    logging.info("Connection successful")
    return engine

def connect_postgresql(user, password, host, port, database):
    logging.info(f"Connecting to PostgreSQL at {host}:{port}, DB: {database}")
    conn_str = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(conn_str)
    with engine.connect():
        pass
    logging.info("PostgreSQL connection successful")
    return engine

def connect_mysql(user, password, host, port, database):
    logging.info(f"Connecting to MySQL at {host}:{port}, DB: {database}")
    conn_str = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(conn_str)
    with engine.connect():
        pass
    logging.info("MySQL connection successful")
    return engine