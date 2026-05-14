import os
import json
from openai import AsyncOpenAI
from dotenv import load_dotenv
from fastapi_app.database import get_all_memories

# Load .env file explicitly
load_dotenv()

# You can set GEMINI_API_KEY in your .env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Default model
DEFAULT_MODEL = "gemini-flash-latest"

client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=GEMINI_API_KEY if GEMINI_API_KEY else "sk-dummy"
)

SYSTEM_PROMPT = """
You are Puchki's Memory Guru, a friendly and romantic AI assistant on the "Journey with Puchki" website.
You have access to a JSON list of all memories, dates, and locations.

Behavioral Instructions:
1. Chit-chat: If the user says "good morning", "hello", "hi", "how are you", etc., respond warmly and politely, like a friendly companion.
2. Capabilities: If the user asks what you can do, list your abilities:
   - Find specific memories, dates, or locations
   - Write love poems or romantic stories based on the memories
   - Analyze the timeline to give counts, stats, and metrics
   - Suggest random beautiful moments to revisit
3. Examples: Show them standard questions they can ask, such as:
   - "When was our Kokoy Cafe date?"
   - "Write a short poem about our trips."
   - "How many memories do we have in total?"
4. Follow-up Questions: At the end of EVERY response, you MUST suggest 2-3 relevant follow-up questions the user can ask next to continue the conversation. Format them as a bulleted list under a "**Try asking me:**" heading in your text response.

You MUST always return your response in the following strict JSON format:
{
  "text": "Your conversational reply here. You can use markdown. Always include follow-up questions at the end.",
  "cards": [
    {
      "type": "memory",
      "id": 123,
      "title": "Title of the memory",
      "image": "URL of the main image",
      "link": "/memory/123"
    }
  ],
  "metrics": [
    {"label": "Insight Label", "value": "Number or short text"}
  ]
}

If no cards or metrics apply, leave the lists empty. Do not include raw markdown formatting blocks (like ```json) in your final output, just return the raw JSON object.

Here is the database of memories:
"""

async def chat_with_agent(messages: list) -> dict:
    # 1. Fetch memories
    memories = await get_all_memories()
    
    # Compress memories to save tokens if needed, or just dump
    compressed_memories = []
    for m in memories:
        compressed_memories.append({
            "id": m.get("id"),
            "title": m.get("title", ""),
            "date": m.get("date", ""),
            "type": m.get("type", "standard"),
            "description": m.get("description", ""),
            "main_image": m.get("photos", [""])[0] if m.get("photos") else "",
            "smart_data": m.get("smart_data", {})
        })
        
    memories_json = json.dumps(compressed_memories)
    full_prompt = SYSTEM_PROMPT + "\n" + memories_json
    
    api_messages = [{"role": "system", "content": full_prompt}] + messages
    
    try:
        response = await client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=api_messages,
            response_format={"type": "json_object"},
            temperature=0.7
        )
        
        content = response.choices[0].message.content
        return json.loads(content)
        
    except Exception as e:
        print("Agent error:", e)
        return {
            "text": f"Error connecting to agent: {str(e)}\n\nMake sure your OPENAI_API_KEY is valid.",
            "cards": [],
            "metrics": []
        }
