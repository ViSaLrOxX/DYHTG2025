# 🍎 BankBuddy Mac Setup Guide

## 🎯 **Educational Personal Finance Assistant for Mac**

This guide will help you set up BankBuddy on your Mac with the new educational AI model designed specifically for beginner savers and investors.

## 📋 **Prerequisites**

### **1. Python Installation**
```bash
# Check if Python 3 is installed
python3 --version

# If not installed, install via Homebrew (recommended)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python3

# Or download from python.org
# Visit: https://www.python.org/downloads/macos/
```

### **2. Verify Installation**
```bash
python3 --version  # Should show Python 3.8+
pip3 --version     # Should show pip version
```

## 🚀 **Quick Start (Mac)**

### **Method 1: Using the Mac Script (Recommended)**
```bash
# Navigate to your project directory
cd /path/to/your/DYHTG2025

# Make the script executable
chmod +x start_app_mac.sh

# Run the startup script
./start_app_mac.sh
```

### **Method 2: Manual Setup**
```bash
# 1. Install Python dependencies
pip3 install -r requirements.txt

# 2. Start the educational API server
python3 educational_chatbot_api.py
```

## 🎓 **New Educational Features**

### **Comprehensive Financial Education Modules:**

#### **📚 Saving Basics**
- Emergency Fund guidance (3-6 months expenses)
- Budgeting with 50/30/20 rule
- Compound interest explanations
- Step-by-step saving strategies

#### **📈 Investing Fundamentals**
- Index funds for beginners
- Risk tolerance assessment
- Stock vs. Bond explanations
- Target date funds
- Dollar-cost averaging

#### **💳 Debt Management**
- Credit card best practices
- Debt snowball vs. avalanche methods
- Student loan strategies
- Credit score building

#### **🏖️ Retirement Planning**
- 401(k) and IRA basics
- Employer matching strategies
- Roth vs. Traditional accounts
- Time value of money

## 🔧 **API Endpoints**

### **Educational Chat**
```bash
POST http://localhost:5000/chat
Content-Type: application/json

{
  "message": "How do I start saving money?",
  "user_id": "your_user_id"
}
```

### **Health Check**
```bash
GET http://localhost:5000/health
```

### **Available Topics**
```bash
GET http://localhost:5000/topics
```

### **Clear History**
```bash
POST http://localhost:5000/clear_history
Content-Type: application/json

{
  "user_id": "your_user_id"
}
```

## 💡 **Sample Questions to Try**

### **Saving Questions:**
- "How much should I have in my emergency fund?"
- "What's the 50/30/20 budgeting rule?"
- "How does compound interest work?"
- "How do I start saving $1000?"

### **Investing Questions:**
- "What's an index fund?"
- "How do I determine my risk tolerance?"
- "What's the difference between stocks and bonds?"
- "Should I invest in a 401(k) or IRA first?"

### **Debt Questions:**
- "How do I pay off credit card debt?"
- "What's the debt snowball method?"
- "How do I improve my credit score?"
- "Should I pay off debt or invest first?"

### **Retirement Questions:**
- "How much should I save for retirement?"
- "What's the difference between Roth and Traditional IRA?"
- "How does employer 401(k) matching work?"
- "Is it too late to start saving for retirement at 30?"

## 🌐 **Web Interface**

### **Using the Web Chat Interface:**
1. Start the API server: `python3 educational_chatbot_api.py`
2. Open `web_chat.html` in your browser
3. Start chatting with BankBuddy!

### **Features:**
- ✅ Real-time chat interface
- ✅ Server status monitoring
- ✅ Message history
- ✅ Educational responses
- ✅ Beginner-friendly explanations

## 🔍 **Troubleshooting**

### **Common Issues:**

#### **Python Not Found**
```bash
# Add Python to PATH
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

#### **Permission Denied**
```bash
# Fix script permissions
chmod +x start_app_mac.sh
```

#### **Port Already in Use**
```bash
# Find and kill process using port 5000
lsof -ti:5000 | xargs kill -9
```

#### **Dependencies Issues**
```bash
# Update pip and reinstall
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

## 📱 **Flutter Integration (Optional)**

### **For Flutter Development:**
```bash
# Install Flutter SDK
brew install --cask flutter

# Navigate to Flutter project
cd flutter/flutter_application_1

# Install dependencies
flutter pub get

# Run on iOS Simulator
flutter run
```

## 🎯 **Key Differences from Previous Version**

### **Enhanced Educational Content:**
- ✅ **Comprehensive Modules**: Saving, Investing, Debt, Retirement
- ✅ **Step-by-Step Guidance**: Detailed explanations for beginners
- ✅ **Real Examples**: Practical scenarios and calculations
- ✅ **Progressive Learning**: Builds knowledge systematically
- ✅ **Encouraging Tone**: Motivates users to take action

### **Improved AI Responses:**
- ✅ **Educational Focus**: Teaches concepts, not just answers
- ✅ **Beginner-Friendly**: No complex jargon
- ✅ **Actionable Advice**: Specific steps users can take
- ✅ **Context Awareness**: Remembers conversation history
- ✅ **Multiple Formats**: Text, examples, and analogies

## 🚀 **Next Steps**

1. **Start the Server**: Run `./start_app_mac.sh`
2. **Test the API**: Try the sample questions above
3. **Use Web Interface**: Open `web_chat.html`
4. **Integrate with Flutter**: Update your Flutter app to use the new API
5. **Customize Content**: Modify `educational_chatbot_api.py` for your needs

## 📞 **Support**

If you encounter any issues:
1. Check the troubleshooting section above
2. Verify Python 3.8+ is installed
3. Ensure all dependencies are installed
4. Check that port 5000 is available

---

**🎉 Congratulations!** You now have a comprehensive educational personal finance assistant running on your Mac!
