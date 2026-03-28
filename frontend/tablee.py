import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, inspect

st.set_page_config(page_title="TableForge", layout="wide")

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
.main { background-color: #f6f8fb; }

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #2c3e50, #4ca1af);
    color: white;
}

h1, h2, h3 { color: #2c3e50; }

.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

div.stButton > button {
    background: linear-gradient(90deg, #4ca1af, #2c3e50);
    color: white;
    border-radius: 10px;
    height: 45px;
    font-size: 16px;
}

[data-testid="stMetric"] {
    background-color: white;
    padding: 10px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# ------------------ DATABASE ------------------
engine = create_engine("sqlite:///tableforge.db")

# ------------------ SIDEBAR ------------------
st.sidebar.title("🚀 TableForge")
page = st.sidebar.radio("Navigate", ["🏠 Home", "🔌 Connect DB", "📊 Table Editor"])

# ================== HOME ==================
if page == "🏠 Home":
    st.title("🚀 TableForge")

    st.markdown("""
    <div class='card'>
    <h3>Spreadsheet-style interface for real databases</h3>
    <p>Edit, manage and visualize your data easily.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    col1.info("📊 Edit tables like Excel")
    col2.info("⚡ Works with real databases")

# ================== CONNECT DB ==================
elif page == "🔌 Connect DB":
    st.title("🔌 Database Connection")

    st.markdown("<div class='card'>Connect your database</div>", unsafe_allow_html=True)

    db_name = st.text_input("Database Name", "tableforge.db")

    if st.button("Connect"):
        st.success(f"✅ Connected to {db_name}")

# ================== TABLE EDITOR ==================
elif page == "📊 Table Editor":

    st.title("📊 Table Editor")

    inspector = inspect(engine)
    tables = inspector.get_table_names()

    if not tables:
        st.warning("⚠ No tables found in database")
    else:
        table_name = st.selectbox("📂 Select Table", tables)

        # Load data
        df = pd.read_sql(f"SELECT * FROM {table_name}", engine)

        # -------- SEARCH --------
        search = st.text_input("🔍 Search")
        if search:
            df = df[df.astype(str).apply(lambda row: row.str.contains(search, case=False).any(), axis=1)]

        # -------- FILTER --------
        if not df.empty:
            col_name = st.selectbox("Filter Column", df.columns)
            value = st.text_input("Filter Value")

            if value:
                df = df[df[col_name].astype(str).str.contains(value, case=False)]

        # -------- SORT --------
        if not df.empty:
            col1, col2 = st.columns(2)
            sort_by = col1.selectbox("Sort By", df.columns)
            order = col2.radio("Order", ["Ascending", "Descending"])

            df = df.sort_values(by=sort_by, ascending=(order == "Ascending"))

        # -------- METRICS --------
        if not df.empty:
            col1, col2 = st.columns(2)
            col1.metric("Total Records", len(df))
            col2.metric("Columns", len(df.columns))

        # -------- TABLE --------
        st.markdown("<div class='card'>📋 Data Table</div>", unsafe_allow_html=True)

        edited_df = st.data_editor(df, num_rows="dynamic")

        if st.button("💾 Save Changes"):
            edited_df.to_sql(table_name, engine, if_exists="replace", index=False)
            st.success("✅ Changes Saved!")

        # -------- ADD RECORD (DYNAMIC) --------
        st.markdown("<div class='card'>➕ Add Record</div>", unsafe_allow_html=True)

        new_data = {}
        for col in df.columns:
            new_data[col] = st.text_input(f"Enter {col}")

        if st.button("Add Record"):
            new_df = pd.DataFrame([new_data])
            new_df.to_sql(table_name, engine, if_exists="append", index=False)
            st.success("🎉 Record Added!")
            st.rerun()

        # -------- CHART --------
        numeric_cols = df.select_dtypes(include="number").columns
        if len(numeric_cols) > 0:
            st.subheader("📊 Visualization")
            st.bar_chart(df[numeric_cols])