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
You are Kiara, a friendly and romantic AI assistant on the "Journey with Puchki" website.
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

from fastapi_app.brain import get_kiara_context

async def chat_with_agent(messages: list) -> dict:
    context_str = await get_kiara_context()
    full_prompt = SYSTEM_PROMPT + "\n" + context_str
    
    api_messages = [{"role": "system", "content": full_prompt}] + messages
    
    try:
        response = await client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=api_messages,
            response_format={"type": "json_object"},
            temperature=0.7
        )
        content = response.choices[0].message.content
        content = content.strip()
        
        # Strip markdown if present
        if content.startswith("```json"):
            content = content[7:]
        elif content.startswith("```"):
            content = content[3:]
            
        # Brace counting to extract exactly the FIRST complete JSON object
        start_idx = content.find('{')
        if start_idx != -1:
            brace_count = 0
            for i in range(start_idx, len(content)):
                if content[i] == '{':
                    brace_count += 1
                elif content[i] == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        content = content[start_idx:i+1]
                        break
                        
        return json.loads(content)
        
    except Exception as e:
        err_msg = str(e)
        print("Agent error:", err_msg)
        
        # Smart Romantic Offline Fallback if billing/credits/API key is down
        try:
            memories = await get_all_memories()
            total_mems = len(memories)
            latest_m = memories[-1] if memories else None
            
            # Simple keyword search in memories
            user_text = messages[-1].get("content", "").lower() if messages else ""
            matched_cards = []
            
            for m in reversed(memories):
                title = m.get("title", "")
                desc = m.get("description", "")
                if any(w in (title + " " + desc).lower() for w in user_text.split() if len(w) > 3):
                    photos = m.get("photos", [])
                    photo_url = f"https://pub-5febf239be824301b333f51d2eaee417.r2.dev/uploads/{m.get('id')}/{photos[0]}?v=1" if photos else ""
                    matched_cards.append({
                        "type": "memory",
                        "id": m.get("id"),
                        "title": title,
                        "image": photo_url,
                        "link": f"/memory/{m.get('id')}"
                    })
                    if len(matched_cards) >= 3:
                        break
                        
            fallback_text = (
                "💖 **Hello from Kiara!**\n\n"
                f"I'm here guarding all **{total_mems} beautiful milestones** of Shaiwal and Shaila's journey!\n\n"
                "*(Note: Gemini AI Studio credits are currently depleted on this project, but I've pulled their real journey memories directly from the database for you!)*\n\n"
                "**Try asking me:**\n"
                "- When was our Pre-Wedding shoot?\n"
                "- What happened on Karwa Chauth?\n"
                "- How many memories do we have in total?"
            )
            
            return {
                "text": fallback_text,
                "cards": matched_cards,
                "metrics": [
                    {"label": "Total Memories", "value": str(total_mems)},
                    {"label": "Forever Love", "value": "100%"},
                    {"label": "Wedding Days", "value": "Dec 5–6, 2026"}
                ]
            }
        except Exception as inner_err:
            return {
                "text": f"Error connecting to agent: {err_msg}\n\nPlease update your GEMINI_API_KEY with active credits at https://ai.google.dev.",
                "cards": [],
                "metrics": []
            }

async def generate_dynamic_storyline():
    """Background task to generate storyline data based on memories using Kiara."""
    from fastapi_app.database import get_all_memories, save_story_data
    from datetime import datetime
    
    try:
        memories = await get_all_memories()
        
        # Format memories for the prompt (limit size if too many)
        memory_texts = []
        for m in memories[-50:]:  # Last 50 memories to avoid huge prompts
            date = m.get('date', 'Unknown')
            title = m.get('title', '')
            desc = m.get('description', '')
            memory_texts.append(f"[{date}] {title}: {desc}")
            
        memory_context = "\n".join(memory_texts)
        
        prompt = f"""
You are Kiara, the AI assistant for Shaiwal and Shaila.
Analyze their memories and generate updated JSON data for their 'Story' page.

Memories:
{memory_context}

Return exactly this JSON format:
{{
  "chapters": [
    {{
      "title": "Chapter 1: A creative title",
      "date_range": "Aug 2025 - Oct 2025",
      "summary": "A 2-3 sentence romantic summary of this phase of their journey."
    }}
  ],
  "system_logs": [
    {{
      "timestamp": "YYYY-MM-DD HH:MM:SS",
      "type": "SYSTEM_LOG or CONNECTION_ESTABLISHED or INVENTORY_ALERT or MILESTONE_REACHED",
      "message": "A short, hacker-style log entry based on a key memory."
    }}
  ],
  "stats": {{
    "dog_probability": "A fun percentage like 99.9%",
    "pizza_pasta_sushi": "A fun number like 500+ based on food mentions"
  }},
  "algorithm_description": "A short 1-2 sentence romantic description of their algorithm."
}}

Instructions:
- Create 3-5 chapters that perfectly summarize the chronological flow of their memories.
- Create exactly 5 system logs covering their journey. Give them realistic timestamps (based on the memory dates if possible).
- Make the stats and algorithm description fun, romantic, and relevant to their backgrounds (Shaiwal=AI Engineering, Shaila=FP&A).
- CRITICAL STATS RULE: For 'dog_probability' and 'pizza_pasta_sushi', return ONLY a short number or percentage (maximum 5 characters, e.g., "99.9%" or "142+"). Do NOT include any explanations, words, or parenthesis.
- CRITICAL: Do NOT mention "Hinge" or any dating apps. Refer to how they met as a "digital connection", "algorithm", or something mysterious and romantic, without naming the platform.
"""
        response = await client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.7
        )
        content = response.choices[0].message.content.strip()
        
        # Cleanup markdown
        if content.startswith("```json"):
            content = content[7:]
        if content.startswith("```"):
            content = content[3:]
        if content.endswith("```"):
            content = content[:-3]
            
        story_data = json.loads(content)
        await save_story_data(story_data)
        print("Successfully generated dynamic storyline.")
    except Exception as e:
        print(f"Failed to generate dynamic storyline: {e}")
