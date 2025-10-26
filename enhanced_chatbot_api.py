from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import re
import random
import requests
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Enhanced Educational AI System for Beginner Savers/Investors
class EnhancedEducationalFinanceAI:
    def __init__(self):
        # Google Custom Search API configuration
        self.google_api_key = "YOUR_GOOGLE_API_KEY"  # Replace with your actual API key
        self.google_search_engine_id = "YOUR_SEARCH_ENGINE_ID"  # Replace with your actual search engine ID
        
        self.system_prompt = """You are Tiny Monopoly, an educational personal finance assistant designed specifically for beginners. Your role is to:

1. TEACH financial concepts in simple, easy-to-understand terms
2. PROVIDE step-by-step guidance for saving and investing
3. EXPLAIN the "why" behind financial decisions
4. BUILD confidence in beginners
5. OFFER practical, actionable advice
6. USE analogies and real-world examples
7. ENCOURAGE questions and learning

Always be encouraging, patient, and educational. Avoid complex jargon and focus on building foundational knowledge."""

        # Enhanced educational content modules with structured format
        self.modules = {
            "saving": {
                "intro": "Saving money is the foundation of financial security! Let's explore how to do it effectively.",
                "topics": {
                    "emergency_fund": {
                        "title": "Emergency Fund: Your Financial Safety Net",
                        "explanation": "An emergency fund is money set aside for unexpected expenses like job loss, medical emergencies, or car repairs. It prevents you from going into debt when life throws a curveball.",
                        "suggestions": [
                            "Aim for 3-6 months of living expenses",
                            "Start with a small, achievable goal like $500",
                            "Automate transfers to a separate savings account",
                            "Keep it in a high-yield savings account for easy access"
                        ],
                        "example": "If your monthly expenses are $2000, aim for $6000-$12000 in your emergency fund.",
                        "search_terms": ["best high yield savings accounts 2024", "emergency fund savings account"]
                    },
                    "budgeting": {
                        "title": "Budgeting: Taking Control of Your Money",
                        "explanation": "A budget is a plan for how you'll spend and save your money. It helps you understand where your money goes and identify areas to cut back.",
                        "suggestions": [
                            "Use the 50/30/20 rule: 50% Needs, 30% Wants, 20% Savings/Debt",
                            "Track your income and expenses for a month",
                            "Use budgeting apps like Mint, YNAB, or PocketGuard",
                            "Review and adjust your budget monthly"
                        ],
                        "example": "50% Needs (rent, groceries), 30% Wants (dining out, entertainment), 20% Savings/Debt Repayment.",
                        "search_terms": ["best budgeting apps 2024", "free budgeting tools"]
                    },
                    "savings_goals": {
                        "title": "Setting Savings Goals: What are you saving for?",
                        "explanation": "Having clear goals makes saving easier. Break large goals into smaller, manageable steps.",
                        "suggestions": [
                            "Define short-term (1-3 years) and long-term (5+ years) goals",
                            "Assign a cost and timeline to each goal",
                            "Use separate savings accounts for different goals",
                            "Celebrate small milestones to stay motivated"
                        ],
                        "example": "Short-term: New laptop ($1000 in 6 months). Long-term: House down payment ($30,000 in 5 years).",
                        "search_terms": ["goal-based savings accounts", "savings goal calculator"]
                    }
                }
            },
            "investing": {
                "intro": "Investing can help your money grow over time, but it's important to start smart and understand the basics.",
                "topics": {
                    "basics": {
                        "title": "Investing Basics: Grow Your Money",
                        "explanation": "Investing means putting your money into assets like stocks, bonds, or real estate with the expectation of earning a return. It comes with risks, but also potential for higher growth than savings accounts.",
                        "suggestions": [
                            "Start by learning about different investment types",
                            "Don't invest money you might need in the short term (less than 5 years)",
                            "Consider your risk tolerance and time horizon",
                            "Start with low-cost index funds or ETFs"
                        ],
                        "example": "Instead of just saving $100, investing it could turn it into $105 or more over time, thanks to compound interest.",
                        "search_terms": ["best beginner investment platforms", "low cost index funds"]
                    },
                    "index_funds": {
                        "title": "Index Funds: Simple Diversification",
                        "explanation": "An index fund is a type of mutual fund or ETF that holds a diversified portfolio of stocks or bonds designed to track the performance of a specific market index.",
                        "suggestions": [
                            "Research low-cost index funds or ETFs",
                            "Consider S&P 500 index funds for broad market exposure",
                            "Look for funds with expense ratios under 0.1%",
                            "Open an investment account with a reputable brokerage"
                        ],
                        "example": "An S&P 500 index fund invests in the 500 largest US companies, giving you broad market exposure with one investment.",
                        "search_terms": ["best S&P 500 index funds", "low cost ETF brokers"]
                    },
                    "risk_tolerance": {
                        "title": "Understanding Risk Tolerance",
                        "explanation": "Risk tolerance is your ability and willingness to take on financial risk. It's crucial for choosing appropriate investments.",
                        "suggestions": [
                            "Assess your comfort level with potential losses",
                            "Consider your age, financial goals, and time horizon",
                            "Start with lower-risk options if you're new to investing",
                            "Gradually increase risk as you gain experience"
                        ],
                        "example": "A young investor with a long time horizon might have a higher risk tolerance than someone nearing retirement.",
                        "search_terms": ["risk tolerance assessment", "conservative investment options"]
                    }
                }
            },
            "debt_management": {
                "intro": "Managing debt effectively is key to financial freedom. Let's learn how to tackle it.",
                "topics": {
                    "good_bad_debt": {
                        "title": "Good Debt vs. Bad Debt",
                        "explanation": "Not all debt is bad. 'Good debt' can help build wealth or increase earning potential, while 'bad debt' is for depreciating assets and can be a financial burden.",
                        "suggestions": [
                            "Prioritize paying off high-interest 'bad debt' first",
                            "Understand the terms of all your loans",
                            "Consider debt consolidation for multiple high-interest debts",
                            "Avoid taking on new bad debt"
                        ],
                        "example": "A student loan for a degree that increases your income is 'good debt'. Credit card debt for a new TV is 'bad debt'.",
                        "search_terms": ["debt consolidation options", "low interest credit cards"]
                    },
                    "debt_snowball_avalanche": {
                        "title": "Debt Repayment Strategies: Snowball vs. Avalanche",
                        "explanation": "The Debt Snowball method pays off smallest debts first for psychological wins. The Debt Avalanche method pays off highest-interest debts first to save money.",
                        "suggestions": [
                            "List all your debts with balances and interest rates",
                            "Choose the method that motivates you most",
                            "Consider debt snowball for psychological motivation",
                            "Consider debt avalanche for maximum interest savings"
                        ],
                        "example": "Snowball: Pay off $500 credit card, then $1000 personal loan. Avalanche: Pay off 20% APR credit card, then 10% APR car loan.",
                        "search_terms": ["debt payoff calculator", "debt management tools"]
                    }
                }
            },
            "retirement": {
                "intro": "Planning for retirement early can make a huge difference thanks to compound interest!",
                "topics": {
                    "basics": {
                        "title": "Retirement Planning Basics",
                        "explanation": "Retirement planning involves setting financial goals for your post-working years and creating a strategy to achieve them.",
                        "suggestions": [
                            "Estimate your desired retirement lifestyle and expenses",
                            "Learn about retirement accounts like 401(k)s and IRAs",
                            "Start saving early to take advantage of compound interest",
                            "Consider working with a financial advisor for complex situations"
                        ],
                        "example": "Saving $100/month from age 25 can grow significantly more than saving $200/month from age 35.",
                        "search_terms": ["retirement planning calculator", "401k vs IRA comparison"]
                    },
                    "401k_ira": {
                        "title": "401(k)s and IRAs: Your Retirement Accounts",
                        "explanation": "These are tax-advantaged retirement savings accounts. A 401(k) is employer-sponsored, often with matching contributions, while an IRA can be opened by anyone.",
                        "suggestions": [
                            "Contribute at least enough to get the full employer match",
                            "Consider opening a Roth IRA for tax-free growth",
                            "Maximize contributions if possible",
                            "Review and rebalance your portfolio annually"
                        ],
                        "example": "If your employer matches 50% up to 6% of your salary, contributing 6% means they add 3% of your salary for free!",
                        "search_terms": ["best IRA providers", "401k contribution limits 2024"]
                    }
                }
            }
        }

    def search_google(self, query, num_results=3):
        """Search Google for bank and investment suggestions"""
        try:
            if self.google_api_key == "YOUR_GOOGLE_API_KEY":
                # Return mock data for demonstration
                return [
                    {
                        'title': f'Best {query.split()[0]} Options 2024',
                        'link': 'https://example.com',
                        'snippet': f'Comprehensive guide to {query} with detailed comparisons and recommendations.'
                    },
                    {
                        'title': f'Top {query.split()[0]} Providers',
                        'link': 'https://example.com',
                        'snippet': f'Compare the best {query} providers with fees, features, and user reviews.'
                    },
                    {
                        'title': f'{query.split()[0]} Reviews and Ratings',
                        'link': 'https://example.com',
                        'snippet': f'Real user reviews and expert ratings for {query} services.'
                    }
                ]
            
            url = "https://www.googleapis.com/customsearch/v1"
            params = {
                'key': self.google_api_key,
                'cx': self.google_search_engine_id,
                'q': query,
                'num': num_results
            }
            
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                results = []
                for item in data.get('items', []):
                    results.append({
                        'title': item.get('title', ''),
                        'link': item.get('link', ''),
                        'snippet': item.get('snippet', '')
                    })
                return results
            return []
        except Exception as e:
            print(f"Google search error: {e}")
            return []

    def format_response(self, title, explanation, suggestions, example=None, search_results=None):
        """Format response with clear structure"""
        response = f"**{title}**\n\n{explanation}\n\n"
        
        if suggestions:
            response += "**My Suggestions:**\n"
            for suggestion in suggestions:
                response += f"• {suggestion}\n"
            response += "\n"
        
        if example:
            response += f"**Example:** {example}\n\n"
        
        if search_results:
            response += "**Current Options to Consider:**\n"
            for result in search_results[:3]:
                response += f"• [{result['title']}]({result['link']})\n"
                response += f"  {result['snippet'][:80]}...\n\n"
        
        response += "**Need more help?** Ask me about other financial topics!"
        return response

    def get_educational_reply(self, user_input, chat_history):
        user_input_lower = user_input.lower()
        reply = ""
        topic_found = False

        # Check for general greetings
        if any(greeting in user_input_lower for greeting in ["hello", "hi", "hey"]):
            reply = """**Hi there! Let's build your financial confidence together!**

I'm Tiny Monopoly, and I believe everyone can become financially successful with the right knowledge and tools.

**Common beginner questions I can help with:**
• "I don't know where to start with saving"
• "What's the difference between stocks and bonds?"
• "How much should I save for emergencies?"
• "Is it too late to start investing?"
• "How do I get out of credit card debt?"

**Remember**: There are no stupid questions in personal finance. Ask me anything!"""
            return reply

        # Check for specific topics
        for module_name, module_content in self.modules.items():
            for topic_name, topic_data in module_content["topics"].items():
                keywords = re.split(r'\W+', topic_data["title"].lower()) + re.split(r'\W+', topic_name.lower())
                if any(keyword in user_input_lower for keyword in keywords if len(keyword) > 2):
                    # Get search results for this topic
                    search_results = []
                    if "search_terms" in topic_data:
                        for search_term in topic_data["search_terms"]:
                            search_results.extend(self.search_google(search_term))
                    
                    reply = self.format_response(
                        topic_data["title"],
                        topic_data["explanation"],
                        topic_data["suggestions"],
                        topic_data.get("example"),
                        search_results
                    )
                    topic_found = True
                    break
            if topic_found:
                break

        # Check for module intros if no specific topic found
        if not topic_found:
            if "saving" in user_input_lower or "save money" in user_input_lower:
                reply = """**Saving Money: Your Financial Foundation**

Saving money is the foundation of financial security! Here's what we can explore:

**Key Topics:**
• Emergency funds (your financial safety net)
• Budgeting (taking control of your money)
• Savings goals (what are you saving for?)

**Which topic interests you most?**"""
                topic_found = True
            elif "investing" in user_input_lower or "invest money" in user_input_lower:
                reply = """**Investing: Grow Your Money Over Time**

Investing can help your money grow, but it's important to start smart and understand the basics.

**Key Topics:**
• Investing basics (how money grows)
• Index funds (simple diversification)
• Risk tolerance (how much risk can you handle?)

**What would you like to learn about?**"""
                topic_found = True
            elif "debt" in user_input_lower or "loan" in user_input_lower:
                reply = """**Debt Management: Path to Financial Freedom**

Managing debt effectively is key to financial freedom. Let's tackle it together!

**Key Topics:**
• Good debt vs. bad debt
• Debt repayment strategies (snowball vs. avalanche)

**What's on your mind?**"""
                topic_found = True
            elif "retirement" in user_input_lower or "retire" in user_input_lower:
                reply = """**Retirement Planning: Start Early, Win Big**

Planning for retirement early can make a huge difference thanks to compound interest!

**Key Topics:**
• Retirement planning basics
• 401(k)s and IRAs (your retirement accounts)

**What would you like to know?**"""
                topic_found = True

        if not topic_found:
            reply = """**I'm Tiny Monopoly, your financial education assistant!**

I can help you learn about:

**Main Topics:**
• **Saving Money**: Emergency funds, budgeting, savings goals
• **Investing**: Basics, index funds, risk tolerance  
• **Debt Management**: Good vs. bad debt, repayment strategies
• **Retirement Planning**: 401(k)s, IRAs

**What topic interests you today?**"""

        return reply

# Initialize the enhanced AI
user_chat_histories = {}
enhanced_ai = EnhancedEducationalFinanceAI()

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_input = data.get('message', '')
        user_id = data.get('user_id', 'default')

        if not user_input:
            return jsonify({'error': 'Message cannot be empty'}), 400

        if user_id not in user_chat_histories:
            user_chat_histories[user_id] = enhanced_ai.system_prompt

        chat_history = user_chat_histories[user_id]

        reply = enhanced_ai.get_educational_reply(user_input, chat_history)

        user_chat_histories[user_id] = chat_history + f"\nUser: {user_input}\nBankBuddy: " + reply

        return jsonify({
            'reply': reply,
            'user_id': user_id
        })

    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'message': 'Tiny Monopoly API is running',
        'version': '3.0',
        'features': ['Enhanced AI', 'Structured Responses', 'Google Search Integration', 'Beginner-focused']
    })

@app.route('/clear_history', methods=['POST'])
def clear_history():
    try:
        data = request.get_json()
        user_id = data.get('user_id', 'default')

        if user_id in user_chat_histories:
            user_chat_histories[user_id] = enhanced_ai.system_prompt

        return jsonify({'message': 'Chat history cleared'})
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/topics', methods=['GET'])
def get_topics():
    """Get all available topics"""
    topics = []
    for module_name, module_content in enhanced_ai.modules.items():
        for topic_name, topic_data in module_content["topics"].items():
            topics.append({
                'module': module_name,
                'topic': topic_name,
                'title': topic_data['title'],
                'description': topic_data['explanation'][:100] + '...'
            })
    
    return jsonify({
        'topics': topics,
        'modules': list(enhanced_ai.modules.keys())
    })

if __name__ == '__main__':
    print("Tiny Monopoly API Server starting...")
    print("Features: Structured responses, Google search integration")
    print("Designed for beginner savers and investors")
    print("Visit http://localhost:5000/health to check server status")
    app.run(host='0.0.0.0', port=5000, debug=True)
