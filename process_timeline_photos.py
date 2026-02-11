import json
import os
import shutil
import subprocess

# Configuration
SOURCE_ROOT = "/Users/geekdon/Documents/Journey with Puchki"
DATA_FILE = os.path.join(SOURCE_ROOT, "fastapi_app/data/memories.json")
STATIC_UPLOADS = os.path.join(SOURCE_ROOT, "fastapi_app/static/uploads")

# Typos mapping (Found from list_dir)
FOLDER_MAPPING = {
    "December 7, 2025": "Decemeber 7, 2025",
    "December 13, 2025": "Decemeber 13, 2025",
    "December 20, 2025": "Decemeber 20, 2025",
    "December 28, 2025": "Decemeber 28, 2025",
    "November 22, 2025": "Novemeber 22, 2025"
}

def convert_heic_to_jpg(heic_path, jpg_path):
    try:
        subprocess.run(["sips", "-s", "format", "jpeg", heic_path, "--out", jpg_path], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error converting {heic_path}: {e}")
        return False

def process_memories():
    with open(DATA_FILE, 'r') as f:
        memories = json.load(f)

    if not os.path.exists(STATIC_UPLOADS):
        os.makedirs(STATIC_UPLOADS)

    for memory in memories:
        mem_id = str(memory['id'])
        folder_name = memory.get('photos_folder')
        
        # Correct folder name if it's in our mapping
        if folder_name in FOLDER_MAPPING:
            source_folder_name = FOLDER_MAPPING[folder_name]
        else:
            source_folder_name = folder_name
            
        target_dir = os.path.join(STATIC_UPLOADS, mem_id)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        print(f"Processing Memory {mem_id}: {memory['title']}")
        
        updated_photos = []
        
        # Check if source is a folder
        source_path = os.path.join(SOURCE_ROOT, source_folder_name) if source_folder_name else None
        
        # Special handling for single files mentioned in notes but maybe not in folders
        if mem_id == "1" and os.path.exists(os.path.join(SOURCE_ROOT, "Hinge.jpg")):
             # Copy Hinge.jpg
             src = os.path.join(SOURCE_ROOT, "Hinge.jpg")
             dst = os.path.join(target_dir, "Hinge.jpg")
             shutil.copy2(src, dst)
             updated_photos.append("Hinge.jpg")
             
        elif mem_id == "1" and os.path.exists(os.path.join(SOURCE_ROOT, "Kundli matching.jpeg")):
             # Copy Kundli matching
             src = os.path.join(SOURCE_ROOT, "Kundli matching.jpeg")
             dst = os.path.join(target_dir, "Kundli_matching.jpg") # Rename for safety
             shutil.copy2(src, dst)
             updated_photos.append("Kundli_matching.jpg")

        elif source_path and os.path.isdir(source_path):
            print(f"  Source Directory: {source_path}")
            for filename in os.listdir(source_path):
                if filename.lower() == ".ds_store":
                    continue
                    
                file_path = os.path.join(source_path, filename)
                if not os.path.isfile(file_path):
                    continue

                name, ext = os.path.splitext(filename)
                ext = ext.lower()
                
                new_filename = filename
                target_path = os.path.join(target_dir, filename)

                if ext == '.heic':
                    new_filename = name + ".jpg"
                    target_path = os.path.join(target_dir, new_filename)
                    if not os.path.exists(target_path):
                        print(f"  Converting {filename} to {new_filename}")
                        convert_heic_to_jpg(file_path, target_path)
                    else:
                        print(f"  Skipping {filename} (already exists)")
                elif ext in ['.jpg', '.jpeg', '.png']:
                    if not os.path.exists(target_path):
                        print(f"  Copying {filename}")
                        shutil.copy2(file_path, target_path)
                    else:
                        print(f"  Skipping {filename} (already exists)")
                else:
                    print(f"  Skipping {filename} (unsupported format)")
                    continue
                
                updated_photos.append(new_filename)
        else:
            print(f"  Source not found or not a directory: {source_path}")

        # specific overrides for known missing folders to avoid emptying the array if we manually added them before? 
        # Actually, for this task, we want to popluate FROM reading the disk.
        
        if updated_photos:
            memory['photos'] = sorted(updated_photos) 
            # Sort to keep order consistent, or we simply rely on the FS order which is random.

    with open(DATA_FILE, 'w') as f:
        json.dump(memories, f, indent=4)
    print("Done! memories.json updated.")

if __name__ == "__main__":
    process_memories()
