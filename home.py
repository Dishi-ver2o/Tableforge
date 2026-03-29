import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="TableForge",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CSS STYLING
# ============================================================
st.markdown("""
<style>
/* ===== FONTS & GENERAL ===== */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@600;700;800&display=swap');
* { margin:0; padding:0; box-sizing:border-box; }
html, body, [class*="css"] { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }

/* ===== BACKGROUND ===== */
body { 
    background: linear-gradient(135deg, #0b0e27 0%, #1a0f3f 50%, #0d1b2a 100%);
    background-attachment: fixed; 
    color: #e2e8f0; 
}
.main { background: transparent; }

/* ===== SCROLLBAR ===== */
::-webkit-scrollbar { width:10px; }
::-webkit-scrollbar-track { background: rgba(15, 23, 42, 0.5); }
::-webkit-scrollbar-thumb { background: linear-gradient(180deg, #7c3aed, #06b6d4); border-radius:10px; }
::-webkit-scrollbar-thumb:hover { background: linear-gradient(180deg, #6d28d9, #0891b2); }

/* ===== NAVBAR ===== */
.navbar-container {
    display:flex; justify-content:flex-start; align-items:center;
    padding:20px 40px; background: rgba(15,23,42,0.4);
    backdrop-filter: blur(10px); border-bottom: 1px solid rgba(124,58,237,0.1);
    border-radius:0 0 20px 20px; margin-bottom:40px; position:sticky; top:0;
    z-index:1000; box-shadow:0 8px 32px rgba(0,0,0,0.3);
}
.logo {
    font-size:28px; font-weight:800; background: linear-gradient(90deg,#7c3aed,#06b6d4);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    letter-spacing:-0.5px; font-family:'Poppins', sans-serif; transition: all 0.3s ease;
}
.logo:hover { filter: drop-shadow(0 0 20px rgba(124,58,237,0.5)); }

/* ===== HERO SECTION ===== */
.hero-container { text-align:center; padding:80px 40px; position:relative; overflow:hidden; display:flex; flex-direction:column; align-items:center; justify-content:center; }
.hero-glow {
    position:absolute; width:600px; height:600px;
    background:radial-gradient(circle, rgba(124,58,237,0.35), transparent 70%);
    filter: blur(100px); top:-100px; left:50%; transform:translateX(-50%); z-index:-1;
}
.hero-title {
    font-size:80px; font-weight:800; background: linear-gradient(135deg,#7c3aed 0%,#06b6d4 50%,#ec4899 100%);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    margin-bottom:20px; letter-spacing:-2px; font-family:'Poppins',sans-serif; line-height:1.1;
    text-shadow:0 0 40px rgba(124,58,237,0.2);
}
.hero-subtitle { font-size:24px; color:#94a3b8; margin-bottom:20px; font-weight:600; line-height:1.4; }
.hero-description { font-size:17px; color:#cbd5e1; line-height:1.7; max-width:700px; margin-bottom:50px; text-align:center; }

/* ===== SECTION TITLE ===== */
.section-title {
    text-align:center; font-size:48px; font-weight:800; margin:100px 0 60px 0;
    color:white; font-family:'Poppins',sans-serif; letter-spacing:-1px; position:relative; z-index:1;
}
.section-title::after {
    content:''; display:block; width:60px; height:4px;
    background:linear-gradient(90deg,#7c3aed,#06b6d4); margin:20px auto 0; border-radius:2px;
}

/* ===== FEATURE CARDS ===== */
.feature-card {
    background: linear-gradient(135deg, rgba(15,23,42,0.8), rgba(30,41,59,0.6));
    padding:40px; border-radius:16px; text-align:center; border:1px solid rgba(124,58,237,0.2);
    transition:all 0.4s cubic-bezier(0.23,1,0.32,1); backdrop-filter:blur(10px); position:relative; overflow:hidden;
}
.feature-card::before {
    content:''; position:absolute; top:0; left:0; right:0; bottom:0;
    background:linear-gradient(135deg, rgba(124,58,237,0.1), rgba(6,182,212,0.1));
    opacity:0; transition:opacity 0.4s ease; z-index:-1;
}
.feature-card:hover {
    transform:translateY(-12px); border:1px solid rgba(124,58,237,0.6);
    box-shadow:0 20px 50px rgba(124,58,237,0.3), inset 0 1px 0 rgba(255,255,255,0.1);
    background: linear-gradient(135deg, rgba(15,23,42,0.9), rgba(30,41,59,0.8));
}
.feature-card:hover::before { opacity:1; }
.feature-icon { font-size:48px; margin-bottom:15px; display:inline-block; animation: float 3s ease-in-out infinite; }
@keyframes float { 0%,100%{ transform:translateY(0px);} 50%{ transform:translateY(-10px);} }
.feature-card:hover .feature-icon { animation: float 1s ease-in-out infinite; }
.feature-card h3 { font-size:22px; font-weight:700; margin-bottom:15px; color:#f1f5f9; font-family:'Poppins',sans-serif; }
.feature-card p { font-size:15px; color:#cbd5e1; line-height:1.6; margin:0; }

/* ===== FOOTER ===== */
.footer { text-align:center; color:#64748b; padding:40px 20px; font-size:15px; margin-top:80px; }
.footer-text {
    background: linear-gradient(90deg, #64748b, #94a3b8);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    background-clip:text; font-weight:600; transition:all 0.3s ease;
}
.footer-text:hover {
    background: linear-gradient(90deg, #7c3aed, #06b6d4);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    background-clip:text;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# NAVBAR (without links)
# ============================================================
st.markdown("""
<div class="navbar-container">
    <div class="logo">📊 TableForge</div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# HERO SECTION
# ============================================================
st.markdown("""
<div class="hero-container">
    <div class="hero-glow"></div>
    <h1 class="hero-title">TableForge</h1>
    <p class="hero-subtitle">Work with real databases like a spreadsheet.</p>
    <p class="hero-description">
        Connect databases, explore tables, and edit data visually — no SQL needed. 
        Experience database management that feels natural and intuitive.
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# FEATURES SECTION
# ============================================================
st.markdown('<div class="section-title">Why TableForge?</div>', unsafe_allow_html=True)

f1, f2, f3 = st.columns(3, gap="large")

with f1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <h3>Spreadsheet Editing</h3>
        <p>Edit database tables like Excel or Google Sheets. Intuitive, familiar interface that feels natural to use.</p>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🗄️</div>
        <h3>Connect Real Databases</h3>
        <p>Works with SQLite, MySQL, and PostgreSQL. Use your own databases without proprietary lock-in.</p>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <h3>No SQL Needed</h3>
        <p>Perfect for beginners and non-technical users. Zero SQL knowledge required. Just point and click.</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown("""
<div class="footer">
    <p class="footer-text">🚀 Built with ❤️ by Team CodeX | Revolutionizing Database Management</p>
</div>
""", unsafe_allow_html=True)