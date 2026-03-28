# backend/config.py

# Default database paths / credentials
DEFAULT_SQLITE_PATH = "database.db"

DEFAULT_POSTGRESQL = {
    "host": "localhost",
    "port": 5432,
    "user": "postgres",
    "password": "",
    "database": "mydb"
}

DEFAULT_MYSQL = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "",
    "database": "mydb"
}