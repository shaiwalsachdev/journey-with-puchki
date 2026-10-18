---
name: sync-instagram-wishlist
description: Automatically sync saved reels and posts from the ShaiX2 Instagram Wishlist collection into MongoDB Atlas for the website.
---

# Sync Instagram Wishlist Skill

Use this skill whenever the user asks to sync, refresh, or update the website wishlist from Instagram, or when they want to pull new saved items from their Instagram collection.

## Target Instagram Collection
- **URL**: `https://www.instagram.com/geeekdonsignals/saved/shaix2-wishlist/17904675006314511/`
- **Target Database**: MongoDB Atlas (`puchki.wishlist`)

## Script Location
The sync automation script is located at:
[`/Users/geekdon/Documents/Journey with Puchki/sync_instagram_wishlist.py`](file:///Users/geekdon/Documents/Journey%20with%20Puchki/sync_instagram_wishlist.py)

## Execution Command

Run the script from the workspace directory:

```bash
cd "/Users/geekdon/Documents/Journey with Puchki"
python3 sync_instagram_wishlist.py
```

## How It Works

1. **Persistent Browser Session**:
   - Launches Chromium using a persistent user data profile located at `~/.instagram_playwright_profile`.
   - On the first run, if not logged in, it will show a visible browser window and wait for the user to log into Instagram. Once authenticated, the session cookies are permanently retained for future headless or headful runs.

2. **Scraping & Collection**:
   - Navigates to the collection URL.
   - Smoothly scrolls the collection view up to 25 passes (stopping early when no new items appear).
   - Extracts all post/reel links (`/p/` or `/reel/`), alt text, thumbnails, and creator usernames (`@handle`).

3. **De-duplication**:
   - Compares the post shortcodes (`/reel/XXXX/` or `/p/XXXX/`) against existing links in the MongoDB Atlas `puchki.wishlist` collection.
   - Ignores all previously saved items and processes only new additions.

4. **Categorization & Formatting**:
   - Cleans the caption and assigns one of four categories:
     - `Future Travel ✈️` (trips, hotels, scenic spots, resorts, getaways)
     - `Home Decor 🏠` (interior design, furniture, lighting, aesthetic items)
     - `Date Ideas 💡` (cafes, restaurants, food, dining, activities)
     - `Special Milestones 💍` (weddings, anniversaries, proposals, celebrations)
   - Formats a human-readable title and preserves creator handle attribution.

5. **Database Sync**:
   - Inserts newly identified items with fields:
     - `title`: Short descriptive title
     - `category`: Category string
     - `creator`: Instagram handle (e.g. `@thetaleoftruelove`)
     - `description`: Cleaned caption/notes
     - `link`: Full Instagram post/reel URL
     - `image_url`: Media thumbnail URL
     - `created_at`: Unix timestamp
     - `source`: `"instagram_sync"`

## Verification
After running the script, verify that the new items appear by checking:
```bash
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8000/wishlist
```
Or navigating to `http://127.0.0.1:8000/wishlist` in the browser.
