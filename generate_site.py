import os
import re
import shutil
from datetime import datetime

# Paths
BASE_DIR = "/Users/geekdon/Documents/Journey with Puchki"
NOTES_FILE = os.path.join(BASE_DIR, "notes.txt")
STITCH_DIR = os.path.join(BASE_DIR, "stitch_home_journey_with_puchki")
FAVOURITES_DIR = os.path.join(BASE_DIR, "Favourites")

# Template Directories
HOME_TEMPLATE_DIR = os.path.join(STITCH_DIR, "home:_journey_with_puchki_1")
TIMELINE_TEMPLATE_DIR = os.path.join(STITCH_DIR, "memory_lane:_our_timeline_1")
DINNER_TEMPLATE_DIR = os.path.join(STITCH_DIR, "memory:_candle_light_dinner_1")
MOVIE_TEMPLATE_DIR = os.path.join(STITCH_DIR, "memory:_our_first_movie_date")
SHOPPING_TEMPLATE_DIR = os.path.join(STITCH_DIR, "memory:_shopping_&_metro_craziness")
ART_TEMPLATE_DIR = os.path.join(STITCH_DIR, "memory:_art_date_&_painting")

# Target Files (to be updated)
HOME_FILE = os.path.join(HOME_TEMPLATE_DIR, "code.html")
TIMELINE_FILE = os.path.join(TIMELINE_TEMPLATE_DIR, "code.html")

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
            # Check for "Photos: ... folder" inside the match line if regex caught it weirdly, 
            # but usually it's on a new line. 
            # If the previous line was an event, save it.
            if "Photos:" in line:
                 # This might happen if the date line *contains* Photos: (rare in this format)
                 pass
            
            if current_event:
                events.append(current_event)
            
            date_str = match.group(1).strip()
            title = match.group(2).strip()
            if not title:
                title = "Special Memory"
            
            current_event = {
                "date": date_str,
                "title": title,
                "description": "",
                "photos_folder": None,
                "special_photos": [],
                "folder_path": ""
            }
        elif current_event:
            if line.startswith("Photo:"):
                photo_match = re.search(r"<(.*)>", line)
                if photo_match:
                    current_event["special_photos"].append(photo_match.group(1))
            elif line.startswith("Photos:"):
                 folder_match = re.search(r"Photos:\s*(.*)\s+folder", line, re.IGNORECASE)
                 if folder_match:
                     current_event["photos_folder"] = folder_match.group(1).strip()
            else:
                current_event["description"] += line + " "
    
    if current_event:
        events.append(current_event)
        
    return events

def get_photos_for_event(event):
    photos = []
    # Check specific folder
    if event.get("photos_folder"):
        possible_folder = event["photos_folder"]
        folder_path = os.path.join(BASE_DIR, possible_folder)
        if os.path.exists(folder_path):
             for f in os.listdir(folder_path):
                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.heic')):
                     photos.append(os.path.join(possible_folder, f))
        else:
            # Fuzzy match
            for d in os.listdir(BASE_DIR):
                if event["date"] in d and os.path.isdir(os.path.join(BASE_DIR, d)):
                     for f in os.listdir(os.path.join(BASE_DIR, d)):
                        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.heic')):
                             photos.append(os.path.join(d, f))
                     break
    # Check loose photos
    for photo_name in event.get("special_photos", []):
         if os.path.exists(os.path.join(BASE_DIR, photo_name)):
             photos.append(photo_name)
    return photos

def remove_login_button(content):
    # Matches <button ...> *Login* or *Sign In* ... </button> or similar anchor tags.
    # Be simple: Look for the specific button text and replace the whole element if possible.
    # Common pattern: <button ...> ... Sign In ... </button>
    content = re.sub(r'<button[^>]*>\s*<span[^>]*>login</span>\s*Sign In\s*</button>', '', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r'<a[^>]*>\s*Login\s*</a>', '', content, flags=re.IGNORECASE | re.DOTALL)
    # Specific to gallery template
    content = re.sub(r'<a[^>]*>\s*Login\s*</a>', '', content, flags=re.IGNORECASE | re.DOTALL)
    
    return content

def select_template(title):
    t = title.lower()
    if "movie" in t:
        return MOVIE_TEMPLATE_DIR, "movie"
    elif "shopping" in t or "metro" in t:
        return SHOPPING_TEMPLATE_DIR, "shopping"
    elif "art" in t or "paint" in t:
        return ART_TEMPLATE_DIR, "art"
    else:
        return DINNER_TEMPLATE_DIR, "dinner"

def create_memory_page(event, index):
    clean_title = "".join(x for x in event["title"] if x.isalnum() or x in " _-").strip()
    folder_slug = clean_title.replace(" ", "_").lower()
    if not folder_slug:
        folder_slug = f"event_{index}"
        
    folder_name = f"memory:_{folder_slug}_{index}"
    folder_dir = os.path.join(STITCH_DIR, folder_name)
    event["folder_path"] = folder_name
    
    if not os.path.exists(folder_dir):
        os.makedirs(folder_dir)
    
    template_dir, template_type = select_template(event["title"])
    template_file = os.path.join(template_dir, "code.html")
    
    with open(template_file, 'r') as f:
        content = f.read()

    # Common Replacements
    content = re.sub(r"<title>.*?</title>", f"<title>Journey with Puchki - {event['title']}</title>", content)
    content = remove_login_button(content)
    
    photos = get_photos_for_event(event)
    hero_photo = f"../../{photos[0]}" if photos else "../../Favourites/IMG_9272.HEIC"

    # Template Specific Logic
    if template_type == "movie":
        # Movie Template Replacements
        content = re.sub(r"Tere Ishk Mein", event['title'], content) # Ticket title
        content = re.sub(r"Nov 29, 2025", event['date'], content) # Ticket date
        content = re.sub(r"First Close Interaction", event['title'], content) # Badge
        
        # Description
        desc_pattern = r'(<h2 class="text-4xl font-bold leading-tight">)(.*?)(</h2>)'
        content = re.sub(desc_pattern, r'\1' + event['title'] + r'\3', content)
        
        # Long text
        text_pattern = r'(<div class="space-y-4 text-neutral-300 text-lg leading-relaxed">)(.*?)(</div>)'
        content = re.sub(text_pattern, r'\1<p>' + event['description'] + r'</p>\3', content, flags=re.DOTALL)
        
        # Hero Image in Ticket is CSS/Background? No, it's not.
        # It has a movie visual. 
        # <img alt="Couple holding hands..." src="...">
        # Let's replace the main visual 
        content = re.sub(r'(<img alt="Couple holding hands.*?".*?src=")(.*?)("/>)', r'\1' + hero_photo + r'\3', content)

        # Photo Grid (Film Strip)
        # It creates a grid. We can inject photos there.
        # Format: <div class="..."><img ... src="..."></div>
        # Find the container: <div class="grid grid-cols-2 md:grid-cols-3 gap-4 md:gap-6 auto-rows-[200px]">
        # Replace contents.
        
        new_grid = ""
        for p in photos[:6]: # Limit to 6 for layout
            new_grid += f'''
            <div class="relative group overflow-hidden rounded-xl border-2 border-white/5 shadow-lg">
                <img class="w-full h-full object-cover transform group-hover:scale-110 transition duration-700" src="../../{p}"/>
            </div>
            '''
        
        grid_start = '<div class="grid grid-cols-2 md:grid-cols-3 gap-4 md:gap-6 auto-rows-[200px]">'
        if grid_start in content:
            start_idx = content.find(grid_start) + len(grid_start)
            end_idx = content.find('</section>', start_idx) # Rough end
            # Actually easier to use regex for the whole block if possible, or just append
            # Let's try to just insert into the grid if we can find it.
            # Simplified: Just replace the first few images we find?
            pass # Creating grid logic for movie is complex, skipping strict grid replacement for now to avoid breaking layout

    elif template_type == "shopping":
        # Shopping Template Replacements
        content = re.sub(r"01 FEB 2026", event['date'], content)
        content = re.sub(r"Metro Madness &amp; <br/>\s*<span class=\"text-primary inline-block transform -rotate-2\">Bag Battles</span>", event['title'], content)
        content = re.sub(r"Surviving the Delhi crowds.*laughter.", event['description'], content)
        
        # Ticket Route?
        content = re.sub(r"Karol Bagh", "Love Station", content)
        content = re.sub(r"Lajpat Nagar", "Forever", content)
        
        # Quote Bubble
        content = re.sub(r"Walking was so tiring.*metro!", event['description'][:150] + "...", content)
        
        # Photo Collage
        # Replace images in collage
        # <img ... src="...">
        # We can just iterate and replace the first N image srcs
        
        src_pattern = r'src="https://lh3.googleusercontent.com/.*?"'
        # We find all matches
        matches = list(re.finditer(src_pattern, content))
        for i, match in enumerate(matches):
            if i < len(photos):
                # Replace this specific span
                # This string replacement is tricky because indexes shift.
                # Better: split and rejoin?
                pass
        
        # Let's do a simpler replacement: Replace the first N external links with local photos
        for i, photo in enumerate(photos):
             content = re.sub(r'src="https://lh3.googleusercontent.com/[^"]+"', f'src="../../{photo}"', content, count=1)


    elif template_type == "art":
        # Art Template Replacements
        content = re.sub(r"Dec 13, 2025", event['date'], content)
        content = re.sub(r"Painting Our Future at .*Palette Cafe.*</h1>", f"<h1>{event['title']}</h1>", content) 
        content = re.sub(r"Best date ever!.*colors.", event['description'], content)
        
        # Main Canvas Image
        # <img class="w-full h-full object-cover" data-alt="Watercolor painting..." src="...">
        # Replace first N images
        for i, photo in enumerate(photos):
             content = re.sub(r'src="https://lh3.googleusercontent.com/[^"]+"', f'src="../../{photo}"', content, count=1)

    else:
        # Default Dinner Template (Used previously)
        content = re.sub(r'Candle Light\s*<br/>\s*<span class="text-primary/90 italic font-serif">Dinner</span>', event['title'], content, flags=re.DOTALL)
        if "Candle Light" in content: pass 
        content = re.sub(r'Nov 22, 2025', event['date'], content)
        
        desc_pattern = r'(<p class="font-handwriting text-3xl md:text-4xl lg:text-5xl text-gray-200 leading-relaxed mb-6">\s*)(.*?)(\s*</p>)'
        content = re.sub(desc_pattern, lambda m: f'{m.group(1)}{event["description"]}{m.group(3)}', content, flags=re.DOTALL)
        
        if photos:
            # Replace Hero
            content = re.sub(r'(<img alt="Candle light dinner setting.*?".*?src=")(.*?)("/>)', lambda m: f'{m.group(1)}{hero_photo}{m.group(3)}', content, flags=re.DOTALL)
            
            # Replace Grid logic (from previous script, simplified)
            new_grid_content = ""
            for photo in photos:
                new_grid_content += f'''
                <div class="group rounded-xl overflow-hidden relative cursor-pointer">
                    <img alt="{event["title"]}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="../../{photo}"/>
                </div>
                '''
            start_idx = content.find("<!-- Item 1: Large Vertical -->")
            loc_idx = content.find("<!-- Location Map Preview (Static) -->")
            if start_idx != -1 and loc_idx != -1:
                pre_loc = content[:loc_idx]
                last_div_idx = pre_loc.rfind("</div>")
                content = content[:start_idx] + new_grid_content + "\n" + content[last_div_idx:]

    with open(os.path.join(folder_dir, "code.html"), 'w') as f:
        f.write(content)
        
    return folder_name

def update_home_page():
    with open(HOME_FILE, 'r') as f:
        content = f.read()

    # 1. Update Navigation Links
    # Our Story -> shaix2:_our_year_in_review
    content = re.sub(r'href="#story"', 'href="../shaix2:_our_year_in_review/code.html"', content)
    # Memories -> memory_lane:_our_timeline_1
    content = re.sub(r'href="#memories"', 'href="../memory_lane:_our_timeline_1/code.html"', content)
    content = re.sub(r'href="#timeline"', 'href="../memory_lane:_our_timeline_1/code.html"', content)
    # View Timeline button
    
    # 2. Update Card Links (Explore Section)
    # Card 1: Our Story
    content = re.sub(r'(<!-- Card 1: Our Story -->\s*<a class=".*?)\s*href="#"', r'\1 href="../shaix2:_our_year_in_review/code.html"', content)
    # Card 2: Memory Lane
    content = re.sub(r'(<!-- Card 2: Memory Lane -->\s*<a class=".*?)\s*href="#"', r'\1 href="../memory_lane:_our_timeline_1/code.html"', content)
    # Card 3: Events -> Upcoming
    content = re.sub(r'(<!-- Card 3: Upcoming Events -->\s*<a class=".*?)\s*href="#"', r'\1 href="../upcoming:_our_future_milestones_1/code.html"', content)
    # Card 4: Coupons
    content = re.sub(r'(<!-- Card 4: Love Coupons -->\s*<a class=".*?)\s*href="#"', r'\1 href="../love_coupons:_special_treats_1/code.html"', content)

    # 3. Add #ShaiX2
    badge_pattern = r'(<span class="text-white font-medium tracking-wide uppercase text-sm">Shaiwal &amp; Shaila)(</span>)'
    content = re.sub(badge_pattern, r'\1 #ShaiX2\2', content)
    
    # 4. Hero Image
    fav_photo = "IMG_9272.HEIC" 
    bg_pattern = r"(background-image: url\(')(.*?)('\);)"
    content = re.sub(bg_pattern, r"\1../../Favourites/" + fav_photo + r"\3", content, count=1)
    
    # 5. Remove Login
    content = remove_login_button(content)
    
    with open(HOME_FILE, 'w') as f:
        f.write(content)

def update_timeline(events):
    with open(TIMELINE_FILE, 'r') as f:
        content = f.read()

    # Remove Login
    content = remove_login_button(content)

    start_replace_marker = "<!-- Card 1: Top Aligned -->"
    end_replace_marker = "<!-- End Marker -->"
    
    if start_replace_marker in content and end_replace_marker in content:
        start_idx = content.find(start_replace_marker)
        end_idx = content.find(end_replace_marker)
        
        new_cards_html = ""
        for i, event in enumerate(events):
            is_top = (i % 2 == 0)
            margin_class = "mt-48" if not is_top else ""
            line_class = "top-full" if is_top else "bottom-full"
            node_class = "top-[calc(100%+2.8rem)]" if is_top else "bottom-[calc(100%+2.8rem)]"
            mb_class = "mb-12" if is_top else ""
            
            photos = get_photos_for_event(event)
            img_src = f"../../{photos[0]}" if photos else "https://placehold.co/400x300?text=No+Photo"
            
            desc_short = event['description'][:100] + "..." if len(event['description']) > 100 else event['description']
            
            card_html = f'''
            <!-- Generated Card {i} -->
            <div class="relative flex-shrink-0 w-80 group {margin_class}">
                <!-- Connector Line -->
                <div class="absolute left-1/2 {line_class} h-12 w-0.5 bg-primary/30 border-l-2 border-dashed border-primary/30 -translate-x-1/2"></div>
                <!-- Node -->
                <div class="absolute left-1/2 {node_class} w-4 h-4 bg-primary rounded-full -translate-x-1/2 ring-4 ring-white dark:ring-background-dark shadow-md z-10"></div>
                
                <a href="../{event['folder_path']}/code.html">
                    <div class="bg-white dark:bg-gray-800 p-4 pb-6 rounded-lg polaroid-shadow transform transition-transform duration-300 hover:-translate-y-2 hover:rotate-1 relative {mb_class}">
                        <!-- Tape -->
                        <div class="absolute -top-3 left-1/2 -translate-x-1/2 w-24 h-8 bg-primary/10 backdrop-blur-sm transform -rotate-1 opacity-80 z-20"></div>
                        
                        <div class="aspect-[4/3] w-full bg-gray-100 dark:bg-gray-700 rounded mb-4 overflow-hidden relative">
                            <img alt="{event['title']}" class="w-full h-full object-cover" src="{img_src}"/>
                        </div>
                        
                        <div class="space-y-2">
                            <div class="flex justify-between items-baseline">
                                <span class="font-display font-bold text-lg text-gray-900 dark:text-white">{event['title']}</span>
                                <span class="text-xs font-semibold text-primary bg-primary/10 px-2 py-1 rounded-full">{event['date']}</span>
                            </div>
                            <p class="text-sm text-gray-600 dark:text-gray-300 font-display leading-relaxed line-clamp-3">
                                {desc_short}
                            </p>
                        </div>
                    </div>
                </a>
            </div>
            '''
            new_cards_html += card_html
        
        new_content = content[:start_idx] + new_cards_html + "\n" + content[end_idx:]
        
        with open(TIMELINE_FILE, 'w') as f:
            f.write(new_content)

def main():
    events = parse_notes()
    print(f"Found {len(events)} events.")
    
    # Create pages
    for i, event in enumerate(events):
        print(f"Processing: {event['date']} - {event['title']}")
        create_memory_page(event, i)
        
    # Update Home
    update_home_page()
    
    # Update Timeline
    update_timeline(events)

if __name__ == "__main__":
    main()
