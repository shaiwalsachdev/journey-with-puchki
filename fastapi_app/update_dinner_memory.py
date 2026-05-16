import os
import sys
import asyncio

# Add current dir to path to import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import update_memory, get_all_memories

async def main():
    memories = await get_all_memories()
    dinner_memory = None
    for m in memories:
        if m.get("title") == "Dinner date" and "Cafe Delhi Heights" in m.get("description", ""):
            dinner_memory = m
            break
            
    if dinner_memory:
        new_desc = '''It was one of the most lovely, spontaneous dates for dinner, and it started with some late night driving. We went to Pacific Mall in Jasola Vihar and decided to eat at Cafe Delhi Heights.

**Itinerary:**
1. **Late Night Drive:** Driving around enjoying the night vibe with the sunroof open.
2. **Nail Painting Session:** I painted your nails, which was such a sweet and intimate moment. You looked so beautiful in that cute dress, and I loved the feeling of holding your hands.
3. **Dinner at Cafe Delhi Heights:** We had an amazing dinner spread.
4. **Photoshoot (May 16):** The next day we clicked so many cute photos and selfies together.

**Food Tags:**
- Mushroom Soup (one of the absolute best!)
- Red Sauce Spaghetti (so saucy and delicious)
- Frozen Hot Chocolate (the true showstopper)

**Place Tags:**
- Pacific Mall, Jasola Vihar
- Cafe Delhi Heights

This was definitely one of the best food dates and a perfect spontaneous late-night dinner date!'''
        await update_memory(dinner_memory["id"], {"description": new_desc})
        print(f"Updated memory {dinner_memory['id']}")
    else:
        print("Memory not found")

if __name__ == "__main__":
    asyncio.run(main())
