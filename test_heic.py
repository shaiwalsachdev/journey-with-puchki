import asyncio
from fastapi_app.database import get_db

async def test():
    db = get_db()
    m = await db.memories.find_one({"id": 22})
    if m and "photos" in m:
        photos = m["photos"]
        print("Total photos:", len(photos))
        print("First 5 photos:", photos[:5])
        cleaned = [p for p in photos if not p.lower().endswith((".heic", ".ds_store"))]
        print("Cleaned photos size:", len(cleaned))
        if len(cleaned) < len(photos):
            print("Cleanup would remove files!")
        else:
            print("Cleanup did NOT remove files. Why? Let's check the types.")
            print([type(p) for p in photos[:5]])

asyncio.run(test())
