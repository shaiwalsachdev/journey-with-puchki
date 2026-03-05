import asyncio
import traceback
from fastapi_app.database import get_db

async def fix():
    try:
        db = get_db()
        memories = await db.memories.find({}).to_list(100)
        print(f"Checking {len(memories)} memories...")
        for m in memories:
            if "photos" in m and isinstance(m["photos"], list):
                cleaned = [p for p in m["photos"] if not p.lower().endswith((".heic", ".ds_store"))]
                if len(cleaned) < len(m["photos"]):
                    await db.memories.update_one({"id": m["id"]}, {"$set": {"photos": cleaned}})
                    print(f"Cleaned memory {m['id']}: removed {len(m['photos']) - len(cleaned)} HEIC/unsupported files.")
        print("Done checking all memories.")
    except Exception as e:
        print("Error:", e)
        traceback.print_exc()

asyncio.run(fix())
