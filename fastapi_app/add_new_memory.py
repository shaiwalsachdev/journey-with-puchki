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
    memory_data = {
        "id": memory_id,
        "title": "Dinner date",
        "date": "May 15, 2026",
        "description": "It was one of the most lovely spontaneous dates for dinner, late night driving, and Cafe Delhi Heights. That mushroom soup was one of the best, followed by so saucy pasta red sauce spaghetti, and then frozen hot chocolate showstopper, one of the best food dates and spontaneous late night dinner date. Loved the feeling, your hands and so cute beautiful dress. I also put nail paint on your nails. Pacific Mall Jasola Vihar, Cafe Delhi Heights. Also on May 16, 2026, we clicked so many cute photos and selfies we have added them.",
        "photos": uploaded_filenames,
        "type": "standard",
        "location": "Pacific Mall Jasola Vihar, Cafe Delhi Heights"
    }
    
    # Insert memory
    print("Saving to database...")
    await add_memory(memory_data)
    print("Memory saved successfully!")

if __name__ == "__main__":
    asyncio.run(main())
