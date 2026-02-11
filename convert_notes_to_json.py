
import os
import re
import json

BASE_DIR = "/Users/geekdon/Documents/Journey with Puchki"
NOTES_FILE = os.path.join(BASE_DIR, "notes.txt")
OUTPUT_FILE = os.path.join(BASE_DIR, "fastapi_app/data/memories.json")

def parse_notes():
    with open(NOTES_FILE, 'r') as f:
        content = f.read()

    date_pattern = r"((?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4})[-:]?(.*)"
    
    events = []
    lines = content.split('\n')
    current_event = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        match = re.match(date_pattern, line)
        if match:
            if current_event:
                events.append(current_event)
            
            date_str = match.group(1).strip()
            title = match.group(2).strip()
            if not title:
                title = "Special Memory"
            
            current_event = {
                "id": len(events) + 1,
                "date": date_str,
                "title": title,
                "description": "",
                "photos_folder": None,
                "type": "dinner", # Default type
                "photos": []
            }
            
            # Simple keyword matching for type
            t_lower = title.lower()
            if "movie" in t_lower:
                current_event["type"] = "movie"
            elif "shopping" in t_lower or "metro" in t_lower:
                current_event["type"] = "shopping"
            elif "art" in t_lower or "paint" in t_lower:
                current_event["type"] = "art"
                
        elif current_event:
            if line.startswith("Photo:"):
                pass # Skip individual photo lines for now, we'll scan folders
            elif line.startswith("Photos:"):
                 folder_match = re.search(r"Photos:\s*(.*)\s+folder", line, re.IGNORECASE)
                 if folder_match:
                     current_event["photos_folder"] = folder_match.group(1).strip()
            else:
                current_event["description"] += line + " "
    
    if current_event:
        events.append(current_event)
        
    return events

def find_photos(events):
    for event in events:
        photos = []
        # Check specific folder
        if event.get("photos_folder"):
            possible_folder = event["photos_folder"]
            # Try exact match first
            folder_path = os.path.join(BASE_DIR, possible_folder)
            
            # If not found, try finding a folder that *contains* this string (fuzzy)
            if not os.path.exists(folder_path):
                 for d in os.listdir(BASE_DIR):
                     if possible_folder.lower() in d.lower() and os.path.isdir(os.path.join(BASE_DIR, d)):
                         folder_path = os.path.join(BASE_DIR, d)
                         break

            if os.path.exists(folder_path):
                 for f in os.listdir(folder_path):
                    if f.lower().endswith(('.png', '.jpg', '.jpeg', '.heic')):
                         photos.append(f)
                 event["source_folder"] = folder_path 
            
        event["photos"] = photos
    return events

def main():
    events = parse_notes()
    events = find_photos(events)
    
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(events, f, indent=4)
    
    print(f"Successfully converted {len(events)} events to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
