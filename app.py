import streamlit as st
import numpy as np
import joblib
import os
import time
import librosa
from utilities import extract_feature

# Set page configuration
st.set_page_config(
    page_title="Speech Emotion Recognition",
    page_icon="🎙️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
        }
        .stButton>button {
            width: 100%;
            background-color: #ff4b4b;
            color: white;
            font-weight: bold;
        }
        .emotion-box {
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: white;
            margin-top: 20px;
        }
        .happy { background-color: #2ecc71; }
        .sad { background-color: #3498db; }
        .angry { background-color: #e74c3c; }
        .neutral { background-color: #95a5a6; }
        .other { background-color: #f1c40f; color: black; }
    </style>
""", unsafe_allow_html=True)

st.title("🎙️ Speech Emotion Recognition")
st.write("Upload an audio file to analyze the emotion.")

# Sidebar
st.sidebar.header("About")
st.sidebar.info(
    "This application uses a Machine Learning model (MLP Classifier) "
    "to detect emotions from speech audio. "
    "Supported emotions: Happy, Sad, Angry, Neutral."
)

# Load Model
@st.cache_resource
def load_model():
    model_path = "model.pkl"
    if os.path.exists(model_path):
        return joblib.load(model_path), True
    else:
        return None, False

model, model_loaded = load_model()

if not model_loaded:
    st.warning("⚠️ **Model file (model.pkl) not found.** Running in **Demo Mode**.")
    st.info("To use the real model, please train it using `python train_model.py` with the RAVDESS dataset.")

# File Uploader
uploaded_file = st.file_uploader("Choose a WAV file", type=["wav"])

if uploaded_file is not None:
    # Display audio player
    st.audio(uploaded_file, format='audio/wav')
    
    if st.button("Analyze Emotion"):
        with st.spinner("Analyzing..."):
            # Simulate processing time for better UX
            time.sleep(1)
            
            try:
                # Save temp file
                with open("temp.wav", "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                emotion_result = ""
                
                if model_loaded:
                    # Extract features
                    # Note: We need to handle the feature extraction exactly as training
                    # extract_feature returns a 1D array, logic needs to match utilities.py/training
                    features = extract_feature("temp.wav", mfcc=True, chroma=True, mel=True)
                    
                    # Reshape for prediction (1 sample, n features)
                    features = features.reshape(1, -1)
                    
                    # Predict
                    prediction = model.predict(features)
                    emotion_result = prediction[0]
                else:
                    # PURELY FOR DEMO/TESTING PURPOSE WHEN NO MODEL IS PRESENT
                    # Randomly pick an emotion based on file name hash or length to be deterministic-ish
                    import random
                    emotions = ["happy", "sad", "angry", "neutral"]
                    # Use file size to seed so it's consistent for the same file
                    random.seed(uploaded_file.size)
                    emotion_result = random.choice(emotions)
                    st.toast("Using Demo/Mock Prediction", icon="🤖")

                # Display Result
                st.subheader("Result:")
                
                # Dynamic styling based on emotion
                emotion_class = emotion_result.lower()
                if emotion_class not in ["happy", "sad", "angry", "neutral"]:
                    emotion_class = "other"
                
                st.markdown(f"""
                    <div class="emotion-box {emotion_class}">
                        Detected Emotion: {emotion_result.upper()}
                    </div>
                """, unsafe_allow_html=True)
                
                # Cleanup
                if os.path.exists("temp.wav"):
                    os.remove("temp.wav")
                    
            except Exception as e:
                st.error(f"An error occurred: {e}")

st.markdown("---")
st.caption("Developed by Amreen Fathima | 2024")
