#!/bin/bash

echo "🎯 Tiny Monopoly - Time to talk about money (Mac)"
echo "📚 Designed for beginner savers and investors"
echo ""

# Check if Python is installed
echo "Checking Python environment..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed. Please install Python 3.8+ first."
    echo "   You can install it from: https://www.python.org/downloads/"
    exit 1
else
    echo "✅ Python 3 is installed: $(python3 --version)"
fi

echo ""
echo "Installing Python dependencies..."
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "❌ Error: Failed to install Python dependencies"
    echo "   Please check your internet connection and try again"
    exit 1
else
    echo "✅ Python dependencies installed successfully"
fi

echo ""
echo "Starting Tiny Monopoly API server..."
echo "📚 Server will run at: http://localhost:8000"
echo "🌱 Focus: Step-by-step financial education for beginners"
echo ""
echo "Keep this terminal open while using the app!"
echo ""

# Start the enhanced API server
python3 qwen_chatbot_api.py
