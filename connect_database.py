import streamlit as st
from sqlalchemy import inspect
from backend.db import connect_sqlite, connect_postgresql, connect_mysql

st.set_page_config(
    page_title="Connect Database - TableForge",
    layout="wide"
)

st.title("🗄️ TableForge - Connect Database")

# Initialize session state
if "db_connected" not in st.session_state:
    st.session_state.db_connected = False
if "db_engine" not in st.session_state:
    st.session_state.db_engine = None
if "db_type" not in st.session_state:
    st.session_state.db_type = None

st.subheader("Select Database Type")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("SQLite"):
        st.session_state.db_type = "sqlite"

with col2:
    if st.button("PostgreSQL"):
        st.session_state.db_type = "postgresql"

with col3:
    if st.button("MySQL"):
        st.session_state.db_type = "mysql"

st.divider()

# SQLite
if st.session_state.db_type == "sqlite":
    st.subheader("SQLite Connection")

    with st.form("sqlite_form"):
        db_path = st.text_input("Database Path", "database.db")
        submit = st.form_submit_button("Connect")

        if submit:
            try:
                # Call backend function
                engine = connect_sqlite(db_path)

                st.session_state.db_engine = engine
                st.session_state.db_connected = True

                st.success("Connected to SQLite!")

                # Show tables
                inspector = inspect(engine)
                tables = inspector.get_table_names()
                st.info(f"Tables found: {len(tables)}")

            except Exception as e:
                st.error(e)

# PostgreSQL
elif st.session_state.db_type == "postgresql":
    st.subheader("PostgreSQL Connection")

    with st.form("pg_form"):
        host = st.text_input("Host", "localhost")
        port = st.number_input("Port", 5432)
        user = st.text_input("User")
        password = st.text_input("Password", type="password")
        database = st.text_input("Database")

        submit = st.form_submit_button("Connect")

        if submit:
            try:
                engine = connect_postgresql(user, password, host, port, database)
                st.session_state.db_engine = engine
                st.session_state.db_connected = True
                st.success("Connected to PostgreSQL!")

            except Exception as e:
                st.error(e)

# MySQL
elif st.session_state.db_type == "mysql":
    st.subheader("MySQL Connection")

    with st.form("mysql_form"):
        host = st.text_input("Host", "localhost")
        port = st.number_input("Port", 3306)
        user = st.text_input("User")
        password = st.text_input("Password", type="password")
        database = st.text_input("Database")

        submit = st.form_submit_button("Connect")

        if submit:
            try:
                engine = connect_mysql(user, password, host, port, database)
                st.session_state.db_engine = engine
                st.session_state.db_connected = True
                st.success("Connected to MySQL!")

            except Exception as e:
                st.error(e)

# Connection status
if st.session_state.db_connected:
    st.divider()
    st.success("Database Connected")

    if st.button("Open Table Editor"):
        st.switch_page("pages/table_editor.py")

    if st.button("Disconnect"):
        st.session_state.db_connected = False
        st.session_state.db_engine = None
        st.session_state.db_type = None
        st.rerun()