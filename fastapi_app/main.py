
from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
import json
import os
import shutil
from typing import List
import base64
import requests
import re

app = FastAPI()

# Mount Static Files
app.mount("/static", StaticFiles(directory="fastapi_app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="fastapi_app/templates")

# Data File
DATA_FILE = "fastapi_app/data/memories.json"

def load_memories():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def push_to_github(file_path, content_str):
    """
    Pushes updates to GitHub directly using the API.
    Required Env Var: GITHUB_TOKEN
    """
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("Skipping GitHub sync: GITHUB_TOKEN not found.")
        return

    repo_slug = "shaiwalsachdev/journey-with-puchki"
    url = f"https://api.github.com/repos/{repo_slug}/contents/{file_path}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # 1. Get current SHA
    try:
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            print(f"Failed to get file SHA from GitHub: {r.text}")
            return
        sha = r.json().get("sha")

        # 2. Update File
        data = {
            "message": "feat(data): update memories.json via app (user action)",
            "content": base64.b64encode(content_str.encode("utf-8")).decode("utf-8"),
            "sha": sha
        }

        r = requests.put(url, headers=headers, json=data)
        if r.status_code in [200, 201]:
            print("Successfully synced data to GitHub.")
        else:
            print(f"Failed to push to GitHub: {r.text}")
    except Exception as e:
        print(f"GitHub Sync Exception: {e}")

def save_memories(memories):
    # 1. Save locally
    with open(DATA_FILE, 'w') as f:
        json_content = json.dumps(memories, indent=4)
        f.write(json_content)
    
    # 2. Sync to GitHub (Background-ish)
    try:
        push_to_github(DATA_FILE, json_content)
    except Exception as e:
        print(f"GitHub Sync Error: {e}")

SETTINGS_FILE = "fastapi_app/data/settings.json"

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as f:
            return json.load(f)
    return {"private_mode": False, "theme": "light"}

def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f, indent=4)
    try:
        push_to_github(SETTINGS_FILE, json.dumps(settings, indent=4))
    except Exception as e:
        print(f"GitHub Sync Error: {e}")

def redact_text(text: str, is_private_mode: bool) -> str:
    if is_private_mode and text:
        # Redact sensitive words
        sensitive_words = ["kiss", "hugs", "hinge", "cheek pecks", "lips", "cuddle", "snuggle"]
        redacted_text = text
        for word in sensitive_words:
            pattern = re.compile(re.escape(word), re.IGNORECASE)
            redacted_text = pattern.sub("✨" * len(word), redacted_text)
        return redacted_text
    return text

@app.middleware("http")
async def add_settings_to_request(request: Request, call_next):
    request.state.settings = load_settings()
    response = await call_next(request)
    return response

# --- Admin Routes ---
@app.get("/admin", response_class=HTMLResponse)
async def admin_panel(request: Request):
    if request.cookies.get("session") != "admin_logged_in":
        return RedirectResponse(url="/login?next=/admin")
    settings = request.state.settings
    return templates.TemplateResponse("admin.html", {"request": request, "page": "admin", "settings": settings})

@app.post("/api/settings")
async def update_settings(request: Request):
    if request.cookies.get("session") != "admin_logged_in":
        return JSONResponse(status_code=401, content={"status": "error", "message": "Unauthorized"})
    
    data = await request.json()
    current_settings = load_settings()
    
    if "private_mode" in data:
        current_settings["private_mode"] = data["private_mode"]
    if "theme" in data:
        current_settings["theme"] = data["theme"]
        
    save_settings(current_settings)
    return {"status": "success", "settings": current_settings}

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as f:
            return json.load(f)
    return {"private_mode": False, "theme": "light"} # Default settings

def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        json_content = json.dumps(settings, indent=4)
        f.write(json_content)
    try:
        push_to_github(SETTINGS_FILE, json_content)
    except Exception as e:
        print(f"GitHub Sync Error: {e}")

def redact_text(text: str, is_private_mode: bool) -> str:
    if is_private_mode and text:
        # Redact sensitive words
        sensitive_words = ["quick hug", "kiss", "hugs", "hinge", "cheek pecks", "lips", "cuddle", "snuggle"]
        redacted_text = text
        for word in sensitive_words:
            pattern = re.compile(re.escape(word), re.IGNORECASE)
            redacted_text = pattern.sub("✨" * len(word), redacted_text)
        return redacted_text
    return text

@app.middleware("http")
async def add_settings_to_request(request: Request, call_next):
    request.state.settings = load_settings()
    response = await call_next(request)
    return response

# ... (Admin Routes omitted for brevity as they shouldn't change) ...

# --- Public Routes ---

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    settings = request.state.settings
    return templates.TemplateResponse("index.html", {"request": request, "page": "home", "settings": settings})

@app.get("/timeline", response_class=HTMLResponse)
async def timeline(request: Request):
    memories = load_memories()
    settings = request.state.settings
    
    # Filter out Memory ID 1 (Hinge) if Private Mode is ON
    if settings.get("private_mode"):
        memories = [m for m in memories if m["id"] != 1]
        # Apply redaction to visible memories
        for m in memories:
            m["description"] = redact_text(m.get("description", ""), True)
            m["title"] = redact_text(m.get("title", ""), True)
            if "smart_data" in m and "itinerary" in m["smart_data"]:
                for item in m["smart_data"]["itinerary"]:
                    item["item"] = redact_text(item.get("item", ""), True)

    return templates.TemplateResponse("timeline.html", {
        "request": request, 
        "memories": memories,
        "page": "timeline",
        "settings": settings
    })

@app.get("/memory/{memory_id}", response_class=HTMLResponse)
async def memory_detail(request: Request, memory_id: int):
    memories = load_memories()
    settings = request.state.settings
    
    memory = next((m for m in memories if m["id"] == memory_id), None)

    if settings.get("private_mode") and memory:
        # If accessing Hinge memory (ID 1) in private mode, block it
        if memory["id"] == 1:
             return RedirectResponse(url="/timeline")
        
        # Redact content
        memory["description"] = redact_text(memory.get("description", ""), True)
        memory["title"] = redact_text(memory.get("title", ""), True)
        if "smart_data" in memory and "itinerary" in memory["smart_data"]:
             for item in memory["smart_data"]["itinerary"]:
                  item["item"] = redact_text(item.get("item", ""), True)

    if not memory:
        # handle 404 cleanly or redirect
        return templates.TemplateResponse("timeline.html", {"request": request, "memories": memories})
    
    # Dynamic Template Selection
    template_name = memory.get("template", "memory.html")
    return templates.TemplateResponse(template_name, {"request": request, "memory": memory})

@app.get("/gallery", response_class=HTMLResponse)
async def read_gallery(request: Request):
    memories = load_memories()
    # Pass 'memories' directly as the template expects it
    return templates.TemplateResponse("gallery.html", {"request": request, "memories": memories})

@app.get("/story", response_class=HTMLResponse)
async def read_story(request: Request):
    settings = request.state.settings
    return templates.TemplateResponse("story.html", {"request": request, "settings": settings})

COUPONS_FILE = "fastapi_app/data/coupons.json"

def load_coupons():
    if os.path.exists(COUPONS_FILE):
        with open(COUPONS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_coupons(coupons):
    with open(COUPONS_FILE, 'w') as f:
        json_content = json.dumps(coupons, indent=4)
        f.write(json_content)
    try:
        push_to_github(COUPONS_FILE, json_content)
    except Exception as e:
        print(f"GitHub Sync Error: {e}")

@app.get("/coupons", response_class=HTMLResponse)
async def read_coupons(request: Request):
    coupons = load_coupons()
    redeemed_count = sum(1 for c in coupons if c.get('is_redeemed'))
    available_count = len(coupons) - redeemed_count
    return templates.TemplateResponse("coupons.html", {
        "request": request, 
        "coupons": coupons,
        "available_count": available_count,
        "redeemed_count": redeemed_count
    })

@app.get("/upcoming", response_class=HTMLResponse)
async def read_upcoming(request: Request):
    return templates.TemplateResponse("upcoming.html", {"request": request})

@app.get("/review", response_class=HTMLResponse)
async def read_review(request: Request):
    return templates.TemplateResponse("year_in_review.html", {"request": request})

@app.post("/redeem/{coupon_id}")
async def redeem_coupon(coupon_id: int):
    coupons = load_coupons()
    for coupon in coupons:
        if coupon['id'] == coupon_id and not coupon['is_redeemed']:
            coupon['is_redeemed'] = True
            from datetime import datetime
            coupon['redeemed_date'] = datetime.now().strftime("%b %d, %Y")
            save_coupons(coupons)
            return {"status": "success", "date": coupon['redeemed_date']}
    return {"status": "error", "message": "Coupon not found or already redeemed"}

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...), next: str = "/add"):
    if username == "puchki" and password == "puchki123":
        # Check query param 'next' from the referer or form if we decide to pass it
        # For now, simple logic: if referer usually has it, but let's stick to default /add or /admin if came from there
        
        # Determine redirect url
        redirect_url = "/add"
        referer = request.headers.get("referer")
        if referer and "next=/admin" in referer:
             redirect_url = "/admin"
        
        response = RedirectResponse(url=redirect_url, status_code=303)
        response.set_cookie(key="session", value="admin_logged_in")
        return response
    return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid Credentials"})

@app.get("/add", response_class=HTMLResponse)
async def add_memory_page(request: Request):
    if request.cookies.get("session") != "admin_logged_in":
        return RedirectResponse(url="/login")
    return templates.TemplateResponse("add_memory.html", {"request": request})

@app.post("/add")
async def add_memory(
    request: Request,
    date: str = Form(...),
    title: str = Form(...),
    description: str = Form(...),
    type: str = Form(...),
    photos: List[UploadFile] = File(...)
):
    memories = load_memories()
    new_id = len(memories) + 1
    
    # Save Photos
    photo_filenames = []
    upload_dir = f"fastapi_app/static/uploads/{new_id}"
    os.makedirs(upload_dir, exist_ok=True)
    
    for photo in photos:
        if photo.filename:
            file_path = os.path.join(upload_dir, photo.filename)
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(photo.file, buffer)
            photo_filenames.append(photo.filename)
    
    new_memory = {
        "id": new_id,
        "date": date,
        "title": title,
        "description": description,
        "type": type,
        "photos": photo_filenames
    }
    
    save_memories(memories)
    
    return RedirectResponse(url="/timeline", status_code=303)

# --- Music Route ---
@app.get("/music", response_class=HTMLResponse)
async def read_music(request: Request):
    return templates.TemplateResponse("music.html", {"request": request})

# --- Guestbook Routes ---
GUESTBOOK_FILE = "fastapi_app/data/guestbook.json"

def load_guestbook():
    if os.path.exists(GUESTBOOK_FILE):
        with open(GUESTBOOK_FILE, 'r') as f:
            return json.load(f)
    return []

def save_guestbook(notes):
    with open(GUESTBOOK_FILE, 'w') as f:
        json_content = json.dumps(notes, indent=4)
        f.write(json_content)
    try:
        push_to_github(GUESTBOOK_FILE, json_content)
    except Exception as e:
        print(f"GitHub Sync Error: {e}")

@app.get("/guestbook", response_class=HTMLResponse)
async def read_guestbook(request: Request):
    notes = load_guestbook()
    return templates.TemplateResponse("guestbook.html", {"request": request, "notes": notes})

@app.post("/guestbook/sign")
async def sign_guestbook(
    request: Request,
    name: str = Form(...),
    message: str = Form(...),
    color: str = Form(...)
):
    notes = load_guestbook()
    from datetime import datetime
    new_note = {
        "id": len(notes) + 1,
        "name": name,
        "message": message,
        "date": datetime.now().strftime("%b %d, %Y"),
        "color_class": color
    }
    notes.insert(0, new_note) # Add to top
    save_guestbook(notes)
    return RedirectResponse(url="/guestbook", status_code=303)

# --- Vault Routes ---
VAULT_FILE = "fastapi_app/data/vault.json"

def load_vault():
    if os.path.exists(VAULT_FILE):
        with open(VAULT_FILE, 'r') as f:
            return json.load(f)
    return []

def save_vault(letters):
    with open(VAULT_FILE, 'w') as f:
        json_content = json.dumps(letters, indent=4)
        f.write(json_content)
    try:
        push_to_github(VAULT_FILE, json_content)
    except Exception as e:
        print(f"GitHub Sync Error: {e}")

@app.get("/vault", response_class=HTMLResponse)
async def read_vault(request: Request):
    letters = load_vault()
    return templates.TemplateResponse("vault.html", {"request": request, "letters": letters})



@app.get("/roka", response_class=HTMLResponse)
async def read_roka(request: Request):
    # Dummy memory object to satisfy partials (smart_highlights, comments)
    dummy_memory = {
        "id": "roka",
        "title": "The Grand Roka",
        "description": "Where two families become one.",
        "date": "March 12, 2026",
        "photos": [],
        "comments": [],
        "smart_data": {
            "itinerary": [],
            "vibe": "Blessed & Happy",
             "entities": {"food": [], "places": []}
        }
    }
    return templates.TemplateResponse("memory_roka.html", {"request": request, "memory": dummy_memory})

# --- Wishlist Routes ---
WISHLIST_FILE = "fastapi_app/data/wishlist.json"

def load_wishlist():
    if os.path.exists(WISHLIST_FILE):
        with open(WISHLIST_FILE, 'r') as f:
            return json.load(f)
    return []

def save_wishlist(items):
    with open(WISHLIST_FILE, 'w') as f:
        json_content = json.dumps(items, indent=4)
        f.write(json_content)
    try:
        push_to_github(WISHLIST_FILE, json_content)
    except Exception as e:
        print(f"GitHub Sync Error: {e}")

@app.get("/wishlist", response_class=HTMLResponse)
async def read_wishlist(request: Request):
    items = load_wishlist()
    # Sort by ID desc (newest first)
    items.sort(key=lambda x: x['id'], reverse=True)
    return templates.TemplateResponse("wishlist.html", {"request": request, "items": items})

@app.post("/wishlist/add")
async def add_wish(
    request: Request,
    title: str = Form(...),
    description: str = Form(...),
    image_url: str = Form(...),
    link: str = Form(None)
):
    items = load_wishlist()
    from datetime import datetime
    new_item = {
        "id": len(items) + 1,
        "title": title,
        "description": description,
        "image_url": image_url,
        "link": link if link else "#",
        "date_added": datetime.now().strftime("%b %d, %Y")
    }
    items.append(new_item)
@app.post("/rate_date/{memory_id}")
async def rate_date(
    memory_id: int,
    fun: int = Form(...),
    food: int = Form(...),
    vibe: int = Form(...),
    romance: int = Form(...),
    comment: str = Form("")
):
    memories = load_memories()
    memory = next((m for m in memories if m["id"] == memory_id), None)
    
    if memory:
        from datetime import datetime
        memory["shaila_rating"] = {
            "fun": fun,
            "food": food,
            "vibe": vibe,
            "romance": romance,
            "comment": comment,
            "timestamp": datetime.now().strftime("%b %d, %Y")
        }
        save_memories(memories)
        
    return RedirectResponse(url=f"/memory/{memory_id}", status_code=303)

@app.post("/add_comment/{memory_id}")
async def add_comment(
    memory_id: int,
    name: str = Form(...),
    message: str = Form(...),
    color: str = Form("bg-blue-100") 
):
    memories = load_memories()
    memory = next((m for m in memories if m["id"] == memory_id), None)
    
    if memory:
        if "comments" not in memory:
            memory["comments"] = []
            
        from datetime import datetime
        new_comment = {
            "name": name,
            "message": message,
            "date": datetime.now().strftime("%b %d, %Y"),
            "color": color
        }
        # Add to top
        memory["comments"].insert(0, new_comment)
        save_memories(memories)
        
    return RedirectResponse(url=f"/memory/{memory_id}", status_code=303)

# --- Dictionary Routes ---
DICTIONARY_FILE = "fastapi_app/data/dictionary.json"

def load_dictionary():
    if os.path.exists(DICTIONARY_FILE):
        with open(DICTIONARY_FILE, 'r') as f:
            return json.load(f)
    return []

def save_dictionary(words):
    with open(DICTIONARY_FILE, 'w') as f:
        json_content = json.dumps(words, indent=4)
        f.write(json_content)
    try:
        push_to_github(DICTIONARY_FILE, json_content)
    except Exception as e:
        print(f"GitHub Sync Error: {e}")

@app.get("/dictionary", response_class=HTMLResponse)
async def read_dictionary(request: Request):
    words = load_dictionary()
    # Sort by ID desc (newest first)
    words.sort(key=lambda x: x['id'], reverse=True)
    return templates.TemplateResponse("dictionary.html", {"request": request, "words": words})

@app.post("/dictionary/add")
async def add_word(
    request: Request,
    word: str = Form(...),
    meaning: str = Form(...),
    context: str = Form(...),
    icon: str = Form("format_quote")
):
    words = load_dictionary()
    from datetime import datetime
    new_word = {
        "id": len(words) + 1,
        "word": word,
        "meaning": meaning,
        "context": context,
        "date": datetime.now().strftime("%b %d, %Y"),
        "icon": icon
    }
    words.insert(0, new_word) # Add to top
    save_dictionary(words)
    return RedirectResponse(url="/dictionary", status_code=303)
