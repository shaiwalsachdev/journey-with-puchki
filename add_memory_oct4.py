import asyncio
import os
import shutil
import mimetypes
import subprocess
import sys

# Ensure app imports work
sys.path.append("/Users/geekdon/Documents/Journey with Puchki")
from fastapi_app.database import add_memory, get_next_memory_id
from fastapi_app.storage import upload_file

SOURCE_DIR = "/Users/geekdon/Documents/Journey with Puchki/Photos-1-001-Oct4"
SCRATCH_DIR = "/Users/geekdon/Documents/Journey with Puchki/scratch_media_oct4"

def compress_video(input_path, output_path):
    print(f"Compressing video {input_path}...")
    subprocess.run([
        "ffmpeg", "-y", "-i", input_path, 
        "-vcodec", "libx264", "-crf", "28", 
        "-preset", "faster", "-acodec", "aac", 
        output_path
    ], check=True, capture_output=True)
    return True

def convert_heic(input_path, output_path):
    print(f"Converting HEIC {input_path}...")
    subprocess.run(["sips", "-s", "format", "jpeg", input_path, "--out", output_path], check=True, capture_output=True)
    return True

async def main():
    new_id = await get_next_memory_id()
    print(f"Adding memory with ID: {new_id}")
    photos_array = []
    os.makedirs(SCRATCH_DIR, exist_ok=True)

    if not os.path.exists(SOURCE_DIR):
        print(f"Source directory {SOURCE_DIR} not found.")
        return

    files = sorted(os.listdir(SOURCE_DIR))
    for filename in files:
        if filename.startswith("."):
            continue

        filepath = os.path.join(SOURCE_DIR, filename)
        upload_filename = filename
        upload_path = filepath
        
        if filename.lower().endswith('.mov'):
            base = os.path.splitext(filename)[0]
            out_filename = base + ".mp4"
            out_path = os.path.join(SCRATCH_DIR, out_filename)
            if compress_video(filepath, out_path):
                upload_filename = out_filename
                upload_path = out_path
                
        elif filename.lower().endswith('.heic'):
            base = os.path.splitext(filename)[0]
            out_filename = base + ".jpg"
            out_path = os.path.join(SCRATCH_DIR, out_filename)
            if convert_heic(filepath, out_path):
                upload_filename = out_filename
                upload_path = out_path

        content_type, _ = mimetypes.guess_type(upload_filename)
        key = f"uploads/{new_id}/{upload_filename}"
        
        print(f"Uploading {upload_filename} to R2 ({key})...")
        with open(upload_path, "rb") as f:
            upload_file(f, key, content_type or "application/octet-stream")
            
        photos_array.append(upload_filename)

    # Cleanup
    if os.path.exists(SCRATCH_DIR):
        shutil.rmtree(SCRATCH_DIR)
    if os.path.exists(SOURCE_DIR):
        shutil.rmtree(SOURCE_DIR)

    # Database Entry
    description = """
    <p class="mb-4">Such a wonderful, spontaneous random date night! We met up at <b>Pacific Mall</b> and had the absolute best time together—and you looked so unbelievably pretty! ✨</p>
    <p class="mb-4">We headed over to <b>Pizza Express</b> for some incredible food. We ordered the mouthwatering <b>Pesto Pannuzzo</b> sandwich and the amazing, crispy thin-crust <b>Leggera Pizza</b>. Everything tasted so delicious!</p>
    <p class="mb-4">After filling our tummies, we had the most fun drive back home, singing along, laughing, and enjoying every single moment.</p>
    <p>Just an amazing date with my favorite person in the world. ❤️</p>
    """.strip()
    
    smart_data = {
        "summary": "A delightful random date at Pacific Mall having delicious Leggera Pizza and Pesto Pannuzzo at Pizza Express, followed by a fun drive back home.",
        "vibe": "Romantic & Fun ✨",
        "entities": {
            "food": [
                "Pesto Pannuzzo",
                "Leggera Pizza",
                "Thin Crust Pizza"
            ],
            "places": [
                "Pacific Mall",
                "Pizza Express"
            ]
        },
        "itinerary": [
            {
                "icon": "favorite",
                "item": "Met up for a spontaneous random date at Pacific Mall."
            },
            {
                "icon": "local_pizza",
                "item": "Ate delicious Pesto Pannuzzo and crispy Leggera Pizza at Pizza Express."
            },
            {
                "icon": "directions_car",
                "item": "Had a super fun, cozy drive back home together."
            }
        ]
    }

    new_memory = {
        "id": new_id,
        "date": "Oct 4, 2026",
        "title": "Random Date at Pizza Express",
        "description": description,
        "type": "date", 
        "template": "memory.html",
        "photos": photos_array,
        "comments": [],
        "hide_all_photos": False,
        "linear_grid": True,
        "smart_data": smart_data,
    }

    await add_memory(new_memory)
    print(f"Memory {new_id} added successfully with {len(photos_array)} photos!")

if __name__ == "__main__":
    asyncio.run(main())
