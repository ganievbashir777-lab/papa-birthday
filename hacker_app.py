import streamlit as st
import time
import random

# --- НАСТРОЙКИ ---
NAME = "Твое Имя" 
# -----------------

st.set_page_config(page_title="PAPA_OS: Hack Edition", page_icon="📟", layout="centered")

def get_matrix_bg():
    svg_txt = "".join([f'<text x="{i*2}%" y="-10%" fill="%2300ff41" font-family="monospace" font-size="25" opacity="0.3" style="writing-mode: tb;"><animate attributeName="y" from="-50%" to="110%" dur="{random.uniform(3,7)}s" begin="-{random.uniform(0,5)}s" repeatCount="indefinite" /></text>' for i in range(50)])
    return f'<svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">{svg_txt}</svg>'.replace('"', "'")

st.markdown(f"""
<style>
    .stApp {{ background-color: #000; background-image: url("data:image/svg+xml;utf8,{get_matrix_bg()}"); background-size: cover; }}
    [data-testid="stVerticalBlock"] {{ display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 85vh; }}
    .wish-card, .login-card {{ border: 2px solid #00ff41; padding: 40px; border-radius: 20px; background: rgba(0,0,0,0.9); box-shadow: 0 0 40px rgba(0,255,65,0.3); width: 100%; max-width: 550px; }}
    .terminal-text {{ color: #00ff41; font-family: 'Courier New', monospace; text-shadow: 0 0 10px #00ff41; }}
    .stButton > button {{ background: transparent !important; border: 2px solid #00ff41 !important; border-radius: 10px !important; }}
    .stButton > button p {{ color: #00ff41 !important; font-family: 'Courier New', monospace !important; font-weight: bold !important; }}
    .left-btn {{ display: flex; justify-content: flex-start; width: 100%; max-width: 550px; margin-top: 20px; }}
    header, footer {{visibility: hidden;}}
</style>
""", unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = 'start'

if st.session_state.step == 'start':
    st.markdown('<div class="login-card"><h1 class="terminal-text" style="text-align:center;">SYSTEM LOCKED</h1><p class="terminal-text" style="text-align:center;">Protocol: BEST_PAPA_EVER</p></div>', unsafe_allow_html=True)
    if st.button("🔓 DECRYPT MESSAGE"):
        st.session_state.step = 'loading'
        st.rerun()
elif st.session_state.step == 'loading':
    st.markdown("<div class='login-card'><h2 class='terminal-text'>BYPASSING SECURITY...</h2></div>", unsafe_allow_html=True)
    bar = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        bar.progress(i + 1)
    st.session_state.step = 'final'
    st.rerun()
else:
    st.snow()
    st.markdown(f'<div class="wish-card"><div class="terminal-text"><p style="font-size: 1.4em; text-align:center;">📊 REPORT: BIRTHDAY_2026</p><p><b>STATUS:</b> LEGENDARY</p><p>С днем рождения, Папа! Желаю жизни без багов!</p><p><b>FROM:</b> {NAME}</p></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="left-btn">', unsafe_allow_html=True)
    if st.button("🔄 REGENERATE LOG"): st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
