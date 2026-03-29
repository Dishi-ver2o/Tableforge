import streamlit as st
from backend.tables import get_tables, read_table, save_table, create_table
from sqlalchemy import create_engine

st.set_page_config(
    page_title="Table Editor - TableForge",
    layout="wide"
)

# --- Inject CSS for bigger green toolbar icons ---
st.markdown(
    """
    <style>
    div[data-testid="stDataEditorToolbar"] {
        visibility: visible !important;
        opacity: 1 !important;
    }
    div[data-testid="stDataEditorToolbar"] button {
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 6px !important;
        padding: 10px 14px !important;
        margin: 4px !important;
        border: none !important;
        font-size: 16px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        cursor: pointer;
    }
    div[data-testid="stDataEditorToolbar"] button svg {
        width: 24px !important;
        height: 24px !important;
        fill: white !important;
    }
    div[data-testid="stDataEditorToolbar"] button:hover {
        background-color: #218838 !important;
        transform: scale(1.05);
        transition: all 0.2s ease-in-out;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📊 TableForge Table Editor")

# --- Check database connection or create demo engine ---
if "db_connected" not in st.session_state or not st.session_state.db_connected:
    st.warning("No database connected. Using a temporary demo database.")
    if "db_engine" not in st.session_state or st.session_state.db_engine is None:
        demo_engine = create_engine("sqlite:///:memory:")  # temporary in-memory DB
        st.session_state.db_engine = demo_engine
        st.session_state.db_connected = True
        st.info("Demo database created! You can try adding tables and editing data.")

engine = st.session_state.db_engine

# --- Get all tables ---
tables = get_tables(engine)

# --- If no tables, show create table form ---
if not tables:
    st.warning("No tables found in this database.")
    st.subheader("Create Your First Table")

    table_name = st.text_input("Table Name", key="first_table_name")
    columns = st.text_area(
        "Columns (name:type)",
        """id:INTEGER
name:TEXT
email:TEXT
age:INTEGER""",
        key="first_table_columns"
    )

    if st.button("Create Table", key="first_table_create"):
        try:
            cols = [
                (line.split(":")[0].strip(), line.split(":")[1].strip())
                for line in columns.split("\n") if line.strip()
            ]
            create_table(engine, table_name, cols)
            st.success("Table created successfully!")
            st.rerun()
        except Exception as e:
            st.error(e)
    st.stop()

# --- Sidebar ---
st.sidebar.title("Tables")
selected_table = st.sidebar.selectbox("Select Table", tables)

# --- Load selected table ---
df = read_table(engine, selected_table)
st.subheader(f"Editing: {selected_table}")

# --- Data editor with styled toolbar ---
edited_df = st.data_editor(
    df,
    use_container_width=True,
    num_rows="dynamic"
)

# --- Action buttons ---
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Save Changes", key="save_btn"):
        try:
            save_table(engine, selected_table, edited_df)
            st.success("Saved successfully")
        except Exception as e:
            st.error(e)

with col2:
    if st.button("Refresh", key="refresh_btn"):
        st.rerun()

with col3:
    if st.button("Create Table", key="show_create_btn"):
        st.session_state.show_create = True

# --- Create table UI ---
if st.session_state.get("show_create"):
    st.divider()
    st.subheader("Create New Table")

    table_name = st.text_input("Table Name", key="new_table_name")
    columns = st.text_area(
        "Columns (name:type)",
        """id:INTEGER
name:TEXT
age:INTEGER""",
        key="new_table_columns"
    )

    if st.button("Create", key="new_table_create"):
        try:
            cols = [
                (line.split(":")[0].strip(), line.split(":")[1].strip())
                for line in columns.split("\n") if line.strip()
            ]
            create_table(engine, table_name, cols)
            st.success("Table created!")
            st.rerun()
        except Exception as e:
            st.error(e)