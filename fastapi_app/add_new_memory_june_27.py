import os
import sys
import asyncio
import io

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import get_next_memory_id, add_memory
from storage import upload_file

async def main():
    folder_path = "/Users/geekdon/Documents/Journey with Puchki/Photos-3-001 2 Compressed"
    
    memory_id = await get_next_memory_id()
    print(f"Next memory ID: {memory_id}", flush=True)
    
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.webp', '.mp4'))]
    files.sort()
    
    uploaded_filenames = []
    
    for filename in files:
        filepath = os.path.join(folder_path, filename)
        print(f"Uploading {filename}...", flush=True)
        
        with open(filepath, "rb") as f:
            content = f.read()
            
        content_type = "video/mp4" if filename.endswith('.mp4') else "image/webp"
        
        key = f"uploads/{memory_id}/{filename}"
        
        fileobj = io.BytesIO(content)
        url = upload_file(fileobj, key, content_type)
        print(f"Uploaded: {url}", flush=True)
        
        uploaded_filenames.append(filename)
        
    smart_data = {
        "itinerary": [
            {"item": "Met Madhvi and her cute 8-month-old daughter Ishita (Ishi).", "icon": "group", "highlight": False},
            {"item": "Went to Saule restaurant in Noida for drinks (Indigo, Lime Soda, Coconut) and food (Mezze Platter, Dahi Kebab, Lucknow Basket Chaat).", "icon": "restaurant", "highlight": False},
            {"item": "Had lots of gupshup for hours, talking about how we met, future, marriage, kids, and responsibilities.", "icon": "forum", "highlight": True},
            {"item": "Went on a crazy, lovely long drive with romantic Bollywood songs.", "icon": "directions_car", "highlight": True},
            {"item": "Explored the streets of Chanakyapuri.", "icon": "explore", "highlight": False},
            {"item": "Ate at Life Yoga / Elevate restaurant serving out-of-the-world ayurvedic/satvic food.", "icon": "local_dining", "highlight": True},
            {"item": "Explored the store, had more lovely gupshup, took happy and cute pictures.", "icon": "photo_camera", "highlight": False},
            {"item": "Long drive back home, feeling very attached and missing each other. Dropped Shaila home.", "icon": "home", "highlight": True}
        ],
        "entities": {
            "food": ["Indigo", "Lime Soda", "Coconut drink", "Mezze Platter", "Dahi Kebab", "Lucknow Basket Chaat", "Ragi Raj Kachori", "Dal Dhokli Ravioli", "Cold Chocolate with chandan", "Fresh juice"],
            "places": ["Saule restaurant, Noida", "Chanakyapuri", "Life Yoga / Elevate restaurant"]
        },
        "vibe": "Fun, Romantic, and Spiritual 🌸",
        "rating": 5,
        "comment": "Such an amazing day with friends, deep talks, long drives, and out-of-this-world satvic food. Made funny jokes like 'aalsi tattoo'."
    }

    memory_data = {
        "id": memory_id,
        "title": "Double Date with Madhvi, Long Drives & Satvic Food",
        "date": "27 June 2026",
        "description": "We met **Madhvi** and her cute 8-month-old daughter **Ishita (Ishi)**! First, we went to **Saule restaurant** in Noida. We ordered drinks like Indigo, Lime Soda, and Coconut drink, plus food like Mezze Platter, Dahi Kebab, and Lucknow Basket Chaat. The food was average, but we had hours of amazing gupshup! We talked about how we met, the future, marriage, kids, and responsibilities—so much fun talking with **Madhvi**, **Shaiwal**, and **Shaila**. \n\nAfter this, we went on a crazy, lovely long drive playing romantic Bollywood songs. We drove to **Chanakyapuri**, explored the streets, and ultimately went to **Life Yoga** (Elevate restaurant). They serve ayurvedic, satvic food, and it was out of the world! We started with Ragi Raj Kachori, Dal Dhokli Ravioli, Cold Chocolate with chandan, and fresh juice. It was some of the best food and health drinks ever. We explored the store, had more lovely gupshup, and took so many cute, happy photos. I was feeling sleepy from the night before, but the energy was amazing! We talked so much on the long drive back home, feeling so attached and missing each other. Dropped Shaila back home. I also said funny things like 'aalsi tattoo' haha!",
        "photos": uploaded_filenames,
        "type": "Date",
        "location": "Saule, Noida & Life Yoga, Chanakyapuri",
        "rating": 5,
        "comment": "Amazing day with deep talks, long drives, and out-of-this-world satvic food.",
        "smart_data": smart_data,
        "tags": ["good", "food", "place"]
    }
    
    print("Saving to database...", flush=True)
    await add_memory(memory_data)
    print("Memory saved successfully!", flush=True)
    
if __name__ == "__main__":
    asyncio.run(main())
