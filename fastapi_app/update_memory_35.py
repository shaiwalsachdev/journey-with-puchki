import asyncio
import os
import sys

# Add current dir to path to import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import get_memory_by_id, update_memory

async def main():
    memory_id = 35
    
    memory = await get_memory_by_id(memory_id)
    if not memory:
        print(f"Memory {memory_id} not found!")
        return

    update_data = {
        "title": "Disappointing Food but pretty gorgeous you",
        "date": "June 5, 2026",
        "description": "It was an exciting Friday date night, but unfortunately, the food was a massive letdown from start to finish. We began with Mushroom Galauti Kebabs, but they were incredibly bland and completely lacked salt. The lime soda was equally disappointing and just tasted very bad. Hoping for a better experience, we moved to Cafe Delhi Heights. There, we ordered Veg Fajitas which came full of paneer, veggies, and tortilla wraps, along with Railway Cutlets and a Tiramisu pastry for dessert. Sadly, all of them tasted really bad as well. It definitely switched our moods off, especially after I had such a busy and exhausting day at work and felt like I disappointed you by not being fully present. Despite the awful food and the off mood, I kept trying my best to make you happy throughout the evening. The absolute highlight of the night was you—you were looking so incredibly beautiful and hot in your stunning black dress! It completely made up for the bad food. I finally dropped you off late at night around 11:45 PM, ending a mixed but memorable Friday."
    }
    
    print(f"Updating memory {memory_id}...")
    await update_memory(memory_id, update_data)
    print("Memory updated successfully!")

if __name__ == "__main__":
    asyncio.run(main())
