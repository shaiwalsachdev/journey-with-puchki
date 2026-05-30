import os
import sys
import asyncio

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from database import update_memory

async def main():
    update_data = {
        "type": "date"
    }
    
    print("Updating memory 34 type to 'date'...")
    await update_memory(34, update_data)
    print("Memory 34 updated successfully!")

if __name__ == "__main__":
    asyncio.run(main())
