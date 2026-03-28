import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests
from sqlalchemy import create_engine, inspect

# Set page config
st.set_page_config(
    page_title="Connect Database - TableForge",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Modern CSS with hover effects, glow, and animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #0f0f1e 0%, #1a1a2e 50%, #16213e 100%);
        color: #fff;
        min-height: 100vh;
    }
    
    /* Header styling */
    .header-container {
        text-align: center;
        padding: 3rem 0 2rem 0;
        margin-bottom: 2rem;
        animation: fadeInDown 0.8s ease-out;
    }
    
    .header-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #00d4ff 0%, #0099ff 50%, #00ccff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
        text-shadow: 0 0 30px rgba(0, 212, 255, 0.3);
        letter-spacing: -1px;
    }
    
    .header-subtitle {
        font-size: 1.1rem;
        color: #b0b0c0;
        margin-top: 0.5rem;
        font-weight: 300;
        letter-spacing: 1px;
    }
    
    /* Database selection cards */
    .db-selector-container {
        display: flex;
        gap: 1.5rem;
        margin: 3rem 0;
        justify-content: center;
        flex-wrap: wrap;
        animation: fadeInUp 0.8s ease-out 0.2s both;
    }
    
    .db-btn-wrapper {
        position: relative;
    }
    
    .db-btn {
        padding: 1.5rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        border: 2px solid transparent;
        border-radius: 15px;
        background: linear-gradient(135deg, #1f3a5f 0%, #16213e 100%);
        color: #00d4ff;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(0, 212, 255, 0.1);
        min-width: 200px;
        text-align: center;
    }
    
    .db-btn::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 212, 255, 0.3), transparent);
        transition: left 0.5s;
    }
    
    .db-btn:hover::before {
        left: 100%;
    }
    
    .db-btn:hover {
        border-color: #00d4ff;
        background: linear-gradient(135deg, #0066cc 0%, #1f3a5f 100%);
        box-shadow: 0 0 40px rgba(0, 212, 255, 0.6), 0 8px 32px rgba(0, 212, 255, 0.3);
        transform: translateY(-5px);
    }
    
    .db-btn:active {
        transform: translateY(-2px);
    }
    
    /* Form container */
    .form-container {
        background: linear-gradient(135deg, rgba(31, 58, 95, 0.3) 0%, rgba(22, 33, 62, 0.3) 100%);
        border: 1px solid rgba(0, 212, 255, 0.2);
        border-radius: 20px;
        padding: 2.5rem;
        margin: 2rem auto;
        max-width: 600px;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(0, 212, 255, 0.1);
        animation: fadeInUp 0.8s ease-out 0.4s both;
        border-top: 2px solid rgba(0, 212, 255, 0.4);
    }
    
    .form-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #00d4ff;
        margin-bottom: 1.5rem;
        text-align: center;
        letter-spacing: 0.5px;
    }
    
    /* Input fields */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 2px solid rgba(0, 212, 255, 0.2) !important;
        border-radius: 12px !important;
        color: #fff !important;
        padding: 0.8rem 1rem !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(5px) !important;
    }
    
    .stTextInput > div > div > input:hover,
    .stNumberInput > div > div > input:hover,
    .stSelectbox > div > div > select:hover {
        border-color: rgba(0, 212, 255, 0.6) !important;
        background: rgba(0, 212, 255, 0.05) !important;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.2) !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #00d4ff !important;
        box-shadow: 0 0 25px rgba(0, 212, 255, 0.4), inset 0 0 10px rgba(0, 212, 255, 0.1) !important;
        background: rgba(0, 212, 255, 0.08) !important;
    }
    
    /* Submit button */
    .stFormSubmitButton > button {
        width: 100%;
        padding: 1rem !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        background: linear-gradient(135deg, #00d4ff 0%, #0099ff 100%) !important;
        color: #000 !important;
        border: none !important;
        border-radius: 12px !important;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        position: relative;
        overflow: hidden;
        box-shadow: 0 10px 40px rgba(0, 212, 255, 0.3) !important;
    }
    
    .stFormSubmitButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 15px 50px rgba(0, 212, 255, 0.5), 0 0 30px rgba(0, 212, 255, 0.4) !important;
    }
    
    .stFormSubmitButton > button:active {
        transform: translateY(-1px) !important;
    }
    
    /* Success and error messages */
    .success-message {
        padding: 1.5rem;
        border-radius: 15px;
        background: linear-gradient(135deg, rgba(76, 175, 80, 0.2) 0%, rgba(56, 142, 60, 0.2) 100%);
        border: 2px solid rgba(76, 175, 80, 0.5);
        color: #81c784;
        margin: 1rem 0;
        font-weight: 500;
        animation: slideIn 0.5s ease-out;
        box-shadow: 0 0 20px rgba(76, 175, 80, 0.2);
    }
    
    .error-message {
        padding: 1.5rem;
        border-radius: 15px;
        background: linear-gradient(135deg, rgba(244, 67, 54, 0.2) 0%, rgba(211, 47, 47, 0.2) 100%);
        border: 2px solid rgba(244, 67, 54, 0.5);
        color: #ef5350;
        margin: 1rem 0;
        font-weight: 500;
        animation: slideIn 0.5s ease-out;
        box-shadow: 0 0 20px rgba(244, 67, 54, 0.2);
    }
    
    .info-message {
        padding: 1.5rem;
        border-radius: 15px;
        background: linear-gradient(135deg, rgba(33, 150, 243, 0.2) 0%, rgba(21, 101, 192, 0.2) 100%);
        border: 2px solid rgba(33, 150, 243, 0.5);
        color: #64b5f6;
        margin: 1rem 0;
        font-weight: 500;
        animation: slideIn 0.5s ease-out;
        box-shadow: 0 0 20px rgba(33, 150, 243, 0.2);
    }
    
    /* Status section */
    .status-container {
        background: linear-gradient(135deg, rgba(31, 58, 95, 0.4) 0%, rgba(22, 33, 62, 0.4) 100%);
        border: 2px solid rgba(76, 175, 80, 0.5);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        animation: fadeInUp 0.8s ease-out 0.6s both;
    }
    
    .status-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #81c784;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    .metric-box {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(0, 212, 255, 0.3);
        border-radius: 15px;
        padding: 1rem;
        text-align: center;
        transition: all 0.3s ease;
        margin: 0.5rem;
    }
    
    .metric-box:hover {
        border-color: rgba(0, 212, 255, 0.8);
        background: rgba(0, 212, 255, 0.1);
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.2);
        transform: translateY(-3px);
    }
    
    /* Navigation button */
    .nav-btn {
        padding: 1rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        background: linear-gradient(135deg, #00d4ff 0%, #0099ff 100%);
        color: #000;
        border: none;
        border-radius: 12px;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 10px 40px rgba(0, 212, 255, 0.3);
        width: 100%;
    }
    
    .nav-btn:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 50px rgba(0, 212, 255, 0.5), 0 0 30px rgba(0, 212, 255, 0.4);
    }
    
    /* Animations */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Divider styling */
    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(0, 212, 255, 0.3), transparent);
        margin: 2rem 0;
        border-radius: 1px;
    }
    
    /* Label styling */
    .stLabel > label {
        color: #b0d4ff !important;
        font-weight: 500 !important;
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(0, 212, 255, 0.05);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #00d4ff, #0099ff);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #00e6ff, #00b3ff);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'db_connected' not in st.session_state:
    st.session_state.db_connected = False
if 'db_type' not in st.session_state:
    st.session_state.db_type = None
if 'db_engine' not in st.session_state:
    st.session_state.db_engine = None

# Header
st.markdown("""
<div class="header-container">
    <h1 class="header-title">🗄️ TableForge Connect</h1>
    <p class="header-subtitle">Connect your database in seconds • Secure • Fast • Reliable</p>
</div>
""", unsafe_allow_html=True)

# Database Type Selection
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #b0b0c0; font-size: 1.1rem; margin: 1rem 0;'>Select Your Database Type</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    if st.button("📊 SQLite", key="sqlite_btn", use_container_width=True):
        st.session_state.db_type = "sqlite"
        st.rerun()

with col2:
    if st.button("🐘 PostgreSQL", key="postgres_btn", use_container_width=True):
        st.session_state.db_type = "postgresql"
        st.rerun()

with col3:
    if st.button("🐬 MySQL", key="mysql_btn", use_container_width=True):
        st.session_state.db_type = "mysql"
        st.rerun()

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# Display connection form based on selected database type
if st.session_state.db_type == "sqlite":
    st.markdown("<div class='form-container'>", unsafe_allow_html=True)
    st.markdown("<p class='form-title'>📊 SQLite Connection</p>", unsafe_allow_html=True)
    
    with st.form("sqlite_form"):
        db_path = st.text_input(
            "Database File Path",
            placeholder="e.g., /path/to/database.db or :memory:",
            help="Enter the path to your SQLite database file. Use ':memory:' for in-memory database."
        )
        
        submitted = st.form_submit_button("🔗 Connect to SQLite", use_container_width=True)
        
        if submitted:
            try:
                if db_path.strip() == "":
                    st.markdown("<div class='error-message'>❌ Please enter a database file path</div>", unsafe_allow_html=True)
                else:
                    engine = create_engine(f"sqlite:///{db_path}")
                    
                    with engine.connect() as conn:
                        pass
                    
                    st.session_state.db_engine = engine
                    st.session_state.db_connected = True
                    st.session_state.db_path = db_path
                    
                    st.markdown(f"<div class='success-message'>✅ Successfully connected to SQLite: {db_path}</div>", unsafe_allow_html=True)
                    
                    inspector = inspect(engine)
                    tables = inspector.get_table_names()
                    st.markdown(f"<div class='info-message'>📈 Database contains {len(tables)} table(s)</div>", unsafe_allow_html=True)
                    
            except Exception as e:
                st.markdown(f"<div class='error-message'>❌ Connection failed: {str(e)}</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.db_type == "postgresql":
    st.markdown("<div class='form-container'>", unsafe_allow_html=True)
    st.markdown("<p class='form-title'>🐘 PostgreSQL Connection</p>", unsafe_allow_html=True)
    
    with st.form("postgres_form"):
        col1, col2 = st.columns(2, gap="medium")
        
        with col1:
            host = st.text_input("Host", placeholder="localhost", value="localhost")
            port = st.number_input("Port", value=5432, min_value=1, max_value=65535)
            username = st.text_input("Username", placeholder="postgres")
        
        with col2:
            database = st.text_input("Database Name", placeholder="your_database")
            password = st.text_input("Password", type="password")
            ssl_mode = st.selectbox("SSL Mode", ["disable", "allow", "prefer", "require"])
        
        submitted = st.form_submit_button("🔗 Connect to PostgreSQL", use_container_width=True)
        
        if submitted:
            try:
                if not all([host, username, database]):
                    st.markdown("<div class='error-message'>❌ Please fill in all required fields</div>", unsafe_allow_html=True)
                else:
                    conn_str = f"postgresql://{username}:{password}@{host}:{port}/{database}"
                    engine = create_engine(conn_str)
                    
                    with engine.connect() as conn:
                        pass
                    
                    st.session_state.db_engine = engine
                    st.session_state.db_connected = True
                    st.session_state.db_config = {
                        "host": host,
                        "port": port,
                        "username": username,
                        "database": database
                    }
                    
                    st.markdown(f"<div class='success-message'>✅ Connected to PostgreSQL: {host}:{port}/{database}</div>", unsafe_allow_html=True)
                    
                    inspector = inspect(engine)
                    tables = inspector.get_table_names()
                    st.markdown(f"<div class='info-message'>📈 Database contains {len(tables)} table(s)</div>", unsafe_allow_html=True)
                    
            except Exception as e:
                st.markdown(f"<div class='error-message'>❌ Connection failed: {str(e)}</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.db_type == "mysql":
    st.markdown("<div class='form-container'>", unsafe_allow_html=True)
    st.markdown("<p class='form-title'>🐬 MySQL Connection</p>", unsafe_allow_html=True)
    
    with st.form("mysql_form"):
        col1, col2 = st.columns(2, gap="medium")
        
        with col1:
            host = st.text_input("Host", placeholder="localhost", value="localhost")
            port = st.number_input("Port", value=3306, min_value=1, max_value=65535)
            username = st.text_input("Username", placeholder="root")
        
        with col2:
            database = st.text_input("Database Name", placeholder="your_database")
            password = st.text_input("Password", type="password")
            charset = st.selectbox("Charset", ["utf8mb4", "utf8", "latin1"])
        
        submitted = st.form_submit_button("🔗 Connect to MySQL", use_container_width=True)
        
        if submitted:
            try:
                if not all([host, username, database]):
                    st.markdown("<div class='error-message'>❌ Please fill in all required fields</div>", unsafe_allow_html=True)
                else:
                    conn_str = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}?charset={charset}"
                    engine = create_engine(conn_str)
                    
                    with engine.connect() as conn:
                        pass
                    
                    st.session_state.db_engine = engine
                    st.session_state.db_connected = True
                    st.session_state.db_config = {
                        "host": host,
                        "port": port,
                        "username": username,
                        "database": database,
                        "charset": charset
                    }
                    
                    st.markdown(f"<div class='success-message'>✅ Connected to MySQL: {host}:{port}/{database}</div>", unsafe_allow_html=True)
                    
                    inspector = inspect(engine)
                    tables = inspector.get_table_names()
                    st.markdown(f"<div class='info-message'>📈 Database contains {len(tables)} table(s)</div>", unsafe_allow_html=True)
                    
            except Exception as e:
                st.markdown(f"<div class='error-message'>❌ Connection failed: {str(e)}</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

else:
    st.markdown("""
    <div style='text-align: center; padding: 3rem 0;'>
        <p style='font-size: 1.3rem; color: #b0d4ff; margin-bottom: 1rem;'>👈 Select a database type to get started</p>
        <div style='display: flex; justify-content: center; gap: 1rem; margin-top: 2rem;'>
            <span style='color: #00d4ff; font-size: 3rem;'>📊</span>
            <span style='color: #00ccff; font-size: 3rem;'>🐘</span>
            <span style='color: #0099ff; font-size: 3rem;'>🐬</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Display connection status
if st.session_state.db_connected:
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("<div class='status-container'>", unsafe_allow_html=True)
    st.markdown("<p class='status-title'>✅ Connection Status</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        st.markdown("""
        <div class='metric-box'>
            <p style='color: #b0b0c0; font-size: 0.9rem; margin-bottom: 0.5rem;'>Status</p>
            <p style='font-size: 1.5rem; color: #81c784; font-weight: 700;'>🟢 Connected</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='metric-box'>
            <p style='color: #b0b0c0; font-size: 0.9rem; margin-bottom: 0.5rem;'>Database Type</p>
            <p style='font-size: 1.5rem; color: #00d4ff; font-weight: 700;'>{st.session_state.db_type.upper()}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        if st.button("🔌 Disconnect", use_container_width=True):
            st.session_state.db_connected = False
            st.session_state.db_engine = None
            st.session_state.db_type = None
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Navigation
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 3])
    with col2:
        if st.button("➡️ Continue to Table Editor", use_container_width=True, key="next_page"):
            st.switch_page("pages/3_Table_Editor.py")