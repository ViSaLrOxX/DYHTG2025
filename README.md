# 🏦 BankBuddy - Personal Finance Assistant

This is a personal finance chatbot application based on Flutter and Python, helping beginners understand banking, savings, and financial knowledge.

## 📋 Features

- 🤖 Intelligent chatbot based on Facebook's Blenderbot model
- 💬 Friendly user interface with real-time chat
- 🏦 Professional banking and financial advice
- 📱 Cross-platform support (Android, iOS, Web, Windows, macOS, Linux)
- 🔄 Real-time server status monitoring
- 📝 Chat history management

## 🚀 Quick Start

### Method 1: Using Startup Script (Recommended)

1. Double-click to run `start_app.bat` file
2. The script will automatically install dependencies and start services

### Method 2: Manual Startup

#### 1. Start Python API Server

```bash
# Install Python dependencies
pip install -r requirements.txt

# Start API server
python chatbot_api.py
```

The API server will run at `http://localhost:5000`

#### 2. Start Flutter Application

```bash
# Enter Flutter project directory
cd flutter/flutter_application_1

# Install Flutter dependencies
flutter pub get

# Run application
flutter run
```

## 📁 Project Structure

```
DYHTG2025/
├── ai_agent.py                 # Original Python chatbot
├── chatbot_api.py              # Flask API server
├── requirements.txt            # Python dependencies
├── start_app.bat              # Startup script
├── README.md                  # Documentation
└── flutter/
    └── flutter_application_1/
        ├── lib/
        │   ├── main.dart              # Main application entry
        │   ├── models/
        │   │   └── chat_message.dart  # Chat message model
        │   ├── providers/
        │   │   └── chat_provider.dart # State management
        │   ├── screens/
        │   │   └── chat_screen.dart   # Chat interface
        │   └── services/
        │       └── chat_service.dart  # API communication service
        ├── pubspec.yaml              # Flutter dependency configuration
        └── ...
```

## 🔧 API Endpoints

### POST /chat
Send message to chatbot

**Request Body:**
```json
{
  "message": "User message",
  "user_id": "User ID (optional)"
}
```

**Response:**
```json
{
  "reply": "Bot reply",
  "user_id": "User ID"
}
```

### GET /health
Check server health status

**Response:**
```json
{
  "status": "healthy",
  "message": "BankBuddy API is running normally"
}
```

### POST /clear_history
Clear user chat history

**Request Body:**
```json
{
  "user_id": "User ID (optional)"
}
```

## 🛠️ Tech Stack

### Backend
- **Python 3.8+**
- **Flask** - Web framework
- **Flask-CORS** - Cross-origin support
- **Transformers** - Hugging Face model library
- **Blenderbot** - Facebook conversation model

### Frontend
- **Flutter** - Cross-platform UI framework
- **Provider** - State management
- **HTTP** - Network requests

## 📱 Supported Platforms

- ✅ Android
- ✅ iOS
- ✅ Web
- ✅ Windows
- ✅ macOS
- ✅ Linux

## 🔍 Troubleshooting

### Common Issues

1. **Cannot connect to server**
   - Ensure Python API server is running
   - Check firewall settings
   - Confirm port 5000 is not occupied

2. **Flutter dependency installation failed**
   ```bash
   flutter clean
   flutter pub get
   ```

3. **Python model download failed**
   - Check network connection
   - Ensure sufficient disk space
   - Consider using domestic mirror sources

### Debug Mode

Start API server with debug information:
```bash
python chatbot_api.py
```

Flutter application debugging:
```bash
flutter run --debug
```

## 📄 License

This project is for learning and demonstration purposes only.

## 🤝 Contributing

Welcome to submit Issues and Pull Requests to improve this project!

## 📞 Support

If you encounter any issues, please check:
1. Python version is 3.8+
2. Flutter SDK is properly installed
3. Network connection is normal
4. All dependencies are correctly installed