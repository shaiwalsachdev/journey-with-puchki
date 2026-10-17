import asyncio
import sys

sys.path.append("/Users/geekdon/Documents/Journey with Puchki")
from fastapi_app.database import get_memory_by_id, update_memory

async def main():
    memory_id = 41
    print(f"Fetching memory {memory_id}...")
    memory = await get_memory_by_id(memory_id)
    if memory:
        description = """
        <p class="mb-4">It was an amazing day! You helped so much picking out some <b>great clothes from Allen Solly</b> and <b>shoes from US Polo and Lifestyle</b>.</p>
        <p class="mb-4">We had an absolutely amazing ice cream date at <b>Frozen Fun</b>—the mango yogurt ice cream was so good!</p>
        <p>The long drive back home got really rough. We had to wait in a long line for South Indian food, which left you starving. We ended up having a big fight because you were so angry with me. We eventually left and just drove back home without eating.</p>
        """.strip()
        
        smart_data = memory.get("smart_data", {})
        smart_data["summary"] = "Shopping at Allen Solly, US Polo, and Lifestyle, followed by mango yogurt ice cream at Frozen Fun. Ended with a long drive home, a fight, and missed South Indian food."
        smart_data["vibe"] = "Productive, sweet but ended in a big fight 😅"
        
        print(f"Updating memory {memory_id}...")
        await update_memory(memory_id, {"description": description, "smart_data": smart_data})
        print("Successfully updated memory description and smart data!")
    else:
        print("Memory not found!")

if __name__ == "__main__":
    asyncio.run(main())
