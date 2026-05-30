import os
import sys
import asyncio

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from database import update_memory

async def main():
    smart_data = {
        "itinerary": [
            {"item": "Met at Eye of Turtle studio (B-502, Victory Cross Roads, Sector 143 Noida). Reviewed amazing cinematic films, teasers, and photos.", "icon": "camera_alt", "highlight": True},
            {"item": "Finalized the photographer for our wedding shoot! Left dreaming of the price asked for pre-wedding.", "icon": "favorite", "highlight": True},
            {"item": "Visited Alma Bakery and Cafe at Advant Sector 142 Noida for a healthy food date.", "icon": "restaurant", "highlight": False},
            {"item": "Enjoyed delicious ABC juice, Watermelon juice, and an amazing vegetarian paneer dish.", "icon": "local_dining", "highlight": True},
            {"item": "Tried the kidney bean patty burger (not very tasty) with sugar-free cold coffee and detox juice.", "icon": "local_cafe", "highlight": False},
            {"item": "Gifted beautiful flowers, captured lots of studio photos and videos with amazing songs playing in the background.", "icon": "photo_library", "highlight": True},
            {"item": "Ended the day with a beautiful long drive back home and received Khattu Shyam Ji's charan and prasad blessings.", "icon": "directions_car", "highlight": True}
        ],
        "entities": {
            "food": ["ABC juice", "Watermelon Juice", "Alma's vegetarian paneer dish", "Kidney bean patty burger", "Sugar free cold coffee with whipped cream", "Detox juice", "Prasad"],
            "places": ["Victory Cross Roads Sector 143 Noida", "Eye of Turtle studio", "Alma Bakery and Cafe", "Advant Sector 142 Noida"]
        },
        "vibe": "Studio Visit & Cafe Date 📸☕",
        "rating": 5,
        "comment": "Finalized the photographer for our wedding shoot! Left dreaming of the price asked for pre-wedding. Amazing healthy food at Alma cafe, lovely long drive back home, and received Khattu Shyam Ji's charan and prasad. Blessings upon us!"
    }

    update_data = {
        "description": "An <b>incredibly amazing day!</b> We started by meeting at <b>Victory Cross Roads, Sector 143 Noida (B-502)</b>, at the <b>Eye of Turtle studio</b>.<br><br>We were completely blown away by the <b>amazing quality of their work</b>—ranging from their stunning videos, short teasers, cinematic films, and photos, to their beautiful story narration and performance videos.<br><br>After thoroughly discussing everything, we <b>finalized the photographer for our wedding shoot!</b> We left <b>dreaming of the price asked for pre-wedding</b>, but we felt a sense of excitement and relief.<br><br>Afterwards, it was amazing to visit a new healthy spot: <b>Alma Bakery and Cafe</b> at <b>Advant Sector 142 Noida</b>.<br><br>We tried their amazing <b>ABC juice</b> and refreshing <b>Watermelon Juice</b>. We also had Alma's <b>vegetarian paneer dish</b>, which was incredibly tasty, healthy, and just amazing!<br><br>Following that, we tried their <b>kidney bean patty burger</b> (though sadly it was not tasty at all), paired with a <b>sugar-free cold coffee</b> topped with whipped cream. You also tried their <b>detox juice</b> which turned out quite tasty.<br><br>We talked, laughed, and enjoyed so much. I gave you <b>beautiful flowers</b> and you just kept smiling. We also took so many wonderful photos and videos together at the studio, listening to amazing songs.<br><br>To top it all off, we went on a <b>beautiful long drive back home</b> which was so relaxing.<br><br>Finally, thank you so much for bringing the pretty <b>Khattu Shyam Ji ke charan and sweet prasad</b>. We feel so blessed to have so much blessings upon us today.",
        "smart_data": smart_data
    }
    
    print("Updating memory 34...")
    await update_memory(34, update_data)
    print("Memory 34 updated successfully!")

if __name__ == "__main__":
    asyncio.run(main())
