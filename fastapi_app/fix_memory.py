import os
import sys
import asyncio

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import update_memory

async def main():
    memory_id = 31
    new_desc = "It was one of the most lovely, spontaneous dates for dinner. We started with some late night driving, enjoying the night vibe with the sunroof open. We went to Pacific Mall in Jasola Vihar and decided to eat at Cafe Delhi Heights. It was definitely one of the best food dates and a perfect spontaneous late-night dinner date!"
    
    smart_data = {
        "itinerary": [
            {"item": "Late Night Drive around enjoying the night vibe with the sunroof open.", "icon": "directions_car", "highlight": False},
            {"item": "I painted your nails, which was such a sweet and intimate moment. You looked so beautiful in that cute dress.", "icon": "favorite", "highlight": True},
            {"item": "Amazing dinner spread at Cafe Delhi Heights.", "icon": "restaurant", "highlight": False},
            {"item": "The next day we clicked so many cute photos and selfies together.", "icon": "photo_camera", "highlight": False}
        ],
        "entities": {
            "food": ["Mushroom Soup", "Red Sauce Spaghetti", "Frozen Hot Chocolate"],
            "places": ["Pacific Mall, Jasola Vihar", "Cafe Delhi Heights"]
        },
        "vibe": "Foodie Heaven 😋"
    }

    await update_memory(memory_id, {"description": new_desc, "smart_data": smart_data})
    print(f"Updated memory {memory_id}")

if __name__ == "__main__":
    asyncio.run(main())
