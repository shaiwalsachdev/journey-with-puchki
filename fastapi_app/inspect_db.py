import asyncio
import json
from database import get_memory_by_id, get_all_memories

async def main():
    # Let's get all memories and find a rich one
    memories = await get_all_memories()
    # print the keys of memory with id 29 or 28
    for mem in memories[-5:]:
        print(f"Memory {mem['id']}: {mem.get('title')}")
        print(json.dumps(mem, indent=2))
        print("-" * 50)

if __name__ == "__main__":
    asyncio.run(main())
