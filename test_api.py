import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env
load_dotenv()

key = os.getenv("OPENAI_API_KEY", "")

client = OpenAI(
    base_url="https://g0i.ai/v1",
    api_key=key,
)

print("Testing qwen3-coder-80b API call with stream=True...")
try:
    response = client.chat.completions.create(
        model="qwen3-coder-80b",
        messages=[{"role": "user", "content": "Hello!"}],
        stream=True,
    )
    for chunk in response:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")
    print("\n--- Done ---")
except Exception as e:
    print("\nError:")
    print(str(e))
