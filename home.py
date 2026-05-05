import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="TableForge",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "show_home_menu" not in st.session_state:
    st.session_state.show_home_menu = False

# ============================================================
# CSS + ANIMATIONS
# ============================================================
st.markdown("""
<style>
/* ===== FONTS & GENERAL ===== */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --bg-start: #060816;
    --bg-mid: #0f1732;
    --bg-end: #15102a;
    --text-primary: #e5ecf6;
    --text-secondary: #97a6bd;
    --text-muted: #6e7f98;
    --surface-1: rgba(11, 18, 36, 0.72);
    --surface-2: rgba(20, 29, 52, 0.82);
    --border-soft: rgba(148, 163, 184, 0.18);
    --border-strong: rgba(125, 211, 252, 0.18);
    --shadow-hero: 0 30px 90px rgba(2, 6, 23, 0.45);
    --shadow-card: 0 20px 50px rgba(15, 23, 42, 0.22);
    --hero-highlight: rgba(255, 255, 255, 0.72);
}

@media (prefers-color-scheme: light) {
    :root {
        --bg-start: #f6f8fc;
        --bg-mid: #eef3fb;
        --bg-end: #fdf7fb;
        --text-primary: #132033;
        --text-secondary: #4f617c;
        --text-muted: #6c7b91;
        --surface-1: rgba(255, 255, 255, 0.9);
        --surface-2: rgba(246, 249, 255, 0.92);
        --border-soft: rgba(15, 23, 42, 0.1);
        --border-strong: rgba(14, 165, 233, 0.16);
        --shadow-hero: 0 28px 80px rgba(15, 23, 42, 0.14);
        --shadow-card: 0 20px 45px rgba(15, 23, 42, 0.12);
        --hero-highlight: rgba(255, 255, 255, 0.92);
    }
}

* { margin:0; padding:0; box-sizing:border-box; }

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

/* ===== BACKGROUND ===== */
body {
    background: linear-gradient(135deg, var(--bg-start) 0%, var(--bg-mid) 45%, var(--bg-end) 100%);
    background-attachment: fixed;
    color: var(--text-primary);
}

.main { background: transparent; }

.block-container {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
}

[data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] > .main,
[data-testid="stMain"] {
    background: transparent;
}

/* Hide Streamlit elements for cleaner look */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }

/* ===== SCROLLBAR ===== */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: rgba(15, 23, 42, 0.3); }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #7c3aed, #06b6d4);
    border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(180deg, #a855f7, #22d3ee);
}

/* ===== KEYFRAMES ===== */
@keyframes float {
    0%, 100% { transform: translateY(0) rotate(0deg) scale(1); }
    33% { transform: translateY(-28px) rotate(4deg) scale(1.05); }
    66% { transform: translateY(14px) rotate(-3deg) scale(0.98); }
}

@keyframes float-reverse {
    0%, 100% { transform: translateY(0) rotate(0deg) scale(1); }
    33% { transform: translateY(20px) rotate(-4deg) scale(0.98); }
    66% { transform: translateY(-32px) rotate(3deg) scale(1.06); }
}

@keyframes pulse-glow {
    0%, 100% { opacity: 0.48; transform: scale(1); }
    50% { opacity: 0.9; transform: scale(1.12); }
}

@keyframes shimmer {
    0% { background-position: -200% center; }
    100% { background-position: 200% center; }
}

@keyframes gradient-shift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(40px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeInScale {
    from { opacity: 0; transform: scale(0.9); }
    to { opacity: 1; transform: scale(1); }
}

@keyframes borderRotate {
    0% { --angle: 0deg; }
    100% { --angle: 360deg; }
}

@keyframes typing {
    from { width: 0; }
    to { width: 100%; }
}

@keyframes blink-caret {
    from, to { border-color: transparent; }
    50% { border-color: #7c3aed; }
}

@keyframes particle-drift {
    0% { transform: translateY(0) translateX(0) scale(0.7); opacity: 0; }
    10% { opacity: 0.95; }
    50% { transform: translateY(-48vh) translateX(18px) scale(1.2); opacity: 1; }
    90% { opacity: 0.95; }
    100% { transform: translateY(-100vh) translateX(60px) scale(0.8); opacity: 0; }
}

@keyframes orb-drift {
    0%, 100% { transform: translate3d(0, 0, 0) scale(1); }
    35% { transform: translate3d(30px, -24px, 0) scale(1.08); }
    70% { transform: translate3d(-22px, 18px, 0) scale(0.95); }
}

@keyframes icon-flicker {
    0%, 100% { opacity: 0.22; filter: drop-shadow(0 0 0 rgba(125, 211, 252, 0)); }
    50% { opacity: 0.46; filter: drop-shadow(0 0 14px rgba(125, 211, 252, 0.35)); }
}

@keyframes orbit {
    from { transform: rotate(0deg) translateX(160px) rotate(0deg); }
    to { transform: rotate(360deg) translateX(160px) rotate(-360deg); }
}

@keyframes spin-slow {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

/* ===== FLOATING ORBS (background decoration) ===== */
.orb-container {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}

.orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(58px);
    animation: pulse-glow 5.4s ease-in-out infinite, orb-drift 12s ease-in-out infinite;
}

.orb-1 {
    width: 500px; height: 500px;
    background: radial-gradient(circle, rgba(124,58,237,0.34), transparent 72%);
    top: -10%; left: -5%;
    animation-delay: 0s;
}

.orb-2 {
    width: 400px; height: 400px;
    background: radial-gradient(circle, rgba(6,182,212,0.3), transparent 72%);
    top: 40%; right: -8%;
    animation-delay: 2s;
}

.orb-3 {
    width: 350px; height: 350px;
    background: radial-gradient(circle, rgba(236,72,153,0.24), transparent 72%);
    bottom: -5%; left: 30%;
    animation-delay: 4s;
}

.orb-4 {
    width: 250px; height: 250px;
    background: radial-gradient(circle, rgba(124,58,237,0.28), transparent 72%);
    top: 60%; left: 10%;
    animation-delay: 1s;
}

/* ===== PARTICLES ===== */
.particles {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}

.particle {
    position: absolute;
    bottom: -10px;
    width: 5px; height: 5px;
    background: rgba(124, 58, 237, 0.78);
    border-radius: 50%;
    animation: particle-drift linear infinite;
    box-shadow: 0 0 12px rgba(125, 211, 252, 0.26);
}

.particle:nth-child(1) { left: 10%; animation-duration: 9s; animation-delay: 0s; background: rgba(124,58,237,0.74); }
.particle:nth-child(2) { left: 20%; animation-duration: 11s; animation-delay: 2s; background: rgba(6,182,212,0.78); width: 4px; height: 4px; }
.particle:nth-child(3) { left: 35%; animation-duration: 8s; animation-delay: 4s; background: rgba(236,72,153,0.68); }
.particle:nth-child(4) { left: 50%; animation-duration: 12s; animation-delay: 1s; background: rgba(124,58,237,0.62); width: 6px; height: 6px; }
.particle:nth-child(5) { left: 65%; animation-duration: 10s; animation-delay: 3s; background: rgba(6,182,212,0.7); }
.particle:nth-child(6) { left: 75%; animation-duration: 8.5s; animation-delay: 5s; background: rgba(236,72,153,0.74); width: 4px; height: 4px; }
.particle:nth-child(7) { left: 85%; animation-duration: 11.5s; animation-delay: 0.5s; background: rgba(124,58,237,0.72); }
.particle:nth-child(8) { left: 45%; animation-duration: 13s; animation-delay: 6s; background: rgba(6,182,212,0.62); width: 6px; height: 6px; }
.particle:nth-child(9) { left: 5%;  animation-duration: 9.5s; animation-delay: 7s; background: rgba(236,72,153,0.62); }
.particle:nth-child(10){ left: 90%; animation-duration: 12.5s; animation-delay: 1.5s; background: rgba(124,58,237,0.76); width: 4px; height: 4px; }

/* ===== NAVBAR ===== */
.navbar-container {
    width: 100vw;
    margin: 0 0 12px calc(50% - 50vw);
    padding: 42px 24px 38px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 28px;
    background:
        radial-gradient(circle at 18% 24%, rgba(255,255,255,0.16), transparent 20%),
        radial-gradient(circle at 82% 28%, rgba(255,255,255,0.14), transparent 20%),
        linear-gradient(135deg, rgba(17, 57, 110, 0.98) 0%, rgba(17, 45, 90, 0.99) 42%, rgba(28, 63, 119, 0.98) 100%);
    backdrop-filter: blur(18px) saturate(160%);
    -webkit-backdrop-filter: blur(18px) saturate(160%);
    border-top: 1px solid rgba(255,255,255,0.12);
    border-bottom: 1px solid rgba(255,255,255,0.14);
    border-radius: 0;
    position: sticky;
    top: 0;
    z-index: 1000;
    overflow: hidden;
    min-height: 220px;
    box-shadow: 0 18px 40px rgba(6, 20, 46, 0.24), inset 0 1px 0 rgba(255,255,255,0.08);
    animation: fadeInUp 0.6s ease-out;
}

.navbar-container::before {
    content: "";
    position: absolute;
    inset: 0;
    background:
        linear-gradient(rgba(255,255,255,0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.05) 1px, transparent 1px);
    background-size: 48px 48px;
    opacity: 0.32;
    pointer-events: none;
}

.navbar-container::after {
    content: "";
    position: absolute;
    left: 50%;
    bottom: 14px;
    width: min(78vw, 1100px);
    height: 110px;
    background:
        radial-gradient(circle at 12% 50%, rgba(109, 198, 255, 0.22), transparent 18%),
        radial-gradient(circle at 88% 50%, rgba(109, 198, 255, 0.22), transparent 18%),
        linear-gradient(90deg, transparent 0%, rgba(109, 198, 255, 0.12) 18%, rgba(109, 198, 255, 0.22) 50%, rgba(109, 198, 255, 0.12) 82%, transparent 100%);
    transform: translateX(-50%);
    filter: blur(22px);
    opacity: 0.88;
    pointer-events: none;
}

.navbar-inner {
    width: min(100%, 1220px);
    margin: 0 auto;
    min-height: 140px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 28px;
    position: relative;
    z-index: 1;
    text-align: center;
}

.navbar-menu-slot {
    position: absolute;
    left: 34px;
    top: 34px;
    z-index: 3;
}

.logo {
    font-size: clamp(34px, 3.4vw, 56px);
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -1.2px;
    font-family: 'Poppins', sans-serif;
    text-shadow: 0 10px 30px rgba(6, 20, 46, 0.28);
    white-space: nowrap;
    text-align: center;
}

.nav-links {
    display: flex;
    gap: clamp(18px, 2vw, 42px);
    align-items: center;
    flex-wrap: wrap;
    justify-content: center;
    width: min(100%, 1040px);
}

.nav-link {
    color: rgba(255,255,255,0.96);
    font-size: clamp(12px, 0.95vw, 15px);
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    transition: all 0.3s ease;
    position: relative;
    padding-bottom: 4px;
    white-space: nowrap;
}

.nav-link::after {
    content: "";
    position: absolute;
    left: 0;
    bottom: -3px;
    width: 100%;
    height: 2px;
    border-radius: 999px;
    background: rgba(255,255,255,0.9);
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.25s ease;
}

.nav-link:hover::after {
    transform: scaleX(1);
}

.nav-badge {
    background: linear-gradient(135deg, rgba(124,58,237,0.18), rgba(14,165,233,0.18));
    color: var(--text-primary);
    padding: 8px 16px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.5px;
    border: 1px solid var(--border-strong);
    box-shadow: 0 8px 20px rgba(14, 165, 233, 0.08);
}

/* ===== FLOATING MENU ===== */
.menu-anchor {
    width: min(260px, 100%);
    margin: -206px 0 0 34px;
    position: relative;
    z-index: 1100;
}

div[data-testid="stButton"] > button[kind="secondary"],
div[data-testid="stButton"] > button[kind="primary"],
div[data-testid="stButton"] > button {
    border-radius: 999px;
    min-height: 46px;
    padding: 0 16px;
    border: 1px solid rgba(125, 211, 252, 0.22);
    background: linear-gradient(135deg, rgba(20, 61, 117, 0.94), rgba(28, 83, 152, 0.94));
    color: #f8fbff;
    font-weight: 700;
    letter-spacing: 0.02em;
    box-shadow: 0 14px 32px rgba(2, 6, 23, 0.18), inset 0 1px 0 rgba(255,255,255,0.08);
}

div[data-testid="stButton"] > button:hover {
    border-color: rgba(125, 211, 252, 0.36);
    background: linear-gradient(135deg, rgba(23, 69, 131, 0.98), rgba(30, 92, 164, 0.98));
    color: #ffffff;
}

.menu-links {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 14px;
    flex-wrap: wrap;
    margin-top: 14px;
}

.menu-links div[data-testid="stPageLink"] {
    width: auto;
    margin-bottom: 0;
}

.menu-links div[data-testid="stPageLink"] a {
    width: auto;
    min-width: 132px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 12px 18px;
    border-radius: 999px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(148, 163, 184, 0.16);
    color: #e5ecf6;
    font-size: 15px;
    font-weight: 600;
    text-decoration: none;
    transition: transform 0.2s ease, background 0.2s ease, border-color 0.2s ease;
}

.menu-links div[data-testid="stPageLink"] a:hover {
    transform: translateY(-1px);
    background: rgba(255,255,255,0.12);
    border-color: rgba(125, 211, 252, 0.28);
    color: #ffffff;
}

.menu-links div[data-testid="stPageLink"] a[aria-current="page"] {
    background: linear-gradient(135deg, rgba(224, 231, 255, 0.95), rgba(214, 221, 236, 0.94));
    border-color: rgba(224, 231, 255, 0.92);
    color: #183153;
    font-weight: 700;
}

.menu-spacer {
    height: 0;
}

/* ===== HERO SECTION ===== */
.hero-container {
    display: none !important;
    text-align: center;
    padding: 100px 40px 72px;
    position: relative;
    overflow: visible;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 70vh;
}

.hero-glow {
    position: absolute;
    width: 920px; height: 920px;
    background:
        radial-gradient(circle at 30% 30%, rgba(124,58,237,0.22) 0%, transparent 30%),
        radial-gradient(circle at 68% 38%, rgba(14,165,233,0.18) 0%, transparent 32%),
        radial-gradient(circle at 50% 70%, rgba(236,72,153,0.12) 0%, transparent 38%);
    filter: blur(120px);
    top: -240px;
    left: 50%;
    transform: translateX(-50%);
    z-index: -1;
    animation: pulse-glow 8s ease-in-out infinite;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: linear-gradient(135deg, rgba(124,58,237,0.12), rgba(14,165,233,0.08));
    border: 1px solid var(--border-strong);
    padding: 8px 20px;
    border-radius: 50px;
    font-size: 13px;
    color: var(--text-secondary);
    font-weight: 500;
    margin-bottom: 30px;
    backdrop-filter: blur(10px);
    animation: fadeInUp 0.8s ease-out 0.2s both;
    letter-spacing: 0.5px;
}

.hero-badge-dot {
    width: 8px; height: 8px;
    background: #22c55e;
    border-radius: 50%;
    animation: pulse-glow 2s ease-in-out infinite;
    box-shadow: 0 0 8px rgba(34,197,94,0.6);
}

.hero-title {
    font-size: 82px;
    font-weight: 800;
    background: linear-gradient(135deg, var(--text-primary) 0%, #8b5cf6 34%, #0ea5e9 64%, #ec4899 100%);
    background-size: 300% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 24px;
    letter-spacing: -3px;
    font-family: 'Poppins', sans-serif;
    line-height: 1.05;
    animation: fadeInUp 0.8s ease-out 0.4s both, gradient-shift 6s ease-in-out infinite;
}

.hero-subtitle {
    font-size: 22px;
    color: var(--text-secondary);
    margin-bottom: 16px;
    font-weight: 400;
    line-height: 1.5;
    animation: fadeInUp 0.8s ease-out 0.6s both;
}

.hero-subtitle strong {
    color: var(--text-primary);
    font-weight: 600;
}

.hero-description {
    font-size: 16px;
    color: var(--text-muted);
    line-height: 1.8;
    max-width: 600px;
    margin-bottom: 56px;
    text-align: center;
    animation: fadeInUp 0.8s ease-out 0.8s both;
}

/* ===== HERO SHOWCASE ===== */
.hero-visual-shell {
    width: min(1120px, 100%);
    padding: 18px;
    border-radius: 36px;
    background:
        linear-gradient(135deg, rgba(255,255,255,0.3), rgba(255,255,255,0.05)),
        linear-gradient(135deg, rgba(124,58,237,0.12), rgba(14,165,233,0.08), rgba(236,72,153,0.08));
    box-shadow: var(--shadow-hero);
    border: 1px solid rgba(255,255,255,0.18);
    animation: fadeInScale 1s ease-out 1s both;
}

.hero-showcase {
    display: grid;
    grid-template-columns: 1.3fr 0.9fr;
    gap: 22px;
    padding: 28px;
    border-radius: 28px;
    background:
        radial-gradient(circle at top left, rgba(255,255,255,0.18), transparent 32%),
        linear-gradient(145deg, var(--surface-1), var(--surface-2));
    border: 1px solid var(--border-soft);
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.16);
    overflow: hidden;
    position: relative;
}

.hero-showcase::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.04), transparent 40%, rgba(14,165,233,0.04));
    pointer-events: none;
}

.showcase-panel,
.showcase-side {
    position: relative;
    z-index: 1;
}

.showcase-panel {
    padding: 24px;
    border-radius: 24px;
    background: linear-gradient(180deg, rgba(255,255,255,0.14), rgba(255,255,255,0.04));
    border: 1px solid var(--border-soft);
    box-shadow: var(--shadow-card);
    text-align: left;
    transition: transform 0.35s ease, box-shadow 0.35s ease;
}

.hero-visual-shell:hover .showcase-panel,
.hero-visual-shell:hover .showcase-side-card {
    transform: translateY(-4px);
    box-shadow: 0 28px 56px rgba(15, 23, 42, 0.18);
}

.showcase-topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 24px;
    gap: 16px;
}

.showcase-brand {
    display: flex;
    align-items: center;
    gap: 12px;
}

.showcase-logo {
    width: 44px;
    height: 44px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    color: #fff;
    background: linear-gradient(135deg, #7c3aed, #0ea5e9);
    box-shadow: 0 10px 24px rgba(14, 165, 233, 0.2);
}

.showcase-brand-text strong,
.showcase-side h3 {
    display: block;
    color: var(--text-primary);
}

.showcase-brand-text strong {
    font-size: 17px;
    margin-bottom: 4px;
}

.showcase-brand-text span,
.showcase-caption,
.showcase-list li {
    color: var(--text-secondary);
}

.showcase-status {
    padding: 8px 14px;
    border-radius: 999px;
    background: rgba(16, 185, 129, 0.12);
    border: 1px solid rgba(16, 185, 129, 0.22);
    color: #10b981;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.showcase-window {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 18px;
    align-items: stretch;
}

.showcase-card-surface {
    border-radius: 22px;
    background: linear-gradient(180deg, var(--hero-highlight), rgba(255,255,255,0.62));
    border: 1px solid rgba(255,255,255,0.45);
    box-shadow: 0 16px 34px rgba(15, 23, 42, 0.1);
    padding: 20px;
}

.showcase-header-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
    gap: 12px;
}

.showcase-header-row strong {
    color: #132033;
    font-size: 15px;
}

.showcase-pill {
    padding: 7px 12px;
    border-radius: 999px;
    background: linear-gradient(135deg, rgba(124,58,237,0.14), rgba(14,165,233,0.14));
    color: #394b63;
    font-size: 12px;
    font-weight: 700;
}

.showcase-grid {
    display: grid;
    gap: 12px;
}

.showcase-row {
    display: grid;
    grid-template-columns: 1.5fr 1fr 1fr;
    gap: 10px;
}

.showcase-cell {
    padding: 12px 14px;
    border-radius: 14px;
    background: rgba(255,255,255,0.78);
    color: #203046;
    font-size: 13px;
    font-weight: 600;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.65);
}

.showcase-row.header .showcase-cell {
    background: linear-gradient(135deg, rgba(124,58,237,0.14), rgba(14,165,233,0.12));
    color: #334155;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.showcase-accent {
    background: linear-gradient(135deg, rgba(59,130,246,0.16), rgba(14,165,233,0.12));
}

.showcase-side {
    display: grid;
    gap: 18px;
}

.showcase-side-card {
    padding: 22px;
    border-radius: 24px;
    background: linear-gradient(180deg, rgba(255,255,255,0.14), rgba(255,255,255,0.05));
    border: 1px solid var(--border-soft);
    box-shadow: var(--shadow-card);
    text-align: left;
    transition: transform 0.35s ease, box-shadow 0.35s ease;
}

.showcase-chart {
    height: 154px;
    border-radius: 18px;
    position: relative;
    overflow: hidden;
    background:
        linear-gradient(180deg, rgba(255,255,255,0.09), rgba(255,255,255,0.02)),
        linear-gradient(135deg, rgba(14,165,233,0.18), rgba(124,58,237,0.18));
}

.showcase-chart::before {
    content: '';
    position: absolute;
    inset: 18px 16px 22px;
    border-radius: 14px;
    background:
        linear-gradient(to top, rgba(255,255,255,0.08) 1px, transparent 1px) 0 0 / 100% 32px,
        linear-gradient(to right, rgba(255,255,255,0.06) 1px, transparent 1px) 0 0 / 25% 100%;
}

.showcase-chart::after {
    content: '';
    position: absolute;
    left: 18px;
    right: 18px;
    bottom: 26px;
    height: 70px;
    border-radius: 999px;
    background: linear-gradient(90deg, rgba(124,58,237,0.65), rgba(14,165,233,0.85), rgba(236,72,153,0.7));
    clip-path: polygon(0 88%, 14% 76%, 28% 80%, 42% 48%, 58% 56%, 72% 28%, 86% 38%, 100% 0, 100% 100%, 0 100%);
    box-shadow: 0 14px 34px rgba(14, 165, 233, 0.2);
}

.showcase-metrics {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 12px;
}

.metric-pill {
    padding: 16px;
    border-radius: 18px;
    background: linear-gradient(180deg, rgba(255,255,255,0.16), rgba(255,255,255,0.06));
    border: 1px solid var(--border-soft);
}

.metric-pill strong {
    display: block;
    color: var(--text-primary);
    font-size: 26px;
    margin-bottom: 4px;
}

.metric-pill span {
    color: var(--text-secondary);
    font-size: 13px;
}

.showcase-caption {
    font-size: 14px;
    line-height: 1.7;
    margin-top: 10px;
}

.showcase-list {
    list-style: none;
    display: grid;
    gap: 12px;
    margin-top: 16px;
}

.showcase-list li {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 14px;
}

.showcase-list-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: linear-gradient(135deg, #7c3aed, #0ea5e9);
    box-shadow: 0 0 0 5px rgba(14,165,233,0.08);
}

/* ===== FLOATING ICONS around hero ===== */
.hero-floating-icons {
    position: absolute;
    width: 100%; height: 100%;
    top: 0; left: 0;
    pointer-events: none;
    z-index: 0;
}

.hero-float-icon {
    position: absolute;
    font-size: 36px;
    opacity: 0.24;
    filter: drop-shadow(0 0 10px rgba(14, 165, 233, 0.18));
}

.hero-float-icon:nth-child(1) { top: 15%; left: 8%;  animation: float 6.5s ease-in-out infinite, icon-flicker 3.4s ease-in-out infinite; }
.hero-float-icon:nth-child(2) { top: 25%; right: 10%; animation: float-reverse 7.2s ease-in-out infinite, icon-flicker 4s ease-in-out infinite; animation-delay: 0.8s; }
.hero-float-icon:nth-child(3) { bottom: 20%; left: 12%; animation: float 7.6s ease-in-out infinite, icon-flicker 3.8s ease-in-out infinite; animation-delay: 1.4s; }
.hero-float-icon:nth-child(4) { bottom: 30%; right: 8%; animation: float-reverse 6.1s ease-in-out infinite, icon-flicker 3.2s ease-in-out infinite; animation-delay: 0.4s; }
.hero-float-icon:nth-child(5) { top: 45%; left: 5%;  animation: float 8.2s ease-in-out infinite, icon-flicker 4.2s ease-in-out infinite; animation-delay: 2.2s; }
.hero-float-icon:nth-child(6) { top: 10%; right: 20%; animation: float-reverse 6.8s ease-in-out infinite, icon-flicker 3.6s ease-in-out infinite; animation-delay: 1.1s; }

/* ===== STATS BAR ===== */
.stats-bar {
    display: flex;
    justify-content: center;
    gap: 60px;
    padding: 50px 40px;
    animation: fadeInUp 0.8s ease-out 1.2s both;
    flex-wrap: wrap;
}

.stat-item {
    text-align: center;
    position: relative;
}

.stat-number {
    font-size: 42px;
    font-weight: 800;
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #a855f7, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -1px;
}

.stat-label {
    font-size: 14px;
    color: var(--text-muted);
    font-weight: 500;
    margin-top: 4px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.stat-divider {
    width: 1px;
    background: linear-gradient(180deg, transparent, rgba(124,58,237,0.3), transparent);
    align-self: stretch;
}

/* ===== SECTION TITLE ===== */
.section-header {
    text-align: center;
    margin: 80px 0 60px 0;
    animation: fadeInUp 0.8s ease-out both;
}

.section-label {
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 3px;
    color: #7c3aed;
    font-weight: 600;
    margin-bottom: 12px;
}

.section-title {
    font-size: 48px;
    font-weight: 800;
    color: var(--text-primary);
    font-family: 'Poppins', sans-serif;
    letter-spacing: -1px;
    margin-bottom: 16px;
}

.section-subtitle {
    font-size: 17px;
    color: var(--text-secondary);
    max-width: 500px;
    margin: 0 auto;
    line-height: 1.6;
}

/* ===== FEATURE CARDS ===== */
.feature-card {
    position: relative;
    background: linear-gradient(180deg, rgba(255,255,255,0.08), rgba(255,255,255,0.03)), var(--surface-1);
    padding: 44px 32px;
    border-radius: 20px;
    text-align: center;
    border: 1px solid var(--border-soft);
    transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    backdrop-filter: blur(20px);
    overflow: hidden;
    min-height: 280px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.feature-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: linear-gradient(135deg, rgba(124,58,237,0.05), transparent 50%, rgba(6,182,212,0.05));
    opacity: 0;
    transition: opacity 0.5s ease;
}

.feature-card::after {
    content: '';
    position: absolute;
    top: -2px; left: -2px;
    right: -2px; bottom: -2px;
    background: linear-gradient(135deg, #7c3aed, #06b6d4, #ec4899, #7c3aed);
    background-size: 300% 300%;
    border-radius: 22px;
    z-index: -1;
    opacity: 0;
    transition: opacity 0.5s ease;
    animation: gradient-shift 4s ease-in-out infinite;
}

.feature-card:hover {
    transform: translateY(-16px) scale(1.02);
    border-color: transparent;
    box-shadow: 0 25px 60px rgba(124,58,237,0.25), 0 0 0 1px rgba(124,58,237,0.1);
}

.feature-card:hover::before {
    opacity: 1;
}

.feature-card:hover::after {
    opacity: 1;
}

.feature-icon-wrapper {
    width: 72px; height: 72px;
    border-radius: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 20px;
    font-size: 32px;
    position: relative;
    transition: all 0.4s ease;
}

.feature-icon-wrapper.purple {
    background: linear-gradient(135deg, rgba(124,58,237,0.2), rgba(124,58,237,0.05));
    border: 1px solid rgba(124,58,237,0.2);
}

.feature-icon-wrapper.cyan {
    background: linear-gradient(135deg, rgba(6,182,212,0.2), rgba(6,182,212,0.05));
    border: 1px solid rgba(6,182,212,0.2);
}

.feature-icon-wrapper.pink {
    background: linear-gradient(135deg, rgba(236,72,153,0.2), rgba(236,72,153,0.05));
    border: 1px solid rgba(236,72,153,0.2);
}

.feature-card:hover .feature-icon-wrapper {
    transform: scale(1.1) rotate(5deg);
}

.feature-card h3 {
    font-size: 20px;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 10px;
    font-family: 'Poppins', sans-serif;
}

.feature-card p {
    font-size: 14px;
    color: var(--text-secondary);
    line-height: 1.7;
}

/* ===== HOW IT WORKS ===== */
.steps-container {
    display: flex;
    justify-content: center;
    gap: 0;
    padding: 20px 40px;
    position: relative;
    flex-wrap: wrap;
}

.step-card {
    text-align: center;
    padding: 40px 30px;
    position: relative;
    flex: 1;
    max-width: 280px;
    min-width: 200px;
}

.step-number {
    width: 56px; height: 56px;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    font-weight: 800;
    font-family: 'Poppins', sans-serif;
    margin: 0 auto 20px;
    position: relative;
    color: white;
}

.step-number.s1 {
    background: linear-gradient(135deg, #7c3aed, #6d28d9);
    box-shadow: 0 8px 25px rgba(124,58,237,0.3);
}

.step-number.s2 {
    background: linear-gradient(135deg, #06b6d4, #0891b2);
    box-shadow: 0 8px 25px rgba(6,182,212,0.3);
}

.step-number.s3 {
    background: linear-gradient(135deg, #ec4899, #db2777);
    box-shadow: 0 8px 25px rgba(236,72,153,0.3);
}

.step-connector {
    position: absolute;
    top: 66px;
    right: -20px;
    width: 40px;
    height: 2px;
    background: linear-gradient(90deg, rgba(124,58,237,0.4), rgba(6,182,212,0.4));
}

.step-card h4 {
    font-size: 18px;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 8px;
    font-family: 'Poppins', sans-serif;
}

.step-card p {
    font-size: 14px;
    color: var(--text-secondary);
    line-height: 1.6;
}

/* ===== TECH BADGE ROW ===== */
.tech-badges {
    display: flex;
    justify-content: center;
    gap: 18px;
    flex-wrap: wrap;
    padding: 24px 40px 64px;
    animation: fadeInUp 0.8s ease-out both;
}

.tech-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    min-width: 132px;
    padding: 13px 22px;
    border-radius: 999px;
    font-size: 14px;
    color: #183153;
    font-weight: 700;
    letter-spacing: 0.15px;
    background:
        linear-gradient(180deg, rgba(255,255,255,0.96), rgba(240,247,255,0.98)),
        linear-gradient(135deg, rgba(56,189,248,0.08), rgba(37,99,235,0.08));
    border: 1px solid rgba(148, 163, 184, 0.22);
    box-shadow:
        0 12px 28px rgba(15, 23, 42, 0.08),
        inset 0 1px 0 rgba(255,255,255,0.85);
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease, color 0.25s ease;
    position: relative;
    overflow: hidden;
}

.tech-badge::before {
    content: "";
    position: absolute;
    inset: 1px;
    border-radius: inherit;
    background: linear-gradient(135deg, rgba(255,255,255,0.6), transparent 42%, rgba(191,219,254,0.2));
    pointer-events: none;
}

.tech-badge:hover {
    border-color: rgba(96, 165, 250, 0.4);
    color: #0f3d91;
    box-shadow:
        0 16px 34px rgba(37, 99, 235, 0.14),
        inset 0 1px 0 rgba(255,255,255,0.92);
    transform: translateY(-3px);
}

/* ===== FOOTER ===== */
.footer-section {
    width: 100vw;
    margin-top: 110px;
    margin-left: calc(50% - 50vw);
    margin-right: calc(50% - 50vw);
    min-height: 48vh;
    padding: 72px 24px 86px;
    text-align: center;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: center;
    background:
        radial-gradient(circle at 18% 22%, rgba(34, 211, 238, 0.12), transparent 24%),
        radial-gradient(circle at 82% 20%, rgba(96, 165, 250, 0.14), transparent 28%),
        linear-gradient(135deg, rgba(13, 37, 84, 0.82), transparent 48%),
        linear-gradient(180deg, #061327 0%, #0a1f40 42%, #08162d 100%);
    border-top: 1px solid rgba(148, 163, 184, 0.18);
    box-shadow: 0 -14px 36px rgba(2, 6, 23, 0.14);
}

.footer-section::before {
    content: "";
    position: absolute;
    inset: 0;
    background:
        linear-gradient(90deg, rgba(255,255,255,0.045) 1px, transparent 1px),
        linear-gradient(180deg, rgba(255,255,255,0.04) 1px, transparent 1px);
    background-size: 72px 72px;
    mask-image: linear-gradient(180deg, rgba(0,0,0,0.45), rgba(0,0,0,0.08));
    -webkit-mask-image: linear-gradient(180deg, rgba(0,0,0,0.45), rgba(0,0,0,0.08));
    opacity: 0.6;
    pointer-events: none;
}

.footer-section::after {
    content: "";
    position: absolute;
    inset: 0;
    background:
        radial-gradient(ellipse at 24% 68%, rgba(56, 189, 248, 0.16) 0%, transparent 18%),
        radial-gradient(ellipse at 76% 70%, rgba(59, 130, 246, 0.14) 0%, transparent 18%),
        radial-gradient(circle at 24% 68%, rgba(255,255,255,0.22) 0 10px, transparent 11px),
        radial-gradient(circle at 24% 72%, rgba(255,255,255,0.08) 0 10px, transparent 11px),
        radial-gradient(circle at 76% 70%, rgba(255,255,255,0.18) 0 10px, transparent 11px),
        radial-gradient(circle at 76% 74%, rgba(255,255,255,0.07) 0 10px, transparent 11px),
        linear-gradient(180deg, rgba(255,255,255,0.03), transparent 24%);
    background-repeat: no-repeat;
    pointer-events: none;
}

.footer-section > div {
    width: min(100%, 760px);
    margin-left: auto;
    margin-right: auto;
}

.footer-logo {
    position: relative;
    z-index: 1;
    font-size: 34px;
    font-weight: 800;
    color: #f8fbff;
    font-family: 'Poppins', sans-serif;
    letter-spacing: -0.9px;
    margin-bottom: 14px;
}

.footer-text {
    position: relative;
    z-index: 1;
    color: rgba(226, 232, 240, 0.88);
    font-size: 16px;
    font-weight: 500;
    letter-spacing: 0.3px;
    margin-bottom: 20px;
}

.footer-copyright {
    position: relative;
    z-index: 1;
    color: rgba(191, 219, 254, 0.82);
    font-size: 14px;
    font-weight: 500;
    letter-spacing: 0.2px;
    line-height: 1.7;
}

/* ===== RESPONSIVE ===== */
@media (max-width: 768px) {
    .hero-title { font-size: 48px; letter-spacing: -1.5px; }
    .hero-subtitle { font-size: 18px; }
    .hero-container { padding: 80px 20px 52px; }
    .hero-visual-shell { padding: 12px; border-radius: 24px; }
    .hero-showcase,
    .showcase-window,
    .showcase-metrics { grid-template-columns: 1fr; }
    .showcase-panel,
    .showcase-side-card { padding: 18px; }
    .showcase-row { grid-template-columns: 1fr; }
    .showcase-topbar { align-items: flex-start; flex-direction: column; }
    .stats-bar { gap: 30px; }
    .stat-number { font-size: 32px; }
    .section-title { font-size: 36px; }
    .steps-container { flex-direction: column; align-items: center; }
    .step-connector { display: none; }
    .navbar-container {
        width: 100vw;
        margin: 0 0 10px calc(50% - 50vw);
        min-height: 180px;
        padding: 30px 20px 26px;
        border-radius: 0;
    }
    .navbar-inner {
        min-height: 120px;
        gap: 20px;
    }
    .navbar-container {
        gap: 18px;
    }
    .nav-links {
        gap: 14px 18px;
        justify-content: center;
    }
    .nav-link {
        display: block;
        font-size: 11px;
        letter-spacing: 0.04em;
    }
    .menu-anchor {
        width: 100%;
        margin: -170px 20px 0;
        max-width: 220px;
    }
    .menu-links {
        gap: 10px;
    }
    .menu-links div[data-testid="stPageLink"] a {
        min-width: 120px;
        font-size: 14px;
    }
    .footer-section {
        margin-top: 88px;
        min-height: 40vh;
        padding: 54px 20px 62px;
    }
    .footer-section::before {
        background-size: 52px 52px;
    }
    .footer-logo { font-size: 28px; }
    .footer-text,
    .footer-copyright {
        font-size: 13px;
    }
    .tech-badges {
        gap: 12px;
        padding: 20px 18px 52px;
    }
    .tech-badge {
        min-width: 124px;
        padding: 12px 18px;
        font-size: 13px;
    }
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# FLOATING ORBS + PARTICLES (background)
# ============================================================
st.markdown("""
<div class="orb-container">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
    <div class="orb orb-4"></div>
</div>

<div class="particles">
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# NAVBAR
# ============================================================
st.markdown("""
<div class="navbar-container">
    <div class="logo">⚡ TableForge</div>
    <div class="nav-links">
        <div class="nav-link">Visual Editing</div>
        <div class="nav-link">SQLite-first</div>
        <div class="nav-link">Zero SQL</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# HOME MENU
# ============================================================
st.markdown('<div class="menu-anchor">', unsafe_allow_html=True)
if st.button("☰ Menu", key="home_menu_toggle", use_container_width=True):
    st.session_state.show_home_menu = not st.session_state.show_home_menu

if st.session_state.show_home_menu:
    st.markdown('<div class="menu-links">', unsafe_allow_html=True)
    st.page_link("home.py", label="home")
    st.page_link("pages/connect_database.py", label="connect database")
    st.page_link("pages/table_editor.py", label="table editor")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div><div class="menu-spacer"></div>', unsafe_allow_html=True)

# ============================================================
# HERO SECTION
# ============================================================
st.markdown("""
<div class="hero-container">
    <div class="hero-glow"></div>

    <div class="hero-floating-icons">
        <div class="hero-float-icon">🗄️</div>
        <div class="hero-float-icon">📊</div>
        <div class="hero-float-icon">⚡</div>
        <div class="hero-float-icon">🔗</div>
        <div class="hero-float-icon">🛡️</div>
        <div class="hero-float-icon">📈</div>
    </div>

    <div class="hero-badge">
        <div class="hero-badge-dot"></div>
        Now in Beta — Try it free
    </div>

    <h1 class="hero-title">Database Management,<br>Reimagined.</h1>

    <p class="hero-subtitle">
        Work with <strong>real databases</strong> like a spreadsheet.<br>
        No SQL required. Just connect, explore, and edit.
    </p>

    <p class="hero-description">
        TableForge transforms complex database operations into an intuitive visual experience.
        Connect to SQLite and start editing in seconds.
    </p>

    <div class="hero-visual-shell">
        <div class="hero-showcase">
            <div class="showcase-panel">
                <div class="showcase-topbar">
                    <div class="showcase-brand">
                        <div class="showcase-logo">⚡</div>
                        <div class="showcase-brand-text">
                            <strong>TableForge Workspace</strong>
                            <span>Elegant data operations for modern teams</span>
                        </div>
                    </div>
                    <div class="showcase-status">Live Sync</div>
                </div>

                <div class="showcase-window">
                    <div class="showcase-card-surface">
                        <div class="showcase-header-row">
                            <strong>Customers</strong>
                            <div class="showcase-pill">Instantly editable</div>
                        </div>
                        <div class="showcase-grid">
                            <div class="showcase-row header">
                                <div class="showcase-cell">Name</div>
                                <div class="showcase-cell">Plan</div>
                                <div class="showcase-cell">Status</div>
                            </div>
                            <div class="showcase-row">
                                <div class="showcase-cell">Acme Labs</div>
                                <div class="showcase-cell showcase-accent">Scale</div>
                                <div class="showcase-cell">Active</div>
                            </div>
                            <div class="showcase-row">
                                <div class="showcase-cell">Northwind</div>
                                <div class="showcase-cell">Pro</div>
                                <div class="showcase-cell">Review</div>
                            </div>
                            <div class="showcase-row">
                                <div class="showcase-cell">Vertex Group</div>
                                <div class="showcase-cell">Enterprise</div>
                                <div class="showcase-cell">Healthy</div>
                            </div>
                        </div>
                    </div>

                    <div class="showcase-side-card">
                        <h3>Confident control</h3>
                        <p class="showcase-caption">
                            Balanced surfaces, clear hierarchy, and strong contrast make every dataset feel polished and easy to scan.
                        </p>
                        <ul class="showcase-list">
                            <li><span class="showcase-list-dot"></span>Premium theme-aware surfaces</li>
                            <li><span class="showcase-list-dot"></span>Readable cards in bright light</li>
                            <li><span class="showcase-list-dot"></span>Refined motion without clutter</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="showcase-side">
                <div class="showcase-side-card">
                    <h3>Operational clarity</h3>
                    <div class="showcase-chart"></div>
                    <p class="showcase-caption">
                        Designed to feel sharp and premium whether your system is in dark mode or light mode.
                    </p>
                </div>
                <div class="showcase-metrics">
                    <div class="metric-pill">
                        <strong>1</strong>
                        <span>Database engine</span>
                    </div>
                    <div class="metric-pill">
                        <strong>0</strong>
                        <span>Queries required</span>
                    </div>
                    <div class="metric-pill">
                        <strong>1s</strong>
                        <span>Fast visual scan</span>
                    </div>
                    <div class="metric-pill">
                        <strong>24/7</strong>
                        <span>Polished workspace feel</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# STATS BAR
# ============================================================
st.markdown("""
<div class="stats-bar">
    <div class="stat-item">
        <div class="stat-number">1</div>
        <div class="stat-label">Database Type</div>
    </div>
    <div class="stat-divider"></div>
    <div class="stat-item">
        <div class="stat-number">0</div>
        <div class="stat-label">SQL Required</div>
    </div>
    <div class="stat-divider"></div>
    <div class="stat-item">
        <div class="stat-number">∞</div>
        <div class="stat-label">Possibilities</div>
    </div>
    <div class="stat-divider"></div>
    <div class="stat-item">
        <div class="stat-number">100%</div>
        <div class="stat-label">Open Source</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# FEATURES SECTION
# ============================================================
st.markdown("""
<div class="section-header">
    <div class="section-label">✦ Features</div>
    <div class="section-title">Why TableForge?</div>
    <div class="section-subtitle">Everything you need to manage databases visually, without writing a single query.</div>
</div>
""", unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon-wrapper purple">📊</div>
        <h3>Spreadsheet Editing</h3>
        <p>Edit database tables like Excel or Google Sheets. Inline editing, sorting, filtering — all visual.</p>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon-wrapper cyan">🗄️</div>
        <h3>SQLite Focus</h3>
        <p>Connect to a local SQLite database and manage it visually without extra server setup.</p>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon-wrapper pink">⚡</div>
        <h3>Zero SQL Needed</h3>
        <p>Perfect for beginners and non-technical users. Visual interface handles all the complexity.</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# HOW IT WORKS
# ============================================================
st.markdown("""
<div class="section-header">
    <div class="section-label">✦ How It Works</div>
    <div class="section-title">Three Simple Steps</div>
    <div class="section-subtitle">Get started in under a minute.</div>
</div>

<div class="steps-container">
    <div class="step-card">
        <div class="step-number s1">1</div>
        <div class="step-connector"></div>
        <h4>Connect</h4>
        <p>Select your local SQLite file and open it instantly.</p>
    </div>
    <div class="step-card">
        <div class="step-number s2">2</div>
        <div class="step-connector"></div>
        <h4>Explore</h4>
        <p>Browse tables, view schemas, and preview data instantly.</p>
    </div>
    <div class="step-card">
        <div class="step-number s3">3</div>
        <h4>Edit & Save</h4>
        <p>Make changes visually and commit them back to the database.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# TECH BADGES
# ============================================================
st.markdown("""
<div class="tech-badges">
    <div class="tech-badge">🐍 Python</div>
    <div class="tech-badge">🎯 Streamlit</div>
    <div class="tech-badge">🗃️ SQLite</div>
    <div class="tech-badge">📊 Pandas</div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================
st.markdown("""
<div class="footer-section">
    <div class="footer-logo">⚡ TableForge</div>
    <div class="footer-text">Revolutionizing Database Management</div>
    <div class="footer-copyright">
        © 2026 TableForge — Built with ❤️ by Team CodeX
    </div>
</div>
""", unsafe_allow_html=True)
