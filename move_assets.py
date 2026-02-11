
import json
import os
import shutil

BASE_DIR = "/Users/geekdon/Documents/Journey with Puchki"
JSON_FILE = os.path.join(BASE_DIR, "fastapi_app/data/memories.json")
STATIC_UPLOADS = os.path.join(BASE_DIR, "fastapi_app/static/uploads")
STATIC_FAV = os.path.join(BASE_DIR, "fastapi_app/static/images/favourites")
SOURCE_FAV = os.path.join(BASE_DIR, "Favourites")

def move_assets():
    # 1. Move Favourites
    if not os.path.exists(STATIC_FAV):
        os.makedirs(STATIC_FAV)
    
    if os.path.exists(SOURCE_FAV):
        for f in os.listdir(SOURCE_FAV):
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.heic')):
                shutil.copy2(os.path.join(SOURCE_FAV, f), os.path.join(STATIC_FAV, f))
        print(f"Copied Favourites to {STATIC_FAV}")

    # 2. Move Event Photos
    with open(JSON_FILE, 'r') as f:
        memories = json.load(f)
        
    for m in memories:
        m_id = m['id']
        dest_dir = os.path.join(STATIC_UPLOADS, str(m_id))
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            
        # We need to find where the photos validly exist.
        # The JSON has "source_folder" if we added it in the previous script?
        # Let's check if 'source_folder' is in the json.
        # If not, we have to re-find them or just rely on 'photos' list and hope we can find them in BASE_DIR/photos_folder
        
        source_folder = m.get('source_folder')
        if not source_folder and m.get('photos_folder'):
             # Try to construct it
             possible = os.path.join(BASE_DIR, m['photos_folder'])
             if os.path.exists(possible):
                 source_folder = possible
             else:
                 # Check fuzzy again? Or just list dirs
                 pass
        
        if source_folder and os.path.exists(source_folder):
            for photo in m.get('photos', []):
                src_path = os.path.join(source_folder, photo)
                if os.path.exists(src_path):
                    shutil.copy2(src_path, os.path.join(dest_dir, photo))
            print(f"Copied photos for Event {m_id} to {dest_dir}")
        else:
            print(f"Warning: Could not find source folder for Event {m_id}: {m.get('title')}")

if __name__ == "__main__":
    move_assets()
