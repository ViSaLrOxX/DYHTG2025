from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import re
import random
from datetime import datetime

# Load model
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

print("🏦 Chase UK – Financial Education Assistant")
print("Type 'help' for commands, 'products' for services, 'quit' to exit\n")

# Enhanced personality for educational focus
chase_personality = (
    "You are a Chase UK financial educator. You explain banking concepts clearly. "
    "You help people understand how banking works in the UK. "
    "You teach about savings, current accounts, and financial basics. "
    "You NEVER access real accounts or give personal financial advice. "
    "You use examples with placeholder amounts like 'for example, £500'. "
    "You are friendly, patient, and focus on financial education. "
    "You explain FSCS protection, interest rates, and banking safety. "
    "You help people make informed decisions about their finances."
)

class ChaseEducationalBot:
    def __init__(self):
        self.chat_history = chase_personality
        self.learning_topics = set()
        
        # Educational scenarios (NO real data)
        self.financial_scenarios = {
            'savings_example': {
                'amount': '£1,000',
                'interest_rate': '4.1%',
                'monthly_saving': '£200',
                'goal': 'emergency fund'
            },
            'budget_example': {
                'income': '£2,500',
                'rent': '£800', 
                'bills': '£300',
                'food': '£250',
                'savings': '£500'
            }
        }
    
    def generate_educational_example(self, topic):
        """Create realistic but fictional examples"""
        examples = {
            'savings': f"If you save {self.financial_scenarios['savings_example']['monthly_saving']} monthly at {self.financial_scenarios['savings_example']['interest_rate']} AER, in one year you could have approximately £2,500 including interest.",
            
            'budgeting': f"With a monthly income of {self.financial_scenarios['budget_example']['income']}, a sample budget might be:\n• Rent: {self.financial_scenarios['budget_example']['rent']}\n• Bills: {self.financial_scenarios['budget_example']['bills']}\n• Food: {self.financial_scenarios['budget_example']['food']}\n• Savings: {self.financial_scenarios['budget_example']['savings']}",
            
            'emergency_fund': "A good emergency fund is 3-6 months of essential expenses. For example, if your essential bills are £1,200 monthly, aim for £3,600-£7,200 in an easy-access savings account.",
            
            'interest_calculation': "With £1,000 at 4.1% AER, you'd earn about £41 interest in one year. Interest is typically calculated daily and paid monthly."
        }
        return examples.get(topic, "Let me explain this concept with a simple example...")
    
    def handle_educational_query(self, user_input):
        """Handle financial education without real data"""
        user_lower = user_input.lower()
        
        # Savings education
        if any(word in user_lower for word in ['save', 'savings', 'interest']):
            self.learning_topics.add('savings')
            return self.generate_educational_example('savings')
        
        # Budgeting education  
        if any(word in user_lower for word in ['budget', 'spending', 'manage money']):
            self.learning_topics.add('budgeting')
            return self.generate_educational_example('budgeting')
        
        # Emergency fund education
        if any(word in user_lower for word in ['emergency', 'rainy day', 'safety net']):
            self.learning_topics.add('emergency_fund')
            return self.generate_educational_example('emergency_fund')
        
        # Banking concepts
        if any(word in user_lower for word in ['how does', 'what is', 'explain']):
            if 'interest' in user_lower:
                return self.generate_educational_example('interest_calculation')
            elif 'fscs' in user_lower:
                return "FSCS protects your money up to £85,000 per person, per banking group. It's like a safety net for your savings if a bank fails."
        
        return None
    
    def get_product_education(self):
        """Educational information about Chase products"""
        return (
            "🏦 **Chase UK Products - Educational Overview**\n\n"
            "💳 **Current Account**:\n"
            "• Learn about cashback rewards on everyday spending\n"
            "• Understand how round-up savings work\n"
            "• No monthly fees - good for learning banking basics\n\n"
            "💰 **Saver Account**:\n" 
            "• Example: 4.1% AER on savings balances\n"
            "• Teaches compound interest concepts\n"
            "• FSCS protected - important safety knowledge\n\n"
            "📈 **Investment Platform**:\n"
            "• Educational resources about investing\n"
            "• Learn about diversification and risk\n"
            "• Understanding stocks vs funds\n\n"
            "Which would you like to learn more about?"
        )
    
    def chat(self):
        print("💬 Hello! I'm here to help you learn about banking and finances. How can I assist you today?")
        
        while True:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ['quit', 'exit']:
                print(f"\nChase UK: Thanks for learning with us! 📚")
                if self.learning_topics:
                    print(f"You explored: {', '.join(self.learning_topics)}")
                break
            
            if user_input.lower() in ['help', 'commands']:
                print("\n📖 I can help you learn about:\n• Banking basics 🏦\n• Savings & interest 💰\n• Budgeting 📊\n• Financial safety 🔒\n• Chase products 📱\n• UK banking terms 🇬🇧\nType 'products' to see educational product info!")
                continue
            
            if user_input.lower() == 'products':
                print(f"\nChase UK: {self.get_product_education()}")
                continue
            
            if user_input.lower() == 'topics':
                topics = self.learning_topics or ["Start by asking about savings or budgeting!"]
                print(f"\n📚 Topics you've explored: {', '.join(topics)}")
                continue
            
            # Try educational response first
            educational_response = self.handle_educational_query(user_input)
            if educational_response:
                print(f"Chase UK: {educational_response}")
                # Add to conversation context
                self.chat_history += f"\nUser: {user_input}\nChase UK: {educational_response}"
                continue
            
            # Use AI for general conversation
            conversation = f"{self.chat_history}\nUser: {user_input}\nChase UK:"
            
            inputs = tokenizer(conversation, return_tensors="pt", truncation=True, max_length=1024)
            reply_ids = model.generate(
                **inputs, max_length=200, do_sample=True, 
                temperature=0.7, pad_token_id=tokenizer.eos_token_id
            )
            reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
            
            if "Chase UK:" in reply:
                reply = reply.split("Chase UK:")[-1].strip()
            
            print(f"Chase UK: {reply}")
            
            # Update context
            self.chat_history = f"{chase_personality}\nUser: {user_input}\nChase UK: {reply}"
            
            # Keep history manageable
            if len(self.chat_history) > 1500:
                self.chat_history = chase_personality + "\n" + "\n".join(self.chat_history.split("\n")[-6:])

# Run the bot
if __name__ == "__main__":
    bot = ChaseEducationalBot()
    bot.chat()