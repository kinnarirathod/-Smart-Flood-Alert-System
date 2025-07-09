# # app.py
# import streamlit as st
# import pickle
# import numpy as np

# # Load model
# model = pickle.load(open("model_nasa.pkl", "rb"))

# # --- Page Config ---
# st.set_page_config(
#     page_title="Smart Flood Alert",
#     page_icon="💧",
#     layout="centered"
# )

# # --- Custom CSS Styling ---
# def local_css():
#     st.markdown("""
#         <style>
#         body {
#             font-family: 'Segoe UI', sans-serif;
#             background-color: #f9fbfc;
#         }
#         .main {
#             background-color: #ffffff;
#             padding: 2rem;
#             border-radius: 12px;
#             box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
#         }
#         h1, h2, h3, h4 {
#             color: #1e3a5f;
#         }
#         .stButton>button {
#             background-color: #0b6e99;
#             color: #fff;
#             padding: 0.75rem 1.5rem;
#             border-radius: 8px;
#             font-weight: 600;
#             font-size: 1rem;
#         }
#         .stButton>button:hover {
#             background-color: #084c6d;
#         }
#         .stTextInput>div>input {
#             padding: 10px;
#             border-radius: 6px;
#         }
#         .output-box {
#             margin-top: 30px;
#             padding: 20px;
#             border-radius: 10px;
#             font-size: 1.1rem;
#             font-weight: 500;
#             box-shadow: inset 0 0 5px rgba(0,0,0,0.05);
#         }
#         .danger {
#             background-color: #fdecea;
#             border-left: 6px solid #d32f2f;
#             color: #b71c1c;
#         }
#         .safe {
#             background-color: #e8f5e9;
#             border-left: 6px solid #388e3c;
#             color: #1b5e20;
#         }
#         footer {
#             visibility: hidden;
#         }
#         </style>
#     """, unsafe_allow_html=True)

# local_css()

# # --- Sidebar ---
# st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3222/3222800.png", width=100)
# st.sidebar.title("ℹ️ Instructions")
# st.sidebar.markdown("""
# - Input recent **rainfall data**.
# - Click **Check Flood Risk**.
# - View the **prediction** instantly.
# """)
# st.sidebar.markdown("---")
# st.sidebar.markdown("📡 Data powered by NASA.")

# # --- Main UI ---
# st.markdown('<div class="main">', unsafe_allow_html=True)
# st.title("💧 Smart Flood Alert System")
# st.subheader("Early Warning. Smart Decisions.")
# st.markdown("Provide rainfall measurements to assess the risk of a flood:")

# # --- Input Form ---
# with st.form("flood_form"):
#     col1, col2 = st.columns(2)
#     with col1:
#         rainfall_1d = st.number_input("🌧️ 1-Day Rainfall (mm)", min_value=0.0, step=0.1, format="%.1f")
#     with col2:
#         rainfall_2d = st.number_input("🌧️ 2-Day Cumulative Rainfall (mm)", min_value=0.0, step=0.1, format="%.1f")

#     submitted = st.form_submit_button("🔍 Check Flood Risk")

# # --- Prediction ---
# if submitted:
#     features = np.array([[rainfall_1d, rainfall_2d]])
#     prediction = model.predict(features)[0]

#     if prediction == 1:
#         st.markdown('<div class="output-box danger">🚨 <strong>High Flood Risk Detected!</strong><br>Please take emergency precautions and stay tuned to alerts.</div>', unsafe_allow_html=True)
#     else:
#         st.markdown('<div class="output-box safe">✅ <strong>No Flood Risk Detected.</strong><br>Continue monitoring the weather and stay safe.</div>', unsafe_allow_html=True)

# st.markdown("</div>", unsafe_allow_html=True)

# # --- Footer ---
# st.markdown("""
# <hr>
# <div style="text-align:center; font-size: 14px; color: #888;">
#     © 2025 Smart Flood Alert | Created by Megha, Heena, Kinnari, Atika & Roshni
# </div>
# """, unsafe_allow_html=True)




# app.py
import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model_nasa.pkl", "rb"))

# --- Page Config ---
st.set_page_config(page_title="Flood Alert System", page_icon="🌧️", layout="centered")

# --- Custom CSS ---
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        background-color: #f2f6fc;
    }
    .main-container {
        background-color: white;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        max-width: 700px;
        margin: auto;
    }
    .header {
        text-align: center;
        padding: 1.5rem 1rem;
        border-radius: 12px;
        background: linear-gradient(135deg, #4fc3f7, #1976d2);
        color: white;
        margin-bottom: 1.5rem;
    }
    .input-row {
        margin-top: 1rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #1976d2;
        color: white;
        padding: 0.6rem;
        border: none;
        border-radius: 8px;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #125ea7;
    }
    .alert-box {
        margin-top: 2rem;
        padding: 1.2rem;
        border-radius: 10px;
        font-size: 1.1rem;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    .danger {
        background-color: #ffebee;
        border-left: 6px solid #d32f2f;
        color: #b71c1c;
    }
    .safe {
        background-color: #e8f5e9;
        border-left: 6px solid #388e3c;
        color: #1b5e20;
    }
    .emoji {
        font-size: 2rem;
    }
    footer {
        visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)

# --- Main UI ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<div class="header"><h2>🌧️ Smart Flood Alert System</h2><p>Predict flood risk based on rainfall data</p></div>', unsafe_allow_html=True)

# --- Input Form ---
with st.form("flood_form"):
    col1, col2 = st.columns(2)
    with col1:
        rainfall_1d = st.number_input("🌧️ 1-Day Rainfall (mm)", min_value=0.0, step=0.1, format="%.1f")
    with col2:
        rainfall_2d = st.number_input("🌧️ 2-Day Total Rainfall (mm)", min_value=0.0, step=0.1, format="%.1f")

    submitted = st.form_submit_button("🔍 Check Flood Risk")

# --- Prediction Display ---
if submitted:
    features = np.array([[rainfall_1d, rainfall_2d]])
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.markdown(
            '<div class="alert-box danger"><span class="emoji">🚨</span>'
            '<div><strong>High Flood Risk Detected!</strong><br>Please take emergency precautions and stay updated.</div></div>',
            unsafe_allow_html=True)
    else:
        st.markdown(
            '<div class="alert-box safe"><span class="emoji">✅</span>'
            '<div><strong>No Flood Risk Detected.</strong><br>Conditions are normal. Stay safe and keep monitoring.</div></div>',
            unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
    <hr style="margin-top:2rem;">
    <div style="text-align: center; font-size: 13px; color: #888;">
        © 2025 Smart Flood Alert • Team: Megha, Heena, Kinnari, Atika & Roshni
    </div>
</div>
""", unsafe_allow_html=True)
