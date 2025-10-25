@echo off
echo 🏦 BankBuddy - Debug and Setup Script
echo.

echo Step 1: Checking Python environment...
python --version
if %errorlevel% neq 0 (
    echo ❌ Error: Python not found. Please install Python first.
    pause
    exit /b 1
)
echo ✅ Python found

echo.
echo Step 2: Installing Python dependencies...
pip install flask==2.3.3 flask-cors==4.0.0 transformers==4.35.2 torch==2.1.1 numpy==1.24.3
if %errorlevel% neq 0 (
    echo ❌ Error: Failed to install dependencies
    echo Try running: pip install --upgrade pip
    pause
    exit /b 1
)
echo ✅ Dependencies installed

echo.
echo Step 3: Testing Flask installation...
python -c "import flask; print('Flask version:', flask.__version__)"
if %errorlevel% neq 0 (
    echo ❌ Error: Flask not properly installed
    pause
    exit /b 1
)
echo ✅ Flask working

echo.
echo Step 4: Starting API server...
echo The server will start at http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
python chatbot_api.py
