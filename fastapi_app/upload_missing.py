import os
import sys
import asyncio
import io

# Add current dir to path to import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import get_memory_by_id, update_memory
from media_optimizer import optimize_file_bytes
from storage import upload_file

async def main():
    folder_path = "/Users/geekdon/Documents/Journey with Puchki/Photos-3-001"
    memory_id = 30
    
    # Get memory
    memory = await get_memory_by_id(memory_id)
    if not memory:
        print("Memory not found!")
        return
        
    existing_photos = set(memory.get("photos", []))
    print(f"Existing photos count: {len(existing_photos)}")
    
    # Read files
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.heic', '.jpg', '.jpeg', '.png', '.mp4', '.mov'))]
    files.sort()
    
    new_uploaded = []
    
    for filename in files:
        base, ext = os.path.splitext(filename)
        expected_ext = ".mp4" if ext.lower() in [".mov", ".mp4", ".avi", ".mkv", ".webm"] else ".webp"
        expected_filename = base + expected_ext
        
        if expected_filename in existing_photos:
            continue
            
        print(f"Processing missing file: {filename}...")
        filepath = os.path.join(folder_path, filename)
        
        with open(filepath, "rb") as f:
            content = f.read()
            
        try:
            # Optimize
            opt_bytes, new_filename, content_type = optimize_file_bytes(content, filename)
            
            # Upload
            key = f"uploads/{memory_id}/{new_filename}"
            print(f"Uploading as {key}...")
            
            fileobj = io.BytesIO(opt_bytes)
            url = upload_file(fileobj, key, content_type)
            print(f"Uploaded: {url}")
            
            new_uploaded.append(new_filename)
        except Exception as e:
            print(f"Error processing {filename}: {e}")
        
    if new_uploaded:
        all_photos = memory.get("photos", []) + new_uploaded
        # Ensure sorting if desired, or just append
        all_photos.sort()
        
        await update_memory(memory_id, {"photos": all_photos})
        print(f"Successfully added {len(new_uploaded)} new media files to memory {memory_id}.")
    else:
        print("No new files to upload.")

if __name__ == "__main__":
    asyncio.run(main())
