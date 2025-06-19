import streamlit as st
import numpy as np
import joblib
import time
from streamlit_lottie import st_lottie
import requests

# Set page config
st.set_page_config(page_title="Movie Success Predictor", page_icon="🎬", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    .title {
        color: #ff4b4b;
        font-size: 40px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Load Lottie animation function
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Use stable URLs
success_anim = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_qp1q7mct.json")
fail_anim = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_lk80fpsm.json")

# Load trained model
model = joblib.load('model.pkl')

st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<div class="title">🎬 Movie Success Predictor</div>', unsafe_allow_html=True)
st.write("Enter your movie details below:")

# Input form
budget = st.number_input("💰 Budget ($)", min_value=10000, value=50000000, format="%d")
runtime = st.number_input("⏱️ Runtime (minutes)", min_value=30, value=120, format="%d")
popularity = st.slider("🔥 Popularity Score", 0.0, 500.0, 50.0)
vote_average = st.slider("⭐ Average Rating", 0.0, 10.0, 7.0)
vote_count = st.number_input("🗳️ Total Votes", min_value=0, value=1000, format="%d")
release_year = st.number_input("📅 Release Year", min_value=1900, max_value=2030, value=2023, format="%d")
num_genres = st.slider("🎭 Number of Genres", 0, 10, 2)

if st.button("🎯 Predict Success"):
    with st.spinner('🔮 Predicting...'):
        time.sleep(2)
        input_data = np.array([[budget, runtime, popularity, vote_average, vote_count, release_year, num_genres]])
        prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.success("🎉 The movie is likely to be a BIG SUCCESS!")
        st.balloons()
        if success_anim is not None:
            st_lottie(success_anim, height=300)
    else:
        st.error("😢 The movie might FLOP.")
        if fail_anim is not None:
            st_lottie(fail_anim, height=300)

st.markdown('</div>', unsafe_allow_html=True)
