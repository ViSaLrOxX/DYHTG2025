from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

print("Starting BankBuddy API Server...")
print("Server will run at: http://localhost:5000")

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'message': 'BankBuddy API is running'})

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get('message', '')
        user_id = data.get('user_id', 'default')
        
        # Simple response logic
        if 'hello' in message.lower() or 'hi' in message.lower():
            reply = "Hello! I'm BankBuddy, your personal finance assistant. How can I help you with banking or savings today?"
        elif 'bank' in message.lower() or 'savings' in message.lower():
            reply = "I can help you with banking advice! Consider opening a high-yield savings account or checking out local credit unions for better rates."
        elif 'money' in message.lower() or 'budget' in message.lower():
            reply = "Great question about money management! Start by tracking your expenses and creating a budget. The 50/30/20 rule is a good starting point."
        elif 'loan' in message.lower() or 'credit' in message.lower():
            reply = "For loans and credit, it's important to understand interest rates and terms. Always compare offers from multiple lenders before deciding."
        else:
            reply = "I'm here to help with your financial questions! Ask me about banking, savings, budgeting, loans, or any other finance topics."
        
        return jsonify({
            'reply': reply,
            'user_id': user_id
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/clear_history', methods=['POST'])
def clear_history():
    return jsonify({'message': 'Chat history cleared'})

if __name__ == '__main__':
    print("BankBuddy API Server is starting...")
    print("Visit http://localhost:5000/health to check server status")
    app.run(host='0.0.0.0', port=5000, debug=True)
