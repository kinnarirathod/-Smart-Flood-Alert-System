


import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model_nasa.pkl", "rb"))

# --- Page Configuration ---
st.set_page_config(page_title="Flood Guardian", page_icon="🌊", layout="centered")
# --- Custom CSS for New Look with Video Background ---
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
        padding: 0;
        margin: 0;
        height: 100%;
        overflow: hidden;
    }

    /* Video background */
    .video-background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        z-index: -1;  /* Make sure the video is behind all other content */
        opacity: 1;  /* Low opacity for the video background */
    }

    .container {
        background-color: rgba(255, 255, 255, 0.85);  /* White container with slight transparency */
        padding: 1.5rem;
        border-radius: 20px;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
        max-width: 450px;
        margin: auto;
        margin-top: 3rem;
    }

    .title {
        text-align: center;
        font-size: 2rem;
        color: #2c3e50;  /* Darker shade of blue */
        font-weight: bold;
        margin-bottom: 0.5rem;
    }

    .subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #7f8c8d;  /* Light gray text */
        margin-bottom: 1.5rem;
    }

    .input-container {
        margin-bottom: 1.2rem;
    }

    .stButton>button {
        background-color: #3498db;  /* Sky blue button */
        color: white;
        font-weight: 600;
        border: none;
        padding: 0.7rem;
        border-radius: 10px;
        width: 100%;
        font-size: 1.1rem;
        margin-top: 1rem;
    }

    .stButton>button:hover {
        background-color: #2980b9;  /* Darker blue on hover */
    }

    .alert-card {
        margin-top: 2rem;
        padding: 1.2rem;
        border-radius: 16px;
        font-size: 1rem;
        font-weight: 500;
        display: flex;
        align-items: flex-start;
        gap: 0.8rem;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    }

    .risk {
        background-color: #f9ebeb;  /* Light red background */
        border-left: 6px solid #e74c3c;  /* Red border */
        color: #c0392b;
    }

    .safe {
        background-color: #e8f5e9;  /* Light green background */
        border-left: 6px solid #27ae60;  /* Green border */
        color: #2ecc71;
    }

    .icon {
        font-size: 2rem;
    }

    footer {
        visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)

# --- Embed Video as Background ---
st.markdown("""
    <video class="video-background" autoplay loop muted>
        <source src="vid.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
""", unsafe_allow_html=True)

# --- Title and Subtitle Inside the Container ---
st.markdown('<div class="title">🌊 Flood Guardian</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Instant flood risk prediction based on recent rainfall data</div>', unsafe_allow_html=True)

# --- Input Form ---
with st.form("flood_input_form"):
    rainfall_1d = st.number_input("1-Day Rainfall (mm)", min_value=0.0, step=0.1, format="%.1f", key="rain1")
    rainfall_2d = st.number_input("2-Day Cumulative Rainfall (mm)", min_value=0.0, step=0.1, format="%.1f", key="rain2")
    submit = st.form_submit_button("🌐 Analyze Now")

# --- Prediction Result ---
if submit:
    input_features = np.array([[rainfall_1d, rainfall_2d]])
    prediction = model.predict(input_features)[0]

    if prediction == 1:
        st.markdown("""
            <div class="alert-card risk">
                <span class="icon">⚠️</span>
                <div><strong>Warning: Potential Flood Conditions!</strong><br>
                Local rainfall suggests possible flooding. Stay alert, follow safety advisories, and prepare an emergency plan.</div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="alert-card safe">
                <span class="icon">🌤️</span>
                <div><strong>All Clear: No Flood Risk Detected</strong><br>
                Current rainfall levels are safe. Continue monitoring weather updates regularly.</div>
            </div>
        """, unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
    <div style="text-align: center; font-size: 12px; margin-top: 3rem; color: #aaa;">
        Developed by Megha and Team 🏄‍♀️
    </div>
""", unsafe_allow_html=True)
