import streamlit as st
from sqlalchemy import inspect
from backend.db import connect_sqlite  # Only SQLite now
from backend.config import DEFAULT_SQLITE_PATH

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

# SQLite works, PostgreSQL/MySQL planned
with col1:
    if st.button("SQLite"):
        st.session_state.db_type = "sqlite"
        st.session_state.db_engine = None  # Reset previous engine

with col2:
    st.button("PostgreSQL (Planned for Future)", disabled=True)

with col3:
    st.button("MySQL (Planned for Future)", disabled=True)

st.divider()

# --- Connection Form Function ---
def connect_database(db_type: str):
    """Display form and connect to the selected database type."""
    engine = None

    if db_type == "sqlite":
        st.subheader("SQLite Connection")
        with st.form("sqlite_form"):
            db_path = st.text_input("Database Path", DEFAULT_SQLITE_PATH)
            submit = st.form_submit_button("Connect")
            if submit:
                try:
                    engine = connect_sqlite(db_path)
                    st.success("Connected to SQLite!")
                except Exception as e:
                    st.error(f"SQLite connection failed: {e}")

    return engine

# --- Handle connection ---
if st.session_state.db_type == "sqlite":
    engine = connect_database(st.session_state.db_type)
    if engine:
        st.session_state.db_engine = engine
        st.session_state.db_connected = True
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