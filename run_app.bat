@echo off
echo [*] Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [!] Error installing dependencies. Please check your python installation.
    pause
    exit /b
)

echo [*] Starting Streamlit App...
echo [*] NOTE: If you haven't trained the model, the app will run in Demo Mode.
echo [*] To train the model, ensure you have data in a 'data' folder and run: python train_model.py
echo.
streamlit run app.py
pause
