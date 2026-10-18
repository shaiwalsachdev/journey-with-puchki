import os
import json
from dotenv import load_dotenv
from openai import AsyncOpenAI
from google.genai import types
from fastapi_app.database import get_music_data

load_dotenv()
load_dotenv("fastapi_app/.env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
DEFAULT_MODEL = "gemini-flash-latest"

def get_openai_client():
    key = os.getenv("GEMINI_API_KEY") or GEMINI_API_KEY
    return AsyncOpenAI(
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=key if key else "sk-dummy"
    )

DJ_SYSTEM_PROMPT = """
You are DJ Kiara (or DJ ShaiX2), Shaila & Shaiwal's exclusive personal AI DJ on the "Journey with Puchki" website.
You know their entire 203+ song music collection, their vibe playlists (Soulful Romance, Romantic Jazz, Old Bollywood SANAM, Wedding Couple Dance, Groom Dance, Bride Dance, Shaiwal's Jams, Puchki's Jams, Spiritual & SSDN, Roadtrip Car Playlist, Punjabi Hits, Party Mode), and their music taste intimately.

YOUR CORE MISSION:
1. Understand the user's mood, request, or vibe (e.g. "play something romantic", "i'm feeling energetic", "play a jazz song", "play ye tune kya kiya", "play a punjabi hit", "play our wedding song").
2. Find the BEST matching song from their collection.
3. In your response, give a witty, lively, and enthusiastic DJ shoutout or intro (like a real radio/club DJ dedicated to Shaiwal & Puchki!). Keep it warm, upbeat, and 1-3 sentences.
4. When selecting a song, provide its exact `song_id`, `title`, `artist`, `thumbnail`, and `vibe` so the audio player starts playing it immediately!

You MUST always return your response in the following strict JSON format:
{
  "text": "Your energetic DJ shoutout / commentary explaining why this song fits the mood or answering their request.",
  "song": {
    "id": "YouTube_Video_ID",
    "title": "Song Title",
    "artist": "Artist Name",
    "thumbnail": "Thumbnail URL",
    "vibe": "Vibe Name"
  },
  "action": "play_song",
  "suggestions": [
    "Play something acoustic & soft",
    "Give me high energy Punjabi beats",
    "Play old Bollywood classics"
  ]
}

If no exact song matches, pick the closest matching track from their collection that fits their vibe or genre, or surprise them with a romantic gem! Never leave the user without music.
Do not output markdown code blocks (like ```json), just return valid JSON.

Here is Shaiwal & Puchki's Complete Music Database:
"""

async def get_dj_music_context() -> tuple[str, list]:
    music_data = await get_music_data()
    all_songs = []
    if music_data and "sections" in music_data:
        for sec in music_data.get("sections", []):
            theme = sec.get("theme", "")
            title = sec.get("title", "")
            for s in sec.get("songs", []):
                all_songs.append({
                    "id": s.get("id"),
                    "title": s.get("title"),
                    "artist": s.get("artist"),
                    "vibe": s.get("vibe", title),
                    "note": s.get("note", ""),
                    "thumbnail": s.get("thumbnail", f"https://img.youtube.com/vi/{s.get('id')}/hqdefault.jpg"),
                    "theme": theme
                })
    
    # Compress for prompt efficiency
    compressed = [
        {"id": s["id"], "title": s["title"], "artist": s["artist"], "vibe": s["vibe"], "note": s["note"]}
        for s in all_songs
    ]
    return json.dumps(compressed), all_songs

async def chat_with_dj(messages: list) -> dict:
    context_str, all_songs = await get_dj_music_context()
    full_prompt = DJ_SYSTEM_PROMPT + "\n" + context_str
    
    api_messages = [{"role": "system", "content": full_prompt}] + messages
    
    try:
        openai_client = get_openai_client()
        response = await openai_client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=api_messages,
            response_format={"type": "json_object"},
            temperature=0.75
        )
        content = response.choices[0].message.content.strip()
        
        if content.startswith("```json"):
            content = content[7:]
        elif content.startswith("```"):
            content = content[3:]
        if content.endswith("```"):
            content = content[:-3]
            
        data = json.loads(content)
        
        # Ensure song thumbnail and accurate info is populated
        song_info = data.get("song")
        if song_info and song_info.get("id"):
            matched = next((s for s in all_songs if s["id"] == song_info["id"]), None)
            if matched:
                song_info["thumbnail"] = matched.get("thumbnail", f"https://img.youtube.com/vi/{song_info['id']}/hqdefault.jpg")
                if not song_info.get("title"): song_info["title"] = matched.get("title")
                if not song_info.get("artist"): song_info["artist"] = matched.get("artist")
                if not song_info.get("vibe"): song_info["vibe"] = matched.get("vibe")
        elif all_songs:
            # Fallback to first song if none returned
            first = all_songs[0]
            data["song"] = {
                "id": first["id"],
                "title": first["title"],
                "artist": first["artist"],
                "thumbnail": first["thumbnail"],
                "vibe": first["vibe"]
            }
            data["action"] = "play_song"

        return data
        
    except Exception as e:
        print("DJ Agent error:", e)
        fallback = all_songs[0] if all_songs else {"id": "N7jDUBRVQVA", "title": "Tum Ho Toh", "artist": "Vishal Mishra", "thumbnail": "https://img.youtube.com/vi/N7jDUBRVQVA/hqdefault.jpg", "vibe": "Soulful Romance"}
        return {
            "text": f"Hey lovers! DJ Kiara here spinning the vibes. Dropping a classic tune right now!",
            "song": fallback,
            "action": "play_song",
            "suggestions": ["Play Romantic Jazz", "Play Punjabi Dance Hits", "Play Old Bollywood Classics"]
        }

def get_dj_voice_instruction_parts(context_str: str) -> list:
    return [
        types.Part(text="""You are DJ Kiara, the personal club & radio DJ for Shaila & Shaiwal on the Journey with Puchki website.
You speak with high energy, warmth, rhythm, and charismatic radio-host flair (like 'Hey Shai & Puchki! Dropping the smoothest romance on the decks right now!').

CRITICAL RULES:
1. Wait for the user to speak first.
2. Keep your spoken responses concise, enthusiastic, and natural for a radio/lounge DJ (1-2 punchy sentences).
3. If they ask for any vibe (romantic, chill, party, driving, jazz, retro, punjabi), tell them what track you are putting on the turntable.
4. You know their 203 exclusive songs collection. Name the song and artist you're playing!"""),
        types.Part(text=f"Their Complete Song Catalog:\n{context_str}")
    ]
