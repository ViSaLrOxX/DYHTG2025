# 🔧 BankBuddy Troubleshooting Guide

## Quick Fix Steps:

### 1. First, try the debug script:
```bash
# Run this to check everything step by step
debug_setup.bat
```

### 2. If you get "Not Found" error, check these:

#### A. Make sure the API server is running:
- Look for this message in the console: "BankBuddy API Server starting..."
- You should see: "Visit http://localhost:5000/health to check server status"

#### B. Test the API manually:
```bash
# Open a new terminal/command prompt and run:
python test_api.py
```

#### C. Check if Flask is installed:
```bash
python -c "import flask; print('Flask version:', flask.__version__)"
```

### 3. Common Issues and Solutions:

#### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution:**
```bash
pip install flask flask-cors
```

#### Issue: "ModuleNotFoundError: No module named 'transformers'"
**Solution:**
```bash
pip install transformers torch
```

#### Issue: Server starts but Flutter can't connect
**Solution:**
- Make sure the API server is running on http://localhost:5000
- Check Windows Firewall settings
- Try accessing http://localhost:5000/health in your browser

#### Issue: "Not Found" when accessing endpoints
**Solution:**
- Make sure you're using POST for /chat endpoint
- Make sure you're using GET for /health endpoint
- Check the exact URL: http://localhost:5000/health

### 4. Manual Testing:

#### Test Health Endpoint:
Open browser and go to: http://localhost:5000/health
You should see: {"status": "healthy", "message": "BankBuddy API is running normally"}

#### Test Chat Endpoint:
Use a tool like Postman or curl:
```bash
curl -X POST http://localhost:5000/chat -H "Content-Type: application/json" -d "{\"message\": \"Hello\"}"
```

### 5. If nothing works:

1. **Restart everything:**
   - Close all terminals
   - Run `debug_setup.bat` again
   - Wait for "BankBuddy API Server starting..." message

2. **Check Python version:**
   ```bash
   python --version
   ```
   Should be Python 3.8 or higher

3. **Reinstall dependencies:**
   ```bash
   pip uninstall flask flask-cors transformers torch numpy
   pip install flask==2.3.3 flask-cors==4.0.0 transformers==4.35.2 torch==2.1.1 numpy==1.24.3
   ```

## Still having issues?

Run this command and share the output:
```bash
python -c "import sys; print('Python:', sys.version); import flask; print('Flask:', flask.__version__)"
```
