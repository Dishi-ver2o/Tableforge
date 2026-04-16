from sqlalchemy import create_engine, text
import logging

def connect_mysql(user, password, host, port, database):
    try:
        logging.info(f"Connecting to MySQL at {host}:{port}")

        engine = create_engine(
            f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}",
            pool_pre_ping=True,
            pool_recycle=3600
        )

        # ✅ FIXED test query
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))

        logging.info("MySQL connection successful")
        return engine

    except Exception as e:
        logging.error(f"MySQL connection failed: {e}")
        raise e