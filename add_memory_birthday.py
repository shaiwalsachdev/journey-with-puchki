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

SOURCE_DIR = "/Users/geekdon/Documents/Journey with Puchki/Photos-1-001"
SCRATCH_DIR = "/Users/geekdon/Documents/Journey with Puchki/scratch_media_birthday"

def compress_video(input_path, output_path):
    subprocess.run([
        "ffmpeg", "-y", "-i", input_path, 
        "-vcodec", "libx264", "-crf", "28", 
        "-preset", "faster", "-acodec", "aac", 
        output_path
    ], check=True, capture_output=True)
    return True

def convert_heic(input_path, output_path):
    subprocess.run(["sips", "-s", "format", "jpeg", input_path, "--out", output_path], check=True, capture_output=True)
    return True

async def main():
    new_id = await get_next_memory_id()
    photos_array = []
    os.makedirs(SCRATCH_DIR, exist_ok=True)

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
            print(f"Compressing {filename}...")
            if compress_video(filepath, out_path):
                upload_filename = out_filename
                upload_path = out_path
                
        elif filename.lower().endswith('.heic'):
            base = os.path.splitext(filename)[0]
            out_filename = base + ".jpg"
            out_path = os.path.join(SCRATCH_DIR, out_filename)
            print(f"Converting {filename}...")
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
    shutil.rmtree(SCRATCH_DIR)
    shutil.rmtree(SOURCE_DIR)

    # Database Entry
    description = """
    <p class="mb-4">Amazing day, so much love given by everyone! ❤️</p>
    <p class="mb-4">We had a party at <b>Saule, Sector 128, Noida</b>.</p>
    <p class="mb-4">Thank you for the soooo tasty Chocolate bouncy cake... soooo daaaamn tasty! 🎂</p>
    <p class="mb-4">Amazing love and gifts received. So cute dress you were wearing. Amazing family time.</p>
    <p class="mb-4">We had tasty dahi kebab to start with, followed by veg platter, then dal makhani, paneer makhani and paneer tikka masala, roti and amazing cake.</p>
    <p>So many memories, photos we clicked, loved the place and gifts from mokobarra bag, dhoni light, skincare products, handwritten notes, allen solly t-shirts.</p>
    <p class="mt-4">Thank you so so much! ✨</p>
    """.strip()
    
    smart_data = {
        "summary": "Birthday celebration at Saule with family, amazing food, gifts and memories.",
        "vibe": "Joyful & Loved 🥰",
        "entities": {
            "food": ["Chocolate bouncy cake", "Dahi Kebab", "Veg Platter", "Dal Makhani", "Paneer Makhani", "Paneer Tikka Masala", "Roti"],
            "places": ["Saule, Sector 128, Noida"],
            "gifts": ["Mokobarra bag", "Dhoni light", "Skincare products", "Handwritten notes", "Allen Solly t-shirts"]
        },
        "itinerary": [
            {"icon": "restaurant", "item": "Party at Saule, Noida."},
            {"icon": "cake", "item": "Cut the tasty Chocolate bouncy cake."},
            {"icon": "redeem", "item": "Received amazing gifts."}
        ]
    }

    new_memory = {
        "id": new_id,
        "date": "July 20, 2026",
        "title": "My Birthday",
        "description": description,
        "type": "dinner", 
        "template": "memory.html",
        "photos": photos_array,
        "comments": [],
        "hide_all_photos": False,
        "linear_grid": True,
        "smart_data": smart_data,
    }

    await add_memory(new_memory)
    print(f"Memory {new_id} added successfully!")

if __name__ == "__main__":
    asyncio.run(main())
