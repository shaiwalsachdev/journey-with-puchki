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
            {"item": "Amazing lunch hosted by family, talking about Punjab, Canada and wedding banquets.", "icon": "restaurant", "highlight": False},
            {"item": "Shopping at Nike and Jack & Jones. Got favourite orange white shoes and comfortable t-shirts.", "icon": "shopping_cart", "highlight": True},
            {"item": "Ended the day at Dosa Coffee cafe with thatte idli, buttermilk and filter coffee.", "icon": "local_cafe", "highlight": False}
        ],
        "entities": {
            "food": ["Paneer sabzi", "rice", "parathi", "raita", "rajma rice", "thatte idli", "buttermilk", "filter coffee"],
            "places": ["Nike", "Jack and Jones", "Dosa Coffee cafe"]
        },
        "vibe": "Family, Food & Shopping 🛍️🍽️",
        "rating": 5,
        "comment": "Best places, finally got my favourite shoes and most comfortable t-shirts! Amazing gupshup."
    }

    memory_data = {
        "id": memory_id,
        "title": "Family Lunch and Shopping",
        "date": "18 May 2026",
        "description": "Amazing lunch hosted by your family, so tasty food so much gupshup, so much talks in PUnjabi amazing day spemt afternoon and so much fun talking about Punjab and Canada and wedding banquets. amzing sooo tassy ty food , Paneer sabzi, rice, parathi , raita, rajma rice were out of the workdl. After that we went to Nike and Jack and Jones best places, finanly got my favioture shoes from there organe white color shoes and jack and jones best t shirts most comftrrabtle t shirts amzing gupshp, ended the day at Dosa Coffee cafe whith thatte idli, buttermilk and filter coffeee.",
        "photos": uploaded_filenames,
        "type": "Family and Shopping",
        "location": "Nike, Jack and Jones, Dosa Coffee cafe",
        "rating": 5,
        "comment": "Amazing gupshup, so much fun talking about Punjab and Canada and wedding banquets. Best places, finanly got my favioture shoes from there organe white color shoes and jack and jones best t shirts most comftrrabtle t shirts.",
        "smart_data": smart_data
    }
    
    # Insert memory
    print("Saving to database...")
    await add_memory(memory_data)
    print("Memory saved successfully!")

if __name__ == "__main__":
    asyncio.run(main())
