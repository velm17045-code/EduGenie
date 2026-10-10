import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None


def get_learning_recommendations(topic: str) -> str:
    try:
        if not client:
            return "Error: GEMINI_API_KEY not found in .env file."
        prompt = f"You are an AI tutor. The student wants to learn about: {topic}. Suggest a structured and adaptive learning path including key topics, order of learning, and resources."
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt,
        )
        return response.text.strip()
    except Exception as e:
        return f"Error in Learning Path: {e}"