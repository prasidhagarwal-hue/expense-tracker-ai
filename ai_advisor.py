import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-3.5-flash")

def chat_with_advisor(expense_summary=None):
    
    chat = model.start_chat()
    
    
    system_context = f"""
You are a personal finance advisor for an Indian student. 
Be helpful, practical, and keep advice relevant to students in India.
Give short, clear responses.
{f"Here is the user's expense summary: {expense_summary}" if expense_summary else ""}
"""
    # send context first
    chat.send_message(system_context)
    
    print("\n AI Finance Advisor ready! Type 'quit' to exit.")
    print("=" * 45)
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == "quit":
            print("Returning to main menu...")
            break
            
        if not user_input:
            continue
            
        try:
            response = chat.send_message(user_input)
            print(f"\n AI: {response.text}")
        except Exception as e:
            print(f" Error: {e}")