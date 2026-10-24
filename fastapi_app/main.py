
from fastapi import FastAPI, Request, Form, UploadFile, File, HTTPException, WebSocket, WebSocketDisconnect, BackgroundTasks
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
import asyncio
import websockets
import base64
# --- Database & Storage imports ---
from fastapi_app.database import (
    get_db, get_all_memories, save_all_memories, update_memory, get_memory_by_id,
    get_next_memory_id, add_memory as db_add_memory, delete_memory,
    get_settings, save_settings,
    get_all_coupons, save_all_coupons, update_coupon, delete_coupon_item, add_coupon,
    get_all_guestbook, add_guestbook_entry, delete_guestbook_entry, update_guestbook_entry,
    get_all_vault,
    get_all_wishlist, add_wishlist_item, delete_wishlist_item, update_wishlist_item,
    get_all_dictionary, add_dictionary_word, save_all_dictionary, delete_dictionary_word, update_dictionary_word,
    get_all_roka_media, add_roka_media, update_roka_media, delete_roka_media,
    get_all_prewedding_media, add_prewedding_media, update_prewedding_media, delete_prewedding_media,
    get_all_ai_plans, save_ai_plan, get_ai_plan
)
from fastapi_app.storage import upload_file, get_photo_url, R2_PUBLIC_URL, get_s3_client, R2_BUCKET_NAME, delete_file
from PIL import Image

app = FastAPI()

# Get base directory of the current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Mount Static Files (still needed for CSS, JS, music, and other non-photo assets)
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Mount Local Photos directly for pristine full-resolution previews
PHOTOS_DIR = os.path.join(os.path.dirname(BASE_DIR), "Photos")
if os.path.exists(PHOTOS_DIR):
    app.mount("/local-photos", StaticFiles(directory=PHOTOS_DIR), name="local_photos")

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


def process_memories_for_display(memories: List[dict], settings: dict, always_include_hot: bool = False) -> List[dict]:
    """
    Processes memories for display:
    1. Filters out blocked memories (e.g. ID 1 in private mode)
    2. Swaps content with 'safe' versions if in private mode
    3. Redacts remaining content if in private mode
    """
    processed_memories = []
    is_private = settings.get("private_mode", False)
    is_birthday = settings.get("birthday_mode", False)

    for m in memories:
        if is_private and m["id"] == 1:
            continue
        
        # Hide 'hot' tagged memories globally unless birthday mode is active
        # (or caller explicitly wants them, e.g. timeline always shows them)
        if not is_birthday and not always_include_hot and m.get("type") == "hot":
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
    if "birthday_mode" in data:
        current_settings["birthday_mode"] = data["birthday_mode"]
    if "theme" in data:
        current_settings["theme"] = data["theme"]
    if "hero_images" in data:
        current_settings["hero_images"] = data["hero_images"]

    await save_settings(current_settings)
    return {"status": "success", "settings": current_settings}


@app.post("/api/hero-images/upload")
async def upload_hero_image(request: Request, file: UploadFile = File(...)):
    """Upload an image file to R2 under images/hero/ and add its URL to hero_images settings."""
    if request.cookies.get("session") != "admin_logged_in":
        return JSONResponse(status_code=401, content={"status": "error", "message": "Unauthorized"})

    import mimetypes
    content_type = file.content_type or mimetypes.guess_type(file.filename)[0] or "image/jpeg"

    # Build a unique key to avoid name collisions
    import time
    safe_name = file.filename.replace(" ", "_")
    key = f"images/hero/{int(time.time())}_{safe_name}"

    file_data = await file.read()
    file_obj = io.BytesIO(file_data)
    public_url = upload_file(file_obj, key, content_type)

    # Persist URL to settings
    current_settings = await get_settings()
    hero_images = current_settings.get("hero_images", [])
    hero_images.append(public_url)
    current_settings["hero_images"] = hero_images
    await save_settings(current_settings)

    return {"status": "success", "url": public_url, "hero_images": hero_images}


@app.delete("/api/hero-images")
async def delete_hero_image(request: Request):
    """Remove a URL from hero_images settings (and delete from R2 if managed)."""
    if request.cookies.get("session") != "admin_logged_in":
        return JSONResponse(status_code=401, content={"status": "error", "message": "Unauthorized"})

    from fastapi_app.storage import delete_file, R2_PUBLIC_URL as R2_BASE
    data = await request.json()
    url_to_remove = data.get("url", "")

    current_settings = await get_settings()
    hero_images = current_settings.get("hero_images", [])

    if url_to_remove in hero_images:
        hero_images.remove(url_to_remove)
        current_settings["hero_images"] = hero_images
        await save_settings(current_settings)

        # If this file lives under images/hero/ in R2, delete the actual file
        if url_to_remove.startswith(R2_BASE):
            key = url_to_remove[len(R2_BASE):].lstrip("/")
            if key.startswith("images/hero/"):
                try:
                    delete_file(key)
                except Exception:
                    pass  # Don't fail if the file is already gone

    return {"status": "success", "hero_images": hero_images}


# --- Public Routes ---

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    import random
    from fastapi_app.database import get_all_roka_media, get_all_memories
    from fastapi_app.highlights import build_memory_lane_highlights
    from fastapi_app.storage import R2_PUBLIC_URL
    settings = request.state.settings
    
    # Fetch highlights for Memory Lane
    all_memories = await get_all_memories()
    highlights = build_memory_lane_highlights(all_memories, R2_PUBLIC_URL)

    # Fetch all Roka media and pick 100 random photos from "Our Moments"
    all_roka = await get_all_roka_media()
    hidden_photos = ["roka/1775666737_SHAIX-9425.webp"]
    roka_photos = [m for m in all_roka if m.get("media_type") == "image" and m.get("chapter") == "Our Moments" and m.get("filename") not in hidden_photos]
    random.shuffle(roka_photos)
    
    old_photos = [
        {"filename": "images/favourites/IMG_7650.jpg"},
        {"filename": "images/favourites/IMG_7813.jpg"},
        {"filename": "images/favourites/IMG_7997.jpg"},
        {"filename": "images/favourites/IMG_8023 (1).jpg"},
        {"filename": "images/favourites/IMG_8895 (1).jpg"},
        {"filename": "images/favourites/IMG_8915.jpg"},
        {"filename": "images/favourites/IMG_9150.jpg"},
        {"filename": "images/favourites/IMG_9272.jpg"},
        {"filename": "images/favourites/IMG_9292.jpg"},
        {"filename": "images/favourites/IMG_9318.jpg"},
        {"filename": "images/favourites/IMG_9454.jpg"},
        {"filename": "images/favourites/IMG_9455.jpg"},
        {"filename": "images/favourites/IMG_9456.jpg"},
        {"filename": "images/favourites/IMG_9457.jpg"}
    ]
    
    # Pick 20 random curated moments to ensure lightning-fast page load
    carousel_photos = old_photos + roka_photos[:12]
    random.shuffle(carousel_photos)
    carousel_photos = carousel_photos[:20]
    
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "page": "home", 
        "settings": settings,
        "carousel_photos": carousel_photos,
        "highlights": highlights
    })


@app.get("/tv", response_class=HTMLResponse)
async def tv_experience(request: Request):
    """Ultra-lightweight 60fps Netflix-style TV interface optimized for Android TV / Chromecast."""
    import random
    from fastapi_app.database import get_all_roka_media, get_all_memories
    from fastapi_app.storage import R2_PUBLIC_URL
    settings = request.state.settings

    raw_memories = await get_all_memories()
    # Apply standard privacy mode filtering: hides ID 1 (Hinge), hot memories, and redacts safe titles
    filtered_memories = process_memories_for_display(raw_memories, settings)

    memories = []
    for m in filtered_memories:
        m_copy = dict(m)
        photos = m.get("photos") or []
        if photos and len(photos) > 0:
            m_copy["photo_url"] = f"{R2_PUBLIC_URL}/uploads/{m['id']}/{photos[0]}"
        else:
            m_copy["photo_url"] = f"{R2_PUBLIC_URL}/uploads/26/IMG_0930.webp"
        memories.append(m_copy)

    all_roka = await get_all_roka_media()
    roka_photos = []
    for r in all_roka:
        if r.get("media_type") == "image":
            r_copy = dict(r)
            filename = r.get("filename")
            r_copy["photo_url"] = f"{R2_PUBLIC_URL}/{filename}" if filename else ""
            roka_photos.append(r_copy)
    random.shuffle(roka_photos)

    hero = {
        "title": "The Start of Forever",
        "description": "Reliving all our most beautiful milestones, dates, laughter, and timeless memories.",
        "photo_url": memories[0]["photo_url"] if memories else "https://pub-5febf239be824301b333f51d2eaee417.r2.dev/prewedding/1792437927_DSC00890.webp"
    }

    return templates.TemplateResponse("tv.html", {
        "request": request,
        "page": "tv",
        "active_page": "home",
        "settings": settings,
        "memories": memories,
        "roka_photos": roka_photos[:30],
        "hero": hero
    })


# --- TV Suite Routes (/tv/...) ---

@app.get("/tv/memory/{memory_id}", response_class=HTMLResponse)
async def tv_memory_detail(request: Request, memory_id: int):
    """TV Cinema experience for an individual memory."""
    from fastapi_app.database import get_all_memories
    from fastapi_app.storage import R2_PUBLIC_URL
    settings = request.state.settings

    memories = await get_all_memories()
    processed_memories = process_memories_for_display(memories, settings, always_include_hot=True)
    memory = next((m for m in processed_memories if m["id"] == memory_id), None)

    if not memory:
        return RedirectResponse(url="/tv/timeline")

    mem_copy = dict(memory)
    # Format photos to full URLs
    full_photos = []
    for p in mem_copy.get("photos", []):
        if p.startswith("http://") or p.startswith("https://"):
            full_photos.append(p)
        else:
            full_photos.append(f"{R2_PUBLIC_URL}/uploads/{memory_id}/{p}")
    mem_copy["photos"] = full_photos

    return templates.TemplateResponse("tv_memory.html", {
        "request": request,
        "active_page": "timeline",
        "memory": mem_copy,
        "settings": settings
    })


@app.get("/tv/timeline", response_class=HTMLResponse)
async def tv_timeline(request: Request):
    """TV-optimized horizontal chronological timeline."""
    from fastapi_app.database import get_all_memories
    from fastapi_app.storage import R2_PUBLIC_URL
    settings = request.state.settings

    raw_memories = await get_all_memories()
    filtered_memories = process_memories_for_display(raw_memories, settings)

    memories = []
    for m in filtered_memories:
        m_copy = dict(m)
        photos = m.get("photos") or []
        if photos and len(photos) > 0:
            m_copy["photo_url"] = f"{R2_PUBLIC_URL}/uploads/{m['id']}/{photos[0]}"
        else:
            m_copy["photo_url"] = f"{R2_PUBLIC_URL}/uploads/26/IMG_0930.webp"
        memories.append(m_copy)

    return templates.TemplateResponse("tv_timeline.html", {
        "request": request,
        "active_page": "timeline",
        "settings": settings,
        "memories": memories
    })


@app.get("/tv/gallery", response_class=HTMLResponse)
async def tv_gallery(request: Request):
    """TV photo gallery grid."""
    from fastapi_app.storage import R2_PUBLIC_URL
    settings = request.state.settings
    gallery_items = await get_filtered_memories(settings)

    return templates.TemplateResponse("tv_gallery.html", {
        "request": request,
        "active_page": "gallery",
        "settings": settings,
        "items": gallery_items[:60],
        "r2_url": R2_PUBLIC_URL
    })


@app.get("/tv/birthday", response_class=HTMLResponse)
async def tv_birthday(request: Request):
    """TV Birthday special showcase."""
    from fastapi_app.database import get_all_memories
    from fastapi_app.storage import R2_PUBLIC_URL
    settings = request.state.settings

    memories = await get_all_memories()
    bday_mem = next((m for m in memories if m.get("id") == 25), None)
    photos = []
    if bday_mem and bday_mem.get("photos"):
        for p in bday_mem["photos"]:
            photos.append(f"{R2_PUBLIC_URL}/uploads/25/{p}")
    else:
        photos.append("https://pub-5febf239be824301b333f51d2eaee417.r2.dev/uploads/25/IMG_0389.webp")

    return templates.TemplateResponse("tv_birthday.html", {
        "request": request,
        "active_page": "birthday",
        "settings": settings,
        "photos": photos
    })


@app.get("/tv/events", response_class=HTMLResponse)
async def tv_events(request: Request):
    """TV Events & milestone cinema."""
    settings = request.state.settings
    return templates.TemplateResponse("tv_events.html", {
        "request": request,
        "active_page": "events",
        "settings": settings
    })


@app.get("/tv/wishlist", response_class=HTMLResponse)
async def tv_wishlist(request: Request):
    """TV Instagram & shared wishlist view."""
    from fastapi_app.database import get_all_wishlist
    settings = request.state.settings
    items = await get_all_wishlist()

    return templates.TemplateResponse("tv_wishlist.html", {
        "request": request,
        "active_page": "wishlist",
        "settings": settings,
        "items": items
    })


@app.get("/tv/guestbook", response_class=HTMLResponse)
async def tv_guestbook(request: Request):
    """TV Guestbook notes & wishes."""
    from fastapi_app.database import get_all_guestbook
    settings = request.state.settings
    notes = await get_all_guestbook()

    return templates.TemplateResponse("tv_guestbook.html", {
        "request": request,
        "active_page": "guestbook",
        "settings": settings,
        "notes": notes
    })


@app.get("/tv/music", response_class=HTMLResponse)
async def tv_music(request: Request):
    """TV Music streaming lounge."""
    settings = request.state.settings
    return templates.TemplateResponse("tv_music.html", {
        "request": request,
        "active_page": "music",
        "settings": settings
    })


@app.get("/tv/dictionary", response_class=HTMLResponse)
async def tv_dictionary(request: Request):
    """TV Puchki dictionary flashcards."""
    from fastapi_app.database import get_all_dictionary
    settings = request.state.settings
    words = await get_all_dictionary()

    return templates.TemplateResponse("tv_dictionary.html", {
        "request": request,
        "active_page": "dictionary",
        "settings": settings,
        "words": words
    })


@app.get("/tv/coupons", response_class=HTMLResponse)
async def tv_coupons(request: Request):
    """TV Romantic coupons redeem screen."""
    from fastapi_app.database import get_all_coupons
    settings = request.state.settings
    if settings.get("private_mode"):
        return RedirectResponse(url="/tv")

    coupons = await get_all_coupons()
    return templates.TemplateResponse("tv_coupons.html", {
        "request": request,
        "active_page": "coupons",
        "settings": settings,
        "coupons": coupons
    })


@app.get("/tv/planner", response_class=HTMLResponse)
async def tv_planner(request: Request):
    """TV Travel & date planner."""
    from fastapi_app.database import get_all_ai_plans
    settings = request.state.settings
    try:
        plans = await get_all_ai_plans()
    except Exception:
        plans = []

    return templates.TemplateResponse("tv_planner.html", {
        "request": request,
        "active_page": "planner",
        "settings": settings,
        "plans": plans
    })


@app.get("/honeymoon", response_class=HTMLResponse)
async def honeymoon_page(request: Request):
    from fastapi_app.database import get_honeymoon_data, save_honeymoon_data
    from fastapi_app.honeymoon_data import DEFAULT_HONEYMOON_DATA
    settings = request.state.settings

    data = await get_honeymoon_data()
    if not data:
        data = DEFAULT_HONEYMOON_DATA
        await save_honeymoon_data(data)

    return templates.TemplateResponse("honeymoon.html", {
        "request": request,
        "page": "honeymoon",
        "settings": settings,
        "honeymoon": data
    })


@app.get("/wedding", response_class=HTMLResponse)
@app.get("/sagan-wedding", response_class=HTMLResponse)
async def wedding_page(request: Request):
    from fastapi_app.wedding_data import WEDDING_DETAILS
    settings = request.state.settings

    return templates.TemplateResponse("wedding.html", {
        "request": request,
        "page": "wedding",
        "settings": settings,
        "wedding": WEDDING_DETAILS
    })


@app.post("/api/honeymoon/toggle-checklist")
async def toggle_honeymoon_checklist(request: Request):
    from fastapi_app.database import get_honeymoon_data, save_honeymoon_data
    from fastapi_app.honeymoon_data import DEFAULT_HONEYMOON_DATA
    body = await request.json()
    item_id = body.get("id")
    category = body.get("category", "visa") # visa or tickets

    data = await get_honeymoon_data()
    if not data:
        data = DEFAULT_HONEYMOON_DATA

    if category == "visa" and "visa" in data and "checklist" in data["visa"]:
        for item in data["visa"]["checklist"]:
            if item.get("id") == item_id:
                item["done"] = not item.get("done", False)
                break
    elif category == "tickets" and "klook_tickets" in data:
        for t in data["klook_tickets"]:
            if t.get("id") == item_id:
                t["booked"] = not t.get("booked", False)
                t["status"] = "Booked ✅" if t["booked"] else "To Book"
                break
    elif category == "packing" and "packing_and_outfits" in data and "packing_checklist" in data["packing_and_outfits"]:
        for p in data["packing_and_outfits"]["packing_checklist"]:
            if p.get("id") == item_id:
                p["packed"] = not p.get("packed", False)
                break

    await save_honeymoon_data(data)
    return {"status": "success", "data": data}


@app.post("/api/honeymoon/packing/save")
async def save_packing_item(request: Request):
    import uuid
    from fastapi_app.database import get_honeymoon_data, save_honeymoon_data
    from fastapi_app.honeymoon_data import DEFAULT_HONEYMOON_DATA
    body = await request.json()
    p_id = body.get("id")
    category = body.get("category", "General")
    item_name = body.get("item", "").strip()
    detail = body.get("detail", "")
    rule = body.get("rule", "")
    icon = body.get("icon", "check_circle")
    packed = bool(body.get("packed", False))

    data = await get_honeymoon_data()
    if not data:
        data = DEFAULT_HONEYMOON_DATA

    if "packing_and_outfits" not in data:
        data["packing_and_outfits"] = DEFAULT_HONEYMOON_DATA.get("packing_and_outfits", {})
    if "packing_checklist" not in data["packing_and_outfits"]:
        data["packing_and_outfits"]["packing_checklist"] = []

    checklist = data["packing_and_outfits"]["packing_checklist"]
    updated = False
    if p_id:
        for p in checklist:
            if p.get("id") == p_id:
                p["category"] = category
                p["item"] = item_name
                p["detail"] = detail
                p["rule"] = rule
                p["icon"] = icon
                p["packed"] = packed
                updated = True
                break

    if not updated:
        checklist.append({
            "id": p_id or f"p-{uuid.uuid4().hex[:8]}",
            "category": category,
            "item": item_name,
            "detail": detail,
            "rule": rule,
            "icon": icon,
            "packed": packed
        })

    await save_honeymoon_data(data)
    return {"status": "success", "checklist": checklist}


@app.delete("/api/honeymoon/packing/{p_id}")
async def delete_packing_item(p_id: str):
    from fastapi_app.database import get_honeymoon_data, save_honeymoon_data
    from fastapi_app.honeymoon_data import DEFAULT_HONEYMOON_DATA

    data = await get_honeymoon_data()
    if not data:
        data = DEFAULT_HONEYMOON_DATA

    if "packing_and_outfits" in data and "packing_checklist" in data["packing_and_outfits"]:
        data["packing_and_outfits"]["packing_checklist"] = [
            p for p in data["packing_and_outfits"]["packing_checklist"] if p.get("id") != p_id
        ]

    await save_honeymoon_data(data)
    return {"status": "success"}


@app.post("/api/honeymoon/visa/status")
async def update_visa_status(request: Request):
    from fastapi_app.database import get_honeymoon_data, save_honeymoon_data
    from fastapi_app.honeymoon_data import DEFAULT_HONEYMOON_DATA
    body = await request.json()
    status = body.get("status")
    application_ref = body.get("application_ref")
    agent_name = body.get("agent_name")
    approval_date = body.get("approval_date")
    notes = body.get("notes")

    data = await get_honeymoon_data()
    if not data:
        data = DEFAULT_HONEYMOON_DATA

    if "visa" not in data:
        data["visa"] = DEFAULT_HONEYMOON_DATA.get("visa", {})

    if status:
        data["visa"]["status"] = status
    if application_ref is not None:
        data["visa"]["application_ref"] = application_ref
    if agent_name is not None:
        data["visa"]["agent_name"] = agent_name
    if approval_date is not None:
        data["visa"]["approval_date"] = approval_date
    if notes is not None:
        data["visa"]["notes"] = notes

    await save_honeymoon_data(data)
    return {"status": "success", "visa": data["visa"]}


@app.post("/api/honeymoon/expense")
async def save_expense(request: Request):
    import uuid
    from fastapi_app.database import get_honeymoon_data, save_honeymoon_data
    from fastapi_app.honeymoon_data import DEFAULT_HONEYMOON_DATA
    body = await request.json()
    
    exp_id = body.get("id")
    item = body.get("item", "").strip()
    category = body.get("category", "General")
    estimated = float(body.get("amount") or body.get("estimated_amount") or 0)
    actual = float(body.get("actual_amount") or 0)
    status = body.get("status", "Estimated")
    notes = body.get("notes", "")
    booking_link = body.get("booking_link", "").strip()

    data = await get_honeymoon_data()
    if not data:
        data = DEFAULT_HONEYMOON_DATA

    if "expenses" not in data:
        data["expenses"] = []

    # Update if exp_id exists, else add
    updated = False
    if exp_id:
        for exp in data["expenses"]:
            if exp.get("id") == exp_id:
                if item: exp["item"] = item
                if "category" in body: exp["category"] = category
                if "amount" in body or "estimated_amount" in body: exp["amount"] = estimated
                if "actual_amount" in body: exp["actual_amount"] = actual
                if "status" in body: exp["status"] = status
                if "notes" in body: exp["notes"] = notes
                if "booking_link" in body: exp["booking_link"] = booking_link
                updated = True
                break
    
    if not updated:
        data["expenses"].append({
            "id": exp_id or f"exp-{uuid.uuid4().hex[:8]}",
            "item": item,
            "category": category,
            "amount": estimated,
            "actual_amount": actual,
            "status": status,
            "currency": "INR",
            "notes": notes,
            "booking_link": booking_link
        })

    await save_honeymoon_data(data)
    return {"status": "success", "expenses": data["expenses"]}


@app.delete("/api/honeymoon/expense/{exp_id}")
async def delete_expense(exp_id: str):
    from fastapi_app.database import get_honeymoon_data, save_honeymoon_data
    from fastapi_app.honeymoon_data import DEFAULT_HONEYMOON_DATA

    data = await get_honeymoon_data()
    if not data:
        data = DEFAULT_HONEYMOON_DATA

    if "expenses" in data:
        data["expenses"] = [e for e in data["expenses"] if e.get("id") != exp_id]

    await save_honeymoon_data(data)
    return {"status": "success", "expenses": data.get("expenses", [])}


@app.post("/api/honeymoon/ticket/update")
async def update_ticket(request: Request):
    from fastapi_app.database import get_honeymoon_data, save_honeymoon_data
    from fastapi_app.honeymoon_data import DEFAULT_HONEYMOON_DATA
    body = await request.json()
    ticket_id = body.get("id")
    status = body.get("status")
    actual_cost = body.get("actual_cost")
    booked = body.get("booked")
    link = body.get("link")

    data = await get_honeymoon_data()
    if not data:
        data = DEFAULT_HONEYMOON_DATA

    if "klook_tickets" in data:
        for t in data["klook_tickets"]:
            if t.get("id") == ticket_id:
                if status is not None:
                    t["status"] = status
                if booked is not None:
                    t["booked"] = bool(booked)
                if actual_cost is not None:
                    t["actual_cost"] = actual_cost
                if link is not None:
                    t["link"] = link.strip()
                break

    await save_honeymoon_data(data)
    return {"status": "success", "tickets": data.get("klook_tickets", [])}


@app.post("/api/honeymoon/dining/save")
async def save_dining_place(request: Request):
    import uuid
    from fastapi_app.database import get_honeymoon_data, save_honeymoon_data
    from fastapi_app.honeymoon_data import DEFAULT_HONEYMOON_DATA
    body = await request.json()
    
    d_id = body.get("id")
    name = body.get("name", "").strip()
    area = body.get("area", "")
    cuisine = body.get("cuisine", "")
    highlight = body.get("highlight", "")
    status = body.get("status", "Shortlisted")
    day_num = body.get("day_number")
    day_number = int(day_num) if day_num and str(day_num).isdigit() else None

    data = await get_honeymoon_data()
    if not data:
        data = DEFAULT_HONEYMOON_DATA

    if "dining_places" not in data:
        data["dining_places"] = []

    updated = False
    if d_id:
        for d in data["dining_places"]:
            if d.get("id") == d_id:
                d["name"] = name
                d["area"] = area
                d["cuisine"] = cuisine
                d["highlight"] = highlight
                d["status"] = status
                d["day_number"] = day_number
                updated = True
                break

    if not updated:
        data["dining_places"].append({
            "id": d_id or f"d-{uuid.uuid4().hex[:8]}",
            "name": name,
            "area": area,
            "cuisine": cuisine,
            "highlight": highlight,
            "status": status,
            "day_number": day_number
        })

    await save_honeymoon_data(data)
    return {"status": "success", "dining_places": data["dining_places"]}


@app.post("/api/honeymoon/outfit/save")
async def save_outfit(request: Request):
    import uuid
    from fastapi_app.database import get_honeymoon_data, save_honeymoon_data
    from fastapi_app.honeymoon_data import DEFAULT_HONEYMOON_DATA
    body = await request.json()
    
    o_id = body.get("id")
    day = int(body.get("day") or 1)
    date_str = body.get("date", "")
    time_slot = body.get("time_slot", "Daytime")
    occasion = body.get("occasion", "Sightseeing")
    style_notes = body.get("style_notes", "")
    
    shaila_data = body.get("shaila", {})
    shaiwal_data = body.get("shaiwal", {})

    data = await get_honeymoon_data()
    if not data:
        data = DEFAULT_HONEYMOON_DATA

    if "packing_and_outfits" not in data:
        data["packing_and_outfits"] = DEFAULT_HONEYMOON_DATA.get("packing_and_outfits", {})
    
    if "daily_outfit_planner" not in data["packing_and_outfits"]:
        data["packing_and_outfits"]["daily_outfit_planner"] = []

    outfits = data["packing_and_outfits"]["daily_outfit_planner"]
    updated = False
    if o_id:
        for item in outfits:
            if item.get("id") == o_id:
                item["day"] = day
                item["date"] = date_str
                item["time_slot"] = time_slot
                item["occasion"] = occasion
                item["style_notes"] = style_notes
                item["shaila"] = shaila_data
                item["shaiwal"] = shaiwal_data
                updated = True
                break

    if not updated:
        new_entry = {
            "id": o_id or f"outfit-{uuid.uuid4().hex[:8]}",
            "day": day,
            "date": date_str,
            "time_slot": time_slot,
            "occasion": occasion,
            "style_notes": style_notes,
            "shaila": shaila_data,
            "shaiwal": shaiwal_data
        }
        outfits.append(new_entry)

    # Sort outfits by day
    outfits.sort(key=lambda x: x.get("day", 1))

    await save_honeymoon_data(data)
    return {"status": "success", "daily_outfits": outfits}


@app.post("/api/honeymoon/todo/save")
async def save_honeymoon_todo(request: Request):
    import uuid
    from fastapi_app.database import get_honeymoon_data, save_honeymoon_data
    from fastapi_app.honeymoon_data import DEFAULT_HONEYMOON_DATA
    body = await request.json()

    todo_id = body.get("id")
    title = body.get("title", "").strip()
    category = body.get("category", "General").strip()
    link = body.get("link", "").strip()
    notes = body.get("notes", "").strip()
    due_date = body.get("due_date", "").strip()
    status = body.get("status", "Pending").strip()

    data = await get_honeymoon_data()
    if not data:
        data = DEFAULT_HONEYMOON_DATA

    if "things_to_do" not in data:
        data["things_to_do"] = []

    todos = data["things_to_do"]
    updated = False
    if todo_id:
        for t in todos:
            if t.get("id") == todo_id:
                if title: t["title"] = title
                if "category" in body: t["category"] = category
                if "link" in body: t["link"] = link
                if "notes" in body: t["notes"] = notes
                if "due_date" in body: t["due_date"] = due_date
                if "status" in body: t["status"] = status
                updated = True
                break

    if not updated and title:
        todos.append({
            "id": f"todo-{uuid.uuid4().hex[:8]}",
            "title": title,
            "category": category,
            "link": link,
            "notes": notes,
            "due_date": due_date,
            "status": status
        })

    await save_honeymoon_data(data)
    return {"status": "success", "things_to_do": todos}


@app.post("/api/honeymoon/todo/toggle")
async def toggle_honeymoon_todo(request: Request):
    from fastapi_app.database import get_honeymoon_data, save_honeymoon_data
    from fastapi_app.honeymoon_data import DEFAULT_HONEYMOON_DATA
    body = await request.json()
    todo_id = body.get("id")
    new_status = body.get("status")

    data = await get_honeymoon_data()
    if not data:
        data = DEFAULT_HONEYMOON_DATA

    todos = data.get("things_to_do", [])
    for t in todos:
        if t.get("id") == todo_id:
            if new_status:
                t["status"] = new_status
            else:
                t["status"] = "Completed ✅" if t.get("status") != "Completed ✅" else "Pending"
            break

    await save_honeymoon_data(data)
    return {"status": "success", "things_to_do": todos}


@app.delete("/api/honeymoon/todo/{todo_id}")
async def delete_honeymoon_todo(todo_id: str):
    from fastapi_app.database import get_honeymoon_data, save_honeymoon_data
    from fastapi_app.honeymoon_data import DEFAULT_HONEYMOON_DATA

    data = await get_honeymoon_data()
    if not data:
        data = DEFAULT_HONEYMOON_DATA

    if "things_to_do" in data:
        data["things_to_do"] = [t for t in data["things_to_do"] if t.get("id") != todo_id]

    await save_honeymoon_data(data)
    return {"status": "success", "things_to_do": data.get("things_to_do", [])}


@app.post("/api/honeymoon/outfit/photo/upload")
async def upload_outfit_photo(
    file: UploadFile = File(...),
    outfit_id: str = Form(...),
    person: str = Form("shaila") # "shaila" or "shaiwal"
):
    import io
    import uuid
    from fastapi_app.storage import upload_file
    from fastapi_app.database import get_honeymoon_data, save_honeymoon_data
    from fastapi_app.honeymoon_data import DEFAULT_HONEYMOON_DATA

    try:
        file_bytes = await file.read()
        orig_filename = file.filename or "outfit.jpg"
        clean_ext = orig_filename.split(".")[-1].lower() if "." in orig_filename else "jpg"
        r2_key = f"honeymoon/outfits/{outfit_id}_{person}_{uuid.uuid4().hex[:6]}.{clean_ext}"
        
        public_url = upload_file(io.BytesIO(file_bytes), r2_key, file.content_type or "image/jpeg")

        data = await get_honeymoon_data()
        if not data:
            data = DEFAULT_HONEYMOON_DATA

        if "packing_and_outfits" in data and "daily_outfit_planner" in data["packing_and_outfits"]:
            for item in data["packing_and_outfits"]["daily_outfit_planner"]:
                if item.get("id") == outfit_id:
                    if person in item:
                        item[person]["photo_url"] = public_url
                    break

        await save_honeymoon_data(data)
        return {"status": "success", "photo_url": public_url, "outfit_id": outfit_id, "person": person}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.delete("/api/honeymoon/outfit/{o_id}")
async def delete_outfit(o_id: str):
    from fastapi_app.database import get_honeymoon_data, save_honeymoon_data
    from fastapi_app.honeymoon_data import DEFAULT_HONEYMOON_DATA

    data = await get_honeymoon_data()
    if not data:
        data = DEFAULT_HONEYMOON_DATA

    if "packing_and_outfits" in data and "daily_outfit_planner" in data["packing_and_outfits"]:
        data["packing_and_outfits"]["daily_outfit_planner"] = [
            o for o in data["packing_and_outfits"]["daily_outfit_planner"] if o.get("id") != o_id
        ]

    await save_honeymoon_data(data)
    return {"status": "success"}


@app.delete("/api/honeymoon/dining/{d_id}")
async def delete_dining_place(d_id: str):
    from fastapi_app.database import get_honeymoon_data, save_honeymoon_data
    from fastapi_app.honeymoon_data import DEFAULT_HONEYMOON_DATA

    data = await get_honeymoon_data()
    if not data:
        data = DEFAULT_HONEYMOON_DATA

    if "dining_places" in data:
        data["dining_places"] = [d for d in data["dining_places"] if d.get("id") != d_id]

    await save_honeymoon_data(data)
    return {"status": "success", "dining_places": data.get("dining_places", [])}


@app.post("/api/honeymoon/ai-adjust")
async def ai_adjust_itinerary(request: Request):
    import os
    import json
    from google import genai
    from google.genai import types
    from dotenv import load_dotenv
    from fastapi_app.database import get_honeymoon_data, save_honeymoon_data
    from fastapi_app.honeymoon_data import DEFAULT_HONEYMOON_DATA

    load_dotenv()
    body = await request.json()
    user_prompt = body.get("prompt", "").strip()
    selected_day = body.get("day") # optional day number (1-9)

    if not user_prompt:
        return {"status": "error", "message": "Please provide your request or choice for the day."}

    data = await get_honeymoon_data()
    if not data:
        data = DEFAULT_HONEYMOON_DATA

    api_key = os.getenv("GEMINI_API_KEY", "")
    if not api_key:
        return {"status": "error", "message": "Gemini API key is not configured."}

    # Context about the trip
    current_days = data.get("days", [])
    
    system_instruction = (
        "You are an expert Singapore & Disney Cruise honeymoon planner AI agent. "
        "The user is currently on or planning their honeymoon (Dec 13-21, 2026 for Shaiwal & Shaila). "
        "They have made a choice or want to adjust their schedule (e.g., 'We went to Sentosa beach in morning and want Italian lunch now', "
        "'It is raining today, change afternoon plan', 'We want to skip River Wonders and go to Chinatown instead', "
        "'Adjust Day 5 schedule to include Trapizza for dinner'). "
        "Your task is to smartly update the specific day's schedule items, time slots, and curated options while preserving the overall trip flow and romantic Disney/Singapore honeymoon vibe. "
        "Return a JSON object containing: "
        "1. 'summary': A warm, concise explanation of the adjustments made for the couple. "
        "2. 'updated_day': The complete updated Day object with keys: 'day' (integer), 'date' (string), 'title' (string), 'location' (string), 'schedule' (array of {time, title, desc, icon}), 'options' (array of {title, desc}). "
        "3. 'suggested_expense': (optional object with {item, amount, category, status} if the adjustment involves a new cost, e.g. taxi or dining)."
    )

    user_message = (
        f"Trip Context: Singapore & Disney Cruise Honeymoon (Dec 13-21, 2026).\n"
        f"Target Day: Day {selected_day if selected_day else 'Appropriate day based on context'}\n"
        f"User Choice / Real-time Update: \"{user_prompt}\"\n\n"
        f"Current Days Itinerary Snapshot:\n{json.dumps(current_days, indent=2)}\n\n"
        f"Please update the schedule seamlessly and respond strictly in valid JSON matching the schema."
    )

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_message,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                response_mime_type="application/json",
                temperature=0.4,
            ),
        )
        ai_result = json.loads(response.text)
        
        # Merge updated day into honeymoon data
        updated_day = ai_result.get("updated_day")
        if updated_day and "day" in updated_day:
            day_num = updated_day["day"]
            for idx, d in enumerate(data.get("days", [])):
                if d.get("day") == day_num:
                    data["days"][idx] = updated_day
                    break
            
            # Optionally add suggested expense
            suggested_exp = ai_result.get("suggested_expense")
            if suggested_exp and isinstance(suggested_exp, dict) and suggested_exp.get("item"):
                import uuid
                data.setdefault("expenses", []).append({
                    "id": f"exp-{uuid.uuid4().hex[:8]}",
                    "item": suggested_exp.get("item"),
                    "amount": float(suggested_exp.get("amount", 0)),
                    "actual_amount": float(suggested_exp.get("actual_amount", 0)),
                    "category": suggested_exp.get("category", "General"),
                    "status": suggested_exp.get("status", "Logged"),
                    "currency": "INR",
                    "notes": "Added via AI Itinerary Adjustment"
                })

            await save_honeymoon_data(data)

        return {
            "status": "success",
            "summary": ai_result.get("summary", "Itinerary updated successfully!"),
            "updated_day": updated_day,
            "days": data.get("days", [])
        }

    except Exception as e:
        return {"status": "error", "message": f"AI Agent error: {str(e)}"}


@app.post("/api/honeymoon/document/upload")
async def upload_honeymoon_document(
    file: UploadFile = File(...),
    name: str = Form(""),
    category: str = Form("General"),
    expense_id: str = Form(""),
    visa_item_id: str = Form("")
):
    import uuid
    from datetime import datetime
    from fastapi_app.storage import upload_file
    from fastapi_app.database import get_honeymoon_data, save_honeymoon_data
    from fastapi_app.honeymoon_data import DEFAULT_HONEYMOON_DATA

    try:
        # Generate safe filename and R2 key
        file_bytes = await file.read()
        file_size_kb = len(file_bytes) / 1024
        size_str = f"{file_size_kb:.1f} KB" if file_size_kb < 1024 else f"{(file_size_kb/1024):.1f} MB"
        
        orig_filename = file.filename or "document.pdf"
        clean_name = name.strip() or orig_filename
        extension = orig_filename.split(".")[-1].lower() if "." in orig_filename else "pdf"
        
        doc_id = f"doc-{uuid.uuid4().hex[:8]}"
        r2_key = f"honeymoon/docs/{doc_id}_{orig_filename.replace(' ', '_')}"
        
        import io
        public_url = upload_file(io.BytesIO(file_bytes), r2_key, file.content_type or "application/pdf")

        # Save to MongoDB
        data = await get_honeymoon_data()
        if not data:
            data = DEFAULT_HONEYMOON_DATA

        if "documents" not in data:
            data["documents"] = []

        new_doc = {
            "id": doc_id,
            "name": clean_name,
            "category": category,
            "filename": orig_filename,
            "url": public_url,
            "key": r2_key,
            "size": size_str,
            "expense_id": expense_id or None,
            "visa_item_id": visa_item_id or None,
            "uploaded_at": datetime.now().strftime("%d %b %Y, %I:%M %p")
        }
        data["documents"].append(new_doc)

        # If expense_id provided, attach document link directly to that expense
        if expense_id and "expenses" in data:
            for exp in data["expenses"]:
                if exp.get("id") == expense_id:
                    exp["doc_url"] = public_url
                    exp["doc_name"] = clean_name
                    exp["doc_id"] = doc_id
                    break

        # If visa_item_id provided, attach document link to that visa checklist item and mark as done
        if visa_item_id and "visa" in data and "checklist" in data["visa"]:
            for v_item in data["visa"]["checklist"]:
                if v_item.get("id") == visa_item_id:
                    v_item["doc_url"] = public_url
                    v_item["doc_name"] = clean_name
                    v_item["done"] = True
                    break

        await save_honeymoon_data(data)

        return {"status": "success", "document": new_doc, "documents": data["documents"], "expenses": data.get("expenses", [])}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.delete("/api/honeymoon/document/{doc_id}")
async def delete_honeymoon_document(doc_id: str):
    from fastapi_app.storage import delete_file
    from fastapi_app.database import get_honeymoon_data, save_honeymoon_data
    from fastapi_app.honeymoon_data import DEFAULT_HONEYMOON_DATA

    data = await get_honeymoon_data()
    if not data:
        data = DEFAULT_HONEYMOON_DATA

    docs = data.get("documents", [])
    target = next((d for d in docs if d.get("id") == doc_id), None)
    if target:
        # Delete from R2 if key is stored
        if "key" in target:
            try:
                delete_file(target["key"])
            except Exception:
                pass
        data["documents"] = [d for d in docs if d.get("id") != doc_id]
        await save_honeymoon_data(data)

    return {"status": "success", "documents": data.get("documents", [])}



@app.get("/birthday", response_class=HTMLResponse)
async def birthday(request: Request):
    settings = request.state.settings
    memories = await get_all_memories()
    
    # Optional logic to pick "hot" tagged memories to pass to the template
    hot_memories = [m for m in memories if m.get("type") == "hot"]
    
    return templates.TemplateResponse("birthday.html", {
        "request": request, 
        "page": "birthday", 
        "settings": settings,
        "hot_memories": hot_memories
    })


@app.get("/timeline", response_class=HTMLResponse)
async def timeline(request: Request):
    memories = await get_all_memories()
    settings = request.state.settings
    visible_memories = process_memories_for_display(memories, settings, always_include_hot=True)
    # Filter out memories specifically hidden from timeline
    visible_memories = [m for m in visible_memories if not m.get("hide_timeline")]

    # Build category pills (mirrors gallery logic)
    EMOJI_MAP = {
        "date": "🍕", "dinner": "🍝", "milestone": "💍", "trip": "✈️",
        "food": "🍜", "movie": "🎬", "shopping": "🛍️", "family": "👨‍👩‍👧",
        "art": "🎨", "celebration": "🎉", "hot": "❤️",
    }
    DISPLAY_NAME_MAP = {"hot": "Beautiful"}
    type_set = set(m.get("type", "") for m in visible_memories if m.get("type"))
    categories = [{"value": t, "label": f"{EMOJI_MAP.get(t, '')} {DISPLAY_NAME_MAP.get(t, t.title())}"} for t in sorted(type_set)]

    return templates.TemplateResponse("timeline.html", {
        "request": request,
        "memories": visible_memories,
        "categories": categories,
        "page": "timeline",
        "settings": settings
    })


@app.get("/memory/{memory_id}", response_class=HTMLResponse)
async def memory_detail(request: Request, memory_id: int):
    memories = await get_all_memories()
    settings = request.state.settings
    processed_memories = process_memories_for_display(memories, settings, always_include_hot=True)
    memory = next((m for m in processed_memories if m["id"] == memory_id), None)

    if not memory:
        return RedirectResponse(url="/timeline")

    template_name = memory.get("template", "memory.html")
    return templates.TemplateResponse(template_name, {"request": request, "memory": memory, "settings": settings})


# --- Gallery ---

async def get_filtered_memories(settings, seed=None):
    memories = await get_all_memories()
    processed_memories = process_memories_for_display(memories, settings)

    VIDEO_EXTS = {'.mov', '.mp4', '.avi', '.mkv', '.webm'}
    gallery_items = []
    for m in processed_memories:
        if m.get("photos"):
            for p in m["photos"]:
                # Skip video files — gallery only shows images
                if any(p.lower().endswith(ext) for ext in VIDEO_EXTS):
                    continue
                gallery_items.append({
                    "id": m["id"],
                    "title": redact_text(m.get("title", ""), settings.get("private_mode")),
                    "date": m.get("date", ""),
                    "type": m.get("type", ""),
                    "photo": p,
                    "is_favorite": m.get("is_favorite", False)
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
    memories = await get_all_memories()
    all_items = await get_filtered_memories(settings, seed=seed)

    # Block hidden categories
    # 'start' hidden when private mode is on; 'hot' hidden when birthday mode is off
    if settings.get("private_mode") and category == "start":
        from starlette.responses import RedirectResponse
        return RedirectResponse(url="/gallery?category=all&page=1", status_code=302)
    if not settings.get("birthday_mode") and category == "hot":
        from starlette.responses import RedirectResponse
        return RedirectResponse(url="/gallery?category=all&page=1", status_code=302)

    if category != "all":
        if category == "favorite":
            all_items = [item for item in all_items if item.get("is_favorite")]
        else:
            all_items = [item for item in all_items if item["type"] == category]
    elif not settings.get("birthday_mode"):
        # When viewing 'all' and birthday mode is off, exclude hot items
        all_items = [item for item in all_items if item.get("type") != "hot"]

    total_items = len(all_items)
    start = (page - 1) * limit
    end = start + limit
    paginated_items = all_items[start:end]
    has_more = end < total_items

    # Build dynamic category filters
    EMOJI_MAP = {
        "date": "🍕", "dinner": "🍝", "milestone": "💍", "trip": "✈️",
        "food": "🍜", "movie": "🎬", "shopping": "🛍️", "family": "👨‍👩‍👧",
        "art": "🎨", "celebration": "🎉", "hot": "❤️",
    }
    DISPLAY_NAME_MAP = {"hot": "Beautiful"}
    PRIVATE_HIDDEN_CATEGORIES = {"start"}
    type_set = set()
    for m in memories:
        if m.get("type"):
            type_set.add(m["type"])
    categories = [{"value": "favorite", "label": "Favorites ❤️"}]
    for t in sorted(type_set):
        # Hide 'start' in private mode
        if settings.get("private_mode") and t in PRIVATE_HIDDEN_CATEGORIES:
            continue
        # Hide 'hot' when birthday mode is off
        if t == "hot" and not settings.get("birthday_mode"):
            continue
        categories.append({"value": t, "label": f"{DISPLAY_NAME_MAP.get(t, t.title())} {EMOJI_MAP.get(t, '')}"})
    return templates.TemplateResponse("gallery.html", {
        "request": request,
        "items": paginated_items,
        "page": page,
        "limit": limit,
        "seed": seed,
        "category": category,
        "has_more": has_more,
        "settings": settings,
        "categories": categories
    })


@app.get("/api/memories")
async def get_memories_api(request: Request, page: int = 1, limit: int = 12, seed: int = None, category: str = "all"):
    settings = request.state.settings
    all_items = await get_filtered_memories(settings, seed=seed)

    if category != "all":
        if category == "favorite":
            all_items = [item for item in all_items if item.get("is_favorite")]
        else:
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

@app.get("/api/admin/chat-logs")
async def get_admin_chat_logs(request: Request):
    if request.cookies.get("session") != "admin_logged_in":
        raise HTTPException(status_code=403, detail="Unauthorized")
    from fastapi_app.database import get_all_chat_logs
    return await get_all_chat_logs()

# --- Agent Copilot ---

@app.post("/api/agent/chat")
async def agent_chat(request: Request):
    from fastapi_app.agent import chat_with_agent
    from fastapi_app.database import log_chat_interaction
    data = await request.json()
    
    messages = data.get("messages", [])
    if not messages and "message" in data:
        messages = [{"role": "user", "content": data.get("message")}]
        
    if not messages:
        return {"text": "Please say something!", "cards": []}
    
    latest_user_message = messages[-1].get("content", "") if messages else ""
    
    response = await chat_with_agent(messages)
    
    # Log to MongoDB
    await log_chat_interaction(latest_user_message, response, messages)
    
    return response


# --- DJ Kiara Personal DJ Assistant ---
@app.post("/api/dj/chat")
async def dj_chat(request: Request):
    from fastapi_app.dj_agent import chat_with_dj
    data = await request.json()
    
    messages = data.get("messages", [])
    if not messages and "message" in data:
        messages = [{"role": "user", "content": data.get("message")}]
        
    if not messages:
        return {"text": "Tell me what vibe or song you want to hear!", "song": None}
    
    response = await chat_with_dj(messages)
    return response


@app.get("/story", response_class=HTMLResponse)
async def read_story(request: Request):
    from fastapi_app.database import get_story_data
    settings = request.state.settings
    story_data = await get_story_data()
    return templates.TemplateResponse("story.html", {"request": request, "settings": settings, "story_data": story_data})


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

@app.get("/api/admin/coupons")
async def get_admin_coupons(request: Request):
    if request.cookies.get("session") != "admin_logged_in":
        raise HTTPException(status_code=403, detail="Unauthorized")
    coupons = await get_all_coupons()
    for c in coupons:
        if '_id' in c:
            c['_id'] = str(c['_id'])
    return coupons


@app.get("/upcoming", response_class=HTMLResponse)
@app.get("/events", response_class=HTMLResponse)
async def read_upcoming(request: Request):
    settings = request.state.settings
    return templates.TemplateResponse("upcoming.html", {"request": request, "settings": settings, "page": "events"})


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
    background_tasks: BackgroundTasks,
    date: str = Form(...),
    title: str = Form(...),
    description: str = Form(...),
    type: str = Form(...),
    template: str = Form("memory.html"),
    title_safe: str = Form(None),
    description_safe: str = Form(None),
    timeline_note: str = Form(None),
    thumbnail_index: int = Form(0),
    smart_data: str = Form(None),
    hide_all_photos: str = Form("false"),
    days_journey: str = Form(None),
    photos: List[UploadFile] = File(None)
):
    if request.cookies.get("session") != "admin_logged_in":
        return RedirectResponse(url="/login")

    new_id = await get_next_memory_id()

    # Format date from YYYY-MM-DD to "Month DD, YYYY"
    from datetime import datetime as dt
    try:
        parsed_date = dt.strptime(date, "%Y-%m-%d")
        date = parsed_date.strftime("%B %d, %Y")
    except ValueError:
        pass  # Keep original if already in text format

    # Upload photos/videos to R2 (with file format validation + parallel upload)
    ALLOWED_TYPES = {"image/jpeg", "image/png", "image/gif", "image/webp", "image/heic",
                     "video/mp4", "video/quicktime", "video/mov"}
    photo_filenames = []
    upload_tasks = []  # (r2_key, content_bytes, content_type)

    if photos:
        for photo in photos:
            if photo.filename and photo.size > 0:
                if photo.content_type and photo.content_type.split(";")[0].strip() not in ALLOWED_TYPES:
                    raise HTTPException(status_code=400, detail=f"Invalid file type: {photo.filename} ({photo.content_type}). Only images and videos are allowed.")
                content = await photo.read()
                filename = photo.filename
                content_type = photo.content_type or ""

                # Auto-optimize: images → WebP 85%/1440px, videos → H.264 MP4 1080p
                try:
                    from fastapi_app.media_optimizer import optimize_file_bytes
                    content, filename, content_type = optimize_file_bytes(content, filename)
                except Exception as e:
                    print(f"Media optimization failed for {filename}: {e}")
                    # Fall back: at minimum convert HEIC → JPEG so browsers can show it
                    if filename.lower().endswith(('.heic', '.heif')):
                        try:
                            from PIL import Image
                            from pillow_heif import register_heif_opener
                            register_heif_opener()
                            img = Image.open(io.BytesIO(content))
                            buf = io.BytesIO()
                            img.convert("RGB").save(buf, format="JPEG", quality=90)
                            content = buf.getvalue()
                            filename = os.path.splitext(filename)[0] + ".jpg"
                            content_type = "image/jpeg"
                        except Exception as e2:
                            print(f"HEIC fallback also failed for {filename}: {e2}")

                r2_key = f"uploads/{new_id}/{filename}"
                upload_tasks.append((r2_key, content, content_type))
                photo_filenames.append(filename)

    # Parallel upload using threads (4 concurrent uploads)
    if upload_tasks:
        import concurrent.futures
        def _upload(args):
            key, data, ct = args
            upload_file(io.BytesIO(data), key, ct)
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            executor.map(_upload, upload_tasks)

    new_memory = {
        "id": new_id,
        "date": date,
        "title": title,
        "description": description,
        "type": type,
        "template": template,
        "photos": photo_filenames,
        "comments": [],
        "hide_all_photos": hide_all_photos.lower() == "true",
        "hidden_photos": [],
        "days_journey": days_journey,
    }

    # Optional safe versions
    if title_safe:
        new_memory["title_safe"] = title_safe
    if description_safe:
        new_memory["description_safe"] = description_safe
    if timeline_note:
        new_memory["timeline_note"] = timeline_note

    # Reorder photos so thumbnail is first (timeline uses first photo)
    if thumbnail_index > 0 and thumbnail_index < len(photo_filenames):
        thumb = photo_filenames.pop(thumbnail_index)
        photo_filenames.insert(0, thumb)
        new_memory["photos"] = photo_filenames

    # Smart data (JSON string from frontend)
    if smart_data:
        try:
            new_memory["smart_data"] = json.loads(smart_data)
        except json.JSONDecodeError:
            pass

    await db_add_memory(new_memory)
    from fastapi_app.agent import generate_dynamic_storyline
    background_tasks.add_task(generate_dynamic_storyline)
    return RedirectResponse(url=f"/memory/{new_id}", status_code=303)


# --- Music ---

@app.get("/music", response_class=HTMLResponse)
async def read_music(request: Request):
    from fastapi_app.database import get_music_data
    music_data = await get_music_data()
    settings = request.state.settings
    return templates.TemplateResponse("music.html", {
        "request": request,
        "settings": settings,
        "music_data": music_data,
        "page": "music"
    })


@app.get("/api/music/sections")
async def get_music_sections_api():
    from fastapi_app.database import get_music_data
    music_data = await get_music_data()
    return music_data or {"sections": []}


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
    media = await get_all_roka_media()
    
    hero_media = None
    first_video = None
    chapters_map = {}
    for item in media:
        if item.get("media_type") == "video":
            if not first_video:
                first_video = item
            if "roka" in item.get("filename", "").lower():
                hero_media = item
                
        ch = item.get("chapter", "Other")
        if ch not in chapters_map:
            chapters_map[ch] = []
        chapters_map[ch].append(item)
        
    if not hero_media:
        hero_media = first_video
        
    settings = request.state.settings
    return templates.TemplateResponse("memory_roka.html", {
        "request": request, 
        "hero_media": hero_media,
        "chapters_map": chapters_map, 
        "settings": settings
    })

# --- Roka Admin Creator ---

@app.get("/admin/roka-creator", response_class=HTMLResponse)
async def roka_creator(request: Request):
    if request.cookies.get("session") != "admin_logged_in":
        return RedirectResponse(url="/login?next=/admin/roka-creator")
    settings = request.state.settings
    media = await get_all_roka_media()
    return templates.TemplateResponse("admin_roka.html", {"request": request, "settings": settings, "media": media})

@app.post("/admin/roka-media/upload")
async def upload_roka_media(
    request: Request,
    chapter: str = Form("The Venue"),
    note: str = Form(""),
    files: List[UploadFile] = File(...)
):
    if request.cookies.get("session") != "admin_logged_in":
        return JSONResponse(status_code=401, content={"status": "error", "message": "Unauthorized"})

    import time
    from fastapi_app.media_optimizer import optimize_file_bytes
    import io
    import uuid

    upload_tasks = []
    
    # Pre-process files
    for file in files:
        if file.filename and file.size > 0:
            content = await file.read()
            filename = file.filename
            content_type = file.content_type or ""

            try:
                content, filename, content_type = optimize_file_bytes(content, filename)
            except Exception as e:
                print(f"Media optimization failed for {filename}: {e}")
                if filename.lower().endswith(('.heic', '.heif')):
                    try:
                        from PIL import Image
                        from pillow_heif import register_heif_opener
                        register_heif_opener()
                        img = Image.open(io.BytesIO(content))
                        buf = io.BytesIO()
                        img.convert("RGB").save(buf, format="JPEG", quality=90)
                        content = buf.getvalue()
                        filename = os.path.splitext(filename)[0] + ".jpg"
                        content_type = "image/jpeg"
                    except Exception:
                        pass
            
            media_type = "video" if "video" in content_type else "image"
            r2_key = f"roka/{int(time.time())}_{filename}"
            upload_tasks.append({
                "key": r2_key,
                "content": content,
                "content_type": content_type,
                "media": {
                    "id": str(uuid.uuid4()),
                    "filename": r2_key,
                    "chapter": chapter,
                    "note": note,
                    "media_type": media_type,
                    "order": int(time.time())
                }
            })
            
    # Parallel upload
    if upload_tasks:
        import concurrent.futures
        def _upload(task):
            upload_file(io.BytesIO(task["content"]), task["key"], task["content_type"])
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            executor.map(_upload, upload_tasks)
            
    # Save to db
    for task in upload_tasks:
        await add_roka_media(task["media"])

    return RedirectResponse(url="/admin/roka-creator", status_code=303)


@app.post("/admin/roka-media/{media_id}")
async def update_roka_item(request: Request, media_id: str, chapter: str = Form(...), note: str = Form(""), order: float = Form(0)):
    if request.cookies.get("session") != "admin_logged_in":
        return JSONResponse(status_code=401, content={"status": "error", "message": "Unauthorized"})

    await update_roka_media(media_id, {
        "chapter": chapter,
        "note": note,
        "order": order
    })
    return RedirectResponse(url="/admin/roka-creator", status_code=303)

@app.post("/admin/roka-media/{media_id}/delete")
async def delete_roka_item(request: Request, media_id: str):
    if request.cookies.get("session") != "admin_logged_in":
        return JSONResponse(status_code=401, content={"status": "error", "message": "Unauthorized"})
    
    await delete_roka_media(media_id)
    return RedirectResponse(url="/admin/roka-creator", status_code=303)


# --- Pre-Wedding Page ---

@app.get("/pre-wedding", response_class=HTMLResponse)
async def read_prewedding(request: Request):
    media = await get_all_prewedding_media()
    
    hero_media = None
    first_video = None
    chapters_map = {
        "Ethnic Look": [],
        "Picnic Look": [],
        "City Look": [],
        "Proposal Look": [],
        "Photographer Shortlisting": [],
        "Teaser & Videos": [],
        "Unassigned": []
    }
    for item in media:
        if item.get("media_type") == "video":
            if not first_video:
                first_video = item
            if "teaser" in item.get("filename", "").lower() or "hero" in item.get("filename", "").lower():
                hero_media = item
                
        ch = item.get("chapter", "Unassigned")
        if ch not in chapters_map:
            chapters_map[ch] = []
        chapters_map[ch].append(item)
        
    if not hero_media:
        hero_media = first_video
        
    settings = request.state.settings
    return templates.TemplateResponse("memory_prewedding.html", {
        "request": request, 
        "hero_media": hero_media,
        "first_video": first_video,
        "chapters_map": chapters_map,
        "media": media,
        "r2_url": R2_PUBLIC_URL,
        "settings": settings,
        "page": "prewedding"
    })


# --- Pre-Wedding Admin Creator ---

@app.get("/admin/prewedding-creator", response_class=HTMLResponse)
async def prewedding_creator(request: Request):
    if request.cookies.get("session") != "admin_logged_in":
        return RedirectResponse(url="/login?next=/admin/prewedding-creator")
    settings = request.state.settings
    media = await get_all_prewedding_media()
    
    # Check local Photos directory
    photos_dir = os.path.join(os.path.dirname(BASE_DIR), "Photos")
    local_photos = []
    if os.path.exists(photos_dir):
        import glob
        for ext in ("*.jpg", "*.jpeg", "*.png", "*.webp", "*.mov", "*.mp4"):
            local_photos.extend(glob.glob(os.path.join(photos_dir, ext)))
            local_photos.extend(glob.glob(os.path.join(photos_dir, ext.upper())))
        local_photos = sorted(list(set(local_photos)))
        local_photos = [os.path.basename(p) for p in local_photos]
        
    return templates.TemplateResponse("admin_prewedding.html", {
        "request": request,
        "settings": settings,
        "media": media,
        "r2_url": R2_PUBLIC_URL,
        "local_photos": local_photos,
        "total_local_count": len(local_photos)
    })

@app.post("/admin/prewedding-media/upload")
async def upload_prewedding_media(
    request: Request,
    chapter: str = Form("Unassigned"),
    note: str = Form(""),
    files: List[UploadFile] = File(...)
):
    if request.cookies.get("session") != "admin_logged_in":
        return JSONResponse(status_code=401, content={"status": "error", "message": "Unauthorized"})

    import time
    from fastapi_app.media_optimizer import optimize_file_bytes
    import io
    import uuid

    upload_tasks = []
    for file in files:
        if file.filename and file.size > 0:
            content = await file.read()
            filename = file.filename
            content_type = file.content_type or ""

            try:
                content, filename, content_type = optimize_file_bytes(content, filename)
            except Exception as e:
                print(f"Media optimization failed for {filename}: {e}")
            
            media_type = "video" if "video" in content_type else "image"
            r2_key = f"prewedding/{int(time.time())}_{filename}"
            upload_tasks.append({
                "key": r2_key,
                "content": content,
                "content_type": content_type,
                "media": {
                    "id": str(uuid.uuid4()),
                    "filename": r2_key,
                    "chapter": chapter,
                    "note": note,
                    "media_type": media_type,
                    "order": int(time.time())
                }
            })
            
    if upload_tasks:
        import concurrent.futures
        def _upload(task):
            upload_file(io.BytesIO(task["content"]), task["key"], task["content_type"])
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            list(executor.map(_upload, upload_tasks))
            
    for task in upload_tasks:
        await add_prewedding_media(task["media"])

    return RedirectResponse(url="/admin/prewedding-creator", status_code=303)


@app.post("/admin/prewedding-media/batch-upload-local")
async def batch_upload_local_prewedding(
    request: Request,
    chapter: str = Form("Unassigned"),
    filenames: List[str] = Form(...)
):
    """Batch compresses and uploads selected photos from local Photos directory to R2."""
    if request.cookies.get("session") != "admin_logged_in":
        return JSONResponse(status_code=401, content={"status": "error", "message": "Unauthorized"})

    import time
    from fastapi_app.media_optimizer import optimize_image_bytes, optimize_file_bytes
    import io
    import uuid
    import concurrent.futures

    photos_dir = os.path.join(os.path.dirname(BASE_DIR), "Photos")
    
    # Clean filenames in case received comma separated or individual
    target_names = []
    for fn in filenames:
        for sub in fn.split(","):
            sub = sub.strip()
            if sub:
                target_names.append(sub)
    target_names = list(dict.fromkeys(target_names))

    uploaded_count = 0
    errors = []

    def _process_and_upload(fname):
        local_path = os.path.join(photos_dir, fname)
        if not os.path.exists(local_path):
            return None
        with open(local_path, "rb") as f:
            raw_bytes = f.read()

        try:
            content, new_fn, content_type = optimize_image_bytes(raw_bytes, fname)
        except Exception:
            try:
                content, new_fn, content_type = optimize_file_bytes(raw_bytes, fname)
            except Exception as e:
                return {"error": str(e), "file": fname}

        media_type = "video" if "video" in content_type else "image"
        r2_key = f"prewedding/{int(time.time())}_{new_fn}"
        
        upload_file(io.BytesIO(content), r2_key, content_type)
        return {
            "id": str(uuid.uuid4()),
            "filename": r2_key,
            "chapter": chapter,
            "note": "",
            "media_type": media_type,
            "order": int(time.time())
        }

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        results = list(executor.map(_process_and_upload, target_names))

    for res in results:
        if res and "error" not in res:
            await add_prewedding_media(res)
            uploaded_count += 1
        elif res and "error" in res:
            errors.append(res)

    return JSONResponse(content={
        "status": "success",
        "uploaded_count": uploaded_count,
        "errors": errors
    })


@app.post("/admin/prewedding-media/{media_id}")
async def update_prewedding_item(request: Request, media_id: str, chapter: str = Form(...), note: str = Form(""), order: float = Form(0)):
    if request.cookies.get("session") != "admin_logged_in":
        return JSONResponse(status_code=401, content={"status": "error", "message": "Unauthorized"})

    # Check if item needs compression and upload to R2
    from fastapi_app.database import get_db
    db = get_db()
    existing = await db.prewedding_media.find_one({"$or": [{"id": media_id}, {"_id": media_id}]})
    
    update_data = {
        "chapter": chapter,
        "note": note,
        "order": order
    }

    if existing and existing.get("is_local") and not str(existing.get("filename", "")).startswith("prewedding/"):
        fname = existing.get("filename")
        photos_dir = os.path.join(os.path.dirname(BASE_DIR), "Photos")
        local_path = os.path.join(photos_dir, fname)
        if os.path.exists(local_path):
            import io
            import time
            from fastapi_app.media_optimizer import optimize_image_bytes
            with open(local_path, "rb") as f:
                raw_bytes = f.read()
            content, new_fn, content_type = optimize_image_bytes(raw_bytes, fname)
            r2_key = f"prewedding/{int(time.time())}_{new_fn}"
            upload_file(io.BytesIO(content), r2_key, content_type)
            update_data["filename"] = r2_key
            update_data["is_local"] = False

    await update_prewedding_media(media_id, update_data)
    return RedirectResponse(url="/admin/prewedding-creator", status_code=303)


@app.post("/admin/prewedding-media/{media_id}/delete")
async def delete_prewedding_item(request: Request, media_id: str):
    if request.cookies.get("session") != "admin_logged_in":
        return JSONResponse(status_code=401, content={"status": "error", "message": "Unauthorized"})
    
    await delete_prewedding_media(media_id)
    return RedirectResponse(url="/admin/prewedding-creator", status_code=303)


# --- Wishlist ---

@app.get("/api/wishlist")
async def api_get_wishlist():
    items = await get_all_wishlist()
    items.sort(key=lambda x: str(x.get('id', '')), reverse=True)
    for item in items:
        if '_id' in item:
            item['_id'] = str(item['_id'])
    return {"items": items}

@app.get("/wishlist", response_class=HTMLResponse)
async def read_wishlist(request: Request):
    items = await get_all_wishlist()
    settings = request.state.settings
    if settings.get("private_mode", False):
        items = [i for i in items if "honeymoon" not in i.get("title", "").lower()]
    items.sort(key=lambda x: str(x.get('id', '')), reverse=True)
    return templates.TemplateResponse("wishlist.html", {"request": request, "items": items, "settings": settings})

@app.post("/wishlist/add")
async def add_wish(
    request: Request,
    title: str = Form(...),
    description: str = Form(...),
    image_url: str = Form(...),
    category: str = Form("Date Ideas 💡"),
    creator: str = Form(None),
    link: str = Form(None)
):
    from datetime import datetime
    items = await get_all_wishlist()
    next_id = max([it.get("id", 0) for it in items] + [0]) + 1
    new_item = {
        "id": next_id,
        "title": title,
        "category": category,
        "creator": creator if creator else "",
        "description": description,
        "image_url": image_url,
        "link": link if link else "#",
        "date_added": datetime.now().strftime("%b %d, %Y")
    }
    await add_wishlist_item(new_item)
    return RedirectResponse(url="/wishlist", status_code=303)


# --- Guestbook ---

@app.get("/api/guestbook")
async def api_get_guestbook():
    notes = await get_all_guestbook()
    for note in notes:
        if '_id' in note:
            note['_id'] = str(note['_id'])
    return {"notes": notes}

@app.get("/guestbook", response_class=HTMLResponse)
async def read_guestbook(request: Request):
    notes = await get_all_guestbook()
    settings = request.state.settings
    return templates.TemplateResponse("guestbook.html", {"request": request, "notes": notes, "settings": settings})


@app.post("/guestbook/add")
async def add_guest(
    request: Request,
    name: str = Form(...),
    message: str = Form(...)
):
    from datetime import datetime
    new_entry = {
        "name": name,
        "message": message,
        "date": datetime.now().strftime("%b %d, %Y")
    }
    await add_guestbook_entry(new_entry)
    return RedirectResponse(url="/guestbook", status_code=303)


# --- Comments ...
# (We preserve the existing Comments & Rate Date routes here)

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


@app.post("/api/memory/{memory_id}/favorite")
async def toggle_favorite(request: Request, memory_id: int):
    memory = await get_memory_by_id(memory_id)
    if not memory:
        raise HTTPException(status_code=404, detail="Memory not found")
    
    current_status = memory.get("is_favorite", False)
    new_status = not current_status
    
    await update_memory(memory_id, {"is_favorite": new_status})
    return {"status": "success", "is_favorite": new_status}


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

@app.get("/api/dictionary")
async def api_get_dictionary():
    words = await get_all_dictionary()
    words.sort(key=lambda x: x['word'].lower())
    for word in words:
        if '_id' in word:
            word['_id'] = str(word['_id'])
    return {"words": words}

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

# --- Admin Delete Routes ---

@app.delete("/api/admin/memory/{memory_id}")
async def api_delete_memory(memory_id: int):
    try:
        await delete_memory(memory_id)
        return {"status": "success", "message": "Memory deleted"}
    except Exception as e:
        import traceback
        return {"status": "error", "message": str(e), "trace": traceback.format_exc()}

@app.delete("/api/admin/wishlist/{item_id}")
async def api_delete_wishlist(item_id: str):
    await delete_wishlist_item(item_id)
    return {"status": "success", "message": "Wishlist item deleted"}

@app.delete("/api/admin/blessing/{note_id}")
async def api_delete_blessing(note_id: str):
    await delete_guestbook_entry(note_id)
    return {"status": "success", "message": "Blessing deleted"}

@app.delete("/api/admin/dictionary/{word_id}")
async def api_delete_dictionary(word_id: str):
    await delete_dictionary_word(word_id)
    return {"status": "success", "message": "Dictionary word deleted"}

@app.delete("/api/admin/coupon/{coupon_id}")
async def api_delete_coupon(coupon_id: str):
    await delete_coupon_item(coupon_id)
    return {"status": "success", "message": "Coupon deleted"}

@app.delete("/api/admin/memory/{memory_id}/photos/{photo_filename:path}")
async def api_delete_memory_photo(memory_id: int, photo_filename: str):
    """Permanently remove a single photo from a memory (DB + R2)."""
    memory = await get_memory_by_id(memory_id)
    if not memory:
        raise HTTPException(status_code=404, detail="Memory not found")

    photos = memory.get("photos", [])
    if photo_filename not in photos:
        raise HTTPException(status_code=404, detail="Photo not found in memory")

    # Remove from photos list and hidden_photos if present
    photos.remove(photo_filename)
    hidden_photos = [p for p in memory.get("hidden_photos", []) if p != photo_filename]

    await update_memory(memory_id, {"photos": photos, "hidden_photos": hidden_photos})

    # Delete from R2
    try:
        from fastapi_app.storage import delete_file
        delete_file(f"uploads/{memory_id}/{photo_filename}")
    except Exception as e:
        print(f"Warning: could not delete from R2: {e}")

    return {"status": "success", "message": f"Photo {photo_filename} deleted"}

@app.post("/api/admin/memory/{memory_id}/photos/add")
async def api_add_memory_photos(memory_id: int, request: Request, files: List[UploadFile] = File(...)):
    """Upload new photos/videos and append them to an existing memory."""
    if request.cookies.get("session") != "admin_logged_in":
        raise HTTPException(status_code=403, detail="Unauthorized")

    memory = await get_memory_by_id(memory_id)
    if not memory:
        raise HTTPException(status_code=404, detail="Memory not found")

    ALLOWED_TYPES = {"image/jpeg", "image/png", "image/gif", "image/webp", "image/heic",
                     "video/mp4", "video/quicktime", "video/mov"}
    new_filenames = []
    upload_tasks = []

    for photo in files:
        if photo.filename and photo.size > 0:
            content = await photo.read()
            filename = photo.filename
            content_type = photo.content_type or "application/octet-stream"

            # Convert HEIC → JPEG
            if filename.lower().endswith(('.heic', '.heif')):
                try:
                    from PIL import Image
                    from pillow_heif import register_heif_opener
                    register_heif_opener()
                    img = Image.open(io.BytesIO(content))
                    buf = io.BytesIO()
                    img.convert("RGB").save(buf, format="JPEG", quality=90)
                    content = buf.getvalue()
                    filename = os.path.splitext(filename)[0] + ".jpg"
                    content_type = "image/jpeg"
                except Exception as e:
                    print(f"HEIC conversion failed: {e}")

            r2_key = f"uploads/{memory_id}/{filename}"
            upload_tasks.append((r2_key, content, content_type))
            new_filenames.append(filename)

    if upload_tasks:
        import concurrent.futures
        def _upload(args):
            key, data, ct = args
            upload_file(io.BytesIO(data), key, ct)
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            executor.map(_upload, upload_tasks)

    updated_photos = memory.get("photos", []) + new_filenames
    await update_memory(memory_id, {"photos": updated_photos})

    return {"status": "success", "added": new_filenames}

# --- Admin Edit Routes ---

@app.put("/api/admin/memory/{memory_id}")
async def api_edit_memory(memory_id: int, request: Request):
    data = await request.json()
    await update_memory(memory_id, data)
    return {"status": "success", "message": "Memory updated"}

@app.put("/api/admin/wishlist/{item_id}")
async def api_edit_wishlist(item_id: str, request: Request):
    data = await request.json()
    await update_wishlist_item(item_id, data)
    return {"status": "success", "message": "Wishlist item updated"}

@app.put("/api/admin/blessing/{note_id}")
async def api_edit_blessing(note_id: str, request: Request):
    data = await request.json()
    await update_guestbook_entry(note_id, data)
    return {"status": "success", "message": "Blessing updated"}

@app.put("/api/admin/dictionary/{word_id}")
async def api_edit_dictionary(word_id: str, request: Request):
    data = await request.json()
    await update_dictionary_word(word_id, data)
    return {"status": "success", "message": "Dictionary word updated"}

@app.put("/api/admin/coupon/{coupon_id}")
async def api_edit_coupon(coupon_id: str, request: Request):
    data = await request.json()
    await update_coupon(coupon_id, data)
    return {"status": "success", "message": "Coupon updated"}

@app.post("/api/admin/new_coupon/new")
async def api_add_coupon(request: Request):
    data = await request.json()
    
    coupons = await get_all_coupons()
    new_id = len(coupons) + 1
    
    new_coupon = {
        "id": new_id,
        "title": data.get("title", ""),
        "description": data.get("description", ""),
        "icon": data.get("icon", "local_activity"),
        "is_redeemed": data.get("is_redeemed", False)
    }
    
    await add_coupon(new_coupon)
    return {"status": "success", "message": "Coupon added successfully"}

@app.delete("/api/admin/memory/{memory_id}/photos/{filename}")
async def api_delete_memory_photo(memory_id: int, filename: str):
    try:
        memory = await get_memory_by_id(memory_id)
        if not memory:
            return {"status": "error", "message": "Memory not found"}
        
        # Remove from R2
        key = f"uploads/{memory_id}/{filename}"
        delete_file(key)
        
        # Update MongoDB
        photos = memory.get("photos", [])
        if filename in photos:
            photos.remove(filename)
            
        hidden_photos = memory.get("hidden_photos", [])
        if filename in hidden_photos:
            hidden_photos.remove(filename)
            
        await update_memory(memory_id, {"photos": photos, "hidden_photos": hidden_photos})
        
        return {"status": "success", "message": "Photo deleted successfully"}
    except Exception as e:
        import traceback
        return {"status": "error", "message": str(e), "trace": traceback.format_exc()}

@app.post("/api/admin/memory/{memory_id}/photos/add")
async def api_add_memory_photos(memory_id: int, files: List[UploadFile] = File(...)):
    try:
        memory = await get_memory_by_id(memory_id)
        if not memory:
            return {"status": "error", "message": "Memory not found"}
            
        new_photos = []
        for file in files:
            if not file.filename:
                continue
            # Upload to R2
            key = f"uploads/{memory_id}/{file.filename}"
            upload_file(file.file, key, file.content_type)
            new_photos.append(file.filename)
            
        # Update MongoDB
        photos = memory.get("photos", [])
        # Ensure no duplicates in the array just in case
        for p in new_photos:
            if p not in photos:
                photos.append(p)
                
        await update_memory(memory_id, {"photos": photos})
        
        return {"status": "success", "message": f"{len(new_photos)} photos uploaded successfully"}
    except Exception as e:
        import traceback
        return {"status": "error", "message": str(e), "trace": traceback.format_exc()}

@app.post("/api/admin/new_memory/new")
async def api_add_new_memory(request: Request):
    data = await request.json()
    await db_add_memory(data)
    return {"status": "success", "message": "Memory added successfully"}

@app.post("/api/admin/new_wishlist/new")
async def api_add_new_wishlist(request: Request):
    data = await request.json()
    await add_wishlist_item(data)
    return {"status": "success", "message": "Wishlist item added successfully"}

@app.post("/api/admin/new_blessing/new")
async def api_add_new_blessing(request: Request):
    data = await request.json()
    await add_guestbook_entry(data)
    return {"status": "success", "message": "Blessing added successfully"}

@app.post("/api/admin/new_dictionary/new")
async def api_add_new_dictionary(request: Request):
    data = await request.json()
    await add_dictionary_word(data)
    return {"status": "success", "message": "Dictionary word added successfully"}


@app.post("/api/rotate-photo")
async def api_rotate_photo(request: Request):
    
    data = await request.json()
    memory_id = data.get("memory_id")
    photo_name = data.get("photo_name")
    angle = data.get("angle")
    
    if not all([memory_id, photo_name, angle is not None]):
        raise HTTPException(status_code=400, detail="Missing parameters")

    try:
        r2_key = f"uploads/{memory_id}/{photo_name}"
        s3 = get_s3_client()
        
        # Download
        buf = io.BytesIO()
        s3.download_fileobj(R2_BUCKET_NAME, r2_key, buf)
        buf.seek(0)
        
        # Rotate
        img = Image.open(buf)
        # expand=True is critical for portrait/landscape flips
        rotated = img.rotate(angle, expand=True)
        
        # Save back as WebP
        out = io.BytesIO()
        rotated.save(out, format="WEBP", quality=85)
        out.seek(0)
        s3.put_object(Bucket=R2_BUCKET_NAME, Key=r2_key, Body=out, ContentType="image/webp")
        
        return {"status": "success", "message": f"Photo rotated by {angle} degrees"}
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return {"status": "error", "message": str(e)}

# --- Realtime Voice Bot (Gemini Live API Proxy) ---
@app.websocket("/ws/voice-chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    from fastapi_app.agent import GEMINI_API_KEY
    from fastapi_app.gemini_live import GeminiLive
    from google.genai import types
    import traceback
    
    try:
        # Load memories
        from fastapi_app.brain import get_kiara_context, get_kiara_voice_instruction_parts
        context_str = await get_kiara_context()
        system_instruction = types.Content(parts=get_kiara_voice_instruction_parts(context_str))
        
        audio_input_queue = asyncio.Queue()
        video_input_queue = asyncio.Queue()
        text_input_queue = asyncio.Queue()

        async def audio_output_callback(data):
            await websocket.send_bytes(data)

        async def audio_interrupt_callback():
            pass

        gemini_client = GeminiLive(
            api_key=GEMINI_API_KEY, 
            model="gemini-3.1-flash-live-preview", 
            input_sample_rate=16000,
            system_instruction=system_instruction
        )
        
        async def receive_from_client():
            try:
                while True:
                    message = await websocket.receive()
                    
                    if message.get("text"):
                        # Parse JSON from client (e.g. {realtimeInput: {audio: {data: ...}}})
                        try:
                            payload = json.loads(message["text"])
                            if "realtimeInput" in payload:
                                if "audio" in payload["realtimeInput"]:
                                    audio_b64 = payload["realtimeInput"]["audio"]["data"]
                                    audio_bytes = base64.b64decode(audio_b64)
                                    await audio_input_queue.put(audio_bytes)
                                if "text" in payload["realtimeInput"]:
                                    await text_input_queue.put(payload["realtimeInput"]["text"])
                        except json.JSONDecodeError:
                            pass
            except WebSocketDisconnect:
                pass
            except Exception as e:
                print("Client receive error:", e)

        receive_task = asyncio.create_task(receive_from_client())

        try:
            async for event in gemini_client.start_session(
                audio_input_queue=audio_input_queue,
                video_input_queue=video_input_queue,
                text_input_queue=text_input_queue,
                audio_output_callback=audio_output_callback,
                audio_interrupt_callback=audio_interrupt_callback,
            ):
                if event:
                    # Forward transcriptions and other events as JSON
                    await websocket.send_json(event)
        finally:
            receive_task.cancel()
            
    except Exception as e:
        print("WebSocket SDK error:", e, traceback.format_exc())
    finally:
        try:
            await websocket.close()
        except:
            pass

# --- DJ Kiara Realtime Live Voice Bot ---
@app.websocket("/ws/dj-voice-chat")
async def dj_websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    from fastapi_app.agent import GEMINI_API_KEY
    from fastapi_app.gemini_live import GeminiLive
    from google.genai import types
    import traceback
    
    try:
        from fastapi_app.dj_agent import get_dj_music_context, get_dj_voice_instruction_parts
        context_str, _ = await get_dj_music_context()
        system_instruction = types.Content(parts=get_dj_voice_instruction_parts(context_str))
        
        audio_input_queue = asyncio.Queue()
        video_input_queue = asyncio.Queue()
        text_input_queue = asyncio.Queue()

        async def audio_output_callback(data):
            await websocket.send_bytes(data)

        async def audio_interrupt_callback():
            pass

        gemini_client = GeminiLive(
            api_key=GEMINI_API_KEY, 
            model="gemini-3.1-flash-live-preview", 
            input_sample_rate=16000,
            system_instruction=system_instruction
        )
        
        async def receive_from_client():
            try:
                while True:
                    message = await websocket.receive()
                    if message.get("text"):
                        try:
                            payload = json.loads(message["text"])
                            if "realtimeInput" in payload:
                                if "audio" in payload["realtimeInput"]:
                                    audio_b64 = payload["realtimeInput"]["audio"]["data"]
                                    audio_bytes = base64.b64decode(audio_b64)
                                    await audio_input_queue.put(audio_bytes)
                                if "text" in payload["realtimeInput"]:
                                    await text_input_queue.put(payload["realtimeInput"]["text"])
                        except json.JSONDecodeError:
                            pass
            except WebSocketDisconnect:
                pass
            except Exception as e:
                print("DJ Client receive error:", e)

        receive_task = asyncio.create_task(receive_from_client())

        try:
            async for event in gemini_client.start_session(
                audio_input_queue=audio_input_queue,
                video_input_queue=video_input_queue,
                text_input_queue=text_input_queue,
                audio_output_callback=audio_output_callback,
                audio_interrupt_callback=audio_interrupt_callback,
            ):
                if event:
                    await websocket.send_json(event)
        finally:
            receive_task.cancel()
            
    except Exception as e:
        print("DJ WebSocket error:", e, traceback.format_exc())
    finally:
        try:
            await websocket.close()
        except:
            pass

# --- AI Planner Endpoints ---

@app.get("/planner", response_class=HTMLResponse)
async def ai_planner_page(request: Request):
    settings = request.state.settings
    return templates.TemplateResponse("planner.html", {"request": request, "settings": settings})

@app.post("/api/planner/search")
async def planner_search(request: Request):
    import os
    from google import genai
    from google.genai import types
    from dotenv import load_dotenv
    
    load_dotenv()
    data = await request.json()
    query = data.get("query", "")
    
    prompt = f"User is planning a honeymoon trip. Query: {query}. Respond with a list of 3-5 recommended destinations."
    
    api_key = os.getenv("GEMINI_API_KEY", "")
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema={
                    "type": "ARRAY",
                    "items": {
                        "type": "OBJECT",
                        "properties": {
                            "name": {"type": "STRING"},
                            "country": {"type": "STRING"},
                            "brief_description": {"type": "STRING"},
                            "imageUrl": {"type": "STRING"}
                        },
                        "required": ["name", "country", "brief_description", "imageUrl"]
                    }
                },
                temperature=0.7,
            ),
        )
        destinations = json.loads(response.text)
    except Exception as e:
        destinations = [{"name": "Error", "brief_description": f"Failed: {e}"}]
        
    return {"destinations": destinations}

@app.post("/api/planner/details")
async def planner_details(request: Request):
    import os
    from google import genai
    from google.genai import types
    from dotenv import load_dotenv
    
    load_dotenv()
    data = await request.json()
    destination = data.get("destination", "")
    month = data.get("month", "December 2026")
    
    prompt = f"Provide detailed honeymoon itinerary and details for {destination} in {month} for a 6-7 day trip."
    
    schema = {
        "type": "OBJECT",
        "properties": {
            "things_to_do": {"type": "ARRAY", "items": {"type": "STRING"}},
            "things_to_eat": {"type": "ARRAY", "items": {"type": "STRING"}},
            "popular_sites": {"type": "ARRAY", "items": {"type": "STRING"}},
            "key_highlights": {"type": "STRING"},
            "honeymoon_rating": {"type": "STRING"},
            "cost_in_inr": {"type": "STRING"},
            "hotels": {
                "type": "ARRAY",
                "items": {
                    "type": "OBJECT",
                    "properties": {
                        "name": {"type": "STRING"},
                        "price_per_night": {"type": "STRING"},
                        "description": {"type": "STRING"}
                    }
                }
            }
        }
    }
    
    api_key = os.getenv("GEMINI_API_KEY", "")
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=schema,
                temperature=0.7,
            ),
        )
        details = json.loads(response.text)
    except Exception as e:
        details = {"error": f"Could not parse details: {e}"}
        
    return details

@app.post("/api/planner/chat")
async def planner_chat(request: Request):
    import os
    from google import genai
    from google.genai import types
    from dotenv import load_dotenv
    
    load_dotenv()
    data = await request.json()
    messages = data.get("messages", [])
    if not messages:
        return {"text": "Please ask a planning question."}
        
    system_prompt = "You are Kiara, a specialized AI Honeymoon Planner. Provide concise, helpful responses to help refine the user's 6-7 day trip and always suggest cost estimates in INR when relevant. You are chatting directly with the user."
    
    # Format messages for genai
    formatted_contents = []
    for m in messages:
        role = "user" if m["role"] == "user" else "model"
        formatted_contents.append(types.Content(role=role, parts=[types.Part.from_text(text=m["content"])]))
    
    api_key = os.getenv("GEMINI_API_KEY", "")
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=formatted_contents,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.7,
            ),
        )
        return {"text": response.text}
    except Exception as e:
        return {"text": f"Error: {e}"}

@app.get("/api/planner/plans")
async def get_planner_plans(request: Request):
    plans = await get_all_ai_plans()
    return {"plans": plans}

@app.post("/api/planner/save")
async def save_planner_plan(request: Request):
    data = await request.json()
    plan_id = await save_ai_plan(data)
    return {"status": "success", "id": plan_id}
