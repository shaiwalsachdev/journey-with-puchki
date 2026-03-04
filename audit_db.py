import asyncio
from fastapi_app.database import get_db
import pprint

async def verify():
    client = get_db()
    c = await client.memories.count_documents({})
    msgs = await client.memories.find({}).sort("id", 1).to_list(100)
    for m in msgs:
        print(f"--- ID {m.get('id')} ---")
        print(f"Title: {m.get('title')}")
        print(f"Safe Title: {m.get('title_safe')}")
        print(f"Date: {m.get('date')}")
        print(f"Desc: {m.get('description')}")
        print(f"Safe Desc: {m.get('description_safe')}")
        print(f"Photos ({len(m.get('photos', [])) if m.get('photos') else 0}): {m.get('photos')}")
        print(f"Itinerary: {len(m.get('smart_data', {}).get('itinerary', []))} items")
        print()
    
asyncio.run(verify())
