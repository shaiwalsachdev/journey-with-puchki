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

SOURCE_DIR = "/Users/geekdon/Documents/Journey with Puchki/Photos-1-001-Oct14"
SCRATCH_DIR = "/Users/geekdon/Documents/Journey with Puchki/scratch_media_oct14"

def compress_video(input_path, output_path):
    print(f"Compressing video {input_path}...")
    subprocess.run([
        "ffmpeg", "-y", "-i", input_path, 
        "-vcodec", "libx264", "-crf", "28", 
        "-preset", "faster", "-pix_fmt", "yuv420p",
        "-acodec", "aac", 
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
    <p class="mb-4">Another spontaneous, beautiful random date night with my favorite person! You were wearing such a stunning, gorgeous outfit that day—absolutely <b>shining in black</b>, a glowing beauty, my cutest <i>Bebo</i>! ✨🖤</p>
    <p class="mb-4">We went to <b>Pizza Express</b> and enjoyed another fantastic feast. We had their amazing fresh, crispy pizza, paired with soothing, warm <b>Chamomile Tea</b> for my tea lover. Our inner foodies were in full swing—we just couldn't stop eating and relishing every single bite!</p>
    <p class="mb-4">As the wedding date draws closer and closer, every moment together feels even more precious. Heading back home, we were already missing each other and counting down the days.</p>
    <p>Endless love, delicious food, and the most beautiful girl in the world. ❤️🍕</p>
    """.strip()
    
    smart_data = {
        "summary": "A spontaneous date night at Pizza Express with my glowing Bebo shining in black, savoring amazing pizza and chamomile tea as we count down to our wedding.",
        "vibe": "Romantic & Glowing ✨🖤",
        "entities": {
            "food": [
                "Pizza",
                "Chamomile Tea"
            ],
            "places": [
                "Pizza Express"
            ]
        },
        "itinerary": [
            {
                "icon": "favorite",
                "item": "Spontaneous date night with my Bebo looking stunning and shining in black."
            },
            {
                "icon": "local_pizza",
                "item": "Feasted on delicious pizza at Pizza Express."
            },
            {
                "icon": "emoji_food_beverage",
                "item": "Enjoyed soothing warm Chamomile Tea together."
            },
            {
                "icon": "directions_car",
                "item": "Drove home missing each other as our wedding day gets closer."
            }
        ]
    }

    new_memory = {
        "id": new_id,
        "date": "Oct 14, 2026",
        "title": "Shining in Black at Pizza Express",
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
    print(f"Memory {new_id} added successfully with {len(photos_array)} photos and videos!")

if __name__ == "__main__":
    asyncio.run(main())
