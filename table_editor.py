import streamlit as st
import pandas as pd
from sqlalchemy import inspect, text

st.set_page_config(
    page_title="Table Editor - TableForge",
    layout="wide"
)

# Check connection
if not st.session_state.get("db_connected"):
    st.warning("⚠️ Please connect to the database first.")
    if st.button("Go to Connect Page"):
        st.switch_page("connect_database.py")
    st.stop()

engine = st.session_state.db_engine
inspector = inspect(engine)

st.title("📊 TableForge Editor")
st.caption("Edit your database like a spreadsheet")

# Get tables
tables = inspector.get_table_names()

if not tables:
    st.info("No tables found in the database.")
    st.stop()

# Sidebar
st.sidebar.title("Database Tables")

selected_table = st.sidebar.selectbox(
    "Select Table",
    tables
)

# Load table
query = f"SELECT * FROM {selected_table}"
df = pd.read_sql(query, engine)

st.subheader(f"Editing: {selected_table}")

edited_df = st.data_editor(
    df,
    use_container_width=True,
    num_rows="dynamic"
)

col1, col2, col3 = st.columns(3)

# Save changes
with col1:
    if st.button("💾 Save Changes"):
        try:
            with engine.begin() as conn:
                conn.execute(text(f"DELETE FROM {selected_table}"))
                edited_df.to_sql(selected_table, conn, if_exists="append", index=False)
            st.success("Changes saved successfully!")
        except Exception as e:
            st.error(str(e))

# Refresh
with col2:
    if st.button("🔄 Refresh"):
        st.rerun()

# Add table
with col3:
    if st.button("➕ Create New Table"):
        st.session_state.show_create_table = True

# Create table UI
if st.session_state.get("show_create_table"):
    st.divider()
    st.subheader("Create New Table")

    table_name = st.text_input("Table Name")

    columns = st.text_area(
        "Columns (format: name:type)",
        placeholder="""
id:INTEGER
name:TEXT
age:INTEGER
        """
    )

    if st.button("Create Table"):
        try:
            cols = []
            for line in columns.split("\n"):
                if line.strip():
                    name, dtype = line.split(":")
                    cols.append(f"{name.strip()} {dtype.strip()}")

            sql = f"CREATE TABLE {table_name} ({', '.join(cols)})"

            with engine.begin() as conn:
                conn.execute(text(sql))

            st.success("Table created successfully!")
            st.rerun()

        except Exception as e:
            st.error(str(e))