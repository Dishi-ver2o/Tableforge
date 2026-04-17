import streamlit as st
from sqlalchemy import inspect

# Updated import - now includes PostgreSQL
from backend.db import connect_sqlite, connect_mysql, connect_postgresql
from backend.config import DEFAULT_SQLITE_PATH

st.set_page_config(
    page_title="Connect Database - TableForge",
    layout="wide",
)

st.title("🗄️ TableForge - Connect Database")

# --- Initialize session state ---
if "db_connected" not in st.session_state:
    st.session_state.db_connected = False

if "db_engine" not in st.session_state:
    st.session_state.db_engine = None

if "db_type" not in st.session_state:
    st.session_state.db_type = None

# --- Show current connection ---
if st.session_state.db_connected:
    st.info(f"Connected to: {st.session_state.db_type.upper()}")

# --- Select Database Type ---
st.subheader("Select Database Type")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🗄️ SQLite", key="sqlite_btn"):
        st.session_state.db_type = "sqlite"
        st.session_state.db_engine = None
        st.session_state.db_connected = False
        st.rerun()  # ← ADD THIS!

with col2:
    if st.button("🐘 PostgreSQL", key="postgres_btn"):
        st.session_state.db_type = "postgres"
        st.session_state.db_engine = None
        st.session_state.db_connected = False
        st.rerun()  # ← ADD THIS!

with col3:
    if st.button("🐬 MySQL", key="mysql_btn"):
        st.session_state.db_type = "mysql"
        st.session_state.db_engine = None
        st.session_state.db_connected = False
        st.rerun()  

st.divider()

# --- Connection Function ---
def connect_database(db_type: str):
    engine = None
    submitted = False

    # -------- SQLITE --------
    if db_type == "sqlite":
        st.subheader("SQLite Connection")

        with st.form("sqlite_form"):
            db_path = st.text_input("Database Path", DEFAULT_SQLITE_PATH)
            submit = st.form_submit_button("Connect")

            if submit:
                submitted = True
                try:
                    engine = connect_sqlite(db_path)
                    st.success("✅ Connected to SQLite!")
                    st.session_state.db_type = "sqlite"
                except Exception as e:
                    st.error(f"❌ SQLite connection failed: {e}")

    # -------- POSTGRESQL --------
    elif db_type == "postgres":
        st.subheader("PostgreSQL Connection")

        with st.form("postgres_form"):
            host = st.text_input("Host", "localhost")
            port = st.number_input("Port", min_value=1, max_value=65535, value=5432)
            user = st.text_input("User", "postgres")
            password = st.text_input("Password", type="password")
            database = st.text_input("Database", "postgres")

            submit = st.form_submit_button("Connect")

            if submit:
                submitted = True
                try:
                    # Using the new dedicated function
                    engine = connect_postgresql(host, port, user, password, database)
                    st.success("✅ Connected to PostgreSQL!")
                    st.session_state.db_type = "postgres"
                except Exception as e:
                    st.error(f"❌ PostgreSQL connection failed: {str(e)}")
                    engine = None

    # -------- MYSQL --------
    elif db_type == "mysql":
        st.subheader("MySQL Connection")

        with st.form("mysql_form"):
            host = st.text_input("Host", "localhost")
            port = st.number_input("Port", min_value=1, max_value=65535, value=3306)
            user = st.text_input("User", "root")
            password = st.text_input("Password", type="password")
            database = st.text_input("Database", "testdb")

            submit = st.form_submit_button("Connect")

            if submit:
                submitted = True
                try:
                    engine = connect_mysql(user, password, host, port, database)
                    st.success("✅ Connected to MySQL!")
                    st.session_state.db_type = "mysql"


                except Exception as e:
                    st.error(f"MySQL connection failed: {e}")
                    engine = None

    return engine, submitted

# --- Handle connection ---
if st.session_state.db_type:
    engine, submitted = connect_database(st.session_state.db_type)

    if submitted and engine:
        st.session_state.db_engine = engine
        st.session_state.db_connected = True

        try:
            tables = inspect(engine).get_table_names()
            st.info(f"📋 Tables found: {len(tables)}")
            if tables:
                st.info(f"Tables: {', '.join(tables[:5])}{'...' if len(tables) > 5 else ''}")
        except Exception as e:
            st.warning(f"Could not list tables: {e}")

    elif submitted:
        st.session_state.db_connected = False
        st.session_state.db_engine = None


# --- Actions ---
if st.session_state.db_connected:
    st.divider()
    st.success("🎉 Database Connected Successfully ✅")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🚀 Open Table Editor", width="stretch"):
            if st.session_state.db_engine is None:
                st.error("❌ No active database connection found. Please connect again.")
            else:
                st.switch_page("pages/table_editor.py")

    with col2:
        if st.button("🔌 Disconnect", width="stretch"):
            st.session_state.db_connected = False
            st.session_state.db_engine = None
            st.session_state.db_type = None
            st.rerun()