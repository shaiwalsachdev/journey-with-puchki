import asyncio
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import update_memory, get_memory_by_id

async def main():
    memory_id = 32
    m = await get_memory_by_id(memory_id)
    if m:
        new_desc = m.get("description", "") + " We also had some amazing pizza and a chocolate shake."
        smart_data = m.get("smart_data", {})
        
        # update itinerary
        if "itinerary" in smart_data:
            smart_data["itinerary"].append({
                "item": "Enjoyed amazing pizza and a chocolate shake.",
                "icon": "local_pizza",
                "highlight": False
            })
            
        # update food entities
        if "entities" in smart_data and "food" in smart_data["entities"]:
            smart_data["entities"]["food"].extend(["Pizza", "Chocolate Shake"])
            
        await update_memory(memory_id, {"description": new_desc, "smart_data": smart_data})
        print(f"Updated memory {memory_id} with pizza and shake.")
    else:
        print("Memory not found")

if __name__ == "__main__":
    asyncio.run(main())
