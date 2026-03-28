import streamlit as st
from backend.tables import get_tables, read_table, save_table, create_table

st.set_page_config(
    page_title="Table Editor - TableForge",
    layout="wide"
)

st.title("📊 TableForge Table Editor")

# Check connection
if "db_connected" not in st.session_state or not st.session_state.db_connected:
    st.warning("Please connect to a database first.")
    if st.button("Go to Connect Page"):
        st.switch_page("connect_database.py")
    st.stop()

engine = st.session_state.db_engine

# Get all tables
tables = get_tables(engine)

# If no tables, show create table form
if not tables:
    st.warning("No tables found in this database.")

    st.subheader("Create Your First Table")
    table_name = st.text_input("Table Name")
    columns = st.text_area(
        "Columns (name:type)",
        """id:INTEGER
name:TEXT
email:TEXT
age:INTEGER"""
    )

    if st.button("Create Table"):
        try:
            # Convert columns text to list of tuples
            cols = [(line.split(":")[0].strip(), line.split(":")[1].strip())
                    for line in columns.split("\n") if line.strip()]

            create_table(engine, table_name, cols)

            st.success("Table created successfully!")
            st.rerun()

        except Exception as e:
            st.error(e)

    st.stop()

# Sidebar
st.sidebar.title("Tables")
selected_table = st.sidebar.selectbox("Select Table", tables)

# Load table
df = read_table(engine, selected_table)

st.subheader(f"Editing: {selected_table}")

edited_df = st.data_editor(
    df,
    use_container_width=True,
    num_rows="dynamic"
)

col1, col2, col3 = st.columns(3)

# Save
with col1:
    if st.button("Save Changes"):
        try:
            save_table(engine, selected_table, edited_df)
            st.success("Saved successfully")
        except Exception as e:
            st.error(e)

# Refresh
with col2:
    if st.button("Refresh"):
        st.rerun()

# New table
with col3:
    if st.button("Create Table"):
        st.session_state.show_create = True

# Create table UI
if st.session_state.get("show_create"):
    st.divider()
    st.subheader("Create New Table")

    table_name = st.text_input("Table Name")
    columns = st.text_area(
        "Columns (name:type)",
        """id:INTEGER
name:TEXT
age:INTEGER"""
    )

    if st.button("Create"):
        try:
            cols = [(line.split(":")[0].strip(), line.split(":")[1].strip())
                    for line in columns.split("\n") if line.strip()]

            create_table(engine, table_name, cols)

            st.success("Table created!")
            st.rerun()

        except Exception as e:
            st.error(e)