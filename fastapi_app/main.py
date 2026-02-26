
from fastapi import FastAPI, Request, Form, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
import json
import os
import shutil
from typing import List
import re
import random
import math
import io

# --- Database & Storage imports ---
from fastapi_app.database import (
    get_db, get_all_memories, save_all_memories, update_memory, get_memory_by_id,
    get_next_memory_id, add_memory as db_add_memory,
    get_settings, save_settings,
    get_all_coupons, save_all_coupons, update_coupon,
    get_all_guestbook, add_guestbook_entry,
    get_all_vault,
    get_all_wishlist, add_wishlist_item,
    get_all_dictionary, add_dictionary_word, save_all_dictionary,
)
from fastapi_app.storage import upload_file, get_photo_url, R2_PUBLIC_URL

app = FastAPI()

# Get base directory of the current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Mount Static Files (still needed for CSS, JS, music, and other non-photo assets)
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Templates
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Make R2 URL available in all templates
templates.env.globals["r2_url"] = R2_PUBLIC_URL


# --- Privacy / Redaction Logic ---

def redact_text(text: str, is_private_mode: bool) -> str:
    if is_private_mode and text:
        sensitive_words = ["kiss", "hugs", "hinge", "cheek pecks", "cuddle", "snuggle"]
        redacted_text = text
        for word in sensitive_words:
            pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
            redacted_text = pattern.sub("✨" * len(word), redacted_text)
        return redacted_text
    return text


def process_memories_for_display(memories: List[dict], settings: dict) -> List[dict]:
    """
    Processes memories for display:
    1. Filters out blocked memories (e.g. ID 1 in private mode)
    2. Swaps content with 'safe' versions if in private mode
    3. Redacts remaining content if in private mode
    """
    processed_memories = []
    is_private = settings.get("private_mode", False)

    for m in memories:
        if is_private and m["id"] == 1:
            continue

        m_copy = m.copy()

        if is_private:
            if "title_safe" in m_copy:
                m_copy["title"] = m_copy["title_safe"]
            if "description_safe" in m_copy:
                m_copy["description"] = m_copy["description_safe"]

            m_copy["description"] = redact_text(m_copy.get("description", ""), True)
            m_copy["title"] = redact_text(m_copy.get("title", ""), True)

            if "smart_data" in m_copy and "itinerary" in m_copy["smart_data"]:
                import copy
                m_copy["smart_data"] = copy.deepcopy(m_copy["smart_data"])
                for item in m_copy["smart_data"]["itinerary"]:
                    if "item_safe" in item:
                        item["item"] = item["item_safe"]
                    item["item"] = redact_text(item.get("item", ""), True)

        # Hide Photos Logic
        if "hide_all_photos" in m_copy and m_copy["hide_all_photos"]:
            m_copy["photos"] = []
        elif "hidden_photos" in m_copy and m_copy["hidden_photos"]:
            m_copy["photos"] = [p for p in m_copy["photos"] if p not in m_copy["hidden_photos"]]

        processed_memories.append(m_copy)

    return processed_memories


# --- Middleware ---

@app.middleware("http")
async def add_settings_to_request(request: Request, call_next):
    request.state.settings = await get_settings()
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
async def update_settings_route(request: Request):
    if request.cookies.get("session") != "admin_logged_in":
        return JSONResponse(status_code=401, content={"status": "error", "message": "Unauthorized"})

    data = await request.json()
    current_settings = await get_settings()

    if "private_mode" in data:
        current_settings["private_mode"] = data["private_mode"]
    if "theme" in data:
        current_settings["theme"] = data["theme"]

    await save_settings(current_settings)
    return {"status": "success", "settings": current_settings}


# --- Public Routes ---

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    settings = request.state.settings
    return templates.TemplateResponse("index.html", {"request": request, "page": "home", "settings": settings})


@app.get("/timeline", response_class=HTMLResponse)
async def timeline(request: Request):
    memories = await get_all_memories()
    settings = request.state.settings
    visible_memories = process_memories_for_display(memories, settings)
    return templates.TemplateResponse("timeline.html", {
        "request": request,
        "memories": visible_memories,
        "page": "timeline",
        "settings": settings
    })


@app.get("/memory/{memory_id}", response_class=HTMLResponse)
async def memory_detail(request: Request, memory_id: int):
    memories = await get_all_memories()
    settings = request.state.settings
    processed_memories = process_memories_for_display(memories, settings)
    memory = next((m for m in processed_memories if m["id"] == memory_id), None)

    if not memory:
        return RedirectResponse(url="/timeline")

    template_name = memory.get("template", "memory.html")
    return templates.TemplateResponse(template_name, {"request": request, "memory": memory, "settings": settings})


# --- Gallery ---

async def get_filtered_memories(settings, seed=None):
    memories = await get_all_memories()
    processed_memories = process_memories_for_display(memories, settings)

    gallery_items = []
    for m in processed_memories:
        if m.get("photos"):
            for p in m["photos"]:
                gallery_items.append({
                    "id": m["id"],
                    "title": redact_text(m["title"], settings.get("private_mode")),
                    "date": m["date"],
                    "type": m["type"],
                    "photo": p
                })

    if seed is not None:
        random.seed(seed)
        random.shuffle(gallery_items)
    else:
        gallery_items.reverse()

    return gallery_items


@app.get("/gallery", response_class=HTMLResponse)
async def read_gallery(request: Request, page: int = 1, limit: int = 12, seed: int = None, category: str = "all"):
    settings = request.state.settings
    all_items = await get_filtered_memories(settings, seed=seed)

    if category != "all":
        all_items = [item for item in all_items if item["type"] == category]

    total_items = len(all_items)
    start = (page - 1) * limit
    end = start + limit
    paginated_items = all_items[start:end]
    has_more = end < total_items

    return templates.TemplateResponse("gallery.html", {
        "request": request,
        "items": paginated_items,
        "page": page,
        "limit": limit,
        "seed": seed,
        "category": category,
        "has_more": has_more,
        "settings": settings
    })


@app.get("/api/memories")
async def get_memories_api(request: Request, page: int = 1, limit: int = 12, seed: int = None, category: str = "all"):
    settings = request.state.settings
    all_items = await get_filtered_memories(settings, seed=seed)

    if category != "all":
        all_items = [item for item in all_items if item["type"] == category]

    total_items = len(all_items)
    start = (page - 1) * limit
    end = start + limit
    paginated_items = all_items[start:end]
    has_more = end < total_items

    return {
        "items": paginated_items,
        "has_more": has_more,
        "next_page": page + 1 if has_more else None
    }


@app.get("/api/admin/memories")
async def get_admin_memories(request: Request):
    if request.cookies.get("session") != "admin_logged_in":
        raise HTTPException(status_code=403, detail="Unauthorized")
    return await get_all_memories()


@app.get("/story", response_class=HTMLResponse)
async def read_story(request: Request):
    settings = request.state.settings
    return templates.TemplateResponse("story.html", {"request": request, "settings": settings})


# --- Coupons ---

@app.get("/coupons", response_class=HTMLResponse)
async def read_coupons(request: Request):
    settings = request.state.settings
    if settings.get("private_mode"):
        return RedirectResponse("/")
    coupons = await get_all_coupons()
    redeemed_count = sum(1 for c in coupons if c.get('is_redeemed'))
    available_count = len(coupons) - redeemed_count
    return templates.TemplateResponse("coupons.html", {
        "request": request,
        "coupons": coupons,
        "available_count": available_count,
        "redeemed_count": redeemed_count,
        "settings": settings
    })


@app.get("/upcoming", response_class=HTMLResponse)
async def read_upcoming(request: Request):
    settings = request.state.settings
    return templates.TemplateResponse("upcoming.html", {"request": request, "settings": settings})


@app.get("/review", response_class=HTMLResponse)
async def read_review(request: Request):
    settings = request.state.settings
    return templates.TemplateResponse("year_in_review.html", {"request": request, "settings": settings})


@app.post("/redeem/{coupon_id}")
async def redeem_coupon(coupon_id: int):
    coupons = await get_all_coupons()
    for coupon in coupons:
        if coupon['id'] == coupon_id and not coupon['is_redeemed']:
            coupon['is_redeemed'] = True
            from datetime import datetime
            coupon['redeemed_date'] = datetime.now().strftime("%b %d, %Y")
            await save_all_coupons(coupons)
            return {"status": "success", "date": coupon['redeemed_date']}
    return {"status": "error", "message": "Coupon not found or already redeemed"}


# --- Login ---

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    settings = request.state.settings
    return templates.TemplateResponse("login.html", {"request": request, "settings": settings})


@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...), next: str = "/add"):
    if username == "puchki" and password == "puchki123":
        redirect_url = "/add"
        referer = request.headers.get("referer")
        if referer and "next=/admin" in referer:
            redirect_url = "/admin"

        response = RedirectResponse(url=redirect_url, status_code=303)
        response.set_cookie(key="session", value="admin_logged_in")
        return response
    return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid Credentials"})


# --- Add Memory ---

@app.get("/add", response_class=HTMLResponse)
async def add_memory_page(request: Request):
    if request.cookies.get("session") != "admin_logged_in":
        return RedirectResponse(url="/login")
    settings = request.state.settings
    return templates.TemplateResponse("add_memory.html", {"request": request, "settings": settings})


@app.post("/add")
async def add_memory(
    request: Request,
    date: str = Form(...),
    title: str = Form(...),
    description: str = Form(...),
    type: str = Form(...),
    photos: List[UploadFile] = File(...)
):
    if request.cookies.get("session") != "admin_logged_in":
        return RedirectResponse(url="/login")

    new_id = await get_next_memory_id()

    # Upload photos to R2
    photo_filenames = []
    for photo in photos:
        if photo.filename:
            r2_key = f"uploads/{new_id}/{photo.filename}"
            content = await photo.read()
            upload_file(io.BytesIO(content), r2_key, photo.content_type)
            photo_filenames.append(photo.filename)

    new_memory = {
        "id": new_id,
        "date": date,
        "title": title,
        "description": description,
        "type": type,
        "photos": photo_filenames
    }

    await db_add_memory(new_memory)
    return RedirectResponse(url="/timeline", status_code=303)


# --- Music ---

@app.get("/music", response_class=HTMLResponse)
async def read_music(request: Request):
    settings = request.state.settings
    return templates.TemplateResponse("music.html", {"request": request, "settings": settings})


# --- Guestbook ---

@app.get("/guestbook", response_class=HTMLResponse)
async def read_guestbook(request: Request):
    notes = await get_all_guestbook()
    settings = request.state.settings
    return templates.TemplateResponse("guestbook.html", {"request": request, "notes": notes, "settings": settings})


@app.post("/guestbook/sign")
async def sign_guestbook(
    request: Request,
    name: str = Form(...),
    message: str = Form(...),
    color: str = Form(...)
):
    from datetime import datetime
    new_note = {
        "id": len(await get_all_guestbook()) + 1,
        "name": name,
        "message": message,
        "date": datetime.now().strftime("%b %d, %Y"),
        "color_class": color
    }
    await add_guestbook_entry(new_note)
    return RedirectResponse(url="/guestbook", status_code=303)


# --- Vault ---

@app.get("/vault", response_class=HTMLResponse)
async def read_vault(request: Request):
    letters = await get_all_vault()
    settings = request.state.settings
    return templates.TemplateResponse("vault.html", {"request": request, "letters": letters, "settings": settings})


# --- Roka ---

@app.get("/roka", response_class=HTMLResponse)
async def read_roka(request: Request):
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
    settings = request.state.settings
    return templates.TemplateResponse("memory_roka.html", {"request": request, "memory": dummy_memory, "settings": settings})


# --- Wishlist ---

@app.get("/wishlist", response_class=HTMLResponse)
async def read_wishlist(request: Request):
    items = await get_all_wishlist()
    settings = request.state.settings
    if settings.get("private_mode", False):
        items = [i for i in items if "honeymoon" not in i["title"].lower()]
    items.sort(key=lambda x: x['id'], reverse=True)
    return templates.TemplateResponse("wishlist.html", {"request": request, "items": items, "settings": settings})


@app.post("/wishlist/add")
async def add_wish(
    request: Request,
    title: str = Form(...),
    description: str = Form(...),
    image_url: str = Form(...),
    link: str = Form(None)
):
    from datetime import datetime
    items = await get_all_wishlist()
    new_item = {
        "id": len(items) + 1,
        "title": title,
        "description": description,
        "image_url": image_url,
        "link": link if link else "#",
        "date_added": datetime.now().strftime("%b %d, %Y")
    }
    await add_wishlist_item(new_item)
    return RedirectResponse(url="/wishlist", status_code=303)


# --- Photo Privacy ---

from pydantic import BaseModel

class PhotoPrivacyUpdate(BaseModel):
    hide_all_photos: bool
    hidden_photos: List[str]


@app.post("/api/memory/{memory_id}/photos_privacy")
async def update_photo_privacy(memory_id: int, update: PhotoPrivacyUpdate):
    await update_memory(memory_id, {
        "hide_all_photos": update.hide_all_photos,
        "hidden_photos": update.hidden_photos
    })
    return {"status": "success", "message": "Privacy settings updated"}


# --- Rate Date ---

@app.post("/rate_date/{memory_id}")
async def rate_date(
    memory_id: int,
    fun: int = Form(...),
    food: int = Form(...),
    vibe: int = Form(...),
    romance: int = Form(...),
    comment: str = Form("")
):
    from datetime import datetime
    await update_memory(memory_id, {
        "shaila_rating": {
            "fun": fun,
            "food": food,
            "vibe": vibe,
            "romance": romance,
            "comment": comment,
            "timestamp": datetime.now().strftime("%b %d, %Y")
        }
    })
    return RedirectResponse(url=f"/memory/{memory_id}", status_code=303)


# --- Comments ---

@app.post("/add_comment/{memory_id}")
async def add_comment(
    memory_id: int,
    name: str = Form(...),
    message: str = Form(...),
    color: str = Form("bg-blue-100")
):
    from datetime import datetime
    memory = await get_memory_by_id(memory_id)
    if memory:
        comments = memory.get("comments", [])
        comments.append({
            "name": name,
            "message": message,
            "date": datetime.now().strftime("%b %d, %Y"),
            "color": color
        })
        await update_memory(memory_id, {"comments": comments})
    return RedirectResponse(url=f"/memory/{memory_id}", status_code=303)


# --- Dictionary ---

@app.get("/dictionary", response_class=HTMLResponse)
async def read_dictionary(request: Request):
    words = await get_all_dictionary()
    words.sort(key=lambda x: x['word'].lower())
    settings = request.state.settings
    return templates.TemplateResponse("dictionary.html", {"request": request, "words": words, "settings": settings})


@app.post("/dictionary/add")
async def add_word(
    request: Request,
    word: str = Form(...),
    meaning: str = Form(...),
    context: str = Form(...),
    icon: str = Form("format_quote")
):
    from datetime import datetime
    words = await get_all_dictionary()
    new_word = {
        "id": len(words) + 1,
        "word": word,
        "meaning": meaning,
        "context": context,
        "date": datetime.now().strftime("%b %d, %Y"),
        "icon": icon
    }
    await add_dictionary_word(new_word)
    return RedirectResponse(url="/dictionary", status_code=303)
