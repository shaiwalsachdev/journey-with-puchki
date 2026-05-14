import asyncio
from database import update_memory, get_memory_by_id

async def main():
    memory_id = 30
    
    update_data = {
        "comments": [],
        "hide_all_photos": False,
        "hidden_photos": [],
        "rating": 5,
        "smart_data": {
            "itinerary": [
                {"item": "Went to Kokoy cafe for a beautiful day out"},
                {"item": "Had the best turmeric latte and Neapolitan-style veggie pizza"},
                {"item": "Admired how pretty you looked in that dress"},
                {"item": "Visited the beautiful cafe Camo with an amazing vibe"},
                {"item": "Enjoyed mushroom chai with kulcha and the tastiest paneer stuffed tikka"},
                {"item": "Drove back with the sunroof open"}
            ],
            "entities": {
                "places": [
                    "Kokoy Cafe",
                    "Camo Cafe"
                ],
                "food": [
                    "Turmeric Latte",
                    "Neapolitan Veggie Pizza",
                    "Mushroom Chai",
                    "Kulcha",
                    "Paneer Stuffed Tikka"
                ],
                "vibe": [
                    "Beautiful Day",
                    "Great Experience",
                    "Amazing Vibe",
                    "Long Drive"
                ]
            }
        },
        "days_journey": None
    }
    
    await update_memory(memory_id, update_data)
    print("Memory 30 updated with smart_data, comments, rating, and tags.")

if __name__ == "__main__":
    asyncio.run(main())
