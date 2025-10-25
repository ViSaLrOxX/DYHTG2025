from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import re

# Load Blenderbot model
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

print("🏦 BankBuddy – Your Beginner Finance Chatbot")
print("Type 'quit' to exit.\n")

# System intro for personality
intro = (
    "You are BankBuddy, a friendly assistant who helps beginners understand personal finance. "
    "Answer clearly, in plain English, with short explanations and simple examples. "
    "If asked about risky investments or personal financial advice, respond with general education only." 
)

chat_history = intro
user_goals = {}

def get_bank_suggestions(query):
    """Return example bank suggestions, optionally using Google search if available"""
    return [
        "JPMorganChase – offers safe savings accounts and new user offer",
        "LloydBank – good long-term savings rates and monthly saving",
        "Monzo – beginner-friendly and insured"
    ]

def extract_intent(user_input):
    """Determine if the user wants a suggestion or general advice"""
    suggestion_keywords = ["suggest", "recommend", "advice", "good bank", "interest rate", "save money", "give me", "advice"]
    if any(word in user_input.lower() for word in suggestion_keywords):
        return "suggestion"
    return "friendly"

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("BankBuddy: Goodbye! Remember, saving regularly builds good habits 💰")
        break

    intent = extract_intent(user_input)

    # Prepare conversation context
    chat_history += f"\nUser: {user_input}\nBankBuddy:"

    # Generate reply from Blenderbot
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

    # Show reply
    print("BankBuddy:", reply)

    # Add reply to chat history
    chat_history += " " + reply
