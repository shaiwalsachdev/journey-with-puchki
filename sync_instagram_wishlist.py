#!/usr/bin/env python3
"""
sync_instagram_wishlist.py

Automates syncing saved Instagram items from your collection:
https://www.instagram.com/geeekdonsignals/saved/shaix2-wishlist/17904675006314511/
directly into MongoDB Atlas ('puchki.wishlist').

Features:
- Launches Chromium with a persistent local user data directory (stores login cookies permanently).
- If not logged in, opens a browser window for you to log in once.
- Once logged in, it opens your Wishlist collection, scrolls to collect all items.
- Checks MongoDB for existing items using their Instagram post shortcode/URL to prevent duplicates.
- For each new item, automatically determines:
    * Title & Notes
    * Category (Future Travel ✈️, Home Decor 🏠, Date Ideas 💡, Special Milestones 💍)
    * Creator handle (@handle)
- Inserts new items into MongoDB Atlas.
"""

import os
import sys
import time
import re
import asyncio
from pathlib import Path
import certifi
from motor.motor_asyncio import AsyncIOMotorClient
from playwright.async_api import async_playwright

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb+srv://shaiwalsachdev_db_user:AZo1cSsUIqWgrlHT@puchki.t0sen64.mongodb.net/?appName=Puchki")
COLLECTION_URL = "https://www.instagram.com/geeekdonsignals/saved/shaix2-wishlist/17904675006314511/"
USER_DATA_DIR = Path.home() / ".instagram_playwright_profile"

def infer_category(text: str) -> str:
    text_lower = text.lower()
    if any(k in text_lower for k in ["travel", "resort", "hotel", "flight", "villa", "trip", "vacation", "lake", "mountain", "beach", "japan", "switzerland", "island"]):
        return "Future Travel ✈️"
    elif any(k in text_lower for k in ["decor", "home", "bedroom", "living room", "kitchen", "lamp", "curtain", "furniture", "couch", "interior"]):
        return "Home Decor 🏠"
    elif any(k in text_lower for k in ["date", "cafe", "restaurant", "dinner", "coffee", "rooftop", "food", "brunch", "pasta", "activity"]):
        return "Date Ideas 💡"
    elif any(k in text_lower for k in ["wedding", "ring", "anniversary", "birthday", "proposal", "milestone"]):
        return "Special Milestones 💍"
    return "Future Travel ✈️"

def format_title(handle: str, alt_text: str) -> str:
    clean_alt = re.sub(r'^(Photo by|Photo shared by|Reel by)\s+[^.]+on[^.]+\.\s*', '', alt_text, flags=re.IGNORECASE).strip()
    clean_alt = re.sub(r'May be an image of\s+', '', clean_alt, flags=re.IGNORECASE).strip()
    if clean_alt and len(clean_alt) > 5:
        # Take first 60 chars or first sentence
        first_sentence = clean_alt.split('.')[0].strip()
        if len(first_sentence) > 65:
            first_sentence = first_sentence[:62] + "..."
        return first_sentence.capitalize()
    return f"Wishlist item by @{handle}" if handle else "Shared Dream Item"

async def sync():
    print("=" * 60)
    print("✨ Starting Instagram Wishlist Sync for ShaiX2")
    print(f"📁 Session Profile: {USER_DATA_DIR}")
    print("=" * 60)

    # 1. Connect to MongoDB
    client = AsyncIOMotorClient(MONGODB_URI, tlsCAFile=certifi.where())
    db = client["puchki"]
    
    # Get all existing wishlist links to prevent duplicates
    existing_items = await db.wishlist.find({}, {"link": 1}).to_list(length=None)
    existing_links = set()
    for item in existing_items:
        link = item.get("link", "")
        # Normalize: extract code /p/XXXXX/ or /reel/XXXXX/
        match = re.search(r'/(?:p|reel)/([A-Za-z0-9_-]+)', link)
        if match:
            existing_links.add(match.group(1))
        elif link:
            existing_links.add(link)

    print(f"📊 Found {len(existing_items)} existing items in MongoDB.")

    # 2. Launch Browser with persistent user data dir
    async with async_playwright() as p:
        browser_context = await p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=False,  # Opens visible window so user can log in if needed
            viewport={"width": 1280, "height": 900},
            args=["--disable-blink-features=AutomationControlled"]
        )

        page = await browser_context.new_page()
        print("🌐 Navigating to Instagram Wishlist Collection...")
        await page.goto(COLLECTION_URL, wait_until="domcontentloaded", timeout=60000)
        await asyncio.sleep(4)

        # Check if redirected to login page
        if "accounts/login" in page.url or await page.locator("input[name='username']").count() > 0:
            print("\n" + "!" * 60)
            print("🔑 Instagram login required.")
            print("👉 Please log into your Instagram account in the opened browser window.")
            print("   The script will automatically detect when you are logged in!")
            print("!" * 60 + "\n")
            
            # Wait for user to finish logging in
            while "accounts/login" in page.url or await page.locator("input[name='username']").count() > 0:
                await asyncio.sleep(2)
            
            print("✅ Login detected! Continuing...")
            await page.goto(COLLECTION_URL, wait_until="domcontentloaded")
            await asyncio.sleep(4)

        # 3. Scroll and extract items
        print("🔍 Scanning collection items...")
        scraped_posts = {}
        last_count = 0
        unchanged_scrolls = 0

        for _ in range(25):  # scroll up to 25 times
            items = await page.evaluate('''() => {
                const results = [];
                const links = document.querySelectorAll('a[href*="/p/"], a[href*="/reel/"]');
                links.forEach(a => {
                    const href = a.href;
                    if (!href.includes('/saved/')) {
                        const img = a.querySelector('img');
                        const alt = img ? img.getAttribute('alt') || '' : '';
                        const imgSrc = img ? img.getAttribute('src') || '' : '';
                        
                        let creator = '';
                        const creatorMatch = alt.match(/(?:by|from)\\s+([a-zA-Z0-9._]+)/i);
                        if (creatorMatch) creator = creatorMatch[1];
                        
                        results.push({ href, alt, imgSrc, creator });
                    }
                });
                return results;
            }''')

            for it in items:
                href = it["href"]
                m = re.search(r'/(?:p|reel)/([A-Za-z0-9_-]+)', href)
                code = m.group(1) if m else href
                if code not in scraped_posts:
                    scraped_posts[code] = it

            if len(scraped_posts) == last_count:
                unchanged_scrolls += 1
                if unchanged_scrolls >= 3:
                    break
            else:
                unchanged_scrolls = 0
                last_count = len(scraped_posts)

            await page.evaluate("window.scrollBy(0, 1000)")
            await asyncio.sleep(1.2)

        print(f"📦 Discovered {len(scraped_posts)} total posts in Instagram collection.")

        # 4. Filter for new items
        new_items_to_add = []
        for code, data in scraped_posts.items():
            if code not in existing_links and data["href"] not in existing_links:
                creator = data.get("creator", "")
                alt = data.get("alt", "")
                title = format_title(creator, alt)
                cat = infer_category(alt + " " + title)
                
                new_doc = {
                    "title": title,
                    "category": cat,
                    "creator": f"@{creator}" if creator and not creator.startswith("@") else creator,
                    "description": alt if len(alt) < 200 else alt[:197] + "...",
                    "link": data["href"],
                    "image_url": data.get("imgSrc", ""),
                    "created_at": time.time(),
                    "source": "instagram_sync"
                }
                new_items_to_add.append(new_doc)

        # 5. Insert new items to DB
        if new_items_to_add:
            print(f"\n🚀 Found {len(new_items_to_add)} new item(s) to add to Wishlist!")
            for item in new_items_to_add:
                print(f"  + [{item['category']}] {item['title']} ({item.get('creator', 'N/A')})")
            
            await db.wishlist.insert_many(new_items_to_add)
            print(f"\n🎉 Successfully added {len(new_items_to_add)} new item(s) to MongoDB Atlas!")
        else:
            print("\n✨ All items are already up to date in your Wishlist database! No new items found.")

        await browser_context.close()

if __name__ == "__main__":
    asyncio.run(sync())
