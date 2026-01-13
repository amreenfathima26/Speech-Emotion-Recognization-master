# Deployment Guide

## 1. Local Setup
I have created a `run_app.bat` file for you.
Double-click **`run_app.bat`** to install dependencies and start the app locally.

## 2. Push to GitHub
I have already initialized the Git repository and committed your files.
To push to GitHub, follow these steps:

1.  **Create a New Repository** on [GitHub](https://github.com/new). Name it `speech-emotion-app` (or similar).
2.  **Copy the URL** of your new repository (e.g., `https://github.com/your-username/speech-emotion-app.git`).
3.  **Run the following commands** in your terminal (or open Git Bash in this folder):

```bash
git remote add origin YOUR_GITHUB_REPO_URL
git branch -M main
git push -u origin main
```
*(Replace `YOUR_GITHUB_REPO_URL` with the actual URL)*

## 3. Deploy to Streamlit Community Cloud (Free)
Streamlit Community Cloud is the best free place to host Streamlit apps.

1.  Go to [share.streamlit.io](https://share.streamlit.io/) and Sign In with GitHub.
2.  Click **"New app"**.
3.  Select your repository (`speech-emotion-app`) from the list.
4.  **Main file path**: `app.py`
5.  Click **"Deploy!"**.

Your app will be live in minutes!

## Notes on the Model
- The app is currently in **Demo Mode** because no trained model (`model.pkl`) exists yet.
- To make it "Real", you need to:
    1.  Download the **RAVDESS** dataset.
    2.  Place the `Actor_*` folders inside a folder named `data` in this directory.
    3.  Run `python train_model.py`.
    4.  This will generate `model.pkl`.
    5.  Commit and push `model.pkl` to GitHub (Warning: It might be large, you might need Git LFS if >100MB, but usually it's small enough).
    6.  **Alternatively**, you can just use the Demo Mode to show off the UI and code logic!
