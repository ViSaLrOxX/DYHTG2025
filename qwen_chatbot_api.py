from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoTokenizer, AutoModelForCausalLM

app = Flask(__name__)
CORS(app)

tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-0.6B")
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-0.6B")

prompt = ("You are BankBuddy, a friendly assistant who helps beginners understand personal finance. "
        "Answer clearly, in plain English, with short explanations and simple examples. "
        "If asked about risky investments or personal financial advice, respond with general education only.")

user_chat_histories = {}

print("Starting BankBuddy API Server...")
print("Server will run at: http://localhost:8000")

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'message': 'BankBuddy API is running'})

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get('message', '')
        user_id = data.get('user_id', 'default')
        
        if not message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        if user_id not in user_chat_histories:
            user_chat_histories[user_id] = [{"role": "system", "content": prompt}]
            
        chat_history = user_chat_histories[user_id]
        chat_history.append({"role": "user", "content": message})
        
        text = tokenizer.apply_chat_template(
            chat_history,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=True)
        
        model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
            
        # conduct text completion
        generated_ids = model.generate(**model_inputs, max_new_tokens=32768)
        output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist()
        
        # parsing thinking content
        try:
            # rindex finding 151668 (</think>)
            index = len(output_ids) - output_ids[::-1].index(151668)
        except ValueError:
            index = 0
            
        content = tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")
        
        return jsonify({
            'reply': content,
            'user_id': user_id
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/clear_history', methods=['POST'])
def clear_history():
    data = request.get_json()
    user_id = data.get('user_id', '')
    if not user_id:
        return jsonify({'error': 'Invalid user id'}), 400
    user_chat_histories.pop(user_id, None)
    return jsonify({'message': 'Chat history cleared'})

if __name__ == '__main__':
    print("BankBuddy API Server is starting...")
    print("Visit http://localhost:8000/health to check server status")
    app.run(host='0.0.0.0', port=8000, debug=True)
