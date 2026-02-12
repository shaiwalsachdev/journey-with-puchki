import json
import re

# Load existing memories
with open('fastapi_app/data/memories.json', 'r') as f:
    memories = json.load(f)

def extract_smart_data(description, title):
    smart_data = {
        "itinerary": [],
        "entities": {
            "food": [],
            "places": []
        },
        "vibe": "Fun & Memorable" # Default
    }

    # --- Heuristic Extraction Logic ---
    
    # 1. Activities / Itinerary (based on keywords)
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', description)
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence: continue
        
        icon = "event"
        highlight = False
        
        if any(w in sentence.lower() for w in ['movie', 'cinema', 'watch']): 
            icon = "movie"; highlight = True
        elif any(w in sentence.lower() for w in ['eat', 'dinner', 'lunch', 'food', 'sushi', 'pizza', 'pasta']): 
            icon = "restaurant"; highlight = True
        elif any(w in sentence.lower() for w in ['shopping', 'bought', 'mall', 'market']): 
            icon = "shopping_bag"
        elif any(w in sentence.lower() for w in ['walk', 'stroll']): 
            icon = "directions_walk"
        elif any(w in sentence.lower() for w in ['game', 'bowling', 'arcade']): 
            icon = "sports_esports"; highlight = True
        elif any(w in sentence.lower() for w in ['drive', 'car']): 
            icon = "directions_car"
        
        # Simple cleanup to make it a bullet point
        item_text = sentence.replace("We ", "").replace("enjoyed ", "").capitalize()
        # Truncation removed to show full content
        # if len(item_text) > 60: item_text = item_text[:57] + "..."
        
        smart_data["itinerary"].append({
            "item": item_text,
            "icon": icon,
            "highlight": highlight
        })

    # 2. Food Entities
    food_keywords = ['sushi', 'pizza', 'pasta', 'burger', 'dimsum', 'bao', 'cheela', 'coffee', 'dessert', 'brownie', 'pastry', 'kebab', 'chaat']
    for word in food_keywords:
        if word in description.lower():
            smart_data["entities"]["food"].append(word.capitalize())
            
    # 3. Places Entities (Capitalized words that look like proper nouns, excluding start of sentence)
    # This is a very rough heuristic
    potential_places = re.findall(r'(?<!^)(?<!\.\s)[A-Z][a-z]+(?:\s[A-Z][a-z]+)*', description)
    known_places = ['PVR', 'Starbucks', 'Theos', 'Burma Burma', 'PF Changs', 'Saule', 'One8 Commune', 'Karigari', 'Advant', 'Worldmark', 'DlF', 'Cyber Hub', 'Hichki', 'Eldeco', 'YouMee', 'Miniso', 'Karol Bagh', 'Lajpat Nagar', 'Music and Mountains']
    
    for place in known_places:
        if place.lower() in description.lower():
            if place not in smart_data["entities"]["places"]:
                smart_data["entities"]["places"].append(place)

    # 4. Vibe Analysis
    if 'romantic' in description.lower() or 'love' in description.lower():
        smart_data["vibe"] = "Romantic ❤️"
    elif 'funny' in description.lower() or 'fun' in description.lower():
        smart_data["vibe"] = "Fun & Crazy 🤪"
    elif 'family' in description.lower():
        smart_data["vibe"] = "Family Time 👨‍👩‍👧‍👦"
    elif 'chill' in description.lower() or 'relax' in description.lower():
        smart_data["vibe"] = "Chill Vibes 😌"
    elif 'food' in description.lower():
        smart_data["vibe"] = "Foodie Heaven 😋"

    return smart_data

# Process all memories
for memory in memories:
    # Only update if smart_data doesn't exist or we want to overwrite
    # For this task, we overwrite to ensure latest logic
    print(f"Processing: {memory['title']}")
    memory['smart_data'] = extract_smart_data(memory.get('description', ''), memory['title'])

# Save back
with open('fastapi_app/data/memories.json', 'w') as f:
    json.dump(memories, f, indent=4)

print("Enrichment complete!")
