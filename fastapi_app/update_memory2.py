import asyncio
from database import update_memory, get_memory_by_id

async def main():
    memory_id = 30
    
    new_description = """It was a beautiful day. We went to **Kokoy Cafe** and had the best turmeric latte and an authentic Neapolitan-style veggie pizza. You looked absolutely stunning in that pretty dress.

After that great experience, we went to another beautiful spot, **Camo Cafe**, which had an amazing vibe. We enjoyed their unique mushroom chai with kulcha, along with the most delicious paneer stuffed tikka.

The perfect end to the day was the long drive back home, with the sunroof open and the wind in our hair."""
    
    update_data = {
        "description": new_description,
        "template": "memory_family.html"
    }
    
    await update_memory(memory_id, update_data)
    print("Memory 30 updated: Description formatted, template changed to memory_family.html")

if __name__ == "__main__":
    asyncio.run(main())
