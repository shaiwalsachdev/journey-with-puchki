"""
Helper module to calculate Memory Lane / Highlights similar to Google Photos
"""
from datetime import date
from dateutil import parser
from dateutil.relativedelta import relativedelta
from typing import List, Dict, Any
import random


def parse_memory_date(date_str: str):
    if not date_str:
        return None
    try:
        # Handle ranges like "September - October 2025"
        clean_d = date_str.split("-")[-1].strip()
        return parser.parse(clean_d, fuzzy=True).date()
    except Exception:
        return None


def get_memory_photo_url(memory_id: int, filename: str, r2_url: str) -> str:
    if filename.startswith("http"):
        return filename
    return f"{r2_url.rstrip('/')}/uploads/{memory_id}/{filename.lstrip('/')}"


def build_memory_lane_highlights(memories: List[Dict[str, Any]], r2_url: str, reference_date: date = None) -> List[Dict[str, Any]]:
    """
    Returns a list of curated highlight story collections:
    - "1 Year Ago"
    - "6 Months Ago"
    - "On This Day" or "This Month Flashback"
    - "Date Night Highlights"
    - "Special Milestone"
    """
    if reference_date is None:
        reference_date = date.today()

    parsed = []
    for m in memories:
        if m.get("hide_timeline") or m.get("hide_all_photos"):
            continue

        raw_photos = m.get("photos", [])
        photos = [
            p for p in raw_photos
            if not p.lower().endswith((".mp4", ".mov", ".js", ".json", ".zip"))
        ]
        if not photos:
            continue

        dt = parse_memory_date(m.get("date", ""))
        parsed.append({
            "memory": m,
            "date": dt,
            "photos": photos
        })

    highlights = []
    seen_memory_ids = set()

    target_1y = reference_date - relativedelta(years=1)
    target_6m = reference_date - relativedelta(months=6)

    # 1. 1 YEAR AGO (Prefer memories with more than 1 photo or closest date)
    matches_1y = [
        p for p in parsed 
        if p["date"] and p["date"].year == target_1y.year and abs((p["date"] - target_1y).days) <= 25
    ]
    if matches_1y:
        # Sort by having multiple photos first, then closest distance
        matches_1y.sort(key=lambda x: (len(x["photos"]) > 1, -abs((x["date"] - target_1y).days)), reverse=True)
        best = matches_1y[0]
        m = best["memory"]
        seen_memory_ids.add(m.get("id"))
        
        slides = []
        for photo in best["photos"][:12]:
            slides.append({
                "url": get_memory_photo_url(m["id"], photo, r2_url),
                "title": m.get("title", ""),
                "date": m.get("date", ""),
                "caption": m.get("smart_data", {}).get("summary", "") or "1 year ago today..."
            })
            
        highlights.append({
            "id": f"highlight-1y-{m.get('id')}",
            "memory_id": m.get("id"),
            "badge": "1 Year Ago",
            "badge_color": "from-rose-500 to-amber-500",
            "icon": "history",
            "title": m.get("title", "1 Year Ago"),
            "subtitle": m.get("date", ""),
            "cover_url": get_memory_photo_url(m["id"], best["photos"][0], r2_url),
            "photo_count": len(best["photos"]),
            "slides": slides,
            "summary": m.get("smart_data", {}).get("summary", ""),
            "vibe": m.get("smart_data", {}).get("vibe", "Nostalgic Romance ✨")
        })

    # 2. 6 MONTHS AGO (Within ±25 days)
    matches_6m = [
        p for p in parsed 
        if p["date"] and abs((p["date"] - target_6m).days) <= 25 and p["memory"].get("id") not in seen_memory_ids
    ]
    if matches_6m:
        matches_6m.sort(key=lambda x: (len(x["photos"]) > 1, -abs((x["date"] - target_6m).days)), reverse=True)
        best = matches_6m[0]
        m = best["memory"]
        seen_memory_ids.add(m.get("id"))
        
        slides = []
        for photo in best["photos"][:12]:
            slides.append({
                "url": get_memory_photo_url(m["id"], photo, r2_url),
                "title": m.get("title", ""),
                "date": m.get("date", ""),
                "caption": m.get("smart_data", {}).get("summary", "") or "6 months ago..."
            })

        highlights.append({
            "id": f"highlight-6m-{m.get('id')}",
            "memory_id": m.get("id"),
            "badge": "6 Months Ago",
            "badge_color": "from-purple-500 to-pink-500",
            "icon": "auto_awesome",
            "title": m.get("title", "6 Months Ago"),
            "subtitle": m.get("date", ""),
            "cover_url": get_memory_photo_url(m["id"], best["photos"][0], r2_url),
            "photo_count": len(best["photos"]),
            "slides": slides,
            "summary": m.get("smart_data", {}).get("summary", ""),
            "vibe": m.get("smart_data", {}).get("vibe", "Sweet Memories 🌸")
        })

    # 3. ON THIS MONTH / SEASONAL FLASHBACK (from previous year or earlier in the journey)
    past_month_matches = [
        p for p in parsed
        if p["date"] and p["date"].month == reference_date.month and p["date"].year < reference_date.year and p["memory"].get("id") not in seen_memory_ids
    ]
    if not past_month_matches:
        # Fallback to any matching month
        past_month_matches = [
            p for p in parsed
            if p["date"] and p["date"].month == reference_date.month and p["memory"].get("id") not in seen_memory_ids
        ]

    if past_month_matches:
        past_month_matches.sort(key=lambda x: len(x["photos"]), reverse=True)
        best = past_month_matches[0]
        m = best["memory"]
        seen_memory_ids.add(m.get("id"))
        
        slides = []
        for photo in best["photos"][:12]:
            slides.append({
                "url": get_memory_photo_url(m["id"], photo, r2_url),
                "title": m.get("title", ""),
                "date": m.get("date", ""),
                "caption": m.get("smart_data", {}).get("summary", "") or f"{reference_date.strftime('%B')} Flashback"
            })

        highlights.append({
            "id": f"highlight-month-{m.get('id')}",
            "memory_id": m.get("id"),
            "badge": f"{reference_date.strftime('%B')} Flashback",
            "badge_color": "from-emerald-500 to-teal-600",
            "icon": "calendar_month",
            "title": m.get("title", f"{reference_date.strftime('%B')} Moments"),
            "subtitle": m.get("date", ""),
            "cover_url": get_memory_photo_url(m["id"], best["photos"][0], r2_url),
            "photo_count": len(best["photos"]),
            "slides": slides,
            "summary": m.get("smart_data", {}).get("summary", ""),
            "vibe": m.get("smart_data", {}).get("vibe", "Timeless 🌿")
        })

    # 4. DATE NIGHT HIGHLIGHT
    food_dates = [
        p for p in parsed
        if p["memory"].get("id") not in seen_memory_ids and (
            p["memory"].get("type") in ["date", "dinner", "food"] or 
            "pizza" in p["memory"].get("title", "").lower() or 
            "date" in p["memory"].get("title", "").lower()
        )
    ]
    if food_dates:
        # Pick one with at least 5 photos if available
        food_dates.sort(key=lambda x: len(x["photos"]), reverse=True)
        chosen = random.choice(food_dates[:5])
        m = chosen["memory"]
        seen_memory_ids.add(m.get("id"))
        
        slides = []
        for photo in chosen["photos"][:12]:
            slides.append({
                "url": get_memory_photo_url(m["id"], photo, r2_url),
                "title": m.get("title", ""),
                "date": m.get("date", ""),
                "caption": m.get("smart_data", {}).get("summary", "") or "A delicious date night..."
            })

        highlights.append({
            "id": f"highlight-date-{m.get('id')}",
            "memory_id": m.get("id"),
            "badge": "Date Night Highlights",
            "badge_color": "from-orange-500 to-red-500",
            "icon": "local_pizza",
            "title": m.get("title", "Date Night"),
            "subtitle": m.get("date", ""),
            "cover_url": get_memory_photo_url(m["id"], chosen["photos"][0], r2_url),
            "photo_count": len(chosen["photos"]),
            "slides": slides,
            "summary": m.get("smart_data", {}).get("summary", ""),
            "vibe": m.get("smart_data", {}).get("vibe", "Romantic & Fun 🍕✨")
        })

    # 5. SPECIAL / MILESTONE HIGHLIGHT
    special_mems = [
        p for p in parsed
        if p["memory"].get("id") not in seen_memory_ids and (
            p["memory"].get("type") in ["milestone", "celebration"] or
            any(w in p["memory"].get("title", "").lower() for w in ["proposal", "pre-wedding", "birthday", "ring", "lehenga", "valentine"])
        )
    ]
    if special_mems:
        special_mems.sort(key=lambda x: len(x["photos"]), reverse=True)
        chosen = special_mems[0]
        m = chosen["memory"]
        seen_memory_ids.add(m.get("id"))
        
        slides = []
        for photo in chosen["photos"][:15]:
            slides.append({
                "url": get_memory_photo_url(m["id"], photo, r2_url),
                "title": m.get("title", ""),
                "date": m.get("date", ""),
                "caption": m.get("smart_data", {}).get("summary", "") or "One of our most special milestones..."
            })

        highlights.append({
            "id": f"highlight-milestone-{m.get('id')}",
            "memory_id": m.get("id"),
            "badge": "Milestone Moment",
            "badge_color": "from-indigo-500 to-pink-500",
            "icon": "favorite",
            "title": m.get("title", "Unforgettable Milestone"),
            "subtitle": m.get("date", ""),
            "cover_url": get_memory_photo_url(m["id"], chosen["photos"][0], r2_url),
            "photo_count": len(chosen["photos"]),
            "slides": slides,
            "summary": m.get("smart_data", {}).get("summary", ""),
            "vibe": m.get("smart_data", {}).get("vibe", "Magical 💍✨")
        })

    return highlights
