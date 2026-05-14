import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=api_key
)

for model_name in ["gemini-1.5-flash", "gemini-1.5-flash-latest", "gemini-flash-latest", "gemini-1.5-flash-001"]:
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": "Hi"}],
            max_tokens=10
        )
        print(f"SUCCESS with {model_name}")
        break
    except Exception as e:
        print(f"FAILED with {model_name}: {e}")
