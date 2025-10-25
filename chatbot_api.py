from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import re
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Load Blenderbot model
print("Loading BankBuddy model...")
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
print("Model loaded successfully!")

# System introduction
intro = (
    "You are BankBuddy, a friendly assistant who helps beginners understand personal finance. "
    "Answer clearly, in plain English, with short explanations and simple examples. "
    "If asked about risky investments or personal financial advice, respond with general education only." 
)

# Store chat history for each user
user_chat_histories = {}

def get_bank_suggestions(query):
    """Return example bank suggestions"""
    return [
        "JPMorganChase – offers safe savings accounts and new user offers",
        "LloydBank – good long-term savings rates and monthly saving",
        "Monzo – beginner-friendly and insured"
    ]

def extract_intent(user_input):
    """Determine if the user wants suggestions or general advice"""
    suggestion_keywords = ["suggest", "recommend", "advice", "good bank", "interest rate", "save money", "give me", "advice"]
    if any(word in user_input.lower() for word in suggestion_keywords):
        return "suggestion"
    return "friendly"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_input = data.get('message', '')
        user_id = data.get('user_id', 'default')
        
        if not user_input:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Get or create user's chat history
        if user_id not in user_chat_histories:
            user_chat_histories[user_id] = intro
        
        chat_history = user_chat_histories[user_id]
        
        # Determine user intent
        intent = extract_intent(user_input)
        
        # Prepare conversation context
        chat_history += f"\nUser: {user_input}\nBankBuddy:"
        
        # Generate reply
        inputs = tokenizer(chat_history, return_tensors="pt", truncation=True)
        reply_ids = model.generate(**inputs, max_length=120, do_sample=True, temperature=0.7)
        reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
        
        # Extract new part (avoid repeating old context)
        if "BankBuddy:" in reply:
            reply = reply.split("BankBuddy:")[-1].strip()
        
        # If intent is suggestion, override with structured suggestions
        if intent == "suggestion":
            if re.search(r"bank|interest", user_input, re.I):
                suggestions = get_bank_suggestions("best savings account UK 3 months")
                reply = "Here are some banks you could check:\n" + "\n".join(suggestions)
            elif re.search(r"save|money", user_input, re.I):
                reply = "You could consider a fixed deposit, a high-interest savings account, or putting money in a beginner-friendly savings plan."
        
        # Update chat history
        user_chat_histories[user_id] = chat_history + " " + reply
        
        return jsonify({
            'reply': reply,
            'user_id': user_id
        })
        
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'message': 'BankBuddy API is running normally'})

@app.route('/clear_history', methods=['POST'])
def clear_history():
    try:
        data = request.get_json()
        user_id = data.get('user_id', 'default')
        
        if user_id in user_chat_histories:
            user_chat_histories[user_id] = intro
        
        return jsonify({'message': 'Chat history cleared'})
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

if __name__ == '__main__':
    print("🏦 BankBuddy API Server starting...")
    print("Visit http://localhost:5000/health to check server status")
    app.run(host='0.0.0.0', port=5000, debug=True)
