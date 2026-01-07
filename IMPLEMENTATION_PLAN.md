# Implementation Plan - Speech Emotion Recognition Web App

## Goal
Create a web interface for the existing Speech Emotion Recognition (SER) project and prepare it for free deployment.

## User Review Required
- **Choice of Web Framework**: I plan to use **Streamlit** because it is perfect for ML demos and offers free hosting via Streamlit Community Cloud.
- **Model Availability**: The current files seem to be training scripts. I need to ensure a trained model is saved to disk so the web app can use it without retraining every time.

## Proposed Changes

### Bug Fixes and Code Cleanup
#### [MODIFY] [utilities.py](file:///c:/Users/Sweet.Vellyn_Vgvvlsa/Desktop/AMreen/Speech-Emotion-Recognization-master/Speech-Emotion-Recognization-master/utilities.py)
- Fix typo `extract features` -> `extract_feature`.
- Handle missing data paths gracefully.
- Ensure correct imports.

### Model Training Script
#### [NEW] [train_model.py](file:///c:/Users/Sweet.Vellyn_Vgvvlsa/Desktop/AMreen/Speech-Emotion-Recognization-master/Speech-Emotion-Recognization-master/train_model.py)
- A dedicated script to train the model and save it as `model.pkl`.
- Will use `joblib` for serialization.
- NOTE: Requires RAVDESS data. I will add a check to see if data exists; if not, it will warn the user.

### Web Interface
#### [NEW] [app.py](file:///c:/Users/Sweet.Vellyn_Vgvvlsa/Desktop/AMreen/Speech-Emotion-Recognization-master/Speech-Emotion-Recognization-master/app.py)
- Streamlit app.
- Loads `model.pkl`.
- **Fallback**: If `model.pkl` is not found (because data is missing to train it), the app will run in "Demo Mode" using a mock predictor to demonstrate functionality without crashing.

### Configuration
#### [NEW] [requirements.txt](file:///c:/Users/Sweet.Vellyn_Vgvvlsa/Desktop/AMreen/Speech-Emotion-Recognization-master/Speech-Emotion-Recognization-master/requirements.txt)
- Dependencies: `streamlit`, `librosa`, `numpy`, `scikit-learn`, `soundfile`, `joblib`.

#### [NEW] [.gitignore](file:///c:/Users/Sweet.Vellyn_Vgvvlsa/Desktop/AMreen/Speech-Emotion-Recognization-master/Speech-Emotion-Recognization-master/.gitignore)
- Ignore `*.pkl`, `__pycache__`, data folders.

## Verification Plan
### Manual Verification
1.  Run `train_model.py` (expect warning about missing data).
2.  Run `streamlit run app.py`.
3.  Upload audio.
4.  Verify "Demo Mode" works if model is missing.
