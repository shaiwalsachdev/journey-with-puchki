import asyncio
from database import update_memory

async def main():
    memory_id = 30
    
    update_data = {
        "type": "date"
    }
    
    await update_memory(memory_id, update_data)
    print("Memory 30 updated: type changed to date")

if __name__ == "__main__":
    asyncio.run(main())
