import os
import re
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None


def clean_json_block(text: str) -> str:
    return re.sub(r"```(?:json)?\n?(.*?)\n?```", r"\1", text, flags=re.DOTALL).strip()


def generate_quiz(text: str) -> list:
    try:
        if not client:
            return []
        prompt = f"""You are a quiz generator.

From the following passage, create 3 multiple-choice questions. Each question should include:
- A "question"
- A list of 4 "options"
- A correct "answer" that must exactly match one of the options.

Format your output as valid JSON, like this:
[
  {{
    "question": "What is ...?",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }}
]

Passage:
{text}"""

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt,
        )
        cleaned_text = clean_json_block(response.text.strip())
        return json.loads(cleaned_text)
    except Exception as e:
        return []