"""
MongoDB Atlas Connection & CRUD Operations
Collections: memories, settings, coupons, guestbook, vault, wishlist, dictionary
"""
import os
import certifi
from motor.motor_asyncio import AsyncIOMotorClient

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb+srv://shaiwalsachdev_db_user:AZo1cSsUIqWgrlHT@puchki.t0sen64.mongodb.net/?appName=Puchki")
DB_NAME = "puchki"

client = None
db = None

def get_db():
    global client, db
    if db is None:
        client = AsyncIOMotorClient(MONGODB_URI, tlsCAFile=certifi.where())
        db = client[DB_NAME]
    return db

# --- Memories ---
async def get_all_memories():
    db = get_db()
    memories = await db.memories.find({}, {"_id": 0}).sort("id", 1).to_list(length=None)
    return memories

async def save_all_memories(memories: list):
    db = get_db()
    # Replace entire collection
    await db.memories.delete_many({})
    if memories:
        await db.memories.insert_many(memories)

async def update_memory(memory_id: int, update_data: dict):
    db = get_db()
    await db.memories.update_one({"id": memory_id}, {"$set": update_data})

async def get_memory_by_id(memory_id: int):
    db = get_db()
    return await db.memories.find_one({"id": memory_id}, {"_id": 0})

async def get_next_memory_id():
    db = get_db()
    last = await db.memories.find_one(sort=[("id", -1)])
    return (last["id"] + 1) if last else 1

async def add_memory(memory: dict):
    db = get_db()
    await db.memories.insert_one(memory)

# --- Settings ---
async def get_settings():
    db = get_db()
    settings = await db.settings.find_one({}, {"_id": 0})
    return settings or {"private_mode": False, "theme": "classic"}

async def save_settings(settings: dict):
    db = get_db()
    await db.settings.replace_one({}, settings, upsert=True)

# --- Coupons ---
async def get_all_coupons():
    db = get_db()
    return await db.coupons.find({}, {"_id": 0}).to_list(length=None)

async def save_all_coupons(coupons: list):
    db = get_db()
    await db.coupons.delete_many({})
    if coupons:
        await db.coupons.insert_many(coupons)

async def update_coupon(coupon_id: int, update_data: dict):
    db = get_db()
    await db.coupons.update_one({"id": coupon_id}, {"$set": update_data})

# --- Guestbook ---
async def get_all_guestbook():
    db = get_db()
    return await db.guestbook.find({}, {"_id": 0}).to_list(length=None)

async def save_all_guestbook(notes: list):
    db = get_db()
    await db.guestbook.delete_many({})
    if notes:
        await db.guestbook.insert_many(notes)

async def add_guestbook_entry(entry: dict):
    db = get_db()
    await db.guestbook.insert_one(entry)

# --- Vault ---
async def get_all_vault():
    db = get_db()
    return await db.vault.find({}, {"_id": 0}).to_list(length=None)

async def save_all_vault(letters: list):
    db = get_db()
    await db.vault.delete_many({})
    if letters:
        await db.vault.insert_many(letters)

# --- Wishlist ---
async def get_all_wishlist():
    db = get_db()
    return await db.wishlist.find({}, {"_id": 0}).to_list(length=None)

async def save_all_wishlist(items: list):
    db = get_db()
    await db.wishlist.delete_many({})
    if items:
        await db.wishlist.insert_many(items)

async def add_wishlist_item(item: dict):
    db = get_db()
    await db.wishlist.insert_one(item)

# --- Dictionary ---
async def get_all_dictionary():
    db = get_db()
    return await db.dictionary.find({}, {"_id": 0}).to_list(length=None)

async def save_all_dictionary(words: list):
    db = get_db()
    await db.dictionary.delete_many({})
    if words:
        await db.dictionary.insert_many(words)

async def add_dictionary_word(word: dict):
    db = get_db()
    await db.dictionary.insert_one(word)
