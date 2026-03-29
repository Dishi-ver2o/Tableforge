from sqlalchemy import create_engine
import logging

logging.basicConfig(level=logging.INFO)

def connect_sqlite(db_path: str):
    logging.info(f"Connecting to SQLite at {db_path}")
    engine = create_engine(f"sqlite:///{db_path}")
    with engine.connect():
        pass
    logging.info("SQLite connection successful")
    return engine