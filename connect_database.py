import streamlit as st
from sqlalchemy import inspect
from backend.db import connect_sqlite, connect_postgresql, connect_mysql
from backend.config import DEFAULT_SQLITE_PATH, DEFAULT_POSTGRESQL, DEFAULT_MYSQL

st.set_page_config(
    page_title="Connect Database - TableForge",
    layout="wide"
)

st.title("🗄️ TableForge - Connect Database")

# --- Initialize session state ---
for key in ["db_connected", "db_engine", "db_type"]:
    if key not in st.session_state:
        st.session_state[key] = None
if st.session_state.db_connected is None:
    st.session_state.db_connected = False

# --- Select Database Type ---
st.subheader("Select Database Type")
col1, col2, col3 = st.columns(3)
db_buttons = {"sqlite": col1, "postgresql": col2, "mysql": col3}

for db_type, col in db_buttons.items():
    with col:
        if st.button(db_type.capitalize()):
            st.session_state.db_type = db_type

st.divider()

# --- Connection Form ---
def connect_database(db_type: str):
    """Display form and connect to the selected database type."""
    
    if db_type == "sqlite":
        st.subheader("SQLite Connection")
        with st.form("sqlite_form"):
            db_path = st.text_input("Database Path", DEFAULT_SQLITE_PATH)
            submit = st.form_submit_button("Connect")
            if submit:
                try:
                    engine = connect_sqlite(db_path)
                    return engine
                except Exception as e:
                    st.error(e)
                    return None

    elif db_type == "postgresql":
        st.subheader("PostgreSQL Connection")
        with st.form("pg_form"):
            host = st.text_input("Host", DEFAULT_POSTGRESQL["host"])
            port = st.number_input("Port", DEFAULT_POSTGRESQL["port"])
            user = st.text_input("User", DEFAULT_POSTGRESQL["user"])
            password = st.text_input("Password", type="password", value=DEFAULT_POSTGRESQL["password"])
            database = st.text_input("Database", DEFAULT_POSTGRESQL["database"])
            submit = st.form_submit_button("Connect")
            if submit:
                try:
                    engine = connect_postgresql(user, password, host, port, database)
                    return engine
                except Exception as e:
                    st.error(e)
                    return None

    elif db_type == "mysql":
        st.subheader("MySQL Connection")
        with st.form("mysql_form"):
            host = st.text_input("Host", DEFAULT_MYSQL["host"])
            port = st.number_input("Port", DEFAULT_MYSQL["port"])
            user = st.text_input("User", DEFAULT_MYSQL["user"])
            password = st.text_input("Password", type="password", value=DEFAULT_MYSQL["password"])
            database = st.text_input("Database", DEFAULT_MYSQL["database"])
            submit = st.form_submit_button("Connect")
            if submit:
                try:
                    engine = connect_mysql(user, password, host, port, database)
                    return engine
                except Exception as e:
                    st.error(e)
                    return None

# --- Handle connection ---
if st.session_state.db_type:
    engine = connect_database(st.session_state.db_type)
    if engine:
        st.session_state.db_engine = engine
        st.session_state.db_connected = True
        st.success(f"Connected to {st.session_state.db_type.capitalize()}!")
        try:
            tables = inspect(engine).get_table_names()
            st.info(f"Tables found: {len(tables)}")
        except Exception:
            tables = []

# --- Connection Status & Actions ---
if st.session_state.db_connected:
    st.divider()
    st.success("Database Connected ✅")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Open Table Editor"):
            st.switch_page("pages/table_editor.py")
    with col2:
        if st.button("Disconnect"):
            for key in ["db_connected", "db_engine", "db_type"]:
                st.session_state[key] = None
            st.rerun()