import asyncio
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from fastapi_app.database import get_db, add_memory

memory_1 = {
    "id": 1,
    "date": "August 30, 2025",
    "title": "Matched on Hinge",
    "title_safe": "A Special Beginning",
    "description": "Loved the energy fun positive dancer vibes talented foodie. After a lot of discussions on life and relationships and kundli matching being on point 32/36. Connected on Instagram Shared life past stories and stalked each other posts. After a month, we Talked over phone and it felt connected right through the heart talking about future marriage astrology and that 1 hour of call is still best memory.",
    "description_safe": "We first connected and our stars matched perfectly (32/36!). We shared stories, and after a month, we had our first long phone call. We talked for an hour about the future, astrology, and life—it's still one of my best memories.",
    "photos_folder": "1",
    "type": "start",
    "photos": ["Hinge.jpg", "kundli matching.jpeg"],
    "smart_data": {
        "itinerary": [
            {
                "item": "Matched on Hinge and loved the energy, fun, positive dancer vibes.",
                "item_safe": "We first matched and loved each other's positive energy.",
                "icon": "favorite",
                "highlight": True
            },
            {
                "item": "Kundli matching was on point at 32/36.",
                "icon": "stars",
                "highlight": False
            },
            {
                "item": "Connected on Instagram and shared life stories.",
                "icon": "chat",
                "highlight": False
            },
            {
                "item": "Had a 1-hour phone call discussing the future, marriage, and astrology.",
                "item_safe": "Had a long phone call discussing our hopes for the future.",
                "icon": "phone",
                "highlight": True
            }
        ],
        "entities": {
            "food": [],
            "places": ["Hinge", "Instagram"]
        },
        "vibe": "Sparks Flying ✨"
    }
}

async def main():
    await add_memory(memory_1)
    print("Memory 1 added to MongoDB")

if __name__ == "__main__":
    asyncio.run(main())
