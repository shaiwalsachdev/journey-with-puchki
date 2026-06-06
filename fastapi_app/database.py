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

async def log_chat_interaction(user_message: str, ai_response: dict, history: list):
    import datetime
    db = get_db()
    interaction = {
        "timestamp": datetime.datetime.utcnow(),
        "user_message": user_message,
        "ai_response": ai_response,
        "history": history
    }
    await db.chat_logs.insert_one(interaction)

async def get_all_chat_logs(limit: int = 100):
    db = get_db()
    logs = await db.chat_logs.find({}, {"_id": 0}).sort("timestamp", -1).limit(limit).to_list(length=limit)
    # Convert datetime to ISO string for JSON serialization
    for log in logs:
        if "timestamp" in log and log["timestamp"]:
            log["timestamp"] = log["timestamp"].isoformat()
    return logs

# --- Settings ---
async def get_settings():
    db = get_db()
    settings = await db.settings.find_one({}, {"_id": 0})
    defaults = {"private_mode": False, "theme": "classic", "birthday_mode": False, "hero_images": []}
    if settings:
        # Ensure all default keys exist
        for key, val in defaults.items():
            if key not in settings:
                settings[key] = val
        return settings
    return defaults

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

async def add_coupon(coupon: dict):
    db = get_db()
    await db.coupons.insert_one(coupon)

async def update_coupon(coupon_id: str, update_data: dict):
    db = get_db()
    await db.coupons.update_one(_build_id_query(coupon_id), {"$set": update_data})

async def delete_coupon_item(coupon_id: str):
    db = get_db()
    await db.coupons.delete_one(_build_id_query(coupon_id))

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

# --- Roka Media ---
async def get_all_roka_media():
    db = get_db()
    return await db.roka_media.find({}, {"_id": 0}).sort("order", 1).to_list(length=None)

async def add_roka_media(media: dict):
    db = get_db()
    await db.roka_media.insert_one(media)

async def update_roka_media(media_id: str, data: dict):
    db = get_db()
    await db.roka_media.update_one(_build_id_query(media_id), {"$set": data})

async def delete_roka_media(media_id: str):
    db = get_db()
    await db.roka_media.delete_one(_build_id_query(media_id))

# --- Delete Operations ---
async def delete_memory(memory_id: int):
    db = get_db()
    await db.memories.delete_one({"id": memory_id})

def _build_id_query(item_id: str):
    from bson.objectid import ObjectId
    from bson.errors import InvalidId
    query = [{"id": item_id}]
    if str(item_id).isdigit():
        query.append({"id": int(item_id)})
    try:
        query.append({"_id": ObjectId(item_id)})
    except InvalidId:
        pass
    return {"$or": query}

async def delete_guestbook_entry(note_id: str):
    db = get_db()
    await db.guestbook.delete_one(_build_id_query(note_id))

async def delete_wishlist_item(item_id: str):
    db = get_db()
    await db.wishlist.delete_one(_build_id_query(item_id))

async def delete_dictionary_word(word_id: str):
    db = get_db()
    await db.dictionary.delete_one(_build_id_query(word_id))

# --- Update Operations ---
async def update_wishlist_item(item_id: str, data: dict):
    db = get_db()
    await db.wishlist.update_one(_build_id_query(item_id), {"$set": data})

async def update_guestbook_entry(note_id: str, data: dict):
    db = get_db()
    await db.guestbook.update_one(_build_id_query(note_id), {"$set": data})

async def update_dictionary_word(word_id: str, data: dict):
    db = get_db()
    await db.dictionary.update_one(_build_id_query(word_id), {"$set": data})

# --- AI Plans ---
async def get_all_ai_plans():
    db = get_db()
    plans = await db.ai_plans.find({}).sort("updated_at", -1).to_list(length=None)
    for p in plans:
        if "_id" in p:
            p["_id"] = str(p["_id"])
    return plans

async def get_ai_plan(plan_id: str):
    db = get_db()
    plan = await db.ai_plans.find_one(_build_id_query(plan_id))
    if plan and "_id" in plan:
        plan["_id"] = str(plan["_id"])
    return plan

async def save_ai_plan(plan: dict):
    db = get_db()
    import datetime
    plan["updated_at"] = datetime.datetime.utcnow()
    # Check if id exists
    if "id" in plan and plan["id"]:
        # Update existing
        plan_id = plan["id"]
        # Remove _id if it's there to avoid immutable field error
        plan_copy = plan.copy()
        if "_id" in plan_copy:
            del plan_copy["_id"]
        await db.ai_plans.update_one(_build_id_query(plan_id), {"$set": plan_copy})
        return plan_id
    else:
        # Generate new ID
        import uuid
        plan["id"] = str(uuid.uuid4())
        plan["created_at"] = plan["updated_at"]
        await db.ai_plans.insert_one(plan)
        return plan["id"]

async def delete_ai_plan(plan_id: str):
    db = get_db()
    await db.ai_plans.delete_one(_build_id_query(plan_id))

# --- Story Data ---
async def get_story_data():
    db = get_db()
    data = await db.story_data.find_one({}, {"_id": 0})
    if not data:
        return {
            "system_logs": [],
            "stats": {"dog_probability": "99.9%", "pizza_pasta_sushi": "500+"},
            "algorithm_description": "When logic meets emotion. A dashboard forecasting our future using advanced predictive modeling."
        }
    return data

async def save_story_data(data: dict):
    db = get_db()
    await db.story_data.replace_one({}, data, upsert=True)
