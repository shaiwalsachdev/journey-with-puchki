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

SOURCE_DIR = "/Users/geekdon/Documents/Journey with Puchki/Photos-2-001"
SCRATCH_DIR = "/Users/geekdon/Documents/Journey with Puchki/scratch_media"

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
        
        print(f"Uploading {upload_filename}...")
        with open(upload_path, "rb") as f:
            upload_file(f, key, content_type or "application/octet-stream")
            
        photos_array.append(upload_filename)

    # Cleanup
    print("Cleaning up directories...")
    if os.path.exists(SCRATCH_DIR):
        shutil.rmtree(SCRATCH_DIR)
    if os.path.exists(SOURCE_DIR):
        shutil.rmtree(SOURCE_DIR)

    # Database Entry
    description = """
    <p class="mb-4">It was an amazing day! You helped so much picking out some <b>great clothes from Allen Solly</b> and <b>shoes from US Polo and Lifestyle</b>.</p>
    <p class="mb-4">We had an absolutely amazing ice cream date at <b>Frozen Fun</b>—the mango yogurt ice cream was so good!</p>
    <p>The long drive back home got a little rough. We had to wait in a long line for South Indian food, which left you hungry and angry. We ended up leaving and just driving back home, but it was still a memorable shopping date overall.</p>
    """.strip()
    
    smart_data = {
        "summary": "Shopping at Allen Solly, US Polo, and Lifestyle, followed by mango yogurt ice cream at Frozen Fun. Ended with a long drive home without South Indian food.",
        "vibe": "Productive, sweet but hangry at the end 😅",
        "entities": {
            "food": ["Mango yogurt ice cream at Frozen Fun", "South Indian food (missed)"],
            "places": ["Allen Solly", "US Polo", "Lifestyle", "Frozen Fun"]
        },
        "itinerary": [
            {"icon": "shopping_bag", "item": "Shopping for clothes and shoes"},
            {"icon": "icecream", "item": "Mango yogurt ice cream at Frozen Fun"},
            {"icon": "directions_car", "item": "Long drive back home"},
            {"icon": "restaurant", "item": "Wait for South Indian food"}
        ]
    }

    new_memory = {
        "id": new_id,
        "date": "July 12, 2026",
        "title": "Shopping Date",
        "description": description,
        "type": "date", # always lowercase! (date, dinner, movie, trip)
        "template": "memory.html",
        "photos": photos_array,
        "comments": [],
        "hide_all_photos": False,
        "linear_grid": True, # Ensure chronological display
        "smart_data": smart_data,
    }

    print("Adding to database...")
    await add_memory(new_memory)
    print(f"Memory {new_id} added successfully!")

if __name__ == "__main__":
    asyncio.run(main())
