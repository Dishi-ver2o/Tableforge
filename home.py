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
# CSS + ANIMATIONS
# ============================================================
st.markdown("""
<style>
/* ===== FONTS & GENERAL ===== */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

* { margin:0; padding:0; box-sizing:border-box; }

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

/* ===== BACKGROUND ===== */
body {
    background: linear-gradient(135deg, #030614 0%, #0a0a2e 30%, #1a0533 60%, #0d1b2a 100%);
    background-attachment: fixed;
    color: #e2e8f0;
}

.main { background: transparent; }

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
    0%, 100% { transform: translateY(0) rotate(0deg); }
    33% { transform: translateY(-20px) rotate(3deg); }
    66% { transform: translateY(10px) rotate(-2deg); }
}

@keyframes float-reverse {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    33% { transform: translateY(15px) rotate(-3deg); }
    66% { transform: translateY(-25px) rotate(2deg); }
}

@keyframes pulse-glow {
    0%, 100% { opacity: 0.4; transform: scale(1); }
    50% { opacity: 0.7; transform: scale(1.05); }
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
    0% { transform: translateY(0) translateX(0); opacity: 0; }
    10% { opacity: 1; }
    90% { opacity: 1; }
    100% { transform: translateY(-100vh) translateX(50px); opacity: 0; }
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
    filter: blur(80px);
    animation: pulse-glow 6s ease-in-out infinite;
}

.orb-1 {
    width: 500px; height: 500px;
    background: radial-gradient(circle, rgba(124,58,237,0.25), transparent 70%);
    top: -10%; left: -5%;
    animation-delay: 0s;
}

.orb-2 {
    width: 400px; height: 400px;
    background: radial-gradient(circle, rgba(6,182,212,0.2), transparent 70%);
    top: 40%; right: -8%;
    animation-delay: 2s;
}

.orb-3 {
    width: 350px; height: 350px;
    background: radial-gradient(circle, rgba(236,72,153,0.15), transparent 70%);
    bottom: -5%; left: 30%;
    animation-delay: 4s;
}

.orb-4 {
    width: 250px; height: 250px;
    background: radial-gradient(circle, rgba(124,58,237,0.2), transparent 70%);
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
    width: 3px; height: 3px;
    background: rgba(124, 58, 237, 0.6);
    border-radius: 50%;
    animation: particle-drift linear infinite;
}

.particle:nth-child(1) { left: 10%; animation-duration: 12s; animation-delay: 0s; background: rgba(124,58,237,0.5); }
.particle:nth-child(2) { left: 20%; animation-duration: 15s; animation-delay: 2s; background: rgba(6,182,212,0.5); width: 2px; height: 2px; }
.particle:nth-child(3) { left: 35%; animation-duration: 10s; animation-delay: 4s; background: rgba(236,72,153,0.4); }
.particle:nth-child(4) { left: 50%; animation-duration: 18s; animation-delay: 1s; background: rgba(124,58,237,0.3); width: 4px; height: 4px; }
.particle:nth-child(5) { left: 65%; animation-duration: 14s; animation-delay: 3s; background: rgba(6,182,212,0.4); }
.particle:nth-child(6) { left: 75%; animation-duration: 11s; animation-delay: 5s; background: rgba(236,72,153,0.5); width: 2px; height: 2px; }
.particle:nth-child(7) { left: 85%; animation-duration: 16s; animation-delay: 0.5s; background: rgba(124,58,237,0.4); }
.particle:nth-child(8) { left: 45%; animation-duration: 20s; animation-delay: 6s; background: rgba(6,182,212,0.3); width: 4px; height: 4px; }
.particle:nth-child(9) { left: 5%;  animation-duration: 13s; animation-delay: 7s; background: rgba(236,72,153,0.3); }
.particle:nth-child(10){ left: 90%; animation-duration: 17s; animation-delay: 1.5s; background: rgba(124,58,237,0.5); width: 2px; height: 2px; }

/* ===== NAVBAR ===== */
.navbar-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px 40px;
    background: rgba(10, 10, 46, 0.6);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border-bottom: 1px solid rgba(124,58,237,0.15);
    border-radius: 0 0 24px 24px;
    margin-bottom: 0;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: 0 8px 32px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.05);
    animation: fadeInUp 0.6s ease-out;
}

.logo {
    font-size: 26px;
    font-weight: 800;
    background: linear-gradient(135deg, #a855f7, #06b6d4, #ec4899);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.5px;
    font-family: 'Poppins', sans-serif;
    animation: gradient-shift 4s ease-in-out infinite;
    cursor: pointer;
}

.nav-links {
    display: flex;
    gap: 32px;
    align-items: center;
}

.nav-link {
    color: #94a3b8;
    text-decoration: none;
    font-size: 14px;
    font-weight: 500;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    transition: all 0.3s ease;
    position: relative;
    padding-bottom: 4px;
}

.nav-link::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0;
    width: 0; height: 2px;
    background: linear-gradient(90deg, #7c3aed, #06b6d4);
    transition: width 0.3s ease;
    border-radius: 1px;
}

.nav-link:hover {
    color: #e2e8f0;
}

.nav-link:hover::after {
    width: 100%;
}

.nav-badge {
    background: linear-gradient(135deg, #7c3aed, #06b6d4);
    color: white;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.5px;
    box-shadow: 0 4px 15px rgba(124,58,237,0.4);
    transition: all 0.3s ease;
    cursor: pointer;
}

.nav-badge:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 25px rgba(124,58,237,0.6);
}

/* ===== HERO SECTION ===== */
.hero-container {
    text-align: center;
    padding: 100px 40px 60px;
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
    width: 800px; height: 800px;
    background: radial-gradient(circle, rgba(124,58,237,0.2) 0%, rgba(6,182,212,0.1) 40%, transparent 70%);
    filter: blur(120px);
    top: -200px;
    left: 50%;
    transform: translateX(-50%);
    z-index: -1;
    animation: pulse-glow 8s ease-in-out infinite;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(124,58,237,0.15);
    border: 1px solid rgba(124,58,237,0.3);
    padding: 8px 20px;
    border-radius: 50px;
    font-size: 13px;
    color: #c4b5fd;
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
    background: linear-gradient(135deg, #e2e8f0 0%, #a855f7 30%, #06b6d4 60%, #ec4899 100%);
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
    color: #94a3b8;
    margin-bottom: 16px;
    font-weight: 400;
    line-height: 1.5;
    animation: fadeInUp 0.8s ease-out 0.6s both;
}

.hero-subtitle strong {
    color: #e2e8f0;
    font-weight: 600;
}

.hero-description {
    font-size: 16px;
    color: #64748b;
    line-height: 1.8;
    max-width: 600px;
    margin-bottom: 50px;
    text-align: center;
    animation: fadeInUp 0.8s ease-out 0.8s both;
}

/* ===== CTA BUTTONS ===== */
.cta-group {
    display: flex;
    gap: 16px;
    align-items: center;
    justify-content: center;
    animation: fadeInUp 0.8s ease-out 1s both;
    flex-wrap: wrap;
}

.cta-primary {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: linear-gradient(135deg, #7c3aed, #6d28d9);
    color: white;
    padding: 16px 36px;
    border-radius: 14px;
    font-size: 16px;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    box-shadow: 0 8px 30px rgba(124,58,237,0.4), inset 0 1px 0 rgba(255,255,255,0.1);
    cursor: pointer;
    position: relative;
    overflow: hidden;
}

.cta-primary::before {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.15), transparent);
    transition: left 0.5s ease;
}

.cta-primary:hover::before {
    left: 100%;
}

.cta-primary:hover {
    transform: translateY(-4px) scale(1.02);
    box-shadow: 0 16px 50px rgba(124,58,237,0.5), inset 0 1px 0 rgba(255,255,255,0.2);
}

.cta-secondary {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: rgba(255,255,255,0.05);
    color: #c4b5fd;
    padding: 16px 36px;
    border-radius: 14px;
    font-size: 16px;
    font-weight: 600;
    text-decoration: none;
    border: 1px solid rgba(124,58,237,0.3);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    cursor: pointer;
    backdrop-filter: blur(10px);
}

.cta-secondary:hover {
    transform: translateY(-4px);
    background: rgba(124,58,237,0.15);
    border-color: rgba(124,58,237,0.5);
    box-shadow: 0 8px 30px rgba(124,58,237,0.2);
    color: white;
}

/* ===== FLOATING ICONS around hero ===== */
.hero-floating-icons {
    position: absolute;
    width: 100%; height: 100%;
    top: 0; left: 0;
    pointer-events: none;
    z-index: -1;
}

.hero-float-icon {
    position: absolute;
    font-size: 28px;
    opacity: 0.15;
}

.hero-float-icon:nth-child(1) { top: 15%; left: 8%;  animation: float 8s ease-in-out infinite; }
.hero-float-icon:nth-child(2) { top: 25%; right: 10%; animation: float-reverse 9s ease-in-out infinite; animation-delay: 1s; }
.hero-float-icon:nth-child(3) { bottom: 20%; left: 12%; animation: float 10s ease-in-out infinite; animation-delay: 2s; }
.hero-float-icon:nth-child(4) { bottom: 30%; right: 8%; animation: float-reverse 7s ease-in-out infinite; animation-delay: 0.5s; }
.hero-float-icon:nth-child(5) { top: 45%; left: 5%;  animation: float 11s ease-in-out infinite; animation-delay: 3s; }
.hero-float-icon:nth-child(6) { top: 10%; right: 20%; animation: float-reverse 8s ease-in-out infinite; animation-delay: 1.5s; }

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
    color: #64748b;
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
    color: white;
    font-family: 'Poppins', sans-serif;
    letter-spacing: -1px;
    margin-bottom: 16px;
}

.section-subtitle {
    font-size: 17px;
    color: #64748b;
    max-width: 500px;
    margin: 0 auto;
    line-height: 1.6;
}

/* ===== FEATURE CARDS ===== */
.feature-card {
    position: relative;
    background: rgba(15, 23, 42, 0.6);
    padding: 44px 32px;
    border-radius: 20px;
    text-align: center;
    border: 1px solid rgba(124,58,237,0.15);
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
    color: #f1f5f9;
    margin-bottom: 10px;
    font-family: 'Poppins', sans-serif;
}

.feature-card p {
    font-size: 14px;
    color: #94a3b8;
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
    color: #f1f5f9;
    margin-bottom: 8px;
    font-family: 'Poppins', sans-serif;
}

.step-card p {
    font-size: 14px;
    color: #64748b;
    line-height: 1.6;
}

/* ===== TECH BADGE ROW ===== */
.tech-badges {
    display: flex;
    justify-content: center;
    gap: 16px;
    flex-wrap: wrap;
    padding: 20px 40px 60px;
    animation: fadeInUp 0.8s ease-out both;
}

.tech-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(15, 23, 42, 0.6);
    border: 1px solid rgba(124,58,237,0.15);
    padding: 10px 20px;
    border-radius: 12px;
    font-size: 13px;
    color: #94a3b8;
    font-weight: 500;
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
}

.tech-badge:hover {
    border-color: rgba(124,58,237,0.4);
    color: #c4b5fd;
    background: rgba(124,58,237,0.1);
    transform: translateY(-2px);
}

/* ===== FOOTER ===== */
.footer-section {
    margin-top: 80px;
    padding: 60px 40px;
    border-top: 1px solid rgba(124,58,237,0.1);
    text-align: center;
    position: relative;
}

.footer-logo {
    font-size: 24px;
    font-weight: 800;
    background: linear-gradient(135deg, #a855f7, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-family: 'Poppins', sans-serif;
    margin-bottom: 16px;
}

.footer-text {
    color: #475569;
    font-size: 14px;
    margin-bottom: 20px;
}

.footer-links {
    display: flex;
    justify-content: center;
    gap: 24px;
    margin-bottom: 30px;
}

.footer-link-item {
    width: 40px; height: 40px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(15,23,42,0.6);
    border: 1px solid rgba(124,58,237,0.15);
    color: #64748b;
    font-size: 18px;
    transition: all 0.3s ease;
    cursor: pointer;
}

.footer-link-item:hover {
    background: rgba(124,58,237,0.15);
    border-color: rgba(124,58,237,0.4);
    color: #a855f7;
    transform: translateY(-3px);
}

.footer-copyright {
    color: #334155;
    font-size: 13px;
}

/* ===== RESPONSIVE ===== */
@media (max-width: 768px) {
    .hero-title { font-size: 48px; letter-spacing: -1.5px; }
    .hero-subtitle { font-size: 18px; }
    .stats-bar { gap: 30px; }
    .stat-number { font-size: 32px; }
    .section-title { font-size: 36px; }
    .steps-container { flex-direction: column; align-items: center; }
    .step-connector { display: none; }
    .navbar-container { padding: 12px 20px; }
    .nav-links { gap: 16px; }
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
        <a class="nav-link" href="#">Features</a>
        <a class="nav-link" href="#">Docs</a>
        <a class="nav-link" href="#">About</a>
        <div class="nav-badge">🚀 Get Started</div>
    </div>
</div>
""", unsafe_allow_html=True)

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
        Connect to SQLite, MySQL, or PostgreSQL and start editing in seconds.
    </p>

    <div class="cta-group">
        <div class="cta-primary">
            🚀 Launch App
        </div>
        <div class="cta-secondary">
            📖 View Documentation
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
        <div class="stat-number">3+</div>
        <div class="stat-label">Database Types</div>
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
        <h3>Multi-DB Support</h3>
        <p>Seamlessly connect to SQLite, MySQL, and PostgreSQL. Switch between databases in one click.</p>
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
        <p>Enter your database credentials or select a local SQLite file.</p>
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
    <div class="tech-badge">🐬 MySQL</div>
    <div class="tech-badge">🐘 PostgreSQL</div>
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
    <div class="footer-links">
        <div class="footer-link-item">⭐</div>
        <div class="footer-link-item">📂</div>
        <div class="footer-link-item">💬</div>
        <div class="footer-link-item">📧</div>
    </div>
    <div class="footer-copyright">
        © 2026 TableForge — Built with ❤️ by Team CodeX
    </div>
</div>
""", unsafe_allow_html=True)