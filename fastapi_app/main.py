
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
    get_next_memory_id, add_memory as db_add_memory, delete_memory,
    get_settings, save_settings,
    get_all_coupons, save_all_coupons, update_coupon, delete_coupon_item, add_coupon,
    get_all_guestbook, add_guestbook_entry, delete_guestbook_entry, update_guestbook_entry,
    get_all_vault,
    get_all_wishlist, add_wishlist_item, delete_wishlist_item, update_wishlist_item,
    get_all_dictionary, add_dictionary_word, save_all_dictionary, delete_dictionary_word, update_dictionary_word
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
    is_birthday = settings.get("birthday_mode", False)

    for m in memories:
        if is_private and m["id"] == 1:
            continue
        
        # Hide 'hot' tagged memories globally unless birthday mode is active
        if not is_birthday and m.get("type") == "hot":
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

    await save_settings(current_settings)
    return {"status": "success", "settings": current_settings}


# --- Public Routes ---

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    settings = request.state.settings
    return templates.TemplateResponse("index.html", {"request": request, "page": "home", "settings": settings})


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
    visible_memories = process_memories_for_display(memories, settings)
    # Filter out memories specifically hidden from timeline
    visible_memories = [m for m in visible_memories if not m.get("hide_timeline")]
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
    PRIVATE_HIDDEN_CATEGORIES = {"start"}
    type_set = set()
    for m in memories:
        if m.get("type"):
            type_set.add(m["type"])
    categories = []
    for t in sorted(type_set):
        # Hide 'start' in private mode
        if settings.get("private_mode") and t in PRIVATE_HIDDEN_CATEGORIES:
            continue
        # Hide 'hot' when birthday mode is off
        if t == "hot" and not settings.get("birthday_mode"):
            continue
        categories.append({"value": t, "label": f"{t.title()} {EMOJI_MAP.get(t, '')}"})
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
                content_type = photo.content_type

                # Convert HEIC → JPEG (browsers can't display HEIC)
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
                        print(f"HEIC conversion failed for {filename}: {e}")

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
    return RedirectResponse(url=f"/memory/{new_id}", status_code=303)


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
