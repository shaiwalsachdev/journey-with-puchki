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
            {"item": "Explored Vasant Kunj DLF Promenade and DLF Emporio.", "icon": "storefront", "highlight": False},
            {"item": "Watched the movie 'Dhurandhar 2: Revenge' with Sumedha.", "icon": "movie", "highlight": True},
            {"item": "Delicious feast at DHana estd 1986.", "icon": "restaurant", "highlight": False},
            {"item": "Ended the day with amazing mix sauce pasta and a chocolate caramel crunch dessert.", "icon": "cake", "highlight": False}
        ],
        "entities": {
            "food": ["Dahi Kebab", "Palak Seekh Kebab", "Pasta Mix Sauce", "Chocolate Caramel Crunch"],
            "places": ["Vasant Kunj DLF Promenade", "DLF Emporio", "DHana estd 1986"]
        },
        "vibe": "Movie & Foodie Heaven 🎬😋"
    }

    memory_data = {
        "id": memory_id,
        "title": "Movie Date Dhurandhar 2: Revenge",
        "date": "May 3, 2026",
        "description": "It was an amazing movie date where we watched 'Dhurandhar 2: Revenge' with Sumedha. We spent time exploring Vasant Kunj DLF Promenade and DLF Emporio. For food, we had some fantastic dahi kebab and palak seekh kebab at DHana estd 1986, followed by a delicious mix sauce pasta and a chocolate caramel crunch. A perfect blend of entertainment and great food!",
        "photos": uploaded_filenames,
        "type": "standard",
        "location": "Vasant Kunj, DLF Promenade",
        "smart_data": smart_data
    }
    
    # Insert memory
    print("Saving to database...")
    await add_memory(memory_data)
    print("Memory saved successfully!")

if __name__ == "__main__":
    asyncio.run(main())
