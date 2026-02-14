
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

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/timeline", response_class=HTMLResponse)
async def timeline(request: Request):
    with open("fastapi_app/data/memories.json", "r") as f:
        memories = json.load(f)
    return templates.TemplateResponse("timeline.html", {"request": request, "memories": memories})

@app.get("/memory/{memory_id}", response_class=HTMLResponse)
async def memory_detail(request: Request, memory_id: int):
    with open("fastapi_app/data/memories.json", "r") as f:
        memories = json.load(f)
    
    memory = next((m for m in memories if m["id"] == memory_id), None)
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
    return templates.TemplateResponse("story.html", {"request": request})

COUPONS_FILE = "fastapi_app/data/coupons.json"

def load_coupons():
    if os.path.exists(COUPONS_FILE):
        with open(COUPONS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_coupons(coupons):
    with open(COUPONS_FILE, 'w') as f:
        json.dump(coupons, f, indent=4)

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
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == "puchki" and password == "puchki123": # Updated credentials
        response = RedirectResponse(url="/add", status_code=303)
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
        json.dump(notes, f, indent=4)

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
        json.dump(items, f, indent=4)

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
