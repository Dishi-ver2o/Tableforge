import streamlit as st
import pandas as pd
from sqlalchemy import inspect, text

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
inspector = inspect(engine)

tables = inspector.get_table_names()

if not tables:
    st.info("No tables found.")
    st.stop()

# Sidebar
st.sidebar.title("Tables")
selected_table = st.sidebar.selectbox("Select Table", tables)

# Load table
df = pd.read_sql(f"SELECT * FROM {selected_table}", engine)

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
            with engine.begin() as conn:
                conn.execute(text(f"DELETE FROM {selected_table}"))
                edited_df.to_sql(selected_table, conn, if_exists="append", index=False)
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
            cols = []
            for line in columns.split("\n"):
                if line.strip():
                    name, dtype = line.split(":")
                    cols.append(f"{name.strip()} {dtype.strip()}")

            sql = f"CREATE TABLE {table_name} ({', '.join(cols)})"

            with engine.begin() as conn:
                conn.execute(text(sql))

            st.success("Table created!")
            st.rerun()

        except Exception as e:
            st.error(e)