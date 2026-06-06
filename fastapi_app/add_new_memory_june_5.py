import os
import sys
import asyncio
import shutil

# Add current dir to path to import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import get_next_memory_id, add_memory
from media_optimizer import optimize_file_bytes
from storage import upload_file

async def main():
    folder_path = "/Users/geekdon/Documents/Journey with Puchki/Photos-3-001 (1)"
    
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
            {"item": "Started dinner with Mushroom Galauti Kebab and Lime Soda that were quite bland and not good.", "icon": "restaurant", "highlight": False},
            {"item": "Moved to Cafe Delhi Heights, had Fajitas Veg (full of paneer and veggies), Railway Cutlets, and Tiramisu pastry, which unfortunately didn't taste good either.", "icon": "restaurant", "highlight": False},
            {"item": "Tried to make up for the bad food and a busy workday, dropping you home late around 11:45 PM.", "icon": "directions_car", "highlight": True}
        ],
        "entities": {
            "food": ["Mushroom Galauti Kebab", "Lime Soda", "Fajitas Veg", "Paneer", "Tortilla wraps", "Railway Cutlets", "Tiramisu pastry"],
            "places": ["Cafe Delhi Heights"]
        },
        "vibe": "Disappointing Food but Trying Hard Date 🍽️😔",
        "rating": 2,
        "comment": "Food was a huge disappointment tonight but she looked absolutely beautiful and hot in her black dress."
    }

    memory_data = {
        "id": memory_id,
        "title": "Disappointing Dinner Date but Beautiful You",
        "date": "5 June 2026",
        "description": "It was an exciting Friday date night, but the food was a huge letdown. The Mushroom Galauti Kebab was so bland with no salt, and the lime soda was very bad. We moved to Cafe Delhi Heights and ordered Veg Fajitas (full of paneer, veggies, and tortilla wraps), Railway Cutlets, and Tiramisu pastry, but all of them tasted really bad. It switched our moods off, especially after I was so busy with work that day and disappointed you. Still, I kept trying to make you happy. You were looking so beautiful and hot in your black dress! Dropped you late night around 11:45 PM.",
        "photos": uploaded_filenames,
        "type": "Dinner",
        "location": "Cafe Delhi Heights",
        "rating": 2,
        "comment": "Worst food dinner, everything tasted bad. Mood was off, but she looked stunning in black dress.",
        "smart_data": smart_data
    }
    
    # Insert memory
    print("Saving to database...")
    await add_memory(memory_data)
    print("Memory saved successfully!")
    
    # Delete folder
    print("Deleting original media folder...")
    shutil.rmtree(folder_path)
    print("Folder deleted.")

if __name__ == "__main__":
    asyncio.run(main())
