import streamlit as st
import random
import time

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
    }
    h1, h2, h3, h4, h5, h6, label {
        color: #ff4d6d !important;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .main-header {
        text-align: center;
        font-size: 3rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-bottom: 2rem;
    }
    input, textarea {
        color: black !important;
        border-radius: 20px !important;
        border: 2px solid #ff69b4 !important;
        padding: 10px !important;
        background-color: rgba(255,255,255,0.9) !important;
        font-size: 1.1rem !important;
    }
    /* Dynamic emoji labels */
    div[data-testid="stTextInput"] div[data-testid="stMarkdownContainer"] p {
        font-size: 2rem !important;
        margin-bottom: 0.5rem !important;
    }
    div.stButton > button {
        background: linear-gradient(45deg, #ff6b9d, #ff8fb2) !important;
        color: white !important;
        border-radius: 25px !important;
        padding: 10px 30px !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(255,107,157,0.4) !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 6px 20px rgba(255,107,157,0.6) !important;
    }
    .heart {
        color: #ff4d6d;
        font-size: 3rem;
        animation: heartbeat 1.5s ease-in-out infinite;
    }
    @keyframes heartbeat {
        0% { transform: scale(1); }
        14% { transform: scale(1.3); }
        28% { transform: scale(1); }
        42% { transform: scale(1.3); }
        70% { transform: scale(1); }
    }
    .result-box {
        background: rgba(255,255,255,0.95);
        padding: 2rem;
        border-radius: 30px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(255,77,109,0.3);
        border: 3px solid #ff69b4;
        font-size: 1.5rem;
        font-weight: bold;
        color: #ff4d6d;
    }
    .floating-hearts {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 9999;
    }
    .heart-particle {
        position: absolute;
        font-size: 20px;
        color: #ff69b4;
        animation: float-up 3s ease-out forwards;
    }
    @keyframes float-up {
        0% {
            opacity: 1;
            transform: translateY(0) rotate(0deg);
        }
        100% {
            opacity: 0;
            transform: translateY(-100vh) rotate(360deg);
        }
    }
    </style>
""", unsafe_allow_html=True)

# Floating hearts background
hearts_html = """
<div class="floating-hearts">
""" + "".join(
    [f'<div class="heart-particle" style="left: {random.randint(0, 100)}%; animation-delay: {i * 0.1}s;">💖</div>' for i
     in range(20)]) + """
</div>
"""
st.markdown(hearts_html, unsafe_allow_html=True)

st.markdown('<h1 class="main-header">💕 Love Percentage Calculator 💕</h1>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("👩‍❤️‍💋‍👨 **Enter first name:**")
    name1 = st.text_input("", placeholder="Your name 💝", key="name1")
with col2:
    st.markdown("💕 **Enter second name:**")
    name2 = st.text_input("", placeholder="Partner's name 🌹", key="name2")

# Real-time emojis based on typing
if name1:
    st.markdown(f"✨ Hi **{name1}**! Looking lovely already 💖")
if name2:
    st.markdown(f"🌟 Hi **{name2}**! So cute together! 😍")

if st.button("💖 Calculate Love % 💖"):
    if name1 and name2:
        with st.spinner('Calculating your love compatibility... 💕'):
            time.sleep(1.5)

        random.seed(name1.lower() + name2.lower())
        lover_percentage = random.randint(50, 100)

        st.markdown(f"""
        <div class="result-box">
            <div class="heart">💖</div>
            <h2>{name1} & {name2}</h2>
            <h1>{lover_percentage}%</h1>
            <p>Love Compatibility! ❤️</p>
            <div style='font-size: 1.2rem; margin-top: 1rem;'>💑 Perfect match! 💕</div>
        </div>
        """, unsafe_allow_html=True)

        st.caption("✨ Python magic decided this, not me! Pure fun calculator ✨")

        extra_hearts = """
        <div class="floating-hearts">
        """ + "".join([
                                                 f'<div class="heart-particle" style="left: {random.randint(0, 100)}%; animation-delay: {i * 0.05}s;">💕</div>'
                                                 for i in range(30)]) + """
        </div>
        """
        st.markdown(extra_hearts, unsafe_allow_html=True)

    else:
        st.warning("😅 Please enter both names to see the magic happen! 👫")

st.markdown("---")
st.markdown("*Made with 💕 for fun! Perfect for Streamlit apps.*")
