import streamlit as st
import datetime
import random

# --- НАСТРОЙКИ ---
NAME = "Твое Имя"  # <--- ЗАМЕНИ НА СВОЕ ИМЯ
# -----------------

st.set_page_config(page_title="С Днем Рождения, Папа!", page_icon="🎂", layout="centered")

# CSS стили
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Roboto:wght@400;700&display=swap');
    .stApp { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }
    [data-testid="stVerticalBlock"] { display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 85vh; }
    
    .envelope-container button {
        background-color: white !important;
        border: 4px dashed #6a11cb !important;
        border-radius: 30px !important;
        padding: 50px 30px !important;
        width: 350px !important;
        height: 220px !important;
        box-shadow: 0 15px 40px rgba(106, 17, 203, 0.15) !important;
    }
    .envelope-container button p { color: #6a11cb !important; font-family: 'Roboto', sans-serif !important; font-size: 1.2rem !important; font-weight: bold !important; }

    .main-card { 
        background-color: white; padding: 40px; border-radius: 30px; 
        box-shadow: 0 20px 40px rgba(0,0,0,0.08); text-align: left; 
        max-width: 550px; width: 100%; animation: fadeIn 0.8s ease-out;
    }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
    .card-title { font-family: 'Pacifico', cursive; color: #6a11cb; font-size: 2.8rem; text-align: center; margin-bottom: 20px; }
    .wish-text { font-family: 'Roboto', sans-serif; font-size: 1.2rem; color: #444; line-height: 1.6; font-style: italic; background: #f9f9f9; padding: 20px; border-radius: 15px; border-left: 5px solid #6a11cb; margin-bottom: 20px; }
    .info-block p { margin: 5px 0; color: #7f8c8d; font-family: 'Roboto', sans-serif; font-size: 0.9rem; }

    .left-btn { display: flex; justify-content: flex-start; width: 100%; max-width: 550px; margin-top: 15px; }
    .left-btn button { background: linear-gradient(to right, #6a11cb 0%, #2575fc 100%) !important; border: none !important; padding: 10px 25px !important; border-radius: 50px !important; }
    .left-btn button p { color: white !important; font-family: 'Roboto', sans-serif !important; font-size: 0.85rem !important; font-weight: bold !important; }
    header, footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

if 'opened' not in st.session_state:
    st.session_state.opened = False

# --- ЛОГИКА ЭКРАНОВ ---
if not st.session_state.opened:
    st.markdown("<h1 style='font-family: Pacifico; color: #6a11cb; text-align: center;'>Для тебя, Папа! ❤️</h1>", unsafe_allow_html=True)
    st.markdown('<div class="envelope-container">', unsafe_allow_html=True)
    if st.button("✉️\n\nНАЖМИ, ЧТОБЫ ОТКРЫТЬ"):
        st.session_state.opened = True
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.snow()
    
    # Список пожеланий (каждое в одну строку, чтобы не было ошибок)
    wishes = [
        "Дорогой папа, поздравляю тебя с днем рождения! Желаю тебе самого крепкого здоровья, долгих лет жизни и чтобы каждый день приносил только радость. Ты — лучший пример для меня во всём!",
        "С днем рождения, папа! Пусть твоя жизнь будет наполнена светом и теплом. Желаю удачи во всех делах, бодрости духа и всегда отличного настроения!",
        "Папа, спасибо тебе за твою мудрость, терпение и поддержку. Желаю тебе финансового благополучия, спокойствия и чтобы все твои самые смелые мечты обязательно сбывались!",
        "Самый лучший папа на свете, с праздником! Пусть этот год принесет тебе много радости, новых успехов и крепкого здоровья. Мы тебя очень сильно любим!",
        "Желаю здоровья на сто лет вперед, чтобы каждый твой день в Кайраккуме был солнечным, добрым и спокойным. С днем рождения, наш дорогой человек!"
    ]

    if 'msg' not in st.session_state:
        st.session_state.msg = random.choice(wishes)

    now = datetime.datetime.now().strftime("%d.%m.%Y")

    st.markdown(f"""
    <div class="main-card">
        <div class="card-title">С Днём Рождения! 🎂</div>
        <div class="wish-text">"{st.session_state.msg}"</div>
        <div class="info-block" style="border-top: 1px solid #eee; padding-top: 15px;">
            <p><b>Для кого:</b> Любимому папе</p>
            <p><b>От кого:</b> {NAME}</p>
            <p><b>Дата:</b> {now}</p>
            <p><b>Место:</b> Кайраккум</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="left-btn">', unsafe_allow_html=True)
    if st.button("Прочитать другое ✨"):
        st.session_state.msg = random.choice(wishes)
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
