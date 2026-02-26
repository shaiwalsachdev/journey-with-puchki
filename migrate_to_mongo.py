"""
One-time migration: Import all JSON data files into MongoDB Atlas.
Run from project root: python migrate_to_mongo.py
"""
import asyncio
import json
import os

# Set up path
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fastapi_app")
DATA_DIR = os.path.join(BASE_DIR, "data")

# Import after path setup
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastapi_app.database import get_db

COLLECTIONS = {
    "memories": "memories.json",
    "settings": "settings.json",
    "coupons": "coupons.json",
    "guestbook": "guestbook.json",
    "vault": "vault.json",
    "wishlist": "wishlist.json",
    "dictionary": "dictionary.json",
}

async def migrate():
    db = get_db()
    
    for collection_name, filename in COLLECTIONS.items():
        filepath = os.path.join(DATA_DIR, filename)
        
        if not os.path.exists(filepath):
            print(f"⚠️  Skipping {filename} (file not found)")
            continue
        
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        # Settings is a single object, not an array
        if collection_name == "settings":
            await db[collection_name].delete_many({})
            await db[collection_name].insert_one(data)
            print(f"✅ {collection_name}: Imported 1 document")
        else:
            if not isinstance(data, list):
                data = [data]
            
            if len(data) == 0:
                print(f"⚠️  {collection_name}: Empty array, skipping")
                continue
            
            # Clear existing and insert
            await db[collection_name].delete_many({})
            result = await db[collection_name].insert_many(data)
            print(f"✅ {collection_name}: Imported {len(result.inserted_ids)} documents")
    
    print("\n🎉 MongoDB migration complete!")
    
    # Verify counts
    print("\n📊 Verification:")
    for collection_name in COLLECTIONS:
        count = await db[collection_name].count_documents({})
        print(f"   {collection_name}: {count} documents")

if __name__ == "__main__":
    asyncio.run(migrate())
