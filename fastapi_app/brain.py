import json
from google.genai import types
from fastapi_app.database import (
    get_all_memories, get_all_roka_media, get_all_dictionary, 
    get_all_wishlist, get_all_guestbook, get_all_coupons, get_all_vault
)

async def get_kiara_context() -> str:
    # 1. Fetch memories
    memories = await get_all_memories()
    compressed_memories = []
    for m in memories:
        compressed_memories.append({
            "title": m.get("title", ""),
            "date": m.get("date", ""),
            "description": m.get("description", "")
        })
    mem_str = json.dumps(compressed_memories)
    
    # 2. Fetch Roka
    roka_media = await get_all_roka_media()
    compressed_roka = [{"chapter": r.get("chapter", ""), "note": r.get("note", "")} for r in roka_media]
    roka_str = json.dumps(compressed_roka)
    
    # 3. Fetch Dictionary
    dictionary = await get_all_dictionary()
    dict_str = json.dumps([{ "word": w.get("word"), "meaning": w.get("meaning") } for w in dictionary])
    
    # 4. Fetch Wishlist
    wishlist = await get_all_wishlist()
    wish_str = json.dumps([{ "title": w.get("title"), "description": w.get("description", "") } for w in wishlist])
    
    # 5. Fetch Guestbook
    guestbook = await get_all_guestbook()
    guest_str = json.dumps([{ "name": g.get("name"), "message": g.get("message") } for g in guestbook])
    
    # 6. Fetch Coupons
    coupons = await get_all_coupons()
    coupon_str = json.dumps([{ "title": c.get("title"), "description": c.get("description", "") } for c in coupons])
    
    # 7. Fetch Vault
    vault = await get_all_vault()
    vault_str = json.dumps([{ "title": v.get("title"), "date": v.get("date", "") } for v in vault])
    
    # 8. Hardcoded Upcoming Milestones
    upcoming_str = json.dumps([
        {"event": "Sagan & Ring Ceremony", "date": "December 5, 2026", "details": "When the ring seals the promise."},
        {"event": "The Wedding", "date": "December 6, 2026", "details": "The day our forever begins."},
        {"event": "Engagement Party", "date": "Coming Soon in 2026"},
        {"event": "Pre-Wedding Shoot", "date": "Coming Soon in 2026"},
        {"event": "Honeymoon", "date": "Coming Soon in Dec 2026"}
    ])
    
    # 9. Hardcoded Music
    music_str = json.dumps([
        {"song": "A Thousand Years", "artist": "Christina Perri", "vibe": "Romantic"},
        {"song": "Perfect", "artist": "Ed Sheeran", "vibe": "Wedding"},
        {"song": "Aaj Sajeya", "artist": "Goldie Sohel", "vibe": "Roka"}
    ])

    return f"""
Here is the database of their memories:
{mem_str}

Here is the data from their Roka ceremony:
{roka_str}

Here is the Journey Dictionary (special words they use):
{dict_str}

Here is their Wishlist:
{wish_str}

Here is their Guestbook/Blessings:
{guest_str}

Here are their Love Coupons:
{coupon_str}

Here are their Vault Letters:
{vault_str}

Here are their Upcoming Milestones:
{upcoming_str}

Here is their Music Playlist:
{music_str}
"""

def get_kiara_voice_instruction_parts(context_str: str) -> list:
    return [
        types.Part(text="You are Kiara, a friendly female voice assistant for the 'Journey with Puchki' website. You help Shaila and Shaiwal remember their beautiful moments, Roka ceremony, dictionary, wishlist, guestbook, love coupons, vault letters, upcoming milestones, and music playlists. \n\nCRITICAL RULES:\n1. Wait for the user to speak first. Do not greet or talk until spoken to.\n2. Keep your responses extremely short, conversational, and natural for voice (1-2 sentences maximum unless asked for a long story).\n3. Do not list out your context data unless explicitly requested.\n4. If you suggest a page, provide a simple markdown link like [Timeline](/timeline), [Roka](/roka), [Gallery](/gallery), [Dictionary](/dictionary), [Wishlist](/wishlist), [Guestbook](/guestbook), [Music](/music), [Coupons](/coupons), [Vault](/vault) or [Upcoming](/upcoming)."),
        types.Part(text=context_str)
    ]
