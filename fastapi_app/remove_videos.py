import asyncio
from database import get_memory_by_id, update_memory

async def main():
    memory_id = 30
    
    # Get memory
    memory = await get_memory_by_id(memory_id)
    if not memory:
        print("Memory not found!")
        return
        
    photos = memory.get("photos", [])
    
    # Files to remove
    to_remove = ["tmpagxzhtd9.mp4", "tmpkr13ywxh.mp4", "tmpi96ws3ef.mp4"]
    
    # Filter out
    filtered_photos = [p for p in photos if p not in to_remove]
    
    if len(filtered_photos) < len(photos):
        await update_memory(memory_id, {"photos": filtered_photos})
        print(f"Removed {len(photos) - len(filtered_photos)} files from memory 30.")
    else:
        print("Files not found in memory.")

if __name__ == "__main__":
    asyncio.run(main())
