import streamlit as st
from sqlalchemy import inspect

from backend.db import connect_sqlite
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
    st.session_state.db_type = "sqlite"

# --- Show current connection ---
if st.session_state.db_connected:
    st.info(f"Connected to: {st.session_state.db_type.upper()}")

st.subheader("SQLite Connection")
st.caption("SQLite is the only active database mode right now.")
st.divider()

# --- Connection Function ---
def connect_database():
    engine = None
    submitted = False

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

    return engine, submitted

# --- Handle connection ---
engine, submitted = connect_database()

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
