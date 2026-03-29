import sqlite3

conn = sqlite3.connect("tableforge.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
""")

cursor.execute("INSERT INTO customers (name, city) VALUES ('Rahul', 'Delhi')")
cursor.execute("INSERT INTO customers (name, city) VALUES ('Anita', 'Mumbai')")

conn.commit()
conn.close()