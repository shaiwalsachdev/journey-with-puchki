import os
import sys
import asyncio

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import update_memory, get_memory_by_id
from media_optimizer import optimize_file_bytes
from storage import upload_file

async def main():
    memory_id = 32
    m = await get_memory_by_id(memory_id)
    if not m:
        print("Memory not found")
        return
        
    image_path = "/Users/geekdon/Documents/Journey with Puchki/MV5BNzdkNjAxNWMtNWY3My00NTI1LTg2YWQtOGI3MDA0NzdhMjEyXkEyXkFqcGc@._V1_.jpg"
    filename = os.path.basename(image_path)
    
    with open(image_path, "rb") as f:
        content = f.read()
        
    opt_bytes, new_filename, content_type = optimize_file_bytes(content, filename)
    key = f"uploads/{memory_id}/{new_filename}"
    
    import io
    fileobj = io.BytesIO(opt_bytes)
    url = upload_file(fileobj, key, content_type)
    print(f"Uploaded cover: {url}")
    
    photos = m.get("photos", [])
    photos.insert(0, new_filename)
    
    # We set type to "movie" as usually templates are matched by type
    await update_memory(memory_id, {
        "type": "movie",
        "photos": photos
    })
    print("Memory updated with new type and cover image.")

if __name__ == "__main__":
    asyncio.run(main())
