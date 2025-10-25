import requests
import json

def test_api():
    base_url = "http://localhost:5000"
    
    print("🧪 Testing BankBuddy API...")
    
    # Test 1: Health check
    try:
        response = requests.get(f"{base_url}/health", timeout=5)
        if response.status_code == 200:
            print("✅ Health check passed")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure the API server is running.")
        return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False
    
    # Test 2: Chat endpoint
    try:
        test_message = "Hello, can you help me with savings?"
        response = requests.post(
            f"{base_url}/chat",
            json={"message": test_message, "user_id": "test_user"},
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            print("✅ Chat endpoint working")
            print(f"   User: {test_message}")
            print(f"   Bot: {data.get('reply', 'No reply')}")
        else:
            print(f"❌ Chat endpoint failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Chat test error: {e}")
        return False
    
    print("\n🎉 All tests passed! The API is working correctly.")
    return True

if __name__ == "__main__":
    test_api()
