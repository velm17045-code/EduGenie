import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None


def summarize_text(text: str) -> str:
    try:
        if not client:
            return "Error: GEMINI_API_KEY not found in .env file."
        prompt = f"Summarize the following text in simple language:\n\n{text}"
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt,
        )
        return response.text.strip()
    except Exception as e:
        return f"Error in Summary: {e}"