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
SCRATCH_DIR = "/Users/geekdon/Documents/Journey with Puchki/scratch_media_oct23"

def convert_and_compress_to_webp(input_path, output_path):
    temp_jpg = output_path + ".temp.jpg"
    # Convert HEIC to JPEG
    subprocess.run(["sips", "-s", "format", "jpeg", input_path, "--out", temp_jpg], check=True, capture_output=True)
    # Compress JPEG to WebP (quality 82, perfectly crisp and lightweight)
    subprocess.run(["cwebp", "-q", "82", temp_jpg, "-o", output_path], check=True, capture_output=True)
    if os.path.exists(temp_jpg):
        os.remove(temp_jpg)
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
        base = os.path.splitext(filename)[0]
        out_filename = base + ".webp"
        out_path = os.path.join(SCRATCH_DIR, out_filename)

        print(f"Processing & compressing {filename} -> {out_filename}...")
        convert_and_compress_to_webp(filepath, out_path)

        key = f"uploads/{new_id}/{out_filename}"
        print(f"Uploading {out_filename} to Cloudflare R2 ({key})...")
        with open(out_path, "rb") as f:
            upload_file(f, key, "image/webp")
            
        photos_array.append(out_filename)

    # Cleanup
    if os.path.exists(SCRATCH_DIR):
        shutil.rmtree(SCRATCH_DIR)
    if os.path.exists(SOURCE_DIR):
        shutil.rmtree(SOURCE_DIR)

    description = """
    <p class="mb-4">Such an amazing, cozy date after a productive day of work from home! Sitting together in the cage seating at <b>Pizza Express</b>, enjoying quiet conversations and the best food.</p>
    <p class="mb-4">We indulged in a spread of comfort favorites: rich and comforting <b>Mushroom Soup</b>, a fresh and vibrant <b>Paneer Protein Salad</b>, and of course our beloved, heavenly <b>Pesto Pasta</b>.</p>
    <p class="mb-4">Between the warm food, cozy ambiance, and sweet smiles across the table, every little second was pure comfort and romance.</p>
    <p>Another delicious chapter with my favorite person in the world. ❤️</p>
    """.strip()
    
    smart_data = {
        "summary": "Cozy work-from-home evening date at Pizza Express enjoying Pesto Pasta, comforting Mushroom Soup, and fresh Paneer Protein Salad in the cage seating.",
        "vibe": "Cozy & Delicious ✨",
        "entities": {
            "food": [
                "Pesto Pasta",
                "Mushroom Soup",
                "Paneer Protein Salad"
            ],
            "places": [
                "Pizza Express"
            ]
        },
        "itinerary": [
            {
                "icon": "laptop_mac",
                "item": "Cozy day working from home and winding down together."
            },
            {
                "icon": "restaurant",
                "item": "Sat in the cozy cage seating at Pizza Express."
            },
            {
                "icon": "soup_kitchen",
                "item": "Savoring hot Mushroom Soup, Paneer Protein Salad, and rich Pesto Pasta."
            }
        ]
    }

    new_memory = {
        "id": new_id,
        "date": "Oct 23, 2026",
        "title": "Cozy Date & Pesto Pasta at Pizza Express",
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
