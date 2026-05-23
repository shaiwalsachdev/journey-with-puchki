import os
import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

async def test_model(model_name):
    client = AsyncOpenAI(
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=os.getenv("GEMINI_API_KEY", "")
    )
    try:
        response = await client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": "Hello! Reply with 'Model works!'"}],
        )
        print(f"[{model_name}] Success: {response.choices[0].message.content}")
    except Exception as e:
        print(f"[{model_name}] Error: {e}")

async def main():
    await test_model("gemini-2.5-flash")
    await test_model("gemini-3.5-flash")

asyncio.run(main())
