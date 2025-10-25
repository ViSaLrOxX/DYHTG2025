from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# Load the model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

print("🏦 BankBuddy – Your Beginner Finance Chatbot")
print("Type 'quit' to exit.\n")

# Simple introduction context
intro = (
    "You are BankBuddy, a friendly assistant who helps beginners understand personal finance. "
    "Answer clearly, in plain English, with short explanations and simple examples. "
    "If asked about risky investments or personal financial advice, respond with general education only."
)

# Keep short chat history
chat_history = intro

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("BankBuddy: Goodbye! Remember, saving regularly builds good habits 💰")
        break

    # Add user input to conversation
    chat_history += f"\nUser: {user_input}\nBankBuddy:"

    # Encode and generate response
    inputs = tokenizer(chat_history, return_tensors="pt", truncation=True)
    reply_ids = model.generate(**inputs, max_length=120, do_sample=True, temperature=0.7)
    reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True)

    # Extract only the new part (avoid repeating old context)
    if "BankBuddy:" in reply:
        reply = reply.split("BankBuddy:")[-1].strip()

    print("BankBuddy:", reply)

    # Add reply to context
    chat_history += " " + reply
