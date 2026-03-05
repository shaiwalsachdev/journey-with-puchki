import asyncio
from fastapi_app.database import get_db

async def fix():
    db = get_db()
    await db.memories.update_one({"id": 23}, {"$set": {"type": "hot"}})
    m = await db.memories.find_one({"id": 23})
    print("Memory 23 type updated to:", m.get("type"))

asyncio.run(fix())
