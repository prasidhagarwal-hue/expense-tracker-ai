import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-3.5-flash")

def get_advice(summary):
    prompt = f"""
You are a personal finance advisor for an Indian student.
Analyze these monthly expenses and give exactly 3 specific 
money saving tips in simple words:

{summary}

Keep advice practical and relevant for a student in India.
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Could not get AI advice: {e}"