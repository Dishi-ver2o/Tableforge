from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
import logging


def connect_postgresql(host, port, user, password, database):
    try:
        logging.info(f"Connecting to PostgreSQL at {host}:{port}")

        url = URL.create(
            "postgresql+psycopg2",
            username=user,
            password=password,
            host=host,
            port=int(port),
            database=database,
        )

        engine = create_engine(
            url,
            pool_pre_ping=True,
            pool_recycle=3600,
        )

        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))

        logging.info("PostgreSQL connection successful")
        return engine

    except Exception as e:
        logging.error(f"PostgreSQL connection failed: {e}")
        raise
