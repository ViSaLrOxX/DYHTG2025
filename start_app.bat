@echo off
echo 🏦 BankBuddy - Personal Finance Assistant Startup Script
echo.

echo Checking Python environment...
python --version
if %errorlevel% neq 0 (
    echo Error: Python environment not found, please install Python first
    pause
    exit /b 1
)

echo.
echo Installing Python dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error: Failed to install Python dependencies
    pause
    exit /b 1
)

echo.
echo Starting Python API server...
echo Please keep this window open, API server will run at http://localhost:5000
echo.
start "BankBuddy API Server" python chatbot_api.py

echo Waiting for API server to start...
timeout /t 5 /nobreak >nul

echo.
echo Starting Flutter application...
echo Please ensure you have Flutter SDK installed
echo.
cd flutter\flutter_application_1
flutter pub get
flutter run

pause
