import asyncio
import os
import sys

# Add current dir to path to import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import get_memory_by_id, update_memory

async def main():
    memory_id = 35
    
    memory = await get_memory_by_id(memory_id)
    if not memory:
        print(f"Memory {memory_id} not found!")
        return

    photos = memory.get("photos", [])
    cover_photo = None
    for p in photos:
        if "IMG_1539" in p:
            cover_photo = p
            break
            
    if cover_photo:
        # Move it to the front of the list, which acts as the cover photo usually.
        photos.remove(cover_photo)
        photos.insert(0, cover_photo)
        
        # Alternatively, set an explicit cover field if the schema supports it.
        # We will set both just in case:
        update_data = {
            "photos": photos,
            "cover_image": cover_photo
        }
        
        print(f"Updating memory {memory_id} to set {cover_photo} as cover...")
        await update_memory(memory_id, update_data)
        print("Memory updated successfully!")
    else:
        print("Could not find IMG_1539 in the photos list.")

if __name__ == "__main__":
    asyncio.run(main())
