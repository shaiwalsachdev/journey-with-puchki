---
name: add-memory
description: Process and upload media files, and insert a beautifully formatted new memory into the MongoDB database.
---

# Add Memory Skill

This skill documents the exact process and script template to use whenever the user asks to add a new memory from a local folder of photos and videos. 

## Workflow Overview

When adding a new memory, follow these steps via a Python script:

1. **Get Next ID**: Fetch the next available memory ID using `get_next_memory_id()` from `fastapi_app.database`.
2. **Process Media**:
   - Iterate through the provided source directory (sorted alphabetically).
   - Convert `.heic` images to `.jpg` using the `sips` command-line tool.
   - Compress `.mov` videos to `.mp4` using `ffmpeg` with `-vcodec libx264 -crf 28 -preset faster`.
   - Save processed files to a temporary `scratch_media` directory.
3. **Upload to R2**:
   - Upload each processed file to the R2 bucket using `upload_file` from `fastapi_app.storage`.
   - The path should be: `uploads/{memory_id}/{filename}`.
4. **Insert into Database**:
   - Construct the memory document with rich HTML in the `description` field (using `<p>`, `<b>`, etc.).
   - Include the `smart_data` object (vibe, entities, itinerary).
   - Insert into MongoDB using `add_memory()`.
5. **Clean up**:
   - Delete the scratch media directory.
   - Delete the original source folder from the user's computer.

## Python Script Template

Use the following template as a basis for your `add_memory.py` script:

```python
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

SOURCE_DIR = "/path/to/user/photos/folder"
SCRATCH_DIR = "/path/to/scratch_media"

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
        
        with open(upload_path, "rb") as f:
            upload_file(f, key, content_type or "application/octet-stream")
            
        photos_array.append(upload_filename)

    # Cleanup
    shutil.rmtree(SCRATCH_DIR)
    shutil.rmtree(SOURCE_DIR)

    # Database Entry
    description = \"\"\"
    <p class="mb-4">First paragraph with <b>bold text</b>.</p>
    <p>Second paragraph.</p>
    \"\"\".strip()
    
    smart_data = {
        "summary": "Short summary of the memory.",
        "vibe": "Romantic ✨",
        "entities": {
            "food": ["Item 1", "Item 2"],
            "places": ["Location 1"]
        },
        "itinerary": [
            {"icon": "favorite", "item": "Did something nice."},
            {"icon": "restaurant", "item": "Ate somewhere nice."}
        ]
    }

    new_memory = {
        "id": new_id,
        "date": "Month DD, YYYY",
        "title": "Title of Memory",
        "description": description,
        "type": "date", # always lowercase! (date, dinner, movie, trip)
        "template": "memory.html",
        "photos": photos_array,
        "comments": [],
        "hide_all_photos": False,
        "linear_grid": True, # Ensure chronological display
        "smart_data": smart_data,
    }

    await add_memory(new_memory)
    print(f"Memory {new_id} added successfully!")

if __name__ == "__main__":
    asyncio.run(main())
```

## Important Formatting Rules

1. **Type Mapping**: Ensure the `type` field is lowercase (e.g., `date`, `dinner`, `movie`, `trip`) so it aligns with `EMOJI_MAP` and categorizes correctly.
2. **Chronological Grid**: Set `linear_grid: True` inside the memory document to override the masonry layout and keep photos perfectly ordered.
3. **HTML Descriptions**: The description should include valid HTML tags (like `<p>`, `<b>`, and spacing classes like `mb-4`) to make it look beautiful.
4. **Cover Photo**: The cover photo is always the first item (`photos_array[0]`). If the user requests a specific cover photo, ensure its name is inserted at index 0 of the array before saving to MongoDB.
