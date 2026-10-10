import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None

def answer_question_with_gemini(question: str) -> str:
    try:
        if not client:
            return "Error: GEMINI_API_KEY not found in .env file."
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=question,
        )
        return response.text.strip()
    except Exception as e:
        return f"Error in QnA: {e}"