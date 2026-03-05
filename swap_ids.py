import asyncio
from fastapi_app.database import get_db

async def swap():
    db = get_db()
    
    # Get both memories
    m23 = await db.memories.find_one({"id": 23})
    m24 = await db.memories.find_one({"id": 24})
    
    print(f"Before swap:")
    print(f"  ID 23: {m23.get('title')} | {m23.get('date')}")
    print(f"  ID 24: {m24.get('title')} | {m24.get('date')}")
    
    # Temporarily assign ID 99 to avoid collision
    await db.memories.update_one({"id": 23}, {"$set": {"id": 99}})
    await db.memories.update_one({"id": 24}, {"$set": {"id": 23}})
    await db.memories.update_one({"id": 99}, {"$set": {"id": 24}})
    
    m23_new = await db.memories.find_one({"id": 23})
    m24_new = await db.memories.find_one({"id": 24})
    
    print(f"\nAfter swap:")
    print(f"  ID 23: {m23_new.get('title')} | {m23_new.get('date')}")
    print(f"  ID 24: {m24_new.get('title')} | {m24_new.get('date')}")

asyncio.run(swap())
