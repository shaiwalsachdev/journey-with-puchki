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

SOURCE_DIR = "/Users/geekdon/Documents/Journey with Puchki/Photos-1-001-Oct10..."
SCRATCH_DIR = "/Users/geekdon/Documents/Journey with Puchki/scratch_media_oct10"

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
    <p class="mb-4">Our official <b>Pre-Wedding Shoot Day</b>! It was a very long, exciting, and unforgettable day shooting across multiple themes and outfits—from <b>Ethnic</b> to a cozy <b>Picnic</b>, stylish <b>City vibes</b>, and finally fulfilling your dream <b>Proposal</b>! 💍✨</p>
    <p class="mb-4">You looked breathtakingly gorgeous in the saree—so incredibly pretty that I couldn't take my eyes off you. We spent hours on the road with long drives between locations, navigating traffic and facing so many challenges throughout the day, but having you by my side made every single moment special.</p>
    <p class="mb-4">After wrapping up, we headed to <b>Cafe Sandoz</b> for a well-deserved late dinner. Even though the food took a while to arrive after the long day, it was completely worth the wait! We feasted on delicious <b>Paalak Patta Chaat</b>, crispy <b>Dahi ke Sholey</b>, fragrant <b>Rice</b> with rich <b>Paneer Butter Masala</b>, paired with a warm <b>Coffee Latte</b> and refreshing <b>Lemonade</b>.</p>
    <p>To top off the night, you had the warm, heavenly <b>Gulab Jamun</b> that brought the biggest, happiest smile to your face. You truly are my happy place, my Puchki. ❤️</p>
    """.strip()
    
    smart_data = {
        "summary": "An unforgettable pre-wedding shoot day covering Ethnic, Picnic, City, and Proposal themes, followed by a late feast at Cafe Sandoz and your favorite Gulab Jamun.",
        "vibe": "Magical & Romantic 💍✨",
        "entities": {
            "food": [
                "Paalak Patta Chaat",
                "Dahi ke Sholey",
                "Paneer Butter Masala",
                "Rice",
                "Coffee Latte",
                "Lemonade",
                "Gulab Jamun"
            ],
            "places": [
                "Pre-Wedding Shoot Locations",
                "Cafe Sandoz"
            ]
        },
        "itinerary": [
            {
                "icon": "photo_camera",
                "item": "Pre-wedding shoot across multiple outfit themes: Ethnic, Picnic, City, and the dream Proposal."
            },
            {
                "icon": "directions_car",
                "item": "Long driving day navigating traffic between shoot locations."
            },
            {
                "icon": "restaurant",
                "item": "Celebratory late dinner at Cafe Sandoz: Paalak Patta Chaat, Dahi ke Sholey, Paneer Butter Masala, and drinks."
            },
            {
                "icon": "favorite",
                "item": "Ended the magical day with delicious hot Gulab Jamun that made Puchki so happy."
            }
        ]
    }

    new_memory = {
        "id": new_id,
        "date": "Oct 10, 2026",
        "title": "Pre-Wedding Shoot & Dream Proposal",
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
