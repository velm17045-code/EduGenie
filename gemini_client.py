import os
from functools import lru_cache

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")


@lru_cache
def get_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured")

    return genai.Client(api_key=api_key)


def generate(
    prompt: str,
    temperature: float = 0.4,
    max_output_tokens: int = 4000
):
    client = get_client()

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=max_output_tokens
        )
    )

    if not response.text:
        raise RuntimeError("Gemini returned an empty response")

    return response.text.strip()


def generate_json(
    prompt: str,
    temperature: float = 0.3,
    max_output_tokens: int = 4000
):
    client = get_client()

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=max_output_tokens,
            response_mime_type="application/json"
        )
    )

    if not response.text:
        raise RuntimeError("Gemini returned an empty response")

    return response.text.strip()