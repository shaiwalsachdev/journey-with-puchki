import os
import sys
import asyncio

# Add current dir to path to import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import get_next_memory_id, add_memory
from media_optimizer import optimize_file_bytes
from storage import upload_file

async def main():
    folder_path = "/Users/geekdon/Documents/Journey with Puchki/Photos-3-001"
    
    # Get next memory ID
    memory_id = await get_next_memory_id()
    print(f"Next memory ID: {memory_id}")
    
    # Read files
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.heic', '.jpg', '.jpeg', '.png', '.mp4', '.mov'))]
    files.sort()
    
    uploaded_filenames = []
    
    for filename in files:
        filepath = os.path.join(folder_path, filename)
        print(f"Processing {filename}...")
        
        with open(filepath, "rb") as f:
            content = f.read()
            
        # Optimize
        opt_bytes, new_filename, content_type = optimize_file_bytes(content, filename)
        
        # Upload
        key = f"uploads/{memory_id}/{new_filename}"
        print(f"Uploading as {key}...")
        
        # Need to wrap bytes in a file-like object for upload_file
        import io
        fileobj = io.BytesIO(opt_bytes)
        url = upload_file(fileobj, key, content_type)
        print(f"Uploaded: {url}")
        
        uploaded_filenames.append(new_filename)
        
    # Create memory object
    smart_data = {
        "itinerary": [
            {"item": "Met the photographer at Eye of Turtle Photo Studio (Victory Crossroads) to discuss and finalize the pre-wedding shoot.", "icon": "camera_alt", "highlight": True},
            {"item": "Visited Alma Bakery and Cafe at Advant for healthy paneer dish, burgers, and fresh juices.", "icon": "restaurant", "highlight": False},
            {"item": "Gifted beautiful flowers, enjoyed studio photoshoots, and went on a lovely long drive back home with Khattu Shyam Ji's blessings.", "icon": "favorite", "highlight": True}
        ],
        "entities": {
            "food": ["ABC juice", "Watermelon Juice", "Alma's vegetarian paneer dish", "Kidney bean patty burger", "Sugar free cold coffee with whipped cream", "Detox juice", "Prasad"],
            "places": ["Victory Cross Roads Sector 143 Noida", "Eye of Turtle Photo Studio", "Alma Bakery and Cafe", "Advant Sector 142 Noida"]
        },
        "vibe": "Studio Visit & Cafe Date 📸☕",
        "rating": 5,
        "comment": "Finalized the photographer and work was done. Amazing healthy food at Alma cafe, lovely long drive back home, and received Khattu Shyam Ji's charan and prasad. Blessings upon us!"
    }

    memory_data = {
        "id": memory_id,
        "title": "Finalizing Photographer and Alma Cafe Date",
        "date": "30 May 2026",
        "description": "Amazing day today, we met the photographer at Victory Cross Roads Sector 143 Noida, B-502, Eye of Turtle photo studio. Amazing quality of work, from videos to short teasers to cinematic films to photos, story narration, and pre-wedding shoots. Finally finalized the photographer! Went to a new healthy cafe, Alma Bakery and Cafe at Advant Sector 142 Noida. Tried amazing ABC juice, Watermelon Juice, and Alma's vegetarian paneer dish which was so tasty and healthy. Also tried the kidney bean patty burger (not so tasty) with sugar-free cold coffee with whipped cream and detox juice. We talked and enjoyed so much, gave you beautiful flowers, you kept smiling. We took so many photos and videos while in the studio with amazing songs. Long drive back home was so beautiful. Thank you for bringing pretty Khattu Shyam Ji ke charan and prasad, so much blessings upon us.",
        "photos": uploaded_filenames,
        "type": "Date Type",
        "location": "Eye of Turtle Photo Studio, Alma Bakery and Cafe",
        "rating": 5,
        "comment": "Finalized the photographer and work was done. Amazing healthy food at Alma cafe, lovely long drive back home, and received Khattu Shyam Ji's charan and prasad.",
        "smart_data": smart_data
    }
    
    # Insert memory
    print("Saving to database...")
    await add_memory(memory_data)
    print("Memory saved successfully!")

if __name__ == "__main__":
    asyncio.run(main())
