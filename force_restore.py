import argparse
import asyncio
import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from fastapi_app.database import get_db, db
from fastapi_app.storage import get_s3_client, R2_BUCKET_NAME

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

async def restore_from_json(json_path):
    get_db()
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    print(f"Loaded {len(data)} memories from {json_path}")
    
    # The final 3 missing memories not present in the Git static JSON file
    mem_holi = {
        "id": 24, "date": "March 15, 2026", "title": "Puchki Looking Stunning ❤️🔥", 
        "description": "Happy Birthday!", "type": "hot", "photos": get_photos_from_r2(23), "smart_data": {"itinerary": [], "entities": {"food":[], "places":[]}, "vibe":"Romantic ❤️"},
        "visibility_status": "birthday_only", "is_hot": True, "hide_all_photos": False, "hidden_photos": []
    }
    
    # Memory 24 holistic mapping with its specific itinerary requested earlier
    mem_birthday_photos = get_photos_from_r2(24)
    photos_to_remove = ["IMG_0188.jpeg", "IMG_0185.jpeg", "IMG_0208.jpeg", "IMG_0205.jpeg", "IMG_0194.jpeg"]
    mem_birthday_photos = [p for p in mem_24_photos if p not in photos_to_remove]
    
    mem_birthday = {
        "id": 23, "date": "March 04, 2026", "title": "Tears, Tea & Drive on Holi", 
        "description": "Today was one of those days that felt soft, dreamy, and full of love. On the colorful festival of Holi, the city felt unusually calm and peaceful. The roads were almost empty, which made our drives around the city feel so fun and magical.\n\nWe watched one of the most beautiful romantic and emotional movies, Do Deewane Sheher Mein. The second half was so touching that we both ended up crying so much — it was such a lovely, heartfelt movie.\n\nBefore the movie, we also had a delicious sweet potato chaat at PVR, which was such a perfect and healthy little treat.\n\nAfter the movie, we slowed the day down with a dreamy and calming tea moment. We had chamomile and mandarin tea, feeling all cozy and fancy together. Along with that, we enjoyed the most delicious mango salad and the tastiest sticky rice — every bite felt amazing.\n\nLater, we went for a lovely car drive with beautiful songs playing in the background. Because it was Holi, the roads were so empty, which made the drive even more fun and special — just the two of us enjoying the music, the quiet city, and the moment together.\n\nAnd today also marked the beginning of our little weight-loss journey — you even lost 1 kg already! We had so much healthy food and made such a good start.\n\nA day filled with love, tears, music, peaceful Holi drives, healthy food, and beautiful moments together. And of course, our wonderful meal at Burma Burma made it even more memorable.\n\nA truly lovely Holi day with you, Puchki. 💛", 
        "type": "date", "photos": mem_24_photos,
        "days_journey": "March 04, 2026",
        "timeline_note": "A dreamy Holi day filled with an emotional movie, sweet potato chaat, cozy tea, healthy food, and fun drives on beautifully empty roads together. 🚗✨",
        "smart_data": {
            "itinerary": [
                {"icon": "park", "item": "Peaceful Holi Morning \u2013 The city was calm because of Holi, with beautifully empty roads that made everything feel magical and peaceful.", "highlight": False},
                {"icon": "restaurant", "item": "Sweet Start \u2013 We enjoyed a delicious sweet potato chaat at PVR, such a perfect healthy treat.", "highlight": False},
                {"icon": "movie", "item": "Movie Time \u2013 We watched the emotional movie Do Deewane Sheher Mein and the second half made us both cry so much. Such a beautiful and touching movie.", "highlight": True},
                {"icon": "local_cafe", "item": "Cozy Tea Moment \u2013 After the movie, we relaxed with dreamy chamomile and mandarin tea, feeling cozy and fancy together.", "highlight": False},
                {"icon": "restaurant", "item": "Delicious Food \u2013 We had the most amazing mango salad and the tastiest sticky rice \u2014 every bite was so good.", "highlight": False},
                {"icon": "directions_car", "item": "Lovely Drive \u2013 With beautiful songs playing, we drove through the empty Holi roads. It felt so fun, peaceful, and special \u2014 just us enjoying the moment.", "highlight": False},
                {"icon": "favorite", "item": "Healthy Beginning \u2013 Our weight-loss journey began, and you already lost 1 kg! Such a great start.", "highlight": True},
                {"icon": "restaurant", "item": "Perfect Ending \u2013 We ended the day with a wonderful meal at Burma Burma.", "highlight": False}
            ],
            "entities": {"food":["Mango salad", "Tea", "Sticky rice", "Chaat sweet potato"], "places":["Burma Burma", "PVR Director's cut"]},
            "vibe":"Emotional Fun"
        },
        "hide_all_photos": False,
        "hidden_photos": []
    }
    
    data.extend([mem_holi, mem_birthday]) # Append 23, 24
    
    # Create dummy mem_22 stub to let the inner loop override rule populate it dynamically
    data.append({"id": 22})
    
    # Delete all
    db_client = get_db()
    await db_client.memories.delete_many({})
    print("Cleared existing DB")
    
    # Insert explicit
    if data:
        for doc in data:
            if '_id' in doc:
                del doc['_id'] # Just in case it existed
            
            # Override Memory 1 as requested by the user
            if doc.get("id") == 1:
                doc["title_safe"] = "A Special Beginning"
                doc["description"] = "Loved the energy fun positive dancer vibes talented foodie. After a lot of discussions on life and relationships and kundli matching being on point 32/36. Connected on Instagram Shared life past stories and stalked each other posts. After a month, we Talked over phone and it felt connected right through the heart talking about future marriage astrology and that 1 hour of call is still best memory."
                doc["description_safe"] = "We first connected and our stars matched perfectly (32/36!). We shared stories, and after a month, we had our first long phone call. We talked for an hour about the future, astrology, and life—it's still one of my best memories."
                
                if "smart_data" not in doc:
                    doc["smart_data"] = {}
                    
                doc["smart_data"]["vibe"] = "Sparks Flying ✨"
                doc["smart_data"]["itinerary"] = [
                    {"item": "Matched on Hinge and loved the energy, fun, positive dancer vibes.", "icon": "favorite", "highlight": True},
                    {"item": "Kundli matching was on point at 32/36.", "icon": "star", "highlight": False},
                    {"item": "Connected on Instagram and shared life stories.", "icon": "event", "highlight": False},
                    {"item": "Had a 1-hour phone call discussing the future, marriage, and astrology.", "icon": "local_cafe", "highlight": True}
                ]
                if "entities" not in doc["smart_data"]:
                    doc["smart_data"]["entities"] = {}
                doc["smart_data"]["entities"]["places"] = ["Hinge", "Instagram"]
            
            # Override Memory 22 with new description and smart_data
            if doc["id"] == 22:
                doc["title"] = "Dress Shopping, Candle Light and Kulcha"
                doc["date"] = "February 22, 2026"
                doc["template"] = "memory_shopping.html"
                doc["description"] = (
                    "Today feels like one of those golden memories we will always hold close to our hearts. The day we picked our roka dresses wasn’t just about shopping… it was about choosing a future together. Seeing you smile, seeing that sparkle in your eyes — that moment is forever etched in my heart.\n\n"
                    "After that, our little food celebration — the best lassi, that cold coffee, and the sooo delicious kulcha at Kulcha Culture — everything tasted better because I was with you. Even the simplest moments felt magical.\n\n"
                    "And then our trip to Greater Kailash 2… you were glowing with happiness, trying so many dresses, laughing, twirling, being your adorable self. That happiness on your face is my favorite sight in the world.\n\n"
                    "You found that beautiful blue birthday dress that day — and you looked absolutely stunning. The candlelight, the warmth, the peaceful vibe, and finally that healthy and tasty dinner at Music & Mountains… it all felt so blessed, so perfect, so us.\n\n"
                    "That day wasn’t just special — it was a memory of love, gratitude, and togetherness. I’m so thankful that I get to live these moments with you. With you, every ordinary day becomes extraordinary.\n\n"
                    "Forever grateful for us. Forever grateful for you. ❤️✨"
                )
                doc["description_safe"] = "One of the most memorable days for us. We had our first candle light dinner and lot of healthy pasta and pizza. Candle light dinner was just amazing with amazing music and atmosphere at Music and Mountains, Greater Kailash 2."
                doc["smart_data"] = {
                    "vibe": "Fun & Memorable ✨",
                    "entities": {"food": ["sizzler", "kulcha", "lassi", "cold coffee", "Pizza", "Pasta"], "places": ["kulcha culture", "music and mountains"]},
                    "itinerary": [
                        {"item": "A memory-happy day for us — the day we picked and tried our roka dresses, choosing our future together.", "icon": "favorite", "highlight": True},
                        {"item": "The sparkle in your eyes and your smile that day made everything feel magical.", "icon": "star", "highlight": False},
                        {"item": "Celebrating with the best lassi and cold coffee, and that sooo tasty kulcha at Kulcha Culture — food always tastes better with you.", "icon": "local_dining", "highlight": True},
                        {"item": "Our trip to Greater Kailash 2, where you were so happy trying so many dresses — your excitement was the cutest thing ever.", "icon": "shopping_cart", "highlight": False},
                        {"item": "The beautiful blue dress you chose for your birthday — you looked absolutely stunning.", "icon": "face", "highlight": True},
                        {"item": "A blessed candlelight moment filled with warmth, love, and gratitude.", "icon": "wb_incandescent", "highlight": False},
                        {"item": "Ending the day with healthy and tasty food at Music & Mountains — peaceful, perfect, and so us.", "icon": "park", "highlight": True},
                        {"item": "A day full of love, laughter, togetherness, and memories I will cherish forever.", "icon": "favorite", "highlight": False}
                    ]
                }
            
            # Only fetch photos for the brand new memories (22 and 24) since they're not in the JSON
            if doc.get('photos', None) == None and doc.get("id", 0) >= 22:
                raw_photos = get_photos_from_r2(doc["id"])
                doc["photos"] = sorted([p for p in raw_photos if not p.lower().endswith(('.heic', '.ds_store'))])
            
            # Re-inject the video template check across all of them
            if "photos" in doc:
                has_video = any(p.lower().endswith(('.mp4', '.mov', '.webm')) for p in doc["photos"])
                if has_video and doc["id"] != 22:
                    doc["template"] = "memory_movie.html"
                    
        await db_client.memories.insert_many(data)
        
    print(f"Database overwritten explicitly with JSON data. Final count: {len(data)}")

if __name__ == "__main__":
    asyncio.run(restore_from_json("/tmp/original_memories.json"))
