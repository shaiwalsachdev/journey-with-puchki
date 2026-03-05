# -*- coding: utf-8 -*-
import os
import sys
import asyncio
import json
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from convert_notes_to_json import parse_notes
from fastapi_app.database import get_all_memories, db, get_db
from restore_1 import memory_1
from fastapi_app.storage import get_s3_client, R2_BUCKET_NAME

def extract_smart_data(description, title):
    smart_data = {
        "itinerary": [],
        "entities": {
            "food": [],
            "places": []
        },
        "vibe": "Fun & Memorable" # Default
    }

    # --- Heuristic Extraction Logic ---
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', description)
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence: continue
        
        icon = "event"
        highlight = False
        
        if any(w in sentence.lower() for w in ['movie', 'cinema', 'watch']): 
            icon = "movie"; highlight = True
        elif any(w in sentence.lower() for w in ['eat', 'dinner', 'lunch', 'food', 'sushi', 'pizza', 'pasta']): 
            icon = "restaurant"; highlight = True
        elif any(w in sentence.lower() for w in ['shopping', 'bought', 'mall', 'market']): 
            icon = "shopping_bag"
        elif any(w in sentence.lower() for w in ['walk', 'stroll']): 
            icon = "directions_walk"
        elif any(w in sentence.lower() for w in ['game', 'bowling', 'arcade']): 
            icon = "sports_esports"; highlight = True
        elif any(w in sentence.lower() for w in ['drive', 'car']): 
            icon = "directions_car"
        
        item_text = sentence.replace("We ", "").replace("enjoyed ", "").capitalize()
        smart_data["itinerary"].append({
            "item": item_text,
            "icon": icon,
            "highlight": highlight
        })

    food_keywords = ['sushi', 'pizza', 'pasta', 'burger', 'dimsum', 'bao', 'cheela', 'coffee', 'dessert', 'brownie', 'pastry', 'kebab', 'chaat']
    for word in food_keywords:
        if word in description.lower():
            smart_data["entities"]["food"].append(word.capitalize())
            
    potential_places = re.findall(r'(?<!^)(?<!\.\s)[A-Z][a-z]+(?:\s[A-Z][a-z]+)*', description)
    known_places = ['PVR', 'Starbucks', 'Theos', 'Burma Burma', 'PF Changs', 'Saule', 'One8 Commune', 'Karigari', 'Advant', 'Worldmark', 'DlF', 'Cyber Hub', 'Hichki', 'Eldeco', 'YouMee', 'Miniso', 'Karol Bagh', 'Lajpat Nagar', 'Music and Mountains']
    
    for place in known_places:
        if place.lower() in description.lower():
            if place not in smart_data["entities"]["places"]:
                smart_data["entities"]["places"].append(place)

    if 'romantic' in description.lower() or 'love' in description.lower():
        smart_data["vibe"] = "Romantic ❤️"
    elif 'funny' in description.lower() or 'fun' in description.lower():
        smart_data["vibe"] = "Fun & Crazy 🤪"
    elif 'family' in description.lower():
        smart_data["vibe"] = "Family Time 👨‍👩‍👧‍👦"
    elif 'chill' in description.lower() or 'relax' in description.lower():
        smart_data["vibe"] = "Chill Vibes 😌"
    elif 'food' in description.lower():
        smart_data["vibe"] = "Foodie Heaven 😋"

    return smart_data

def get_photos_from_r2(memory_id):
    s3 = get_s3_client()
    prefix = f"uploads/{memory_id}/"
    try:
        response = s3.list_objects_v2(Bucket=R2_BUCKET_NAME, Prefix=prefix)
        photos = []
        if "Contents" in response:
            for obj in response["Contents"]:
                key = obj["Key"]
                filename = key.split("/")[-1]
                if filename:
                    photos.append(filename)
        return photos
    except Exception as e:
        print(f"Error fetching R2 for {memory_id}: {e}")
        return []

async def restore_db():
    print("Parsing notes...")
    events = parse_notes()
    
    # ID Map based on the user's provided list from the backup HTML:
    # 1. Matched on Hinge (1)
    # 2. Family Meet (2)
    # 3. Family Meeting Karigari (5)
    # 4. Chocolate Date (6)
    # 5. First Shopping (7)
    # 6. First Candle Light (8)
    # 7. First Movie Date (9)
    # 8. Gaming Zone Date (10)
    # 9. Zootopia 2 (11)
    # 10. Art Date & Painting (12)
    # 11. Meeting Sumedha (13)
    # 12. Avatar Fire (14)
    # 13. New Year (15)
    # 14. Family Meeting Roka (16)
    
    # Let's completely remap IDs based on title matches to get exact match with the saved HTML!
    title_to_id = {
        "Matched on Hinge": 1,
        "The Beginning: Connected to Family Meet": 2,
        "Family Meeting at Karigari": 5,
        "Chocolate Date": 6,
        "First Shopping & Quick Hug": 7,
        "First Candle Light Dinner": 8,
        "First Movie Date": 9,
        "Gaming Zone Date": 10,
        "Zootopia 2 & One8 Commune": 11,
        "Art Date & Painting": 12,
        "Meeting Sumedha": 13,
        "Avatar Fire & Ash": 14,
        "New Year & Gurdwara Visit": 15,
        "Family Meeting & Roka Decision": 16,
        "Happy Patel & Saule Date": 17,
        "Asian YouMee & Penguin Gift": 18,
        "Metro & Karol Bagh Shopping": 19,
        "Lajpat Nagar & Theos": 20,
        "Our First Valentine's Day": 21,
        "Dress Shopping, Candle Light and Kulcha": 22,
        "Puchki Looking Stunning ❤️🔥": 23,
        "Tears, Tea & Drive on Holi": 24,
    }
    
    for ev in events:
        if ev["title"] in title_to_id:
            ev["id"] = title_to_id[ev["title"]]
        else:
            # For fuzzy match issues
            for k, v in title_to_id.items():
                if k.lower() in ev["title"].lower() or ev["title"].lower() in k.lower():
                    ev["id"] = v
                    break

    
    # Inject missing UI events manually extracted from the HTML backup
    extra_events = [
        {"id": 17, "date": "January 17, 2026", "title": "Happy Patel & Saule Date", "description": ""},
        {"id": 18, "date": "January 25, 2026", "title": "Asian YouMee & Penguin Gift", "description": ""},
        {"id": 19, "date": "February 1, 2026", "title": "Metro & Karol Bagh Shopping", "description": ""},
        {"id": 20, "date": "February 8, 2026", "title": "Lajpat Nagar & Theos", "description": ""},
        {"id": 21, "date": "February 14, 2026", "title": "Our First Valentine's Day", "description": ""},
        {"id": 22, "date": "February 22, 2026", "title": "Dress Shopping, Candle Light and Kulcha", "description": ""},
        {"id": 23, "date": "March 15, 2026", "title": "Puchki Looking Stunning ❤️🔥", "description": "", "visibility_status": "birthday_only", "is_hot": True},
        {"id": 24, "date": "March 04, 2026", "title": "Tears, Tea & Drive on Holi", "description": ""}
    ]
    
    # avoid duplicates
    existing_ids = {e["id"] for e in events}
    for e in extra_events:
        if e["id"] not in existing_ids:
            events.append(e)
            
    # Sort events by ID
    events.sort(key=lambda x: x["id"])
    
    # Ensure MongoDB Client is created
    get_db()
    
    # Process each event
    for event in events:
        if event["id"] == 1:
            # Overwrite event 1 with the restore_1.py logic entirely
            event.update(memory_1)
            # Re-fetch photos from R2 though just in case
            r2_photos = get_photos_from_r2(1)
            if r2_photos:
                event["photos"] = r2_photos
        elif event["id"] == 24:
            # Fetch photos from R2
            event["photos"] = get_photos_from_r2(event["id"])
            
            # Enrich with smart_data
            event["smart_data"] = extract_smart_data(event.get("description", ""), event["title"])
            
            # Inject memory 24 custom logic
            photos_to_remove = ["IMG_0188.jpeg", "IMG_0185.jpeg", "IMG_0208.jpeg", "IMG_0205.jpeg", "IMG_0194.jpeg"]
            event["photos"] = [p for p in event["photos"] if p not in photos_to_remove]
            
            event["days_journey"] = "March 04, 2026"
            event["smart_data"]["itinerary"] = [
                {"icon": "park", "item": "Peaceful Holi Morning \u2013 The city was calm because of Holi, with beautifully empty roads that made everything feel magical and peaceful.", "highlight": False},
                {"icon": "restaurant", "item": "Sweet Start \u2013 We enjoyed a delicious sweet potato chaat at PVR, such a perfect healthy treat.", "highlight": False},
                {"icon": "movie", "item": "Movie Time \u2013 We watched the emotional movie Do Deewane Sheher Mein and the second half made us both cry so much. Such a beautiful and touching movie.", "highlight": True},
                {"icon": "local_cafe", "item": "Cozy Tea Moment \u2013 After the movie, we relaxed with dreamy chamomile and mandarin tea, feeling cozy and fancy together.", "highlight": False},
                {"icon": "restaurant", "item": "Delicious Food \u2013 We had the most amazing mango salad and the tastiest sticky rice \u2014 every bite was so good.", "highlight": False},
                {"icon": "directions_car", "item": "Lovely Drive \u2013 With beautiful songs playing, we drove through the empty Holi roads. It felt so fun, peaceful, and special \u2014 just us enjoying the moment.", "highlight": False},
                {"icon": "favorite", "item": "Healthy Beginning \u2013 Our weight-loss journey began, and you already lost 1 kg! Such a great start.", "highlight": True},
                {"icon": "restaurant", "item": "Perfect Ending \u2013 We ended the day with a wonderful meal at Burma Burma.", "highlight": False}
            ]
            temp_layout = "memory_movie.html"
            for p in event["photos"]:
                if p.lower().endswith(('.mp4', '.mov', '.webm')):
                    temp_layout = "memory_movie.html"
                    break
            event["template"] = temp_layout
        else:
            # Just normal process
            event["photos"] = get_photos_from_r2(event["id"])
            event["smart_data"] = extract_smart_data(event.get("description", ""), event["title"])
            
            # Set template automatically if a video exists
            event["template"] = "memory.html"
            for p in event["photos"]:
                if p.lower().endswith(('.mp4', '.mov', '.webm')):
                    event["template"] = "memory_movie.html"
                    break

    print(f"Reconstructed {len(events)} memories.")
    
    # Delete and Insert via explicit motor
    from fastapi_app.database import db
    try:
        await db.memories.delete_many({})
        if events:
            # We insert one by one just in case one of them fails on unicode
            for e in events:
                try:
                    await db.memories.insert_one(e)
                except Exception as ex:
                    print(f"Failed to insert memory {e.get('id')}: {ex}")
        print("Restored successfully.")
    except Exception as e:
        print(f"Mongo error: {e}")
        
if __name__ == "__main__":
    asyncio.run(restore_db())
