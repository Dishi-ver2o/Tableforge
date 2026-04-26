import pandas as pd
import streamlit as st

from backend.tables import add_column, create_table, get_tables, read_table, save_table

st.set_page_config(
    page_title="Table Editor - TableForge",
    layout="wide",
)

st.markdown(
    """
    <style>
    :root {
        --page-bg: #cfeaff;
        --shell-bg: #ffffff;
        --hero-blue: #4da3f5;
        --hero-blue-dark: #2f80ed;
        --panel-blue: #bfe4ff;
        --beige-border: #e4cdaf;
        --card-bg: rgba(255, 255, 255, 0.92);
        --text-main: #18324a;
        --text-soft: #52708b;
        --mint-accent: #ddf7ea;
        --peach-accent: #ffe6d6;
        --lavender-accent: #eee5ff;
        --border-blue: #afcbe3;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(47, 128, 237, 0.20), transparent 30%),
            radial-gradient(circle at bottom right, rgba(191, 228, 255, 0.32), transparent 26%),
            linear-gradient(180deg, #eaf6ff 0%, var(--page-bg) 100%);
    }

    .block-container {
        max-width: 1500px;
        padding-top: 1.4rem;
        padding-bottom: 1.5rem;
    }

    .app-shell {
        background: linear-gradient(180deg, rgba(255, 255, 255, 0.96), rgba(247, 251, 255, 0.94));
        border: 1px solid rgba(175, 203, 227, 0.95);
        border-radius: 28px;
        padding: 1.25rem;
        box-shadow: 0 18px 40px rgba(47, 128, 237, 0.10);
    }

    .hero-wrap {
        background: linear-gradient(135deg, #2f80ed 0%, #4da3f5 55%, #bfe4ff 100%);
        color: white;
        border-radius: 24px;
        padding: 1.25rem 1.35rem;
        margin-bottom: 1rem;
        box-shadow: 0 14px 28px rgba(47, 128, 237, 0.18);
    }

    .hero-kicker {
        font-size: 0.76rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.14em;
        opacity: 0.92;
        margin-bottom: 0.35rem;
    }

    .hero-title {
        font-size: 2rem;
        font-weight: 800;
        color: white;
        margin: 0;
        line-height: 1.1;
    }

    .hero-subtitle {
        margin-top: 0.45rem;
        font-size: 0.96rem;
        font-weight: 600;
        opacity: 0.92;
    }

    .toolbar-card {
        background: linear-gradient(180deg, #f6e8d5, #f3e1cb);
        border: 1px solid rgba(228, 205, 175, 0.95);
        border-radius: 22px;
        padding: 1rem;
        margin-bottom: 1rem;
    }

    .toolbar-label {
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        color: var(--hero-blue-dark);
        font-weight: 800;
        margin-bottom: 0.7rem;
    }

    .section-card {
        background: var(--card-bg);
        border: 1px solid rgba(175, 203, 227, 0.85);
        border-radius: 22px;
        padding: 1rem;
        box-shadow: 0 12px 24px rgba(47, 128, 237, 0.08);
        height: 100%;
    }

    .section-label {
        font-size: 0.78rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        color: var(--hero-blue-dark);
        margin-bottom: 0.3rem;
    }

    .section-title {
        font-size: 1.12rem;
        font-weight: 800;
        color: var(--text-main);
        margin-bottom: 0.2rem;
    }

    .section-subtitle {
        color: var(--text-soft);
        font-size: 0.92rem;
        margin-bottom: 0.95rem;
        font-weight: 600;
    }

    .schema-name {
        font-size: 0.92rem;
        font-weight: 800;
        color: var(--text-main);
    }

    .schema-panel-card {
        margin-bottom: 1rem;
    }

    .schema-label-card {
        padding: 0.88rem 1rem;
        border-radius: 14px;
        background: linear-gradient(180deg, rgba(191, 228, 255, 0.62), rgba(255, 255, 255, 0.95));
        border: 1px solid rgba(160, 197, 224, 0.95);
        min-height: 3rem;
        display: flex;
        align-items: center;
    }

    .schema-panel-card div[data-baseweb="select"] > div {
        min-height: 3rem;
    }

    .sheet-note {
        background: linear-gradient(180deg, rgba(221, 247, 234, 0.92), rgba(255, 230, 214, 0.62));
        border: 1px solid rgba(175, 203, 227, 0.75);
        color: var(--text-main);
        border-radius: 14px;
        padding: 0.8rem 0.95rem;
        margin-bottom: 0.9rem;
        font-size: 0.9rem;
        font-weight: 600;
    }

    .status-bar {
        margin-top: 1rem;
        border-radius: 18px;
        padding: 0.85rem 1rem;
        color: var(--text-main);
        border: 1px solid rgba(175, 203, 227, 0.9);
        background: linear-gradient(90deg, rgba(238, 229, 255, 0.55), rgba(255, 255, 255, 0.9));
        font-weight: 700;
    }

    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div,
    .stTextInput > div > div,
    .stTextArea textarea,
    .stNumberInput > div > div {
        border-radius: 14px !important;
        background: rgba(255, 255, 255, 0.92);
        border: 1px solid rgba(175, 203, 227, 0.95) !important;
    }

    .stButton > button {
        border-radius: 14px;
        min-height: 2.65rem;
        border: 1px solid rgba(175, 203, 227, 0.95);
        background: linear-gradient(180deg, #ffffff, #dff0ff);
        color: var(--text-main);
        font-weight: 700;
    }

    .stButton > button:hover {
        color: var(--hero-blue-dark);
        border-color: rgba(47, 128, 237, 0.55);
    }

    .stButton > button[kind="primary"] {
        background: linear-gradient(180deg, #4da3f5, #2f80ed);
        color: white;
        border: none;
    }

    div[data-testid="stDataEditor"] {
        border: 1px solid rgba(175, 203, 227, 1);
        border-radius: 18px;
        overflow: hidden;
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.62);
    }

    div[data-testid="stDataEditor"] [role="columnheader"] {
        background: #4da3f5 !important;
        color: white !important;
        font-weight: 800 !important;
    }

    div[data-testid="stDataEditor"] [role="gridcell"] {
        background: rgba(255, 255, 255, 0.96);
    }

    /* Hide the built-in data editor toolbar (bar above the grid). */
    div[data-testid="stDataEditor"] [data-testid="stDataFrameToolbar"] {
        display: none !important;
    }

    /* Hide the internal seed column entry (always last) in the native column selector list. */
    div[data-testid="stDataEditor"] div[role="dialog"] div[data-testid="stCheckbox"]:last-of-type {
        display: none !important;
    }

    .stAlert {
        border-radius: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


DATA_TYPE_OPTIONS = ["INTEGER", "TEXT", "REAL", "BOOLEAN", "DATE", "BLOB"]


def merge_visible_and_hidden_columns(view_df: pd.DataFrame, original_df: pd.DataFrame):
    merged_df = view_df.copy()
    hidden_columns = [column for column in original_df.columns if column not in merged_df.columns]

    if hidden_columns:
        merged_df = merged_df.join(original_df[hidden_columns], how="left")

    for column in original_df.columns:
        if column not in merged_df.columns:
            merged_df[column] = pd.NA

    return merged_df[original_df.columns]


def parse_columns(columns_text: str, db_type: str):
    cols = []
    type_mapping = {
        "sqlite": {"int": "INTEGER", "str": "TEXT", "float": "REAL"},
        "postgres": {"int": "INTEGER", "str": "TEXT", "float": "NUMERIC"},
        "mysql": {"int": "INT", "str": "VARCHAR(255)", "float": "DECIMAL(10,2)"},
    }

    for line_num, line in enumerate(columns_text.split("\n"), 1):
        line = line.strip()
        if not line:
            continue

        if ":" not in line:
            st.error(f"Line {line_num}: invalid format '{line}' (use name:TYPE)")
            st.stop()

        name, col_type = line.split(":", 1)
        name = name.strip()
        col_type = col_type.strip().upper()

        if db_type in type_mapping and col_type.lower() in type_mapping[db_type]:
            col_type = type_mapping[db_type][col_type.lower()]

        cols.append(f"{name} {col_type}")

    return cols


def validate_no_nulls(df: pd.DataFrame):
    for row_idx, row in df.iterrows():
        for column in df.columns:
            value = row[column]

            if column.lower() == "id":
                continue

            if pd.isna(value):
                return False, f"Row {row_idx + 1}, column '{column}' cannot be empty."

            if isinstance(value, str) and not value.strip():
                return False, f"Row {row_idx + 1}, column '{column}' cannot be empty."

    return True, ""


def infer_editor_type(series: pd.Series):
    if pd.api.types.is_bool_dtype(series):
        return "BOOLEAN"
    if pd.api.types.is_integer_dtype(series):
        return "INTEGER"
    if pd.api.types.is_float_dtype(series):
        return "REAL"
    if pd.api.types.is_datetime64_any_dtype(series):
        return "DATE"
    return "TEXT"


if "db_connected" not in st.session_state or not st.session_state.get("db_connected", False):
    st.error("No database connection found.")
    st.info("Go back to the connect page and connect to a database first.")
    st.stop()

if "db_engine" not in st.session_state or st.session_state.db_engine is None:
    st.error("No database engine found. Please reconnect.")
    st.stop()

engine = st.session_state.db_engine
db_type = st.session_state.get("db_type", "unknown")

try:
    tables = get_tables(engine)
except Exception as e:
    st.error(f"Could not load tables: {e}")
    st.stop()

if "show_create" not in st.session_state:
    st.session_state.show_create = False

if "show_add_column" not in st.session_state:
    st.session_state.show_add_column = False

if not tables:
    st.markdown('<div class="app-shell">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="hero-wrap">
            <div class="hero-kicker">TableForge Workspace</div>
            <div class="hero-title">Smart Table Editor</div>
            <div class="hero-subtitle">Start by creating your first table.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.warning("No tables found in this database.")

    table_name = st.text_input("Table Name", key="first_table_name")
    columns = st.text_area(
        "Columns (name:TYPE)",
        """id:INTEGER PRIMARY KEY
name:TEXT
email:TEXT
age:INTEGER""",
        height=160,
        key="first_table_columns",
    )

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Create Table", width="stretch", type="primary", key="first_table_create"):
            try:
                cols = parse_columns(columns, db_type)
                create_table(engine, table_name, cols)
                st.success("Table created successfully.")
                st.rerun()
            except Exception as e:
                st.error(f"{e}")
    with c2:
        st.button("Refresh", width="stretch", disabled=True)

    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

with st.sidebar:
    st.markdown("### Tables")
    selected_table = st.selectbox("Select Table", tables, key="table_select")
    st.markdown("---")

try:
    df = read_table(engine, selected_table)
except Exception as e:
    st.error(f"Could not load table '{selected_table}': {e}")
    st.stop()

if f"column_types_{selected_table}" not in st.session_state:
    initial_types = {}
    for column in df.columns:
        initial_types[column] = infer_editor_type(df[column])
    st.session_state[f"column_types_{selected_table}"] = initial_types

column_types = st.session_state[f"column_types_{selected_table}"]
row_count = len(df)
column_count = len(df.columns)

st.markdown('<div class="app-shell">', unsafe_allow_html=True)

st.markdown(
    """
    <div class="hero-wrap">
        <div class="hero-kicker">TableForge Workspace</div>
        <div class="hero-title">Smart Table Editor</div>
        <div class="hero-subtitle">A cleaner spreadsheet-style layout with polished schema controls and a full-width data workspace.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="toolbar-card">', unsafe_allow_html=True)
st.markdown('<div class="toolbar-label">Action Ribbon</div>', unsafe_allow_html=True)

action_toolbar = st.columns([1.2, 1.2, 1.35, 1.2], gap="small")
with action_toolbar[0]:
    save_clicked = st.button("Save Changes", width="stretch", type="primary", key="save_btn")
with action_toolbar[1]:
    refresh_clicked = st.button("Refresh", width="stretch", key="refresh_btn")
with action_toolbar[2]:
    create_clicked = st.button("Create Table", width="stretch", key="show_create_btn")
with action_toolbar[3]:
    add_column_clicked = st.button("Add Column", width="stretch", key="show_add_column_btn")

st.markdown("</div>", unsafe_allow_html=True)

if refresh_clicked:
    st.rerun()

if create_clicked:
    st.session_state.show_create = True

if add_column_clicked:
    st.session_state.show_add_column = True

st.markdown(
    """
    <div class="section-card schema-panel-card">
        <div class="section-label">Schema Panel</div>
        <div class="section-title">Column Setup</div>
        <div class="section-subtitle">Keep the structure clean and spreadsheet-like.</div>
    """,
    unsafe_allow_html=True,
)

for column in df.columns:
    default_index = DATA_TYPE_OPTIONS.index(column_types.get(column, "TEXT"))
    label_col, select_col = st.columns([1.45, 1], gap="medium")
    with label_col:
        st.markdown(
            f'<div class="schema-label-card"><div class="schema-name">{column}</div></div>',
            unsafe_allow_html=True,
        )
    with select_col:
        column_types[column] = st.selectbox(
            f"Type for {column}",
            DATA_TYPE_OPTIONS,
            index=default_index,
            key=f"type_{selected_table}_{column}",
            label_visibility="collapsed",
        )

st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="section-card">
        <div class="section-label">Data Workspace</div>
        <div class="section-title">Spreadsheet View</div>
        <div class="section-subtitle">Edit live records inside a cleaner sheet canvas.</div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="sheet-note">
        Active table: <strong>{selected_table}</strong> &nbsp;&nbsp;|&nbsp;&nbsp;
        Session: <strong>{db_type.upper()}</strong> &nbsp;&nbsp;|&nbsp;&nbsp;
        Rows loaded: <strong>{row_count}</strong>
    </div>
    """,
    unsafe_allow_html=True,
)

view = f"view_{selected_table}"
if view not in st.session_state:
    st.session_state[view] = list(df.columns)

seed = "__eye_seed__"

cols = [c for c in st.session_state[view] if c in df.columns]
if st.session_state[view] and not cols:
    cols = list(df.columns)
    st.session_state[view] = cols
elif len(cols) != len(st.session_state[view]):
    st.session_state[view] = cols

column_config = {}
for column in df.columns:
    actual_type = infer_editor_type(df[column])
    selected_type = column_types.get(column, actual_type)
    editor_type = selected_type

    if actual_type in {"INTEGER", "REAL", "BOOLEAN", "DATE"} and selected_type == "TEXT":
        editor_type = actual_type

    if column.lower() == "id":
        column_config[column] = st.column_config.NumberColumn(column.upper())
    elif editor_type == "INTEGER":
        column_config[column] = st.column_config.NumberColumn(column, step=1)
    elif editor_type == "REAL":
        column_config[column] = st.column_config.NumberColumn(column)
    elif editor_type == "BOOLEAN":
        column_config[column] = st.column_config.CheckboxColumn(column)
    else:
        column_config[column] = st.column_config.TextColumn(column)

work_df = df.copy()
work_df[seed] = ""

column_config[seed] = None

grid = st.data_editor(
    work_df,
    width="stretch",
    num_rows="dynamic",
    hide_index=False,
    column_order=cols,
    column_config=column_config,
    key=f"editor_{selected_table}",
)

cols = [c for c in grid.columns if c in df.columns]
if cols:
    st.session_state[view] = cols
elif df.columns.tolist():
    st.session_state[view] = list(df.columns)

candidate_save_df = merge_visible_and_hidden_columns(grid, df)

st.markdown("</div>", unsafe_allow_html=True)

if save_clicked:
    valid, message = validate_no_nulls(candidate_save_df)
    if not valid:
        st.error(message)
    else:
        try:
            save_table(engine, selected_table, candidate_save_df)
            st.success("Changes saved successfully.")
            st.rerun()
        except Exception as e:
            st.error(f"Save failed: {e}")

if st.session_state.get("show_add_column", False):
    st.markdown("---")
    st.markdown("### Add Column")
    col1, col2, col3 = st.columns([1.4, 1, 0.9])
    with col1:
        new_column_name = st.text_input("Column Name", key="new_column_name")
    with col2:
        new_column_type = st.selectbox("Data Type", DATA_TYPE_OPTIONS, key="new_column_type")
    with col3:
        st.markdown("<div style='height: 1.8rem;'></div>", unsafe_allow_html=True)
        add_column_submit = st.button("Add to Table", width="stretch", type="primary", key="add_column_submit")

    if add_column_submit:
        try:
            add_column(engine, selected_table, new_column_name, new_column_type)
            st.session_state[f"column_types_{selected_table}"][new_column_name] = new_column_type
            st.success(f"Column '{new_column_name}' added successfully.")
            st.session_state.show_add_column = False
            st.rerun()
        except Exception as e:
            st.error(f"Could not add column: {e}")

if st.session_state.get("show_create", False):
    st.markdown("---")
    st.markdown("### Create New Table")

    table_name = st.text_input("Table Name", key="new_table_name")
    columns = st.text_area(
        "Columns (name:TYPE)",
        """id:INTEGER PRIMARY KEY
name:TEXT
created_at:DATE""",
        height=150,
        key="new_table_columns",
    )

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Create Table", width="stretch", type="primary", key="new_table_create"):
            try:
                cols = parse_columns(columns, db_type)
                create_table(engine, table_name, cols)
                st.success("New table created successfully.")
                st.session_state.show_create = False
                st.rerun()
            except Exception as e:
                st.error(f"Create failed: {e}")
    with c2:
        if st.button("Cancel", width="stretch", key="cancel_create"):
            st.session_state.show_create = False
            st.rerun()

st.markdown(
    f"""
    <div class="status-bar">
        Connected to {db_type.upper()} • {selected_table} • {column_count} columns • {row_count} rows
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)
