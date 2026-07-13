import asyncio
import os
import mimetypes
import subprocess
import sys

sys.path.append("/Users/geekdon/Documents/Journey with Puchki")
from fastapi_app.database import get_memory_by_id, update_memory
from fastapi_app.storage import upload_file

async def main():
    memory_id = 41
    filepath = "/Users/geekdon/Documents/Journey with Puchki/IMG_1976.HEIC"
    filename = "IMG_1976.HEIC"
    base = os.path.splitext(filename)[0]
    out_filename = base + ".jpg"
    out_path = f"/Users/geekdon/Documents/Journey with Puchki/{out_filename}"

    print(f"Converting {filepath} to {out_path}...")
    subprocess.run(["sips", "-s", "format", "jpeg", filepath, "--out", out_path], check=True, capture_output=True)

    print(f"Uploading {out_filename} to uploads/{memory_id}/{out_filename}...")
    content_type, _ = mimetypes.guess_type(out_filename)
    key = f"uploads/{memory_id}/{out_filename}"
    
    with open(out_path, "rb") as f:
        upload_file(f, key, content_type or "image/jpeg")

    print(f"Fetching memory {memory_id}...")
    memory = await get_memory_by_id(memory_id)
    if memory:
        photos = memory.get("photos", [])
        if out_filename not in photos:
            photos.append(out_filename)
            print(f"Updating memory {memory_id} photos...")
            await update_memory(memory_id, {"photos": photos})
            print("Successfully updated memory!")
        else:
            print("Photo already in memory.")
    else:
        print("Memory not found!")
        
    if os.path.exists(out_path):
        os.remove(out_path)

if __name__ == "__main__":
    asyncio.run(main())
