# backend/db.py
from sqlalchemy import create_engine

def connect_sqlite(db_path):
    """Connect to SQLite database."""
    engine = create_engine(f"sqlite:///{db_path}")
    with engine.connect():
        pass
    return engine

def connect_postgresql(user, password, host, port, database):
    """Connect to PostgreSQL database."""
    conn_str = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(conn_str)
    with engine.connect():
        pass
    return engine

def connect_mysql(user, password, host, port, database):
    """Connect to MySQL database."""
    conn_str = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(conn_str)
    with engine.connect():
        pass
    return engine