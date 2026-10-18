"""
Default structured itinerary, visa guide, dining options, and checklists for Singapore Honeymoon (Dec 13-21, 2026)
Featuring Disney Adventure Cruise, Disney Princess & Mickey & Minnie Magic!
"""

DEFAULT_HONEYMOON_DATA = {
    "title": "Singapore & Disney Princess Honeymoon 🇸🇬✨🏰",
    "subtitle": "13–21 December 2026 · Shaiwal & Shaila (Our Fairytale Magic)",
    "dates": "Dec 13 - Dec 21, 2026 (8 Nights / 9 Days)",
    "overview": "Disney Adventure Cruise (Mickey, Minnie, Princess Fairytale & Marvel at sea!), 4 nights at Oasia Resort Sentosa, Pandas at River Wonders, Cable Car SkyPass, Gardens by the Bay, Marina Bay Sands SkyPark & Romantic Dining.",
    
    # Stay Plan with Verified Hotel Policies, Photos & Booking Rules
    "stays": [
        {
            "id": "stay-carlton",
            "dates": "13–14 December 2026 (1 Night)",
            "hotel": "Carlton Hotel Singapore",
            "type": "City Luxury Hotel (Opposite CHIJMES & Raffles)",
            "address": "76 Bras Basah Road, City Hall, Singapore 189558",
            "website": "https://www.carltonhotel.sg/",
            "photo": "https://images.unsplash.com/photo-1566073771259-6a8506099945?q=80&w=1200&auto=format&fit=crop",
            "checkin": "3:00 PM",
            "checkout": "12:00 PM (Noon)",
            "deposit": "SGD 100 per night (Credit Card pre-authorization on arrival, refunded upon room check)",
            "policies": [
                "Strictly Non-Smoking property (SGD 500 deep-cleaning penalty for in-room smoking)",
                "Minimum age 18 for primary guest (Original Indian Passport matching booking name mandatory)",
                "Early luggage drop available free of charge at concierge on arrival",
                "Complimentary high-speed Wi-Fi, swimming pool with sun-loungers & 24/7 fitness center"
            ],
            "notes": "Arrive at Changi Airport around 6:00 PM. Take Grab taxi (~20 mins, ~SGD 25–35) to Carlton. Perfect location across the street from historic CHIJMES courtyards for an enchanting first night dinner.",
            "badge": "1 Night · City Center"
        },
        {
            "id": "stay-disney",
            "dates": "14–17 December 2026 (3 Nights)",
            "hotel": "Disney Adventure Cruise Line 🚢✨",
            "type": "Disney Magic at Sea (Singapore Roundtrip)",
            "address": "Marina Bay Cruise Centre Singapore (MBCCS), 61 Marina Coastal Drive",
            "website": "https://disneycruise.disney.go.com/en-in/ships/adventure/",
            "photo": "https://images.unsplash.com/photo-1548574505-5e239809ee19?q=80&w=1200&auto=format&fit=crop",
            "checkin": "All Aboard: 4:00 PM (Ship sails at 5:00 PM on 14 Dec)",
            "checkout": "Debarkation: 7:00 AM (17 Dec)",
            "deposit": "Stateroom 11680 Paid in Full ✅ (Credit card pre-authorization for onboard incidental purchases)",
            "policies": [
                "Online Check-In begins 14 November 2026 (select earliest Port Arrival Time / PAT window)",
                "Strictly NO garment steamers, electric irons, heating appliances or extension cords",
                "NO smoking or vaping on verandahs (strictly allowed only in designated open-air deck smoking zones)",
                "Alcohol policy: Max 2 unopened bottles of wine/champagne (750ml) or 6 beers per adult (21+) strictly in carry-on hand luggage"
            ],
            "notes": "Stateroom 11680 (Category 06C Deluxe Oceanview with Verandah, Deck 11 Midship). Reservation #44985264. Broadway shows at 5:45 PM & Rotational Main Dining at 8:15 PM.",
            "badge": "3 Nights · Disney Cruise"
        },
        {
            "id": "stay-oasia",
            "dates": "17–21 December 2026 (4 Nights)",
            "hotel": "Oasia Resort Sentosa",
            "type": "Luxury Island Sanctuary by Far East Hospitality",
            "address": "23 Beach View, Palawan Ridge, Sentosa Island, Singapore 098679",
            "website": "https://www.fareasthospitality.com/en/Hotels-and-Serviced-Residences/Hotels/Oasia-Resort-Sentosa",
            "photo": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?q=80&w=1200&auto=format&fit=crop",
            "checkin": "3:00 PM (Early luggage storage free upon arrival from cruise)",
            "checkout": "12:00 PM (Noon)",
            "deposit": "SGD 50 per room, per night (SGD 200 total for 4 nights, credit/debit card pre-auth, refunded at checkout)",
            "policies": [
                "Strict No-Name-Change policy (Original passport matching reservation name required)",
                "Strictly Non-Smoking property across all guest rooms",
                "Complimentary Sentosa Express monorail pass & free island transit throughout your stay",
                "Direct 2-minute walk to Imbiah Monorail Station (easy access to Universal, S.E.A. Aquarium & Beaches)"
            ],
            "notes": "Base resort for Sentosa Island. Disembark Disney Cruise at 7:00 AM on 17 Dec, take taxi straight to Oasia Resort, drop luggage with concierge, refresh, and start Sentosa exploration!",
            "badge": "4 Nights · Island Luxury"
        }
    ],

    # Confirmed Disney Cruise Reservation Details (Dec 14-17, 2026)
    "cruise_booking": {
        "ship": "Disney Adventure 🚢✨",
        "reservation_number": "44985264",
        "stateroom": "11680",
        "stateroom_type": "Deluxe Oceanview Stateroom with Verandah (Category 06C)",
        "deck": "Deck 11 · Midship",
        "guests": ["SHAIWAL SACHDEV", "SHAILA MANAKTAHLA"],
        "status": "Paid in Full ✅",
        "dates": "14 - 17 December 2026 (3-Night Cruise from Singapore)",
        "support_phone": "+91 80357-38899",
        "support_hours": "Mon-Fri: 8:00 AM - 10:00 PM IST | Sat-Sun: 9:00 AM - 8:00 PM IST",
        "online_checkin_date": "14 November 2026",
        "activities_booking_deadline": "11 December 2026",
        "dining_seating": "8:15 PM Main Dining (Rotational Dining)",
        "evening_show_time": "5:45 PM Signature Theatre Show",
        "all_aboard_time": "4:00 PM (14 Dec 2026)",
        "departure_time": "5:00 PM (14 Dec 2026)",
        "debarkation_time": "7:00 AM (17 Dec 2026)"
    },

    # Disney Cruise Rules, Regulations, Do's and Don'ts
    "cruise_rules": {
        "prohibited_items": [
            {"item": "No Irons, Steamers or Heating Appliances", "reason": "Strict fire hazard. Clothing steamers, electric irons, hot plates, and heating pads are confiscated at embarkation. Laundry/pressing services are available on board.", "icon": "iron"},
            {"item": "No Extension Cords or Surge Protectors", "reason": "Surge protectors interfere with the ship's marine electrical safety system. Multi-port USB hubs without surge protectors are permitted.", "icon": "electrical_services"},
            {"item": "No Hookah, Vapes or E-Cigarettes in Staterooms / Verandah", "reason": "Smoking or vaping on verandahs or in staterooms carries a $250+ cleaning fine and possible debarkation. Smoking is ONLY permitted in designated open-air deck smoking zones.", "icon": "vape_free"},
            {"item": "No Hard Liquor or Spirits Brought Onboard", "reason": "Hard liquor is prohibited in carry-on and checked luggage. Each adult (21+) is allowed to bring up to 2 bottles of unopened wine/champagne (750ml) OR six 355ml beers strictly in carry-on luggage at embarkation.", "icon": "no_drinks"},
            {"item": "No Drones, Kites or Remote Air Toys", "reason": "Prohibited maritime regulation. Drones will be confiscated at port security.", "icon": "flight_disturb"},
            {"item": "No Candles, Incense or Open Flames", "reason": "Open flames of any kind are strictly prohibited at sea.", "icon": "fire_extinguisher"},
            {"item": "No Weapons, Toy Replicas or Fireworks", "reason": "Any realistic toy guns, swords, knives, or flammable devices are strictly barred.", "icon": "shield"}
        ],
        "important_dos": [
            {"title": "Online Check-In on 14 Nov 2026", "desc": "Check-in opens midnight 14 November. Upload passport photos and immediately select the earliest Port Arrival Time (PAT) window for priority boarding!", "badge": "14 Nov 2026"},
            {"title": "Carry Critical Items in Hand Luggage", "desc": "Keep passports, Singapore e-Visa printouts, cruise documents, jewelry, medications, and your first-day swimwear/clothes in hand luggage. Checked bags arrive at your stateroom late afternoon.", "badge": "Embarkation Day"},
            {"title": "Mandatory Guest Assembly Drill", "desc": "Complete the safety check-in via the Disney Cruise Line Navigator App upon boarding and report to your designated assembly muster station before sail away (around 3:45 PM).", "badge": "Mandatory Safety"},
            {"title": "Download Disney Cruise Navigator App", "desc": "Essential on board (works on ship's complimentary intranet without paying for internet). Unlocks daily schedules, character meet & greets, chat, deck plans, and restaurant menus.", "badge": "App Required"},
            {"title": "Book Royal Gathering & Princess Meets Promptly", "desc": "As soon as you board and connect to ship Wi-Fi, open the Navigator app to book the free Disney Princess Royal Gathering slots before they fill up.", "badge": "Princess Magic"},
            {"title": "Attend Rotational Dining at 8:15 PM", "desc": "Your assigned table follows you each night. Inform Disney in advance if you have vegetarian/Jain dietary needs via Special Requests.", "badge": "Table Reserved"},
            {"title": "Catch 5:45 PM Broadway Shows", "desc": "Arrive 15–20 minutes early at the Walt Disney Theatre to get the best honeymoon seats for Broadway musicals before dinner.", "badge": "Entertainment"}
        ],
        "verandah_safety": [
            "Never leave verandah furniture near railings or sit on railings.",
            "Always lock the childproof safety latch on the verandah sliding glass door.",
            "Do not hang towels or clothing to dry on verandah railings (they can blow overboard).",
            "Keep the verandah exterior door closed when using room air conditioning to prevent condensation."
        ]
    },

    # Comprehensive Disney Adventure Deck-by-Deck Activity Guide (Based on Official Tour)
    "cruise_activities": {
        "video_url": "https://youtu.be/dA3clKO6qeY?si=NesYyPfoRNYgZrw-",
        "video_title": "Disney Adventure Full Ship Walking Tour & Activities Blueprint",
        "decks": [
            {
                "deck": "Deck 18: Marvel Landing, Pools & Upper Thrills",
                "badge": "Top Deck Adrenaline",
                "activities": [
                    {"name": "Groot Galaxy Spin", "time": "15:11 & 1:49:22", "desc": "High-energy spinner ride with upbeat cosmic tunes high above the open sea.", "icon": "toys"},
                    {"name": "PYM Quantum Racers", "time": "18:18 & 1:48:34", "desc": "Ant-Man & The Wasp themed mini electric race cars on an open-air track with panoramic ocean views.", "icon": "sports_motorsports"},
                    {"name": "Upper Infinity Pool", "time": "16:47 & 1:50:05", "desc": "Cantilevered glass infinity pool hanging right over the ship's edge overlooking endless ocean horizons.", "icon": "pool"},
                    {"name": "Waterslides & Waterpark", "time": "1:41:54", "desc": "Multi-story twisting body slides, splash zones, and aqua water coasters for sunny afternoon fun.", "icon": "water"},
                    {"name": "Wheezy's Freezies", "time": "1:43:45", "desc": "Toy Story poolside soft-serve ice cream and frozen smoothies.", "icon": "icecream"},
                    {"name": "Pizza Planet", "time": "1:44:55", "desc": "Grab hot fresh slices of pizza right on the pool deck anytime.", "icon": "local_pizza"}
                ]
            },
            {
                "deck": "Deck 6: Town Square, Princess Hall & Rotational Dining",
                "badge": "Royal Fairytale & Gala",
                "activities": [
                    {"name": "Town Square Grand Hall & Royal Court", "time": "34:35 & 36:36", "desc": "Majestic multi-deck atrium inspired by Disney Castle with crystal chandeliers, grand staircase, and Princess meet & greets.", "icon": "castle"},
                    {"name": "Spellbound Lounge", "time": "35:36", "desc": "Intimate fairy-godmother / evil queen inspired cocktail parlor for enchanting evening craft drinks.", "icon": "local_bar"},
                    {"name": "Maximus & Olaf Themed Dining Rooms", "time": "38:18 & 39:28", "desc": "Tangled and Frozen themed companion dining halls filled with storybook artistry and Nordic ice motifs.", "icon": "restaurant"},
                    {"name": "Navigator's Club", "time": "41:45 & 2:02:14", "desc": "Nautical club celebrating the golden age of seafaring with Captain Mickey maritime portraits.", "icon": "explore"},
                    {"name": "Buccaneer Bar", "time": "43:21", "desc": "Pirates of the Caribbean themed tavern with craft grog, rum cocktails, and lively sea shanties.", "icon": "sports_bar"},
                    {"name": "Animator's Palate", "time": "46:45 & 2:01:37", "desc": "Famous Disney dining room where your personal sketches come to life dancing on giant digital walls!", "icon": "draw"},
                    {"name": "Tiana's Bayou Lounge", "time": "50:42", "desc": "Princess and the Frog New Orleans jazz parlor serving warm powdered beignets, chicory coffee, and southern mocktails.", "icon": "music_note"}
                ]
            },
            {
                "deck": "Deck 7: Entertainment, San Fransokyo & Baymax",
                "badge": "Broadway Musicals & Pixar Fun",
                "activities": [
                    {"name": "Walt Disney Theatre", "time": "21:50", "desc": "Spectacular 1,200+ seat Broadway showhouse hosting full Disney musical stage productions like 'Remember'.", "icon": "theater_comedy"},
                    {"name": "San Fransokyo Street", "time": "7:08 & 25:23", "desc": "Big Hero 6 Tokyo-meets-San-Francisco street market with neon signs, interactive street games, and character encounters.", "icon": "storefront"},
                    {"name": "Baymax Cinemas", "time": "30:14", "desc": "Twin ultra-plush state-of-the-art Dolby cinema screening first-run Disney, Marvel, and Star Wars movies throughout the voyage.", "icon": "movie"},
                    {"name": "D Lounge", "time": "22:34", "desc": "Family game show studio, couples karaoke, Disney trivia showdowns, and live bingo games.", "icon": "mic"},
                    {"name": "Marvel Style Studio", "time": "45:08", "desc": "Heroic apparel, couture Marvel jackets, pins, and custom superhero souvenir styling.", "icon": "checkroom"}
                ]
            },
            {
                "deck": "Deck 11: Imagination Garden & Open-Air Stage",
                "badge": "Heart of the Ship",
                "activities": [
                    {"name": "Disney Imagination Garden & Castle Stage", "time": "1:13:19", "desc": "Enchanted central open-air atrium featuring Sorcerer Mickey topiary and open-air stage for headline productions.", "icon": "park"},
                    {"name": "LET'S SET SAIL PARTY Show", "time": "8:30", "desc": "Embarkation sail-away musical celebration with Mickey, Minnie, Donald, and Goofy dancing on top deck!", "icon": "celebration"},
                    {"name": "AVENGERS ASSEMBLE! Live Stunt Show", "time": "1:16:27", "desc": "Live acrobatic rooftop battle featuring Spider-Man, Iron Man, Captain America, and Black Widow.", "icon": "shield"},
                    {"name": "Mowgli's Eatery", "time": "1:14:22", "desc": "Jungle Book themed quick-service dining serving flavorful Indian-inspired wraps, samosas, curries, and spiced street bites.", "icon": "takeout_dining"},
                    {"name": "Gramma Tala's Kitchen", "time": "1:15:18", "desc": "Moana Pacific Islander flavors: poke bowls, grilled skewers, and tropical fruit platters.", "icon": "soup_kitchen"},
                    {"name": "Garden Bar", "time": "1:12:13", "desc": "Alfresco bar overlooking the castle courtyard for chilled beer and floral mocktails.", "icon": "local_cafe"}
                ]
            },
            {
                "deck": "Decks 12–14: Wayfinder Bay, Discovery Reef & Adult Romance",
                "badge": "Romantic Adults Oasis",
                "activities": [
                    {"name": "Wayfinder Bay Pools & Sunset Amphitheater", "time": "1:26:12", "desc": "Moana open-ocean poolside deck with tiered daybeds and infinity horizon views.", "icon": "wb_twilight"},
                    {"name": "MOANA: CALL OF THE SEA Live Show", "time": "1:27:40", "desc": "Original island theatrical musical featuring live drumming, water effects, and ocean chants.", "icon": "surfing"},
                    {"name": "Palo Trattoria", "time": "1:32:51", "desc": "Adult-exclusive upscale Italian fine dining with antipasti carts, handmade pastas, and premium wines.", "icon": "dinner_dining"},
                    {"name": "Mike & Sulley's Asian Eatery & Omakase Teppanyaki", "time": "1:34:23 & 1:34:49", "desc": "Monsters, Inc. themed Teppanyaki grill with interactive chefs and fresh sushi counters.", "icon": "set_meal"},
                    {"name": "Cosmic Kebabs & Stitch's 'Ohana Grill", "time": "1:36:05 & 1:37:47", "desc": "Mediterranean shawarma & Hawaiian pineapple burgers by the open ocean breeze.", "icon": "kebab_dining"},
                    {"name": "Bewitching Boba & Brews", "time": "1:38:45", "desc": "Ursula themed bubble tea bar with popping boba, cold brew teas, and mocktails.", "icon": "emoji_food_beverage"},
                    {"name": "The Lion King: Celebration in the Sky (Fireworks)", "time": "2:37:20", "desc": "Disney's world-famous fireworks bursting into the midnight sky over the high seas synchronized to Lion King melodies!", "icon": "auto_awesome"}
                ]
            },
            {
                "deck": "Deck 9 & 10: Wellness, Spa & Midnight Strolls",
                "badge": "Spa, Serenity & Stateroom",
                "activities": [
                    {"name": "Infinite Bliss Spa & Couples Retreat", "time": "1:08:39", "desc": "Aromatherapy steam rooms, dry sauna, heated stone loungers, and private ocean-view couples massage suites.", "icon": "spa"},
                    {"name": "Oceanfront Fitness Center", "time": "1:09:29", "desc": "State-of-the-art gym with floor-to-ceiling glass windows facing the open ocean waves.", "icon": "fitness_center"},
                    {"name": "Stateroom 11680 Verandah Stargazing", "time": "2:18:42", "desc": "Private balcony on Deck 11 for midnight ocean breezes, wine, and peaceful couple stargazing.", "icon": "balcony"},
                    {"name": "Door Magnet Decorating & Pixie Dusting", "time": "2:23:10", "desc": "Disney cruise tradition! Decorate your metallic stateroom door with Disney magnets and participate in fish extender gift exchanges.", "icon": "auto_fix_high"},
                    {"name": "World of Disney & Treasures Untold Shopping", "time": "2:27:48 & 2:35:50", "desc": "Exclusive maritime Mickey & Minnie ears, Disney Adventure spirit jerseys, and honeymoon keepsakes.", "icon": "card_giftcard"},
                    {"name": "Character Dance Party at 10:00 PM", "time": "2:05:17", "desc": "Late-night dance party with Disney characters and DJ under open starlight.", "icon": "nightlife"}
                ]
            }
        ]
    },

    # Visa Timeline & Requirements
    "visa": {
        "apply_date": "November 1, 2026",
        "target_decision": "Within 3–5 working days (issued as e-Visa)",
        "processing_window": "Must apply within 30 days of arrival (Nov 1 is the perfect date!)",
        "fee": "SGD 30 ICA fee + authorized visa agent service fee (~₹1,200 - ₹1,800)",
        "status": "In Progress", # "Documents Gathering", "Submitted to Agent", "In Progress", "Processing at ICA", "Approved & Issued"
        "application_ref": "ICA-SG-2026-PENDING",
        "agent_name": "Authorised Visa Agent / MMT",
        "approval_date": "",
        "notes": "Target submission date: Nov 1, 2026. Keep hard copies ready for immigration.",
        "checklist": [
            {
                "id": "v1",
                "title": "Original Indian Passports",
                "due_date": "Due: Ready Now (Verify Validity > Jun 2027)",
                "detail": "Must have min. 6 months validity from Dec 13, 2026 (at least 2 blank pages).",
                "done": True
            },
            {
                "id": "v2",
                "title": "Completed & Signed Form 14A",
                "due_date": "Due: Oct 28, 2026",
                "detail": "Official Singapore visa application form for both Shaiwal and Shaila. Print & sign.",
                "done": False
            },
            {
                "id": "v3",
                "title": "Passport-sized Photos (ICA Spec)",
                "due_date": "Due: Oct 28, 2026",
                "detail": "35mm x 45mm, matte finish, pure white background, 80% face coverage, no spectacles.",
                "done": False
            },
            {
                "id": "v4",
                "title": "Confirmed Flight Tickets",
                "due_date": "Done ✅",
                "detail": "Roundtrip Delhi - Singapore (Dec 13 arrival 6 PM, Dec 21 departure 4:40 PM).",
                "done": True
            },
            {
                "id": "v5",
                "title": "Hotel & Disney Cruise Confirmations",
                "due_date": "Done ✅",
                "detail": "Vouchers for Carlton Hotel (13 Dec), Disney Adventure Cruise (14-16 Dec), Oasia Resort Sentosa (17-21 Dec).",
                "done": True
            },
            {
                "id": "v6",
                "title": "Bank Statements (Last 3–6 Months)",
                "due_date": "Due: Oct 30, 2026",
                "detail": "Bank stamped statements showing healthy balance (≥ ₹1.5–2 Lakhs) for Shaiwal.",
                "done": False
            },
            {
                "id": "v7",
                "title": "Cover Letter & Employment Details",
                "due_date": "Due: Oct 30, 2026",
                "detail": "Honeymoon cover letter detailing travel dates + salary slips / company leave approval.",
                "done": False
            },
            {
                "id": "v8",
                "title": "SG Arrival Card (Electronic)",
                "due_date": "Due: Dec 10–12, 2026 (strictly 72 hrs prior)",
                "detail": "Submit online at ica.gov.sg strictly within 3 days (72 hours) before landing in Singapore (Dec 10-12). Free of cost.",
                "done": False
            }
        ]
    },

    # Day-by-Day Itinerary with Real-time Options & MRT Station Routing
    "days": [
        {
            "day": 1,
            "date": "Sunday, 13 December 2026",
            "title": "Welcome to Singapore & City Lights",
            "location": "Changi Airport ➔ Carlton Hotel",
            "mrt_guide": {
                "start": "Changi Airport Station (CG2)",
                "end": "City Hall MRT (EW13 / NS25) or Bras Basah (CC2)",
                "lines": "East-West Line (Green) ➔ Transfer at Tanah Merah to City Hall",
                "route_desc": "Changi Airport MRT (CG2) ➔ Tanah Merah (EW4) cross platform ➔ City Hall MRT (EW13) Exit A. Carlton Hotel is directly a 4-minute walk (350m) across Bras Basah Rd.",
                "fare": "~SGD 2.05 (Tap contactless card or EZ-Link)",
                "payment_tips": "Simply tap your contactless VISA / Mastercard at MRT fare gates. EZ-Link card is also accepted for MRT & buses.",
                "bus_alternative": "Public Bus No. 36 departs directly from Changi Airport basement bus bays (Terminals 1, 2, 3 & 4) and goes straight into the city / Bras Basah & Orchard Rd (~SGD 2.00, scenic route!).",
                "taxi_alternative": "Grab/Taxi ~20 mins (SGD 22–28) recommended with heavy honeymoon luggage."
            },
            "schedule": [
                {"time": "6:00 PM", "title": "Touchdown at Changi Airport", "desc": "Clear immigration, collect luggage, grab physical local SIM / eSIM or activate international roaming.", "icon": "flight_land"},
                {"time": "6:45 PM – 7:15 PM", "title": "Transfer to Carlton Hotel", "desc": "Take taxi or Grab to Carlton Hotel (City Hall area). Check-in and freshen up.", "icon": "local_taxi"},
                {"time": "8:00 PM – 10:00 PM", "title": "Romantic First Dinner & Stroll", "desc": "Enjoy a delicious dinner near City Hall / CHIJMES and a relaxed romantic evening walk.", "icon": "restaurant"}
            ],
            "options": [
                {"title": "Dinner Option A (Romantic Italian):", "desc": "Dine at the illuminated courtyards of CHIJMES (right opposite Carlton Hotel) — delicious pizza, pasta, and wines in a fairytale heritage setting."},
                {"title": "Dinner Option B (Pure Vegetarian Fine Dining):", "desc": "Nalan Restaurant at Capitol Singapore (2 min walk) for authentic, high-end North & South Indian delicacies."},
                {"title": "Late Night Sweet Treat:", "desc": "Grab artisan gelato or dessert at Mr. Stork (Andaz rooftop) overlooking the skyline."}
            ]
        },
        {
            "day": 2,
            "date": "Monday, 14 December 2026",
            "title": "Boarding the Disney Adventure Cruise! 🚢🏰",
            "location": "Marina Bay Cruise Centre ➔ High Seas",
            "mrt_guide": {
                "start": "City Hall MRT (EW13 / NS25)",
                "end": "Marina South Pier MRT (NS28) - Exit B",
                "lines": "North-South Line (Red Line Direct)",
                "route_desc": "Board North-South Line (Red) southbound at City Hall ➔ Ride 4 stops directly to Marina South Pier (NS28, terminal stop). Follow the sheltered, air-conditioned linkway (approx. 600m / 7-8 min walk) directly to Marina Bay Cruise Centre Singapore (MBCCS).",
                "fare": "~SGD 1.60 per person",
                "taxi_alternative": "Grab Taxi ~12 mins (SGD 12–16) directly to passenger drop-off portico."
            },
            "schedule": [
                {"time": "9:30 AM – 11:30 AM", "title": "Breakfast & Morning Leisure", "desc": "Enjoy breakfast at Carlton, leisurely stroll near National Gallery or Fort Canning Park.", "icon": "free_breakfast"},
                {"time": "12:00 PM – 2:00 PM", "title": "Transfer to Marina Bay Cruise Terminal", "desc": "Arrive at terminal. Check-in, drop bags, and walk the red carpet onto the Disney Adventure!", "icon": "directions_boat"},
                {"time": "2:00 PM – 4:00 PM", "title": "Explore the 7 Disney Worlds", "desc": "Explore Disney Imagination Garden, Town Square (Disney Princess realm), and San Fransokyo Street.", "icon": "castle"},
                {"time": "4:00 PM", "title": "Sailing Party with Mickey & Minnie!", "desc": "Top-deck sailaway musical party with Mickey, Minnie, Donald, and Goofy in full cruise celebration!", "icon": "sailing"},
                {"time": "Evening", "title": "Disney Rotational Dining & Broadway Show", "desc": "First royal dinner at Hollywood Spotlight Club or Animator's Palate, followed by a Broadway-caliber Disney musical.", "icon": "theater_comedy"}
            ],
            "options": [
                {"title": "Disney Character Photo:", "desc": "Take your first official honeymoon portrait with Mickey & Minnie in the Grand Atrium!"},
                {"title": "Princess Greeting:", "desc": "Visit Town Square for royal meet-and-greets with Disney Princesses."}
            ]
        },
        {
            "day": 3,
            "date": "Tuesday, 15 December 2026",
            "title": "Disney Magic at Sea — Princesses, Romance & Thrills 👑✨",
            "location": "Disney Adventure High Seas",
            "mrt_guide": {
                "start": "High Seas (At Sea)",
                "end": "Disney Adventure 7 Themed Realms",
                "lines": "Ship Elevators & Grand Staircase",
                "route_desc": "Sailing open international waters! No MRT today — navigate between Deck 4 Town Square, Deck 7 Wayfinder Bay, and Deck 11 Stateroom 11680."
            },
            "schedule": [
                {"time": "Morning", "title": "Fairytale Breakfast on Balcony / Buffet", "desc": "Wake up to endless ocean views. Indulge in Mickey waffles and fresh pastries.", "icon": "wb_sunny"},
                {"time": "10:30 AM – 1:00 PM", "title": "Royal Meet & Greet with Disney Princesses", "desc": "Meet Cinderella, Belle, Jasmine, Rapunzel, and Ariel. Capture dream fairytale photos for Puchki!", "icon": "auto_awesome"},
                {"time": "Afternoon", "title": "Wayfinder Bay Pool & Marvel Landing", "desc": "Relax on Moana's Wayfinder Bay daybeds, enjoy adult-only quiet cove pool, or ride the Ironcycle rollercoaster!", "icon": "pool"},
                {"time": "Night", "title": "Gala Royal Night & Celebration in the Sky", "desc": "Dress up in royal cocktail attire for gala dinner, followed by fireworks and Lion King musical extravaganza under the stars.", "icon": "nightlife"}
            ],
            "options": [
                {"title": "Couples Romance:", "desc": "Book Senses Spa couples' sea-view massage or private jacuzzi retreat."},
                {"title": "Evening Cocktails:", "desc": "Spellbound Lounge or Captain's Bar for Disney-themed signature honeymoon cocktails."}
            ]
        },
        {
            "day": 4,
            "date": "Wednesday, 16 December 2026",
            "title": "Disney Sea Voyage & Pixar Magic 💫",
            "location": "High Seas Returning to Singapore",
            "mrt_guide": {
                "start": "High Seas (At Sea)",
                "end": "Walt Disney Theatre & San Fransokyo",
                "lines": "Ship Decks 3 to 14",
                "route_desc": "Cruising smoothly back towards Singapore waters. Pack large luggage by midnight with Disney baggage tags."
            },
            "schedule": [
                {"time": "Daytime", "title": "Discovery Reef, Toy Story Place & Trivia", "desc": "Walk under the Little Mermaid coral ceilings, enjoy Toy Story slides, Disney movie marathons & trivia games.", "icon": "celebration"},
                {"time": "Evening", "title": "Farewell Magical Dinner with Disney Friends", "desc": "Final evening rotational dining where characters bid personal farewells to guests.", "icon": "dinner_dining"},
                {"time": "Night", "title": "Packing Protocol & Stargazing", "desc": "Stargaze from the top deck. Tag main luggage and place outside cabin door by midnight for seamless morning exit.", "icon": "luggage"}
            ],
            "options": [
                {"title": "Disney Souvenirs:", "desc": "Pick up exclusive Disney Adventure Singapore commemorative Mickey & Minnie plushies and honeymoon pins!"}
            ]
        },
        {
            "day": 5,
            "date": "Thursday, 17 December 2026",
            "title": "Soothing Sentosa Arrival: Sanctuary Rest, Palawan & Wings of Time",
            "location": "Oasia Resort Sentosa & Palawan Beach",
            "mrt_guide": {
                "start": "HarbourFront MRT Station (NE1 / CC29) · Inside VivoCity Mall",
                "end": "Imbiah Station (Oasia Resort Sentosa) ➔ Beach Station / Central Beach Bazaar (Terminal)",
                "lines": "North-East Line (Purple) / Circle Line (Yellow) ➔ VivoCity Mall (Level 3 Monorail / Tower 2 Cable Car)",
                "route_desc": "1. Reaching HarbourFront MRT: The station exits directly inside VivoCity Mall (Basement 2).\n2. Sentosa Express Monorail: Take the escalator inside VivoCity up to Level 3 (Lobby L). Board the Sentosa Express Monorail directly into Sentosa. Line has 4 stations: VivoCity ➔ Resorts World ➔ Imbiah (Stop 2, right at front steps of Oasia Resort Sentosa!) ➔ Beach Station (Final Stop: Central Beach Bazaar, Wings of Time, street food street, & beach shuttles).\n3. Singapore Cable Car: From HarbourFront MRT Exit B, walk sheltered linkway to HarbourFront Tower 2 (Level 15) to board the Mount Faber Line cable car across the water directly to Sentosa Cable Car Station (Imbiah Lookout).",
                "fare": "SGD 4.00 Monorail entry ticket (Pay once, 100% FREE unlimited rides across all stations thereafter with Oasia Resort Sentosa keycard/pass; Cable Car included in your Klook/Pelago SkyPass).",
                "payment_tips": "Monorail Tickets: Cost is SGD 4.00 per person to enter Sentosa from VivoCity Level 3. Buy at kiosks or simply tap your contactless VISA/Mastercard/EZ-Link directly at the gantry! After the initial $4 entry (or once checked into Oasia Resort Sentosa), all monorail rides inside Sentosa island and back are 100% FREE OF COST without any further charges.",
                "cable_car_guide": "Singapore Cable Car departs from HarbourFront Tower 2 across Keppel Bay to Mount Faber & Sentosa Island (spectacular 360° romantic panoramic harbor view).",
                "taxi_alternative": "Grab/Taxi ~18 mins (SGD 16–22) with suitcases directly to Oasia Resort lobby."
            },
            "schedule": [
                {"time": "7:00 AM – 8:30 AM", "title": "Cruise Disembarkation", "desc": "Follow cruise exit instructions. Clear customs smoothly at Marina Bay Cruise Centre.", "icon": "exit_to_app"},
                {"time": "8:30 AM – 9:30 AM", "title": "Scenic Transfer to Oasia Resort Sentosa", "desc": "Arrive at Oasia Resort Sentosa (Imbiah Station). Drop heavy bags with concierge, sip soothing welcome wellness tea, and relax in the lush lobby lounge.", "icon": "hotel"},
                {"time": "10:00 AM – 1:00 PM", "title": "Soothing Palawan Beach & Wooden Suspension Bridge 🏝️🌉", "desc": "Take a gentle breezy ride on the Free Beach Shuttle tram to Palawan Beach. Stroll hand-in-hand along the quiet morning sands, walk across the iconic wooden rope suspension bridge over turquoise water to the offshore islet, stand at the Southernmost Point of Continental Asia, and climb the twin timber viewing towers for panoramic sea views.", "icon": "beach_access"},
                {"time": "1:00 PM – 3:00 PM", "title": "Peaceful Beachside Lunch at Tanjong Beach 🏖️🍹", "desc": "Hop one stop over on the free beach tram to secluded Tanjong Beach. Enjoy a romantic, unhurried lunch with cold coconuts, mocktails, and fresh Mediterranean fare at Tanjong Beach Club daybeds.", "icon": "waves"},
                {"time": "3:00 PM – 6:15 PM", "title": "Check-in to Oasia Sanctuary & Afternoon Rest 🛏️🌿", "desc": "Head back to Oasia Resort Sentosa for 3 PM check-in. Unpack at your leisure, take a warm herbal bath, enjoy the resort's tranquil wellness pool and tea amenities, and take a refreshing afternoon nap to recharge after the cruise.", "icon": "spa"},
                {"time": "6:15 PM – 7:30 PM", "title": "Golden Sunset & Arrive Early at Beach Bazaar 🌅", "desc": "Take the Sentosa Express 1 stop to Beach Station / Central Beach Bazaar. Watch the golden sunset over the sea, admire the 80m Sentosa SkyJet fountain, sample light evening street food, and claim prime center seats comfortably 1 hour early.", "icon": "storefront"},
                {"time": "Daily Shows: 7:40 PM & 8:40 PM", "title": "Wings of Time Night Show (Sentosa Island) 🎆✨", "desc": "Spectacular open-sea light, water, laser, fire, and fireworks symphony at Central Beach Bazaar on Sentosa Island. Daily showtimes start promptly at 7:40 PM (Show 1) and 8:40 PM (Show 2).", "icon": "auto_awesome"},
                {"time": "8:30 PM – 9:30 PM", "title": "Sentosa Sensoryscape: 'ImagiNite' Evening Light Walk (100% FREE) 🌟🌺", "desc": "Instead of waiting for the monorail, take the romantic, illuminated biophilic walkway right outside Beach Station. Stroll gently through 6 glowing themed gardens with interactive floor light projections and scented night mist that leads right to the front doors of Oasia Resort!", "icon": "flare"}
            ],
            "options": [
                {"title": "🌿 Dec 17 Vibe — Light, Soothing & Restorative:", "desc": "• Unrushed Morning: Soft beach strolling at Palawan Beach without tight schedules.\n• 3-Hour Afternoon Hotel Rest: Check-in at 3:00 PM with ample time for a spa bath, nap, and unpacking.\n• Easy Evening: Sunset at Beach Bazaar, Wings of Time show, and a peaceful stroll through the glowing Sensoryscape trail directly back to bed."},
                {"title": "🌟 Sentosa Sensoryscape 'ImagiNite' (100% FREE Night Experience):", "desc": "• Perfect Location: A 350-meter biophilic illuminated sensory corridor connecting Beach Station directly to Imbiah Lookout / Oasia Resort Sentosa.\n• ImagiNite Light Show (7:50 PM – 9:40 PM nightly): Free entry! Features 6 sensory gardens with interactive digital light projections, floor beam art, glowing basket-weave architectural gazebos, and misty light displays."},
                {"title": "🚎 Sentosa Beach Shuttle (100% Free):", "desc": "• Zero Cost: Runs continuously every 10–15 mins linking Beach Station ⇄ Siloso Beach ⇄ Palawan Beach ⇄ Tanjong Beach.\n• Effortless Hop-On Hop-Off: Seamlessly connects all beaches without long walks in the sun."},
                {"title": "⭐ Crucial Tip — Reach Wings of Time 1 Hour Early:", "desc": "For the 7:40 PM show, arrive at Central Beach Bazaar by 6:40 PM; for the 8:40 PM show, arrive by 7:40 PM for prime center-stage seats."}
            ]
        },
        {
            "day": 6,
            "date": "Friday, 18 December 2026",
            "title": "Oceanarium, Harry Potter Magic, Fort Siloso Skywalk & Siloso Sunset",
            "location": "Resorts World Sentosa & Siloso Beach",
            "mrt_guide": {
                "start": "Imbiah Station (Sentosa Express, outside Oasia)",
                "end": "Resorts World Station (Sentosa Express) ➔ Siloso Beach / Fort Siloso",
                "lines": "Sentosa Express Monorail (1 stop, 2 mins) + Free Beach Shuttle Tram",
                "route_desc": "Hop on Sentosa Express at Imbiah Station ➔ Ride 1 stop (2 mins) to Resorts World Station. Walk 3 mins through the festive plaza to S.E.A. Aquarium & Harry Potter: Visions of Magic exhibition.\nIn late afternoon, take the free beach shuttle tram to Fort Siloso Skywalk & Siloso Beach.",
                "fare": "Free with Oasia Resort Sentosa guest pass!"
            },
            "schedule": [
                {"time": "9:30 AM – 12:30 PM", "title": "Singapore Oceanarium (S.E.A. Aquarium)", "desc": "Walk through giant glass tunnels surrounded by manta rays, sharks, and vibrant coral reefs.", "icon": "water"},
                {"time": "12:30 PM – 2:00 PM", "title": "Lunch Break at Resorts World", "desc": "Enjoy lunch at Malaysian Food Street or Din Tai Fung / gourmet burger spots.", "icon": "restaurant"},
                {"time": "2:00 PM – 4:30 PM", "title": "Harry Potter: Visions of Magic", "desc": "Step into the magical interactive wizarding world art experience (timed entry).", "icon": "magic_button"},
                {"time": "4:45 PM – 6:15 PM", "title": "Fort Siloso Skywalk (100% FREE Aerial Canopy Trail) 🌲🌁", "desc": "Hop on the free Beach Shuttle or Sentosa Line Cable Car to Siloso Point. Take the scenic glass elevator 11 storeys up (36m high) to the 181-meter scenic elevated treetop walkway. Enjoy panoramic views of western Sentosa, cruise waters, and coastal rainforest!", "icon": "nature_people"},
                {"time": "6:15 PM – 8:30 PM", "title": "Siloso Beach: Sunset Walk, Boardwalk & Dinner at Trapizza 🌅🍕", "desc": "Stroll down from Fort Siloso directly onto Siloso Beach. Walk the vibrant beachfront boardwalk during golden sunset, sip tropical cocktails, and enjoy wood-fired authentic Italian pizza right on the beach at Trapizza with the waves rolling in.", "icon": "local_pizza"},
                {"time": "8:30 PM – Late", "title": "Evening at Leisure in Sentosa", "desc": "Stroll back to Oasia Resort or enjoy a quiet nightcap at the Mess Hall or Sentosa Cove.", "icon": "nightlife"}
            ],
            "options": [
                {"title": "🌁 Fort Siloso Skywalk (100% Free Treetop Walk):", "desc": "• Free Access: No tickets required! Glass elevator 11 storeys up (36 meters high) to an 181m elevated treetop canopy trail.\n• Views & Photography: Sensational panoramic views of western Sentosa, cruise waters, and coastal rainforest.\n• How to Reach: Take the free Beach Shuttle to Siloso Point, or ride the Sentosa Line Cable Car directly to Siloso Point Station."},
                {"title": "🍕 Sunset Dinner at Siloso Beach (Trapizza):", "desc": "• Wood-Fired Pizza: Authentic thin-crust artisan pizza, pastas, and crisp wine at Trapizza right on the sands of Siloso Beach.\n• Golden Hour: Watching the sunset over the western sea from an open-air beachfront table is the ultimate romantic dinner on Sentosa!"},
                {"title": "Alternative Thrill:", "desc": "Skyline Luge Sentosa (4 exhilarating downhill tracks) if you prefer action before dinner!"}
            ]
        },
        {
            "day": 7,
            "date": "Saturday, 19 December 2026",
            "title": "Shopping Day: Pandas, Little India, Chinatown, Bugis Street & Haji Lane",
            "location": "Mandai ➔ Little India ➔ Chinatown ➔ Bugis Street & Haji Lane",
            "mrt_guide": {
                "start": "HarbourFront MRT (NE1)",
                "end": "Khatib (NS14) ➔ Little India (NE7) ➔ Chinatown (NE4) ➔ Bugis (DT14/EW12) ➔ Sentosa",
                "lines": "North-East Line (Purple) ➔ Downtown Line (Blue) ➔ Sentosa Express Monorail",
                "route_desc": "1. Mandai ➔ Little India: Khatib MRT (Red line) south to Dhoby Ghaut ➔ Purple line to Little India (NE7) / Farrer Park (NE8 for Mustafa Centre).\n2. Little India ➔ Chinatown: Direct Purple Line southbound from Little India (NE7) to Chinatown (NE4 Exit A, 4 stops, ~8 mins).\n3. Chinatown ➔ Bugis Street: Direct Downtown Line (Blue line) from Chinatown MRT (DT19) to Bugis MRT (DT14 Exit C, 4 stops, ~7 mins) directly opposite Bugis Street Market!\n4. Bugis ➔ Haji Lane: Just a breezy 5-minute stroll (400m) from Bugis MRT / Bugis Junction to Haji Lane's colorful street art & quirky boutiques.\n5. Returning to Sentosa: From Bugis MRT (DT14), take Downtown Line to Chinatown (DT19) ➔ Transfer to Purple Line to HarbourFront (NE1) ➔ Sentosa Express Monorail.",
                "fare": "~SGD 1.50–2.20 per MRT leg (Tap Contactless VISA/Mastercard directly at gantries)."
            },
            "schedule": [
                {"time": "7:30 AM – 8:30 AM", "title": "Early Morning Transit to Khatib MRT & Mandai Shuttle 🚌", "desc": "Take North-South Line (Red) to Khatib MRT Station (NS14 Exit A). Board the Mandai Khatib Shuttle (~Rs 170 / SGD 2.70, runs every 10–15 mins) for a quick 15-min direct ride to Singapore Zoo & River Wonders in Mandai.", "icon": "directions_bus"},
                {"time": "8:30 AM – 12:30 PM", "title": "Singapore Zoo (World-Famous Open-Concept Wildlife Safari) 🦁🐘🦘", "desc": "Enter Singapore Zoo at 8:30 AM opening! Explore 300+ species across open lush rainforest habitats with natural moats instead of cages. Highlights: White tigers, African lions, Asian elephants splash, Australian kangaroos/wallabies walk-through, Great Rift Valley baboons, primate island, aviary birds, and the famous Splash Safari Sea Lion presentation at the amphitheatre!", "icon": "pets"},
                {"time": "12:30 PM – 1:30 PM", "title": "Lunch at Mandai Rainforest Pavilion / Ah Meng Kitchen 🍜", "desc": "Enjoy Singapore hawker dishes (chicken rice, laksa) and chilled drinks at Ah Meng Restaurant or Mama Panda Kitchen before heading to Little India.", "icon": "lunch_dining"},
                {"time": "1:15 PM – 2:00 PM", "title": "House of Tan Teng Niah & Sri Veeramakaliamman Temple", "desc": "Take vibrant couple photos at the 1900 rainbow-colored House of Tan Teng Niah (Kerbau Rd), then walk 2 mins to seek blessings at Sri Veeramakaliamman Temple (Shri Viliyam).", "icon": "temple_hindu"},
                {"time": "2:00 PM – 3:15 PM", "title": "Mustafa Centre: 24/7 Mega Electronics & Packed Foods", "desc": "Stock up on packed Indian ready-to-eat meals, snacks, cosmetics, wholesale Tiger Balm, Type G adapters, power banks, and duty-free perfumes.", "icon": "shopping_cart"},
                {"time": "3:30 PM – 4:00 PM", "title": "Chinatown Transfer (Purple Line MRT Direct)", "desc": "Hop on the North-East MRT (Purple Line) direct from Little India (NE7) to Chinatown MRT (NE4 Exit A, 8 mins).", "icon": "subway"},
                {"time": "4:00 PM – 5:30 PM", "title": "Chinatown Market, Sri Mariamman & Buddha Tooth Relic", "desc": "Shop Singapore's cheapest Merlion souvenirs on Pagoda Street, seek blessings at Sri Mariamman Temple (1827), and marvel at the 3.5-ton solid gold stupa at the Buddha Tooth Relic Temple.", "icon": "storefront"},
                {"time": "5:30 PM – 6:00 PM", "title": "Chinatown to Bugis (Downtown Line MRT Direct)", "desc": "Board the Downtown Blue Line direct from Chinatown MRT (DT19) to Bugis MRT (DT14 Exit C, only 4 stops / 7 mins).", "icon": "train"},
                {"time": "6:00 PM – 7:15 PM", "title": "Bugis Street Market: Singapore's Largest & Cheapest Clothes Market", "desc": "Dive into Bugis Street — 3 levels of 800+ sheltered stalls! Grab trendy Korean & street fashion clothes ($10–$15), cute sunglasses, luggage bags, bags, watches, phone cases, and $1 fresh juice cups.", "icon": "checkroom"},
                {"time": "7:15 PM – 8:30 PM", "title": "Haji Lane (5-Min Walk from Bugis): Street Art & Quirky Boutiques 🎨", "desc": "Stroll 5 mins from Bugis into Haji Lane. Pose against world-famous vibrant graffiti wall murals, browse independent quirky fashion boutiques, vintage vinyl, handmade jewelry, and enjoy live music cafes with iced mocktails & dinner.", "icon": "palette"},
                {"time": "8:30 PM – 9:15 PM", "title": "Return to Sentosa & Rest", "desc": "Bugis MRT (Downtown Line) ➔ Chinatown ➔ Purple line to HarbourFront ➔ Sentosa Express Monorail to Oasia Resort. Unwind in your suite with your shopping haul!", "icon": "night_shelter"}
            ],
            "options": [
                {"title": "🛍️ Bugis Street Market (Cheapest Clothes & Accessories):", "desc": "• Trendy Clothing & Outfits: Summer dresses, beach shirts, trendy tees, and streetwear at $10 to $15.\n• Electronics & Phone Accessories: Fast chargers, novelty phone cases, cables, selfie sticks, and portable fans for $5–$12.\n• Bags, Footwear & Luggage: Extra duffel bags & foldable trolley bags if your shopping exceeds luggage space!\n• Budget Souvenirs & $1 Refreshments: 3 for $10 souvenir bundles and freshly pressed dragonfruit/watermelon juices for $1–$1.50."},
                {"title": "🎨 Haji Lane (5 Mins from Bugis — Colorful Murals & Quirky Boutiques):", "desc": "• Vibrant Street Art Murals: Legendary colorful geometric and pop-art murals on heritage shophouse walls — absolute must-visit for romantic couple photography!\n• Quirky Fashion & Indie Boutiques: One-of-a-kind dresses, handmade leather accessories, bespoke perfume blending, retro sunglasses, and artisanal jewelry.\n• Hip Cafes & Live Music: Open-air chill bars, Turkish lamp cafes, artisanal coffee roasters, and Mexican/Middle Eastern bistros."},
                {"title": "🏮 Chinatown Shopping & Temples:", "desc": "• Pagoda Street: Singapore's best Merlion souvenirs (magnets/keychains 5–6 for $10), silk nightgowns, and kaya jam.\n• Sri Mariamman Temple: Singapore's oldest 1827 national monument Hindu temple.\n• Buddha Tooth Relic Temple: 4-storey Tang-style architectural marvel with 3.5-ton gold stupa."},
                {"title": "Mustafa Centre Electronics & Packed Food Checklist:", "desc": "• Packed Foods: Ready-to-eat MTR/Haldiram meals, samosas, sweets, and dry fruits.\n• Electronics: Travel adapters, fast power banks, earphones, and multi-pin plugs.\n• Daily Essentials: Wholesale toiletries, sunscreens, shampoos, and Tiger Balm."}
            ]
        },
        {
            "day": 8,
            "date": "Sunday, 20 December 2026",
            "title": "Marina Bay Sands SkyPark, The Shoppes Mall, Gardens by the Bay & Spectra Show",
            "location": "Marina Bay Sands, The Shoppes & Gardens by the Bay",
            "mrt_guide": {
                "start": "HarbourFront MRT (NE1 / CC29) · Sentosa Gateway",
                "end": "Bayfront MRT Station (DT16 / CE1) · Main Station for Gardens by the Bay & Marina Bay Sands",
                "lines": "Circle Line (Yellow) direct OR Downtown Line (Blue) directly into Bayfront MRT (CE1 / DT16)",
                "route_desc": "• Primary Station — Bayfront MRT (DT16 / CE1): The central station serving both Gardens by the Bay AND Marina Bay Sands!\n• Exit B (Underground Sheltered Linkway): Leads directly into Gardens by the Bay outside Dragonfly Bridge. Floral Fantasy is located right beside Exit B!\n• 🚐 Gardens by the Bay Shuttle Service (SGD 3.00): Board the air-conditioned electric shuttle right at Bayfront MRT Exit B! For just SGD 3.00 per person (unlimited all-day rides), this shuttle whisks you straight across the gardens to the entrance of Flower Dome, Cloud Forest & Jurassic World — saving you a 15-minute walk in the tropical heat!\n• Exit C & D: Connects directly inside The Shoppes at Marina Bay Sands, the Casino, Food Court, and lifts up to the Level 57 MBS SkyPark Observation Deck!\n• Returning to Sentosa at Night: Board Downtown Line at Bayfront MRT (DT16) ➔ Chinatown (DT19) ➔ Transfer to Purple Line to HarbourFront (NE1) ➔ Free Sentosa Express Monorail back to Oasia Resort.",
                "fare": "~SGD 1.90 MRT fare + optional SGD 3.00 Gardens Shuttle (unlimited rides between Bayfront MRT Exit B & Conservatories)."
            },
            "schedule": [
                {"time": "9:30 AM – 10:30 AM", "title": "Floral Fantasy & Flight of the Dragonfly 4D Show 🌸🚁", "desc": "Start right outside Bayfront MRT Exit B at Floral Fantasy (~₹1,400 / person). Stroll through 4 magical garden landscapes (Dance, Float, Waltz, Drift) with hanging floral bouquets, cascading flowers, and poison dart frogs, ending with the thrilling 4D simulated ride 'Flight of the Dragonfly' soaring over Gardens by the Bay!", "icon": "spa"},
                {"time": "10:30 AM – 1:30 PM", "title": "Flower Dome + Cloud Forest & Jurassic World (Must-Visit) 🦖🌸", "desc": "Take the $3 electric shuttle to the main Conservatories. 1. Flower Dome: The world's largest glass greenhouse with Mediterranean gardens and seasonal floral displays. 2. Cloud Forest & Jurassic World: Step into the misty 35m indoor mountain waterfall, surrounded by roaring animatronic dinosaurs (towering Brachiosaurus & T-Rex) with the aerial Cloud Walk and Tree Top Walk!", "icon": "local_florist"},
                {"time": "1:30 PM – 2:30 PM", "title": "Lunch at Marina Bay Mall / The Shoppes at MBS 🍜🍔", "desc": "Cross the short covered linkbridge into Marina Bay Mall (The Shoppes at Marina Bay Sands). Choose from the world-class Rasapura Masters Food Hall, Michelin-starred Din Tai Fung, Yardbird Southern Table, or waterfront cafes overlooking the bay.", "icon": "restaurant"},
                {"time": "2:30 PM – 5:00 PM", "title": "Marina Bay Mall (The Shoppes at MBS): Shopping, Sampan Canal & Apple Floating Store 🛍️🛶🍏", "desc": "Dedicated afternoon inside Marina Bay Mall (The Shoppes at MBS, directly connected to Bayfront MRT Exit C/D)! 1. High-End & High-Street Shopping: Explore 170+ luxury flagship boutiques, Sephora, cosmetics, and the TWG Tea Salon. 2. Sampan Boat Ride: Board a traditional wooden Sampan boat cruising the indoor Venetian canal right around the swirling Rain Oculus whirlpool! 3. Apple Marina Bay Sands: Walk through the underwater tunnel to the world's only 360-degree floating glass sphere Apple store on the bay water.", "icon": "shopping_bag"},
                {"time": "5:00 PM – 6:30 PM", "title": "Marina Bay Sands SkyPark Observation Deck (Level 57 Sunset) 🏙️🌅", "desc": "Take the express elevator up to Level 57 of Marina Bay Sands! Stand 200m above the ground on the ship-shaped cantilever rooftop. Soak in breathtaking 360° golden-hour sunset panoramas of the Singapore Strait, the bay, and the city skyline as night lights illuminate the metropolis.", "icon": "apartment"},
                {"time": "6:45 PM – 7:45 PM", "title": "Supertree Grove Picnic Spot & Twilight Rest 🧺💧", "desc": "Walk across the Lion Bridge back into Gardens by the Bay. Spread your bedsheet on the lush green lawns directly beneath the Supertrees, drink water, and lay down side-by-side looking up into the towering illuminated branches in cool comfort.", "icon": "deck"},
                {"time": "7:45 PM – 8:15 PM", "title": "Garden Rhapsody Supertree Light & Sound Show ✨🎶", "desc": "Watch the world-famous synchronized light symphony dance across the Supertree canopy directly overhead from your bedsheet! (100% free, magical #1 honeymoon highlight).", "icon": "auto_awesome"},
                {"time": "8:30 PM – 9:30 PM", "title": "Spectra Light & Water Show at Marina Bay Mall Waterfront 🌊🎆", "desc": "Stroll 10 mins back to the Event Plaza outside Marina Bay Mall for the 9:00 PM Spectra outdoor laser and dancing water fountain show against the shimmering bay.", "icon": "celebration"},
                {"time": "9:30 PM – 10:30 PM", "title": "Merlion Park Night View & Return to Sentosa 🦁🚇", "desc": "Take the scenic stroll across Jubilee Bridge to Merlion Park for classic night photos in front of the illuminated water-spouting Merlion statue with Marina Bay Sands shining in the backdrop. Return smoothly via Raffles Place MRT back to Sentosa.", "icon": "photo_camera"}
            ],
            "options": [
                {"title": "🛍️ Marina Bay Mall (The Shoppes at Marina Bay Sands):", "desc": "• Complete Shopping Paradise: 800,000+ sq ft of high-end fashion, luxury jewelry, cosmetics, and high-street labels.\n• Sampan Boat Ride: Traditional wooden boat ride along the indoor canal (~SGD 15 / person) circling the bottom of the Rain Oculus whirlpool.\n• Apple Marina Bay Sands: Iconic floating glass orb on the water with underwater entrance tunnel.\n• Direct Metro Access: Connects directly inside Bayfront MRT Station (Exit C & D)."},
                {"title": "🏙️ Marina Bay Sands SkyPark Observation Deck (Level 57 Sunset):", "desc": "Perched 200m above the city atop Tower 3 of Marina Bay Sands. 360-degree panoramic vistas of the Singapore Strait, shipping lanes, and skyline lights. Timed entry on Klook/Pelago (Slot: 5:00 PM – 5:30 PM). Skipping the secondary Supertree Observatory rooftop queue saves ₹1,600 and gives you relaxed, unhurried time!"},
                {"title": "🌸 Floral Fantasy (~₹1,400 / person):", "desc": "Located right at Bayfront MRT Exit B. Includes 4 whimsical floral dreamscapes and the immersive 4D simulated 'Flight of the Dragonfly' motion theatre."},
                {"title": "🧺 Pro-Tip for Garden Rhapsody (7:45 PM & 8:45 PM):", "desc": "Do NOT stand or crane your neck! Bring a lightweight bedsheet or picnic mat and cold bottled water. Spread it on the soft grass directly under the Supertrees 15–20 mins before showtime and lay flat on your backs to watch the lights dance directly overhead!"},
                {"title": "🚐 Gardens by the Bay $3 Shuttle Service:", "desc": "Bayfront MRT (Exit B) ⇄ Conservatories. SGD 3.00 unlimited rides all day."},
                {"title": "🌊 Spectra Light & Water Show (Nightly 8:00 PM & 9:00 PM):", "desc": "Free outdoor spectacle at the MBS Event Plaza along the waterfront promenade. The 9:00 PM slot fits seamlessly right after the 7:45 PM Garden Rhapsody show!"}
            ]
        },
        {
            "day": 9,
            "date": "Monday, 21 December 2026",
            "title": "Jewel Changi Rain Vortex & Flight Home",
            "location": "Oasia Resort ➔ Jewel Changi ➔ Delhi",
            "mrt_guide": {
                "start": "HarbourFront MRT (NE1)",
                "end": "Changi Airport MRT (CG2)",
                "lines": "North-East Line (Purple) ➔ Outram Park ➔ East-West Line (Green) to Tanah Merah ➔ Changi Airport",
                "route_desc": "Sentosa Express to HarbourFront ➔ North-East Line to Outram Park (NE3) ➔ East-West Line (Green) eastbound to Tanah Merah (EW4) ➔ Cross platform to Changi Airport (CG2). Directly connects to Jewel Changi Rain Vortex & Terminal 1/2/3.",
                "fare": "~SGD 2.30 per person (approx. 50 mins).",
                "taxi_alternative": "Grab/Taxi ~28 mins (SGD 26–32) highly recommended for luggage-free comfort."
            },
            "schedule": [
                {"time": "8:30 AM – 9:00 AM", "title": "Early Check-out from Oasia Resort Sentosa 🧳🚕", "desc": "Check out early from Oasia Resort Sentosa. Hop in a Grab / taxi directly to Changi Airport (~25–30 mins) to arrive a full 5 to 6 hours before flight time to thoroughly explore the world's #1 airport!", "icon": "luggage"},
                {"time": "9:30 AM – 10:15 AM", "title": "Early Baggage Check-in / Left Luggage Counter ✈️🎒", "desc": "Head directly to Jewel Changi Airport (Level 1). If your airline offers Early Check-In (ECI, open 3–12 hrs before flight for Air India, Singapore Airlines, IndiGo, etc.), drop your heavy suitcases immediately! If ECI is not open yet, drop bags at Jewel Left Baggage storage on Level 1 so you can explore completely hands-free.", "icon": "how_to_reg"},
                {"time": "10:15 AM – 12:30 PM", "title": "Explore Jewel Changi: Rain Vortex & Forest Valley 🌊🌿", "desc": "Immerse yourselves in Jewel Changi! 1. HSBC Rain Vortex: Marvel at the world's tallest 40m indoor waterfall from Level 1, Basement 1 acrylic funnel, and the Level 2 viewing deck. 2. Shiseido Forest Valley: Stroll the romantic 4-storey indoor terraced rainforest trails among 2,000+ trees. 3. Canopy Park (Level 5): Walk across the glass Canopy Bridge, Topiary Walk, and petal gardens.", "icon": "water_drop"},
                {"time": "12:30 PM – 1:45 PM", "title": "Jewel Dining & Souvenir Shopping 🍜🛍️", "desc": "Enjoy a farewell lunch at Jewel: Shake Shack, Din Tai Fung, Violet Oon Singapore, or the Five Spice Food Court. Pick up signature Singapore edible gifts: Bengawan Solo fresh pandan chiffon cake, Irvins salted egg chips, and TWG luxury teas.", "icon": "restaurant"},
                {"time": "1:45 PM – 2:30 PM", "title": "Immigration & Skytrain to Departure Terminal 🚊🛂", "desc": "Clear automated biometric immigration seamlessly. Take the complimentary Skytrain between Terminals 1, 2, and 3 (the T2-T3 Skytrain route glides right past the roaring Rain Vortex for a jaw-dropping aerial view!).", "icon": "flight_takeoff"},
                {"time": "2:30 PM – 4:00 PM", "title": "Explore Airside Wonders: Free Movie Theatres & Butterfly Garden 🎬🦋", "desc": "Inside transit departure gates: 1. Terminal 3 Free Movie Theatre: Relax in plush cinema seats watching 24/7 free blockbuster movies! 2. Terminal 3 Butterfly Garden: 2-storey tropical greenhouse with 1,000+ flying tropical butterflies and indoor waterfall. 3. Terminal 2 Dreamscape & Wonderfall. 4. Duty-Free shopping for perfumes, cosmetics, and tech.", "icon": "movie"},
                {"time": "4:00 PM – 4:40 PM", "title": "Gate Boarding & Flight to Delhi 🛫🇮🇳", "desc": "Proceed to departure gate for security screening and boarding. Relax and fly back to Delhi, carrying unforgettable honeymoon memories! Estimated landing at Delhi IGI Airport around 8:00 PM IST.", "icon": "flight_takeoff"}
            ],
            "options": [
                {"title": "🎬 24/7 Free Movie Theatres at Changi Airport:", "desc": "• 100% Free Admission: No booking or payment needed! Just walk in and sink into plush theatre seats.\n• Terminal 3 Free Movie Theatre: Located near the Ambassador Transit Lounge on Level 3 (Departure Transit Lounge, near Gates A1–A8). Runs non-stop 24 hours a day with current Hollywood blockbusters and family movies on a large cinema screen.\n• Terminal 2 Free Movie Area: Level 3 near Sunflower Garden.\n• Perfect Cozy Rest: If you want to put your feet up and relax for 45 minutes in dark air-conditioned comfort before boarding your flight to Delhi!"},
                {"title": "🚊 Moving Between Terminals via Changi Skytrain (100% Free):", "desc": "• Free & Fast: The automated Skytrain is completely FREE of cost, runs every 2 to 4 minutes, and takes only 90 seconds between terminals (operates daily 05:00 AM – 02:30 AM).\n• Dual Sides (Public vs Transit): Skytrain has two separate lines: Public Landside (before immigration) and Airside Transit (after immigration). You can move between T1, T2, and T3 on both sides!\n• ⭐ MUST-DO T2 ⇄ T3 Rain Vortex Route: The Skytrain route connecting Terminal 2 and Terminal 3 cuts directly through the central glass dome of Jewel Changi, gliding just meters away from the roaring 40m Rain Vortex waterfall! Stand right by the window for incredible slow-motion video footage.\n• Jewel Changi Walking Access: Jewel is physically connected via sheltered air-conditioned link bridges: 2-min walk from T1 Arrival Hall, and 5–8 min travelator bridge from T2 & T3.\n• Terminal 4 Shuttle: If departing from T4, a free 24-hour electric shuttle bus runs every 10 mins from Terminal 1 & 2 Arrival Halls."},
                {"title": "⏰ Why Arriving 5–6 Hours Early is Essential:", "desc": "Changi is not just an airport — it's a world-class attraction and botanical paradise! Arriving 5–6 hours before your 4:40 PM flight gives you 3+ hours in Jewel (Rain Vortex, Forest Valley, shopping) and 2 hours inside the transit departure lounges (Butterfly Garden, duty-free shopping) without any rush."},
                {"title": "🧳 Hands-Free Exploring (Early Check-In vs. Left Luggage):", "desc": "• Early Check-In (ECI) Lounge at Jewel (Level 1): Many major airlines (including Singapore Airlines, Air India, IndiGo) allow check-in and luggage drop up to 12 hours prior to scheduled departure!\n• Jewel Left Baggage (Level 1): If early baggage drop isn't open for your airline, safely store your suitcases at the 24-hour Baggage Storage on Level 1 (~SGD 10–15 per bag) and explore completely luggage-free."},
                {"title": "🌊 Best HSBC Rain Vortex Photo Points:", "desc": "• Level 1 Deck: Right in front of the thundering falls surrounded by misty air.\n• Basement 1 / B2: The massive glass acrylic vortex tube where the water plunges into the subterranean basin.\n• Skytrain between T2 & T3: Ride the free monorail right alongside the waterfall for stunning slow-motion video footage!"},
                {"title": "🛍️ Last-Minute Duty-Free & Souvenir Checklist:", "desc": "• Bengawan Solo: Fresh pandan chiffon cake & kaya roll cakes (buy at Jewel or airside).\n• TWG Tea Salon: Luxury tea gift boxes & macarons.\n• Irvins: Dangerously addictive salted egg fish skin & potato chips.\n• Bacha Coffee: Heritage Moroccan drip coffee gift sets & sweet croissants."}
            ]
        }
    ],

    # Tickets to Book (Klook & Pelago Checklist) with Due Dates
    "klook_tickets": [
        {
            "id": "t0", 
            "date": "13 Dec 2026 (Arrival)", 
            "due_date": "Book by Dec 5, 2026 📱 (Install QR in Delhi)", 
            "name": "Singtel Singapore 5G High-Speed Data Tourist eSIM", 
            "status": "To Book", 
            "link": "https://www.klook.com/en-IN/activity/176809-singtel-singapore-data-esim/", 
            "pelago_link": "https://www.pelago.com/en-SG/activity/p8pl4-singtel-prepaid-sim-card-singapore/",
            "booked": False, 
            "price": "~₹950 / person (10–20 GB)"
        },
        {
            "id": "t0-sea", 
            "date": "13 Dec 2026 (Arrival)", 
            "due_date": "Book by Dec 5, 2026 (Multi-Country / Cruise Waters)", 
            "name": "South East Asia Multi-Country High-Speed Data eSIM (Singapore, Malaysia, Thailand, Indonesia)", 
            "status": "To Book", 
            "link": "https://www.klook.com/en-IN/activity/105381-south-east-asia-esim/", 
            "pelago_link": "https://www.pelago.com/en-SG/activity/p8pl4-singtel-prepaid-sim-card-singapore/",
            "booked": False, 
            "price": "~₹450 - ₹1,200 / person (Flexible Data/Days)"
        },
        {
            "id": "t0-physical", 
            "date": "13 Dec 2026 (Arrival)", 
            "due_date": "Book by Dec 5, 2026 (Pickup at Changi T1/T2/T3/T4)", 
            "name": "Singtel 4G/5G Physical Tourist SIM Card (Changi Airport Pickup)", 
            "status": "To Book", 
            "link": "https://www.klook.com/en-IN/activity/77287-4g-travel-sim-card-singtel-singapore/?spm=SearchResult.SearchResult_LIST&clickId=752b002a05", 
            "pelago_link": "https://www.pelago.com/en-SG/activity/p8pl4-singtel-prepaid-sim-card-singapore/",
            "booked": False, 
            "price": "~₹750 - ₹950 / person (100 GB)"
        },
        {
            "id": "t1", 
            "date": "17 Dec 2026", 
            "due_date": "Book by Nov 20, 2026", 
            "name": "Singapore Cable Car SkyPass", 
            "status": "To Book", 
            "link": "https://www.klook.com/en-IN/activity/132-singapore-cable-car-sky-pass-singapore/", 
            "pelago_link": "https://www.pelago.com/en-SG/activity/singapore-cable-car-singapore",
            "booked": False, 
            "price": "~₹2,200 / person"
        },
        {
            "id": "t2", 
            "date": "17 Dec 2026", 
            "due_date": "Book by Nov 20, 2026 · Daily Shows: 7:40 PM & 8:40 PM", 
            "name": "Wings of Time Fireworks Symphony (Sentosa Central Beach Bazaar — Daily 7:40 PM & 8:40 PM)", 
            "status": "To Book", 
            "link": "https://www.klook.com/en-IN/activity/124-wings-of-time-singapore/", 
            "pelago_link": "https://www.pelago.com/en-SG/activity/wings-of-time-singapore",
            "booked": False, 
            "price": "~₹1,200 / person (SGD ~19)"
        },
        {
            "id": "t3", 
            "date": "18 Dec 2026", 
            "due_date": "Book by Nov 25, 2026", 
            "name": "Singapore Oceanarium (S.E.A. Aquarium)", 
            "status": "To Book", 
            "link": "https://www.klook.com/en-IN/activity/119-sea-aquarium-singapore/", 
            "pelago_link": "https://www.pelago.com/en-SG/activity/oceanarium-ticket-singapore",
            "booked": False, 
            "price": "~₹2,800 / person"
        },
        {
            "id": "t4", 
            "date": "18 Dec 2026", 
            "due_date": "Book by Nov 20, 2026 ⚠️ (Slots Fill Fast)", 
            "name": "Harry Potter: Visions of Magic", 
            "status": "To Book", 
            "link": "https://www.klook.com/en-IN/activity/112678-harry-potter-visions-of-magic-singapore/", 
            "pelago_link": "https://www.pelago.com/en-SG/activity/harry-potter-visions-of-magic",
            "booked": False, 
            "price": "~₹3,200 / person"
        },
        {
            "id": "t5", 
            "date": "19 Dec 2026", 
            "due_date": "Book by Nov 25, 2026", 
            "name": "River Wonders (with Giant Panda Forest)", 
            "status": "To Book", 
            "link": "https://www.klook.com/en-IN/activity/123-river-safari-singapore/", 
            "pelago_link": "https://www.pelago.com/en-SG/activity/river-wonders-singapore",
            "booked": False, 
            "price": "~₹2,600 / person"
        },
        {
            "id": "t6", 
            "date": "20 Dec 2026", 
            "due_date": "Book by Nov 20, 2026 ⚠️ (Prime Sunset Domes)", 
            "name": "Gardens by the Bay (Flower Dome + Cloud Forest & Jurassic World Experience)", 
            "status": "To Book", 
            "link": "https://www.klook.com/en-IN/activity/127-gardens-by-the-bay-singapore/", 
            "pelago_link": "https://www.pelago.com/en-SG/activity/gardens-by-the-bay-ticket-singapore",
            "booked": False, 
            "price": "~₹3,100 / person"
        },
        {
            "id": "t6-floral", 
            "date": "20 Dec 2026", 
            "due_date": "Book by Nov 20, 2026", 
            "name": "Floral Fantasy + Flight of the Dragonfly 4D Ride", 
            "status": "To Book", 
            "link": "https://www.klook.com/en-IN/activity/127-gardens-by-the-bay-singapore/", 
            "pelago_link": "https://www.pelago.com/en-SG/activity/gardens-by-the-bay-ticket-singapore",
            "booked": False, 
            "price": "~₹1,400 / person (SGD ~22)"
        },
        {
            "id": "t7", 
            "date": "20 Dec 2026", 
            "due_date": "Book by Nov 20, 2026 ⚠️ (Sunset Slot 5:30 PM)", 
            "name": "Marina Bay Sands SkyPark Observation Deck", 
            "status": "To Book", 
            "link": "https://www.klook.com/en-IN/activity/148-skypark-observation-deck-singapore/", 
            "pelago_link": "https://www.pelago.com/en-SG/activity/marina-bay-sands-skypark-observation-deck-new-singapore",
            "booked": False, 
            "price": "~₹2,100 / person"
        }
    ],

    # Camera Rental Strategy: SharePal Recommendation & Comparison
    "camera_rental": {
        "due_date": "15 November 2026",
        "recommended_choice": "DJI Osmo Pocket 3 Creator Combo",
        "rental_platform": "SharePal India (Delhi-NCR free home delivery & return pickup, 0 deposit)",
        "why_recommended": "For a romantic honeymoon in Singapore and on the Disney Adventure, DJI Osmo Pocket 3 is the undisputed winner. It has a massive 1-inch sensor for stunning low-light videos in dimly lit Disney evening shows, Gardens by the Bay night lights, and romantic dinners. The mechanical 3-axis gimbal gives buttery-smooth cinematic walking footage without bulky gear, and the rotatable screen flips to vertical for instant Instagram Reels.",
        "cameras": [
            {
                "name": "DJI Osmo Pocket 3 (Creator Combo)",
                "verdict": "⭐ Highly Recommended for Honeymoon",
                "ideal_for": "Romantic couple vlogging, Disney Cruise musicals, low-light indoor dinners, Gardens by the Bay light show, high-quality audio with wireless mic.",
                "pros": "1-inch CMOS sensor (unbeatable low-light & creamy background blur), 3-axis physical gimbal stabilization (true cinematic movie look), rotatable 2-inch OLED touchscreen (quick horizontal/vertical Reels switch), ultra-compact pocket size, DJI Mic 2 wireless transmitter included.",
                "cons": "Not waterproof (needs rain cover or umbrella during monsoon showers; don't take into cruise swimming pools).",
                "sharepal_note": "Book by Nov 15 on SharePal Delhi for Dec 12 delivery."
            },
            {
                "name": "Insta360 X4 (8K 360° Action Cam)",
                "verdict": "Alternative for Action / Riding / Beach Only",
                "ideal_for": "Action sports, Skyline Luge downhill racing, Siloso beach water splashes, 'third-person invisible selfie stick' drone-like shots.",
                "pros": "Complete 360-degree capture (reframe in app after shooting), invisible selfie stick effect, fully waterproof down to 10m, rugged and durable.",
                "cons": "Weak in low-light and indoor restaurants (360 lenses split pixels, causing graininess); requires tedious reframing/editing for every clip; not flattering for couple close-ups or soft portraits.",
                "sharepal_note": "Great for biking/sports trips, but secondary to Pocket 3 for romantic honeymoon moments."
            },
            {
                "name": "Insta360 Ace Pro (Co-engineered with Leica)",
                "verdict": "Rugged Action Alternative",
                "ideal_for": "High-impact water sports, wet pool decks, action POV shots.",
                "pros": "Flip screen, Leica lens, good PureVideo low-light mode for an action camera, tough waterproof body.",
                "cons": "Wide action lens with electronic crop (no true optical/mechanical bokeh), heavier than Pocket 3, lacks the motorized face-tracking gimbal that keeps Shaiwal & Shaila smoothly centered.",
                "sharepal_note": "Sturdy, but Pocket 3 produces vastly more romantic, movie-like honeymoon footage."
            }
        ]
    },

    # Free Romantic Attractions
    "free_attractions": [
        "Siloso Beach & Palawan Beach (Sentosa rope bridge to southernmost point of Asia)",
        "Garden Rhapsody Light & Sound Show at Supertree Grove (Nightly 7:45 PM & 8:45 PM)",
        "Spectra Light & Water Show at Marina Bay Sands Event Plaza (Nightly 8:00 PM & 9:00 PM)",
        "Merlion Park & Marina Bay Waterfront Promenade",
        "Jewel Changi Rain Vortex indoor waterfall and Shiseido Forest Valley",
        "Little India & Chinatown vibrant heritage streets and temples",
        "Fort Canning Park Tree Tunnel and Spice Garden (near Carlton Hotel)"
    ],

    # Little India Heritage Temples & Best Shopping Guide
    "little_india_guide": {
        "title": "Little India Temples & Best Shopping Places 🛕🛍️",
        "subtitle": "Serangoon Road Cultural Heart & Bazaars",
        "temples": [
            {
                "name": "Sri Veeramakaliamman Temple (Shri Viliyam)",
                "year": "Est. 1855 · Historic Little India",
                "desc": "Singapore's most prominent Kali temple along Serangoon Road. Built in 1855 by early Indian pioneer settlers for divine protection.",
                "highlight": "Breathtaking multi-tiered Rajagopuram entrance tower adorned with hundreds of colorful, intricate statues of Goddess Kali and Hindu deities."
            },
            {
                "name": "Sri Mariamman Temple (Chinatown Link)",
                "year": "Est. 1827 · Singapore's Oldest Hindu Temple",
                "desc": "Singapore's oldest and grandest national monument Hindu temple, dedicated to Goddess Mariamman (healer & protector). Located along South Bridge Road right next to Chinatown.",
                "highlight": "Legendary 6-tier monumental Gopuram covered in detailed plaster sculptures of Hindu mythological figures, flags, and deities. Host of the historic firewalking (Theemithi) ceremony."
            },
            {
                "name": "Sri Srinivasa Perumal Temple",
                "year": "Est. 1855 · National Monument",
                "desc": "Majestic temple dedicated to Lord Vishnu, featuring expansive temple courtyards and serene sanctity. Serves as the key starting ground for the annual Thaipusam festival.",
                "highlight": "Soaring 20-meter high Gopuram depicting the Dashavatara (10 celestial incarnations of Lord Vishnu) and intricate ceiling mandala carvings."
            },
            {
                "name": "Sakya Muni Buddha Gaya Temple",
                "year": "Temple of 1,000 Lights",
                "desc": "Renowned Buddhist monastery located along Race Course Road, founded in 1927 by the venerable Vutthisasna.",
                "highlight": "Spectacular 15-meter tall seated Buddha statue illuminated by a dazzling chain of 1,000 glowing lights, plus a reclining Buddha chamber."
            },
            {
                "name": "Abdul Gafoor Mosque",
                "year": "Est. 1859 · National Monument",
                "desc": "Unique architectural marvel blending Moorish, South Indian, and Victorian Roman neoclassical styles on Dunlop Street.",
                "highlight": "Delicate Roman-inspired columns, ornate minarets, and a rare sundial adorned with 25 rays representing the 25 Islamic prophets."
            }
        ],
        "shops": [
            {
                "name": "House of Tan Teng Niah (Heritage Rainbow Villa)",
                "tag": "Iconic 1900 Chinese Villa & Photo Hotspot",
                "desc": "Located on Kerbau Road. The last surviving Chinese villa in Little India, celebrated for its 8-color kaleidoscope pastel shophouse facade.",
                "what_to_buy": "The #1 honeymoon photo destination in Little India! Surrounded by cozy artisanal cafes, art souvenir stalls, and flower garland stands."
            },
            {
                "name": "Mustafa Centre",
                "tag": "24/7 Mega Mall · Packed Food & Daily Essentials",
                "desc": "A legendary multi-storey retail powerhouse across Syed Alwi Road. Sells virtually everything under the sun across 6 massive interconnected levels at unbeatable wholesale rates.",
                "what_to_buy": "Packed Food & Ready-to-Eat Meals (MTR & Haldiram retort curry/rice pouches, instant noodles, freshly packed samosas, puffs & Indian mithai), Daily Essentials & Toiletries (sunscreens, moisturisers, shampoos, wet wipes, Tiger Balm), Groceries & Dry Fruits, Swiss & Belgian chocolates, travel adapters, and designer perfumes."
            },
            {
                "name": "Little India Arcade",
                "tag": "Campbell Lane Pedestrian Bazaar",
                "desc": "Restored 1920s heritage shophouses buzzing with vibrant music, traditional craftsmanship, and aromatic flower garland weavers.",
                "what_to_buy": "Traditional silk saris, embroidered kurtas, brass statues & pooja lamps, intricate henna (mehndi) body art, and handmade handicrafts."
            },
            {
                "name": "Tekka Centre",
                "tag": "Iconic Wet Market & Hawker Complex",
                "desc": "Located right beside Little India MRT (NE7). Singapore's largest indoor traditional apparel and culinary market.",
                "what_to_buy": "Affordable ethnic Punjabi suits, Bollywood dresses, tailoring services, and Singapore's finest masala dosa, biryani & teh tarik."
            },
            {
                "name": "Serangoon Road Gold & Jewelry Corridor",
                "tag": "22K & 24K Gold Specialists",
                "desc": "The glittering main thoroughfare of Little India lined with prestigious Indian jewelers like Malabar Gold, Joyalukkas, and GRT.",
                "what_to_buy": "Authentic hallmarked 22K gold rings, bangles, bridal designs, and tax-free certified jewelry (eligible for 8-9% GST refund)."
            }
        ]
    },

    # Chinatown Heritage & Shopping Guide (What to Buy & Where to Go)
    "chinatown_guide": {
        "title": "Chinatown Heritage & Best Shopping Guide 🏮🛍️",
        "subtitle": "Pagoda Street, Trengganu Street & Heritage Shophouses",
        "how_to_reach": "Take North-East Line (Purple MRT) direct to Chinatown MRT (NE4). Take Exit A to emerge right into the heart of Pagoda Street souvenir bazaar.",
        "shops": [
            {
                "name": "Pagoda Street Souvenir Street Market",
                "tag": "Best Budget Souvenirs in Singapore",
                "desc": "The pedestrian-only epicenter of Chinatown shopping directly at Chinatown MRT Exit A. Colorful rows of heritage shophouses offering unbeatable prices on Singapore souvenirs.",
                "what_to_buy": "Singapore Merlion fridge magnets (5–6 for $10), metal keychains, snow globes, engraved bottle openers, Singapore T-shirts ($5–$10), coasters, and postcards."
            },
            {
                "name": "Yue Hwa Chinese Products (Eu Tong Sen St)",
                "tag": "6-Storey Heritage Department Store",
                "desc": "Iconic multi-storey department store housed in a grand 1927 heritage landmark. Offers authentic high-quality Chinese cultural goods, fashion, teas, and wellness products.",
                "what_to_buy": "Pure silk cheongsams & silk sleepwear robes, hand-painted porcelain tea sets, authentic ceramic dining sets, calligraphy brushes, and traditional medicinal ointments."
            },
            {
                "name": "Pek Sin Choon & Tea Merchants",
                "tag": "Oldest Tea Merchant (Est. 1925)",
                "desc": "Historic tea artisans that supply tea to famous bak kut teh restaurants and tea connoisseurs across Southeast Asia.",
                "what_to_buy": "Premium loose-leaf Chinese teas: Royal Jasmine tea, floral blooming tea balls (blooms in hot water), Tie Guan Yin Oolong, and artisanal clay tea pots."
            },
            {
                "name": "Chinatown Herbal Dispensaries & Tiger Balm",
                "tag": "Traditional Wellness & Balms",
                "desc": "Old-world Chinese medical halls along Temple Street and South Bridge Road selling certified natural remedies and ointments.",
                "what_to_buy": "Tiger Balm Red & White ointments, cooling muscle pain relief patches, Kwan Loong medicated oil, and soothing herbal throat drops."
            },
            {
                "name": "Lim Chee Guan & Traditional Confectionery",
                "tag": "Heritage Sweet Treats & Bakkwa",
                "desc": "Famed heritage confectioneries along New Bridge Road and Smith Street renowned for Singapore's sweetest gourmet souvenirs.",
                "what_to_buy": "Pandan coconut Kaya jam jars (for authentic Singapore breakfast toasts), handmade pineapple tarts, and sweet barbecued bakkwa jerky."
            }
        ],
        "attractions": [
            {
                "name": "Sri Mariamman Temple (Singapore's Oldest Hindu Temple)",
                "year": "Est. 1827 · National Monument of Singapore",
                "location": "244 South Bridge Road (corner of Pagoda Street, Chinatown)",
                "desc": "Singapore's oldest, most revered Hindu temple, founded in 1827 by Naraina Pillai. Dedicated to Goddess Mariamman, worshipped for healing illnesses, rains, and protection. Features the famous annual fire-walking (Theemithi) ceremony.",
                "highlight": "Breathtaking 6-tiered monumental Gopuram entrance tower towering over Chinatown, lavishly sculpted with hundreds of colorful Hindu gods, mythical beasts, and divine dancers. Inside, admire ornate ceiling murals and sanctums dedicated to Lord Murugan, Lord Vinayagar, and Lord Rama."
            },
            {
                "name": "Buddha Tooth Relic Temple & Museum",
                "year": "Est. 2007 · Tang Dynasty Buddhist Stupa",
                "location": "288 South Bridge Road (3 mins walk from Sri Mariamman Temple)",
                "desc": "Monumental Tang-style Buddhist architectural marvel housing what is believed to be the sacred left canine tooth of Buddha.",
                "highlight": "4th-floor Sacred Light Hall housing a massive 3.5-ton solid gold stupa, plus a rooftop rooftop garden with a giant Tibetan prayer wheel."
            }
        ]
    },

    # Bugis Street & Haji Lane Shopping & Street Art Guide
    "bugis_haji_guide": {
        "title": "Bugis Street & Haji Lane Guide 👗🎨🛍️",
        "subtitle": "Singapore's Cheapest Fashion Market & Iconic Street Art Alley",
        "how_to_reach": "Take Downtown Line (Blue MRT) from Chinatown MRT (DT19) direct to Bugis MRT (DT14 Exit C, only 4 stops / 7 mins!). Haji Lane is a scenic 5-minute walk (400m) from Bugis MRT / Bugis Junction.",
        "spots": [
            {
                "name": "Bugis Street Market (3-Storey Fashion Maze)",
                "tag": "Singapore's #1 Cheap Fashion Mecca",
                "location": "Opposite Bugis Junction (Bugis MRT Exit C)",
                "desc": "Singapore's largest undercover street shopping destination with 800+ stalls. The ground level features budget trendy streetwear, level 2 is packed with air-conditioned boutique Korean and Japanese style dresses, and level 3 has shoe and luggage shops.",
                "what_to_buy": "Trendy summer maxi dresses ($10–$15), beach co-ord sets, graphic crop tops, cute sun hats, trendy sunglasses, handbags, Korean skincare/cosmetics, phone cases, and portable rechargeable neck fans."
            },
            {
                "name": "Iconic Haji Lane Graffiti Murals & Wall Paintings 🎨",
                "tag": "World-Famous Instagram Couple Photos",
                "location": "Along Haji Lane & corner of Beach Road / Ophir Road",
                "desc": "A dazzling open-air gallery of towering multi-story wall murals and kaleidoscopic street art. World-famous artists have transformed heritage shophouses into photographic masterpieces.",
                "what_to_buy": "Highlights: The towering Aztec/Mayan warrior mural outside Piedra Negra, vibrant pop-art cartoon murals outside Blu Jaz Cafe, and monochrome vintage paintings. Strike romantic couple poses with natural daylight or evening neon glow!"
            },
            {
                "name": "Trendy Aesthetic Cafes & Dessert Bars ☕🍰",
                "tag": "Hipster Coffee & Couple Chillout",
                "location": "Haji Lane, Arab Street & Baghdad Street",
                "desc": "The most fashionable cluster of aesthetic concept cafes in Singapore, featuring pastel interiors, neon signs, and artisan baristas.",
                "what_to_buy": "Top Trendy Cafes: • Selfie Coffee (print your couple photo on foam!), • Earlybird Cafe (famous fried chicken & birdcage aesthetic), • Windowsill Pies (gourmet floral pies), • I Am... Cafe (Dutch-themed mocktails), and • % Arabica (world-famous minimalist Japanese coffee)."
            },
            {
                "name": "Quirky Fashion Boutiques & Vintage Stores 👗✨",
                "tag": "Indie Fashion & Bohemian Treasures",
                "location": "Mid-section of Haji Lane (between North Bridge Rd & Beach Rd)",
                "desc": "Chic, independent concept stores offering one-of-a-kind handcrafted garments, accessories, and nostalgic collectibles away from generic mall brands.",
                "what_to_buy": "Vintage Y2K clothing, bespoke handmade leather totes, retro cat-eye sunglasses, artisan perfume blending (scents customized for couples), handmade bohemian silver jewelry, and indie lifestyle home decor."
            }
        ]
    },

    # Strict Rules, Do's & Don'ts (The Fine City)
    "rules": {
        "donts": [
            {"title": "No Chewing Gum", "desc": "Importing or carrying bulk chewing gum is strictly illegal. Fines up to SGD 1,000."},
            {"title": "No Eating or Drinking on MRT / Buses", "desc": "Strictly no snacks or drinks (even plain water) inside MRT stations and trains. Fine: SGD 500."},
            {"title": "No Vapes / E-Cigarettes", "desc": "Completely prohibited and confiscated at customs. Fines up to SGD 2,000."},
            {"title": "No Smoking Outside Designated Areas", "desc": "Only smoke in yellow box Designated Smoking Areas (DSAs). Fine: SGD 200 - SGD 1,000."},
            {"title": "No Littering or Spitting", "desc": "Dropping tissue or trash carries a SGD 300 first-time on-the-spot fine."},
            {"title": "No Jaywalking", "desc": "Always use pedestrian crossings or overhead bridges within 50m of traffic. Fine: SGD 50+."},
            {"title": "No Connecting to Open Unsecured Wi-Fi", "desc": "Legally considered unauthorized network access under Computer Misuse Act."},
            {"title": "Don't Over-Rely on Cabs as a Couple", "desc": "Cabs (Grab/Gojek) cost SGD 15–25 (₹1,500–2,000) per trip. MRT is only SGD 1.5–2 (₹100–150) and reaches everywhere fast."},
            {"title": "Don't Buy Tickets at Venue Counters", "desc": "Counter queues take 30–60 mins and cost 10–20% more than booking in advance on Klook."}
        ],
        "dos": [
            {"title": "Tap Water is 100% Safe (Refill Flasks)", "desc": "Singapore tap water is cleaner than bottled water. Bottled water costs SGD 2.50 (~₹180). Carry reusable insulated flasks and refill at hotels & attractions."},
            {"title": "Claim 8–9% GST Tourist Refund at Changi", "desc": "Spend > SGD 100 at any single participating store? Present your passport at checkout for eTRS tax-free slip and claim 8–9% refund at Changi Airport kiosks before your flight home."},
            {"title": "Tap Contactless VISA / Mastercard or EZ-Link for MRT & Buses", "desc": "You can tap contactless VISA or Mastercard directly at MRT gantry turnstiles and bus card readers with no setup! Alternatively, traditional EZ-Link stored-value cards are also widely accepted."},
            {"title": "Tipping is NOT Customary", "desc": "10% service charge and 9% GST are already included in hotel and restaurant bills."},
            {"title": "Modest Temple Attire", "desc": "Cover shoulders and knees when entering Hindu, Buddhist, or Muslim places of worship in Little India and Chinatown."},
            {"title": "Download Grab & Gojek Apps", "desc": "Download both apps in India before flying. Airport street taxis charge premium surge rates; Grab/Gojek offer fixed upfront prices."},
            {"title": "Watch Free Night Light Shows", "desc": "Supertree Grove Garden Rhapsody (7:45 PM & 8:45 PM) and Spectra Waterfront Laser Show (8:00 PM & 9:00 PM) are 100% free romantic highlights!"}
        ]
    },

    # Curated Romantic Dining & Places to Eat (Fully Editable)
    "dining_places": [
        {
            "id": "d1",
            "name": "Trapizza (Siloso Beach, Sentosa)",
            "area": "Sentosa Beachfront",
            "cuisine": "Italian / Pizza / Casual Beachfront",
            "highlight": "Wood-fired Pizzas & Pastas right on the sand. Perfect for sunset with cocktails.",
            "status": "Must Visit",
            "day_number": 5
        },
        {
            "id": "d2",
            "name": "Cassia (Capella Singapore)",
            "area": "Sentosa Heritage",
            "cuisine": "Ultra-Luxury Cantonese / Dim Sum",
            "highlight": "Heritage 1880s manor. Exceptional vegetarian black truffle crystal dumplings.",
            "status": "Must Visit",
            "day_number": 6
        },
        {
            "id": "d3",
            "name": "Quayside Isle (Sentosa Cove)",
            "area": "Sentosa Marina",
            "cuisine": "Mediterranean & Italian Waterfront",
            "highlight": "Miska Café and Sole Pomodoro facing luxury yachts. Very romantic evening walk.",
            "status": "Shortlisted",
            "day_number": 5
        },
        {
            "id": "d4",
            "name": "CHIJMES Courtyards",
            "area": "City Hall (Opp. Carlton)",
            "cuisine": "Gothic Chapel Outdoor Dining",
            "highlight": "Lit with fairy lights. Great tapas, wood-fired pizza, and craft drinks across from Carlton.",
            "status": "Day 1 Dinner",
            "day_number": 1
        },
        {
            "id": "d5",
            "name": "Nalan Vegetarian (Capitol Singapore)",
            "area": "City Hall",
            "cuisine": "100% Pure Vegetarian Fine Dining",
            "highlight": "2 mins from Carlton Hotel. High quality North & South Indian curries and dosas.",
            "status": "Shortlisted",
            "day_number": 1
        },
        {
            "id": "d6",
            "name": "Lau Pa Sat (Satay Street & Hawker Centre)",
            "area": "Downtown Marina Bay",
            "cuisine": "Iconic Street Food & Satay",
            "highlight": "Boon Tat Street shuts down every evening into an open-air Satay grill feast. Spectacular vibe under city skyscrapers.",
            "status": "Must Visit",
            "day_number": 8
        },
        {
            "id": "d7",
            "name": "Little India Vegetarian Gems (Gandhi Mess, MTR, Ananda Bhavan)",
            "area": "Little India / Serangoon Rd",
            "cuisine": "Authentic Pure Vegetarian South & North Indian",
            "highlight": "Gandhi Mess for $2 dosas on banana leaves, MTR for rava idlis, Jaggi's for homestyle Punjabi parathas.",
            "status": "Shortlisted",
            "day_number": 7
        },
        {
            "id": "d8",
            "name": "Cultivate Cafe (Maxwell Reserve)",
            "area": "Tanjong Pagar / Chinatown",
            "cuisine": "Candlelit Library Plant-Based",
            "highlight": "Candlelit library setting with artisanal pastas and plant-based fine dining.",
            "status": "Shortlisted",
            "day_number": 8
        },
        {
            "id": "d9",
            "name": "Palo Trattoria (Disney Adventure)",
            "area": "Disney Adventure High Seas",
            "cuisine": "Adults-Only Northern Italian Fine Dining",
            "highlight": "Exclusive sunset ocean views, handmade ravioli, and fine wine pairings aboard the ship.",
            "status": "Must Visit",
            "day_number": 3
        },
        {
            "id": "d10",
            "name": "Old Chang Kee (Curry Puffs & Skewers)",
            "area": "Changi Airport & Citywide Kiosks",
            "cuisine": "Classic Singapore Street Snacks",
            "highlight": "Crispy golden handmade curry puffs filled with spiced potato & egg, plus satay chicken skewers on the go.",
            "status": "Must Eat 🥟",
            "day_number": 1
        },
        {
            "id": "d11",
            "name": "Ya Kun Kaya Toast (Since 1944)",
            "area": "Far East Square / Chinatown / Sentosa",
            "cuisine": "Traditional Nanyang Breakfast",
            "highlight": "Charcoal-grilled thin toast with fragrant pandan kaya jam & cold butter, soft-boiled runny eggs with dark soy sauce, and hot Kopi/Teh.",
            "status": "Must Eat ☕",
            "day_number": 7
        },
        {
            "id": "d12",
            "name": "Chinatown Complex Hawker (Peking Duck & Popiah)",
            "area": "Chinatown (Smith Street)",
            "cuisine": "Michelin Bib Gourmand Hawker Stalls",
            "highlight": "Freshly rolled Popiah (spring rolls), handmade Dim Sum, and famous soy sauce chicken / vegetarian mushroom noodles ($3–$5 SGD).",
            "status": "Must Eat 🍜",
            "day_number": 7
        },
        {
            "id": "d13",
            "name": "Singapore Iconic 'Ice Cream Sandwich' Cart",
            "area": "Orchard Road & Waterfront Merlion Park",
            "cuisine": "Beloved Singapore Street Dessert",
            "highlight": "Street carts slicing thick blocks of wafer/rainbow bread filled with sweet corn, mint chip, durian, or mango ice cream ($1.50 SGD).",
            "status": "Must Eat 🍦",
            "day_number": 8
        },
        {
            "id": "d14",
            "name": "Roti Prata & Teh Tarik (Little India)",
            "area": "Serangoon Road / Jalan Besar",
            "cuisine": "Crispy Flaky Indian-Malay Flatbread",
            "highlight": "Flaky, hot crispy Roti Canai/Prata dipped in spicy dhal curry or sugar, washed down with frothy pulled 'Teh Tarik' milk tea.",
            "status": "Must Eat 🫓",
            "day_number": 7
        },
        {
            "id": "d15",
            "name": "Jewel Changi Shake Shack & Birds of Paradise Gelato",
            "area": "Jewel Changi Airport (Level 1)",
            "cuisine": "Botanical Artisanal Gelato",
            "highlight": "Michelin-recommended botanical gelato infused with Southeast Asian herbs & fruits (White Chrysanthemum, Pandan, Lychee Raspberry) inside fresh thyme cones.",
            "status": "Must Eat 🍧",
            "day_number": 9
        }
    ],

    # Live Expense Tracker Items (Fully Editable with actual expense tracking)
    "expenses": [
        {"id": "exp-1", "category": "Visa", "item": "Singapore e-Visa (2 Adults)", "amount": 6500, "actual_amount": 0, "currency": "INR", "status": "Pending", "notes": "Submit Nov 1"},
        {"id": "exp-2", "category": "Flights", "item": "Singapore Airlines Roundtrip (DEL - SIN · SQ 401 & SQ 406)", "amount": 81696, "actual_amount": 81696, "currency": "INR", "status": "Booked", "notes": "PNR: DVXVBM · MMT: NN7AMSIR48944422426 · Paid ₹81,696", "doc_url": "https://pub-5febf239be824301b333f51d2eaee417.r2.dev/honeymoon/docs/original_New_Delhi_To_Singapore_Flight_Tickets_13Dec_2026_21Dec.pdf", "doc_name": "Singapore Airlines Roundtrip E-Ticket & Receipt", "doc_id": "doc-sia-flights"},
        {"id": "exp-3", "category": "Hotels", "item": "Carlton Hotel Singapore (1 Night · Deluxe King Room with Breakfast)", "amount": 23950, "actual_amount": 23950, "currency": "INR", "status": "Booked", "notes": "Booking ID: NH76149509489544 · PNR: 0184752125 · Dec 13-14 · Honeymoon King Bed", "doc_url": "https://pub-5febf239be824301b333f51d2eaee417.r2.dev/honeymoon/docs/original_CarlonHotel_Dec13_Dec14.pdf", "doc_name": "Carlton Hotel Singapore Official Voucher", "doc_id": "doc-carlton-hotel"},
        {"id": "exp-oasia-sentosa", "category": "Hotels", "item": "Oasia Resort Sentosa (4 Nights · Family Suite with Sofa Bed)", "amount": 135804, "actual_amount": 135804, "currency": "INR", "status": "Booked", "notes": "Booking ID: NH77022510686190 · PNR: 0185175700 · Dec 17–21 · Palawan Ridge Sentosa", "doc_url": "https://pub-5febf239be824301b333f51d2eaee417.r2.dev/honeymoon/docs/original_Oasis_Resort_Sentosa_Dec17_Dec21.pdf", "doc_name": "Oasia Resort Sentosa Official Voucher (4 Nights)", "doc_id": "doc-oasia-sentosa"},
        {"id": "exp-ins-hotel", "category": "Insurance", "item": "Tata AIG Travel Insurance ($250,000 USD Medical Cover · 2 Adults)", "amount": 886, "actual_amount": 886, "currency": "INR", "status": "Paid", "notes": "Cert No: 50027999 · Order ID: MTMINFIH41529640636128 · Dec 13-14 Singapore", "doc_url": "https://pub-5febf239be824301b333f51d2eaee417.r2.dev/honeymoon/docs/original_Insurance_MTMINFIH41529640636128_Shaiwal_and_Shaila.pdf", "doc_name": "Tata AIG Travel Insurance Certificate ($250,000 USD)", "doc_id": "doc-tata-aig-insurance"},
        {"id": "exp-4", "category": "Cruise", "item": "Disney Adventure Cruise (3-Night Deluxe Verandah Stateroom #11680)", "amount": 178000, "actual_amount": 178000, "currency": "INR", "status": "Booked", "notes": "Reservation: 44985264 · $2,115.90 USD (~₹1.78L) · Dec 14–17 · Second Dining 8:15 PM", "doc_url": "https://pub-5febf239be824301b333f51d2eaee417.r2.dev/honeymoon/docs/original_Disney_Cruise_Bibbidi_bobbidi_booked.pdf", "doc_name": "Disney Adventure Cruise Official Confirmation & Contract", "doc_id": "doc-dcl"},
        {"id": "exp-5", "category": "Activities", "item": "All 7 Klook Sightseeing Passes (2 Adults)", "amount": 34000, "actual_amount": 0, "currency": "INR", "status": "To Book", "notes": "Cable Car, River Wonders, Gardens, MBS"},
        {"id": "exp-6", "category": "Food & Dining", "item": "Romantic Dinners, Cafes, Gelato & Street Food", "amount": 40000, "actual_amount": 0, "currency": "INR", "status": "Budget", "notes": "Trapizza, CHIJMES, Rotational dining tips"}
    ],

    # Uploaded Tickets, Vouchers & PDF Documents (Original Customer PDFs)
    "documents": [
        {
            "id": "doc-dcl",
            "name": "Disney Adventure Cruise Official Confirmation & Contract",
            "category": "Cruise",
            "filename": "Disney Cruise- Bibbidi, bobbidi, booked!.pdf",
            "url": "https://pub-5febf239be824301b333f51d2eaee417.r2.dev/honeymoon/docs/original_Disney_Cruise_Bibbidi_bobbidi_booked.pdf",
            "size": "634 KB · 18 Pages",
            "expense_id": "exp-4",
            "uploaded_at": "04-Aug-2026 · Confirmed",
            "booking_id": "44985264",
            "pnr": "11680 (Deck 11)",
            "dates": "14-Dec-2026 (4 PM) to 17-Dec-2026 (7 AM)",
            "stateroom": "Stateroom 11680 · Category 06C (Deluxe Oceanview with Verandah)",
            "meal_plan": "Second Seating: 8:15 PM Rotational Dining",
            "travellers": "Mr Shaiwal Sachdev (Adult), Ms Shaila Manaktahla (Adult)",
            "special_requests": "Late Dining 8:15 PM, Verandah Oceanview Deck 11 Aft, Magnetic Door Art, Broadway Shows & Character Greets included",
            "amount_paid": "$2,115.90 USD (~ ₹1,78,000 Total Paid in Full)"
        },
        {
            "id": "doc-sia-flights",
            "name": "Singapore Airlines Roundtrip E-Ticket & Receipt",
            "category": "Flights",
            "filename": "New_Delhi_To_Singapore_Flight_Tickets_13Dec_2026_21Dec.pdf",
            "url": "https://pub-5febf239be824301b333f51d2eaee417.r2.dev/honeymoon/docs/original_New_Delhi_To_Singapore_Flight_Tickets_13Dec_2026_21Dec.pdf",
            "size": "1.09 MB · Confirmed",
            "expense_id": "exp-2",
            "uploaded_at": "6 Aug 2026 · Confirmed",
            "booking_id": "NN7AMSIR48944422426",
            "pnr": "DVXVBM",
            "dates": "13 Dec 2026 – 21 Dec 2026",
            "travellers": "Shaila Manaktahla (2479949698), Shaiwal Sachdev (2479949699)",
            "flight_summary": "DEL (09:45) -> SIN (18:00) [SQ 401] | SIN (16:40) -> DEL (20:00) [SQ 406]",
            "baggage": "Cabin: 7kg/person · Check-in: 25kg (DEL-SIN) / 30kg (SIN-DEL)",
            "inclusions": "Tata AIG Travel Insurance (P1C1X1/P2C1X1), Visa Protection Guarantee, Price Drop Protection, Jewel Changi Airport Ticket",
            "amount_paid": "₹81,696 (Paid via EMI Credit Card)"
        },
        {
            "id": "doc-carlton-hotel",
            "name": "Carlton Hotel Singapore Official Voucher",
            "category": "Hotels",
            "filename": "CarlonHotel_Dec13_Dec14.pdf",
            "url": "https://pub-5febf239be824301b333f51d2eaee417.r2.dev/honeymoon/docs/original_CarlonHotel_Dec13_Dec14.pdf",
            "size": "137 KB · Confirmed",
            "expense_id": "exp-3",
            "uploaded_at": "16 Aug 2026 · Confirmed",
            "booking_id": "NH76149509489544",
            "pnr": "0184752125",
            "dates": "Check-in: Sun, 13 Dec (2 PM) · Check-out: Mon, 14 Dec (11 AM)",
            "address": "76 Bras Basah Road, Singapore 189558 (+65 6338 8333)",
            "room_type": "1x Deluxe Room (Guaranteed King Bed)",
            "meal_plan": "Buffet Breakfast Included for 2 + 10% F&B Discount",
            "special_requests": "Late Check-out 3 PM (Cruise Departure), Honeymoon Cake & Decor, Higher Floor, Airport Transfer note (Changi SQ 401 landing 6 PM)",
            "insurance": "Tata AIG Hotel Insurance (MTMINFIH41529640636128)",
            "amount_paid": "₹23,950 (HDFC Bank: ₹23,450 + Gift Card: ₹500)"
        },
        {
            "id": "doc-carlton-policy",
            "name": "Carlton Hotel Singapore Booking Rules & House Policies",
            "category": "Hotels",
            "filename": "Carlton_Hotel_Booking_Policy.pdf",
            "url": "https://pub-5febf239be824301b333f51d2eaee417.r2.dev/honeymoon/docs/original_Carlton_Hotel_Booking_Policy.pdf",
            "size": "155 KB · Official Rules",
            "uploaded_at": "16 Aug 2026 · Policy",
            "booking_id": "NH76149509489544",
            "special_requests": "Cash & Card deposit accepted, Passport required, 100% Smoke-Free, Outside food allowed",
            "amount_paid": "Official Policy Document"
        },
        {
            "id": "doc-oasia-sentosa",
            "name": "Oasia Resort Sentosa Official Voucher (4 Nights)",
            "category": "Hotels",
            "filename": "Oasis Resort Sentosa_Dec17_Dec21.pdf",
            "url": "https://pub-5febf239be824301b333f51d2eaee417.r2.dev/honeymoon/docs/original_Oasis_Resort_Sentosa_Dec17_Dec21.pdf",
            "size": "146 KB · Confirmed",
            "expense_id": "exp-oasia-sentosa",
            "uploaded_at": "20 Aug 2026 · Confirmed",
            "booking_id": "NH77022510686190",
            "pnr": "0185175700",
            "dates": "Check-in: Thu, 17 Dec (3 PM) · Check-out: Mon, 21 Dec (12 PM)",
            "address": "23 Beach View Rd, Palawan Ridge, Sentosa Island, 098679 (+65 6818 3388)",
            "room_type": "1x Family Suite with Sofa Bed (1 King Bed + 1 Sofa Bed)",
            "inclusions": "Complimentary welcome drinks (Soft Beverages) on arrival, Wellness & Pool access",
            "special_requests": "Early Check-in 11:00 AM (Post-cruise docking at 7 AM), Honeymoon celebration cake, Room decoration, Late check-out 1 PM, Non-smoking near lift",
            "insurance": "Acko General Insurance (MTMINFIH41529691940492)",
            "amount_paid": "₹1,35,804 (Paid via HDFC Bank ending 8189)"
        },
        {
            "id": "doc-oasia-policy",
            "name": "Oasia Resort Sentosa Official Rules & House Policies",
            "category": "Hotels",
            "filename": "Oasis_Hotel_Booking_Policy.pdf",
            "url": "https://pub-5febf239be824301b333f51d2eaee417.r2.dev/honeymoon/docs/original_Oasis_Hotel_Booking_Policy.pdf",
            "size": "154 KB · Official Rules",
            "uploaded_at": "20 Aug 2026 · Policy",
            "booking_id": "NH77022510686190",
            "special_requests": "Mandatory SGD 50/night deposit, 100% Cashless, No outside food, 100% Smoke-Free",
            "amount_paid": "Official Policy Document"
        },
        {
            "id": "doc-tata-aig-insurance",
            "name": "Tata AIG Travel Insurance Certificate ($250,000 USD)",
            "category": "Insurance",
            "filename": "Insurance_MTMINFIH41529640636128_Shaiwal_and_Shaila.pdf",
            "url": "https://pub-5febf239be824301b333f51d2eaee417.r2.dev/honeymoon/docs/original_Insurance_MTMINFIH41529640636128_Shaiwal_and_Shaila.pdf",
            "size": "709 KB · 11 Pages",
            "expense_id": "exp-ins-hotel",
            "uploaded_at": "15 Aug 2026 · Active",
            "policy_no": "Master Policy: 0239870137 · Certificate: 50027999",
            "order_id": "MTMINFIH41529640636128",
            "coverage_dates": "13 Dec 2026 to 14 Dec 2026 (2 Travel Days · Single Trip)",
            "insured_persons": "Shaiwal Sachdev (Primary), Shaila Manaktahla",
            "sum_insured": "$250,000 USD Medical per person (Includes COVID-19 Inpatient)",
            "key_benefits": "Emergency Medical Evacuation ($250k), Repatriation ($250k), Personal Liability ($50k), Baggage Loss ($500), Passport Loss ($250), Compassionate Visit ($1,000)",
            "assistance": "24x7 Global Helpline: +91 22 6822 7600 · WhatsApp: +91 9136160375",
            "amount_paid": "₹886 (Gross: ₹750.85 + GST: ₹135.15)"
        }
    ],

    # Rainy Season Packing Essentials & Outfit Planner (Dec 13-21)
    "packing_and_outfits": {
        "weather_insight": "December is Singapore's Northeast Monsoon season. Expect frequent, short tropical rain showers and thunderstorms (usually 45–90 mins, often in afternoons), warm temperatures (27°C–31°C), and high humidity (80%+). Strong indoor air conditioning on Disney Cruise and malls contrasts with outdoor warmth.",
        "rainy_essentials": [
            {"item": "2x Compact Windproof Umbrellas", "desc": "Tuck one into Shaiwal's daypack and one in Shaila's bag. Essential for sudden tropical showers.", "icon": "umbrella"},
            {"item": "Lightweight Breathable Rain Ponchos", "desc": "Far more breathable than heavy winter raincoats. Keeps you dry at River Wonders, Universal, and Sentosa without sweating.", "icon": "water_drop"},
            {"item": "Waterproof Phone Pouch / Dry Bag (10L)", "desc": "Keep phones, passports, and cameras bone-dry at Sentosa beach, water slides, and river safari.", "icon": "lock"},
            {"item": "Quick-Drying Fabrics (Linen, Poly-Blend)", "desc": "Avoid heavy denim or thick cotton that stays damp for hours in tropical humidity.", "icon": "checkroom"},
            {"item": "Waterproof Sandals & Comfortable Walking Shoes", "desc": "Birkenstock EVA / waterproof sandals for rainy streets + 1 pair ultra-comfy broken-in sneakers each (12,000–18,000 steps daily).", "icon": "hiking"},
            {"item": "Light Cardigan / Shawl for Cruise & Indoors", "desc": "Walt Disney Theatre, Rotational Dining rooms, and Cloud Forest run at chilly 19°C–21°C air-conditioning.", "icon": "ac_unit"},
            {"item": "Silica Gel Packs / Ziploc Bags", "desc": "Place silica gel packets in luggage and camera bags to prevent lens moisture during humid-to-cold transitions.", "icon": "inventory_2"}
        ],
        "packing_checklist": [
            # Electronics & Power
            {
                "id": "p-elec-1",
                "category": "Electronics & Power",
                "item": "Universal Travel Adapter (Type G / UK 3-Pin)",
                "detail": "Singapore and Disney Adventure use Type G (UK 3-pin). Bring a multi-plug universal adapter with built-in USB-C fast charging ports.",
                "rule": "Mandatory for Carlton Hotel & Oasia Sentosa. Pack in cabin or checked luggage.",
                "icon": "electrical_services",
                "packed": False,
                "target_days": [1, 2, 5]
            },
            {
                "id": "p-elec-2",
                "category": "Electronics & Power",
                "item": "Power Banks (10,000–20,000 mAh max 2 per person)",
                "detail": "Strict Airline Rule: Power banks are 100% FORBIDDEN in checked luggage! Must be in HAND LUGGAGE only (< 100Wh).",
                "rule": "Strict Hand Luggage Only (DGCA / CAAS). Essential for all-day navigation & photos.",
                "icon": "battery_charging_full",
                "packed": False,
                "target_days": [1, 6, 7, 8, 9]
            },
            {
                "id": "p-elec-3",
                "category": "Electronics & Power",
                "item": "Multi-Port USB-C Fast GaN Charger (65W–100W)",
                "detail": "Charges 2 phones, DJI camera, smartwatch, and power bank simultaneously from a single wall socket.",
                "rule": "Saves outlet space in hotel rooms & cruise cabin.",
                "icon": "power",
                "packed": False,
                "target_days": [1, 2, 5]
            },
            {
                "id": "p-elec-4",
                "category": "Electronics & Power",
                "item": "Long Braided Charging Cables (Type-C & Lightning 2m)",
                "detail": "Wall outlets on cruise staterooms and bedside hotel tables are sometimes positioned away from pillows.",
                "rule": "Pack 2x 2-meter cables.",
                "icon": "cable",
                "packed": False,
                "target_days": [1, 2, 5]
            },
            {
                "id": "p-elec-5",
                "category": "Electronics & Power",
                "item": "Rented Pocket Camera (DJI Pocket 3 / Osmo / Insta360) + Extra SD Cards",
                "detail": "Collect on Nov 15 from SharePal. Bring mini tripod, magnetic clip, and extra high-speed U3 MicroSD (128GB+).",
                "rule": "Carry on board in camera pouch.",
                "icon": "videocam",
                "packed": False,
                "target_days": [1, 2, 3, 5, 6, 8]
            },

            # Monsoon & Weather Armor
            {
                "id": "p-rain-1",
                "category": "Rain & Sun Protection",
                "item": "2x Compact Windproof Travel Umbrellas",
                "detail": "Keep one in Shaiwal's daypack and one in Shaila's handbag at all times. Tropical showers start without warning.",
                "rule": "Carry-on friendly. Instant rain defense.",
                "icon": "umbrella",
                "packed": False,
                "target_days": [1, 4, 6, 7, 8]
            },
            {
                "id": "p-rain-2",
                "category": "Rain & Sun Protection",
                "item": "2x Lightweight Breathable Rain Ponchos",
                "detail": "Far superior to heavy raincoats in 85% humidity. Keeps your clothes and backpacks bone dry at Universal and River Wonders.",
                "rule": "Reusable, packs into tiny pouch.",
                "icon": "water_drop",
                "packed": False,
                "target_days": [6, 7, 8]
            },
            {
                "id": "p-rain-3",
                "category": "Rain & Sun Protection",
                "item": "Waterproof Floating Phone Pouches (IPX8) + 10L Dry Bag",
                "detail": "Essential for Disney Cruise cantilevered infinity pool, waterslides, and Siloso beach swimming.",
                "rule": "Protects phones and cash from chlorinated pool and sea spray.",
                "icon": "lock",
                "packed": False,
                "target_days": [3, 5, 6]
            },
            {
                "id": "p-rain-4",
                "category": "Rain & Sun Protection",
                "item": "High-SPF Broad Spectrum Sunscreen (SPF 50+ PA++++)",
                "detail": "Singapore sits 1° north of the equator. UV index frequently hits 11–12 (Extreme). Apply 20 mins before stepping outdoors.",
                "rule": "Reapply every 2 hours when outdoors.",
                "icon": "wb_sunny",
                "packed": False,
                "target_days": [2, 3, 5, 6, 7, 8]
            },
            {
                "id": "p-rain-5",
                "category": "Rain & Sun Protection",
                "item": "Silica Gel Packs (For Camera & Electronics Bags)",
                "detail": "Stops internal condensation and lens fogging when moving from cold air-conditioned rooms (19°C) to humid outdoors (31°C).",
                "rule": "Drop into camera bag and stateroom pouch.",
                "icon": "inventory_2",
                "packed": False,
                "target_days": [1, 2, 4, 8]
            },

            # Cruise Traditions & Special Items
            {
                "id": "p-cruise-1",
                "category": "Cruise Special",
                "item": "Cabin Door Decorative Magnets (Stateroom 11680)",
                "detail": "Disney cruise doors are metal! Cruisers personalize their stateroom doors with custom name magnets (Shaiwal ❤️ Shaila Honeymoon).",
                "rule": "Beloved Disney cruise tradition. Prepare printed magnets beforehand.",
                "icon": "door_front",
                "packed": False,
                "target_days": [2]
            },
            {
                "id": "p-cruise-2",
                "category": "Cruise Special",
                "item": "Lanyards with Clear Card Pouches",
                "detail": "Used for holding your Disney 'Key to the World' cabin cards around the ship without carrying bags.",
                "rule": "Wear comfortably around ship deck.",
                "icon": "badge",
                "packed": False,
                "target_days": [2, 3, 4]
            },
            {
                "id": "p-cruise-3",
                "category": "Cruise Special",
                "item": "Light Evening Shawl / Cardigan",
                "detail": "Walt Disney Theatre and rotational dining restaurants are air-conditioned to 19°C. A light wrap keeps Shaila warm during Broadway shows.",
                "rule": "Keep in evening bag.",
                "icon": "ac_unit",
                "packed": False,
                "target_days": [2, 3, 4, 8]
            },

            # Health, Comfort & Pharmacy
            {
                "id": "p-health-1",
                "category": "Health & Comfort",
                "item": "Motion Sickness / Seasickness Tablets (Avomine / Dramamine)",
                "detail": "Although the mega ship Disney Adventure has advanced stabilizers, keep a pack handy for high seas.",
                "rule": "Take 30 mins before boarding if sea-sensitive.",
                "icon": "medication",
                "packed": False,
                "target_days": [2, 3]
            },
            {
                "id": "p-health-2",
                "category": "Health & Comfort",
                "item": "Blister Prevention Gel Cushions & Band-Aids",
                "detail": "You will walk 12,000 to 18,000 steps daily across Gardens by the Bay, Universal Studios, and cruise decks.",
                "rule": "Put inside sneakers or sandals on first sign of rubbing.",
                "icon": "healing",
                "packed": False,
                "target_days": [6, 7, 8]
            },
            {
                "id": "p-health-3",
                "category": "Health & Comfort",
                "item": "DEET-Free Mosquito Repellent Spray & Patches",
                "detail": "Must-have for evening Mandai Rainforest Wildlife Lumina, Night Safari, and Sentosa coastal trails.",
                "rule": "Non-aerosol spray (< 100ml for cabin).",
                "icon": "bug_report",
                "packed": False,
                "target_days": [5, 7]
            },
            {
                "id": "p-health-4",
                "category": "Health & Comfort",
                "item": "Personal Medical Kit (Paracetamol, ORS Electrolytes, Antacids)",
                "detail": "Tropical humidity dehydrates quickly; pack electrolyte fizz tablets. Antacids for spicy hawker satay and chili crab.",
                "rule": "Keep in original labeled foil strips.",
                "icon": "medical_services",
                "packed": False,
                "target_days": [1, 2, 5, 8]
            },

            # Hand Luggage Day 1 Criticals
            {
                "id": "p-hand-1",
                "category": "Hand Luggage Day 1",
                "item": "Zero Forex Credit & Debit Cards (Niyo / Scapia / Fi)",
                "detail": "Keep in wallet. Tapped for MRT gates, Grab taxis, and 7-Eleven. Carry SGD 150 cash for hawker stalls.",
                "rule": "Ensure International Card Usage is toggled ON in your banking app before flying.",
                "icon": "credit_card",
                "packed": False,
                "target_days": [1, 9]
            },
            {
                "id": "p-hand-2",
                "category": "Hand Luggage Day 1",
                "item": "Passports + e-Visa Printouts + Singapore Arrival Card PDF",
                "detail": "Never put travel documents in checked bags! Always in Shaiwal's secure daypack.",
                "rule": "Keep 2 physical hard-copy sets + saved in your portal Document Vault.",
                "icon": "folder_shared",
                "packed": False,
                "target_days": [1, 2, 4, 9]
            },
            {
                "id": "p-hand-3",
                "category": "Hand Luggage Day 1",
                "item": "First Day Embarkation Change of Clothes & Swimwear in Carry-on",
                "detail": "On cruise embarkation day, checked luggage takes until 5 PM to arrive at Stateroom 11680. Hand luggage swimwear lets you hit the infinity pool at 1 PM!",
                "rule": "Essential cruise pro-tip.",
                "icon": "luggage",
                "packed": False,
                "target_days": [2]
            }
        ],
        "outfit_count_summary": {
            "trip_duration": "9 Days / 8 Nights (Dec 13–21, 2026)",
            "shaila_total": "12–14 Outfits (Daywear, Cruise Glamour, Resort Casual, Swimwear)",
            "shaiwal_total": "11–13 Outfits (Smart Casual, Cruise Gala, Resort Linens, Swimwear)",
            "swimwear_count": "2–3 Sets each (Allows one to dry while wearing the other)"
        },
        "shaila_outfits": [
            {"category": "Disney Cruise Formal / Gala", "count": "1–2 Outfits", "suggestion": "Cocktail dress, elegant maxi, or fairytale dress for Captain Mickey Gala & Walt Disney Theatre."},
            {"category": "Disney Daywear & Princess Meet", "count": "2–3 Outfits", "suggestion": "Cute Disney-themed or pastel sundresses/rompers for daytime ship exploration and Town Square Princess meet."},
            {"category": "Romantic Dinners (City & Sentosa)", "count": "3 Outfits", "suggestion": "Classy resort-chic dresses or linen sets for CHIJMES (Day 1), Cassia Capella (Day 5), and Trapizza sunset."},
            {"category": "Sightseeing & Active Days", "count": "4 Outfits", "suggestion": "Lightweight breathable cotton/linen co-ords, breathable culottes, UV sun-hat for River Wonders, Gardens by the Bay & Universal."},
            {"category": "Swimwear & Beach Resort", "count": "2–3 Sets", "suggestion": "Swimsuits/bikinis + 2 stylish breezy kimonos/kaftan cover-ups for Wayfinder Bay cruise pool & Sentosa beaches."},
            {"category": "Footwear", "count": "3 Pairs", "suggestion": "1 pair comfy walking sneakers, 1 pair waterproof sandals (beach/rain), 1 pair elegant dinner wedges/flats."}
        ],
        "shaiwal_outfits": [
            {"category": "Disney Cruise Gala / Evening", "count": "1–2 Outfits", "suggestion": "Crisp dress shirt (or blazer/chinos combo) with formal leather loafers for Captain's Gala & Rotational Dining."},
            {"category": "Cruise Daywear & Pool Deck", "count": "2–3 Outfits", "suggestion": "Smart polo shirts, lightweight cotton shorts, linen button-downs for Imagination Garden & pool deck."},
            {"category": "Romantic Island & City Dinners", "count": "3 Outfits", "suggestion": "Linen shirts (white, sky blue, sage), tailored chinos, smart leather slip-ons for CHIJMES, Trapizza, and Quayside Isle."},
            {"category": "Sightseeing & Active Days", "count": "4 Outfits", "suggestion": "Moisture-wicking tees, comfortable stretch chino shorts, and UV sunglasses for Mandai River Safari & Marina Bay."},
            {"category": "Swimwear", "count": "2–3 Pairs", "suggestion": "Quick-dry board shorts for cruise swimming pools, Sentosa Siloso beach & Oasia resort pool."},
            {"category": "Footwear", "count": "3 Pairs", "suggestion": "1 pair supportive walking sneakers, 1 pair waterproof pool slides/sandals, 1 pair smart loafers/boat shoes for dinner."}
        ],
        "daily_outfit_planner": [
            {
                "id": "outfit-d1-eve",
                "day": 1,
                "date": "Dec 13 (Sun)",
                "time_slot": "Evening (6:30 PM - 11 PM)",
                "occasion": "Flight Arrival & CHIJMES Romantic Night Walk",
                "shaila": {
                    "dress_type": "Breezy Floral Midi Dress / Linen Co-ord",
                    "color": "Blush Pink / Lavender Pastel",
                    "color_hex": "#F472B6",
                    "footwear": "Comfortable Walking Flats / Smart Espadrilles",
                    "accessories": "Mini crossbody bag, light pearl studs, delicate hair clip",
                    "photo_url": ""
                },
                "shaiwal": {
                    "dress_type": "Crisp Linen Button-down & Tailored Chino Shorts",
                    "color": "Soft White Shirt + Olive Chinos",
                    "color_hex": "#60A5FA",
                    "footwear": "Breathable White Sneakers / Slip-on Loafers",
                    "accessories": "Leather-strap watch, compact sling bag with passports",
                    "photo_url": ""
                },
                "style_notes": "Comfortable for 6-hr flight + instant evening dinner glow at Carlton & CHIJMES courtyard."
            },
            {
                "id": "outfit-d2-morn",
                "day": 2,
                "date": "Dec 14 (Mon)",
                "time_slot": "Morning & Afternoon (10 AM - 4 PM)",
                "occasion": "Marina Bay Terminal & Disney Adventure Embarkation Party",
                "shaila": {
                    "dress_type": "Disney Princess Sundress / Nautical Sailor Chic",
                    "color": "Sky Blue or Polka Dot Red (Minnie Theme)",
                    "color_hex": "#38BDF8",
                    "footwear": "Waterproof White Slides or Platform Sneakers",
                    "accessories": "Disney Minnie Mouse Ears headband, sunglasses, tote bag",
                    "photo_url": ""
                },
                "shaiwal": {
                    "dress_type": "Smart Nautical Polo Shirt & Khaki Chino Shorts",
                    "color": "Navy Blue Polo + Beige Chino Shorts",
                    "color_hex": "#1E40AF",
                    "footwear": "Classic Boat Shoes or Clean White Low-tops",
                    "accessories": "Polarized sunglasses, DJI Pocket camera wrist strap",
                    "photo_url": ""
                },
                "style_notes": "Wear your cruise check-in outfit ready for embarkation photos and Sailaway party at Imagination Garden!"
            },
            {
                "id": "outfit-d2-night",
                "day": 2,
                "date": "Dec 14 (Mon)",
                "time_slot": "Night (6 PM - 11 PM)",
                "occasion": "Captain's Gala, Broadway Theatre & Animator's Palate Dinner",
                "shaila": {
                    "dress_type": "Elegant Cocktail Dress or Flowing Satin Evening Gown",
                    "color": "Emerald Green or Royal Navy",
                    "color_hex": "#059669",
                    "footwear": "Strappy Block Heels / Chic Dressy Wedges",
                    "accessories": "Statement pendant necklace, sparkling clutch, diamond-look earrings",
                    "photo_url": ""
                },
                "shaiwal": {
                    "dress_type": "Sharp Tailored Blazer / Crisp Collar Dress Shirt & Trousers",
                    "color": "Charcoal / Dark Navy Blazer + Crisp White Shirt",
                    "color_hex": "#334155",
                    "footwear": "Polished Leather Loafers / Oxford Dress Shoes",
                    "accessories": "Dress watch, cufflinks, pocket square",
                    "photo_url": ""
                },
                "style_notes": "Formal cruise gala night! Beautiful photos with Mickey & Minnie in captain tuxedos."
            },
            {
                "id": "outfit-d3-day",
                "day": 3,
                "date": "Dec 15 (Tue)",
                "time_slot": "Daytime (9 AM - 5 PM)",
                "occasion": "Marvel Landing, Rooftop Infinity Pool & Waterslides",
                "shaila": {
                    "dress_type": "Chic One-Piece Swimsuit + Breezy Silk Kaftan / Robe",
                    "color": "Coral Red / Tropical Floral Cover-up",
                    "color_hex": "#FB7185",
                    "footwear": "Waterproof Pool Slides (Birkenstock EVA)",
                    "accessories": "Wide-brim straw sunhat, UV sunglasses, waterproof tote",
                    "photo_url": ""
                },
                "shaiwal": {
                    "dress_type": "Marvel Graphic Rashguard / Quick-dry Board Shorts",
                    "color": "Cobalt Blue or Marvel Red",
                    "color_hex": "#2563EB",
                    "footwear": "Waterproof Deck Slides / Water Shoes",
                    "accessories": "UV shades, Insta360 selfie pole, waterproof phone pouch",
                    "photo_url": ""
                },
                "style_notes": "Swim-ready for Cantilevered Glass Infinity Pool and Marvel thrill slides on Deck 18!"
            },
            {
                "id": "outfit-d3-night",
                "day": 3,
                "date": "Dec 15 (Tue)",
                "time_slot": "Night (6:30 PM - Midnight)",
                "occasion": "Palo Trattoria Romantic Dinner & Lion King Sky Fireworks",
                "shaila": {
                    "dress_type": "Romantic Tiered Maxi Dress or Italian Resort Chic",
                    "color": "Sunset Peach / Champagne Gold",
                    "color_hex": "#F59E0B",
                    "footwear": "Elegant Kitten Heels or Embellished Sandals",
                    "accessories": "Dainty gold bracelets, evening shawl (ocean breeze)",
                    "photo_url": ""
                },
                "shaiwal": {
                    "dress_type": "Long-sleeve Linen Shirt & Tailored Grey Chinos",
                    "color": "Soft Sage Green or Sky Blue Linen",
                    "color_hex": "#10B981",
                    "footwear": "Brown Suede Loafers",
                    "accessories": "Classic chronometer watch, woven leather belt",
                    "photo_url": ""
                },
                "style_notes": "Adult-exclusive fine dining at Palo followed by open ocean fireworks stargazing."
            },
            {
                "id": "outfit-d4-day",
                "day": 4,
                "date": "Dec 16 (Wed)",
                "time_slot": "All Day (9 AM - 6 PM)",
                "occasion": "Disembarkation & Marina Bay Sands / Cloud Forest Walk",
                "shaila": {
                    "dress_type": "Breathable Cotton Co-ord Set (Culottes + Top)",
                    "color": "Mint Green / Botanical Olive",
                    "color_hex": "#34D399",
                    "footwear": "Cushioned Walking Sneakers (All-day walking)",
                    "accessories": "Crossbody phone bag, light knit cardigan (Cloud Forest is 19°C chilly)",
                    "photo_url": ""
                },
                "shaiwal": {
                    "dress_type": "Moisture-wicking Aeroready Polo & Stretch Travel Shorts",
                    "color": "Heather Grey Polo + Navy Shorts",
                    "color_hex": "#64748B",
                    "footwear": "Ultra-boost Walking Sneakers (15,000 steps)",
                    "accessories": "Daypack for umbrellas and water bottles, cap",
                    "photo_url": ""
                },
                "style_notes": "Important: Domes are air-conditioned to 19°C with water mist. A light cardigan/shawl is mandatory!"
            },
            {
                "id": "outfit-d5-eve",
                "day": 5,
                "date": "Dec 17 (Thu)",
                "time_slot": "Evening (6 PM - 10 PM)",
                "occasion": "Oasia Sentosa Check-in & Trapizza Sunset Dinner on Siloso Beach",
                "shaila": {
                    "dress_type": "Boho Beach Sundress / Barefoot Resort Glam",
                    "color": "Sunset Orange / Terracotta",
                    "color_hex": "#EA580C",
                    "footwear": "Flat Strappy Beach Sandals (Easy to slip off on sand)",
                    "accessories": "Seashell earrings, bamboo woven bag, flower hair pin",
                    "photo_url": ""
                },
                "shaiwal": {
                    "dress_type": "Cuban Collar Short-Sleeve Resort Shirt & White Linen Shorts",
                    "color": "Tropical Print / Clean White Linen",
                    "color_hex": "#F97316",
                    "footwear": "Espadrilles / Suede Slides",
                    "accessories": "Casual braided wristband, aviator sunglasses",
                    "photo_url": ""
                },
                "style_notes": "Cocktails right on the beach sand watching the sunset over the Singapore Strait."
            },
            {
                "id": "outfit-d6-day",
                "day": 6,
                "date": "Dec 18 (Fri)",
                "time_slot": "All Day (10 AM - 7 PM)",
                "occasion": "Universal Studios Singapore (USS) Thrill Rides & Photo Ops",
                "shaila": {
                    "dress_type": "Sporty Athleisure Romper / Tennis Skirt with Built-in Shorts",
                    "color": "Bright Sunshine Yellow or Pastel Lilac",
                    "color_hex": "#EAB308",
                    "footwear": "Broken-in Running / Walking Shoes + Ankle Socks",
                    "accessories": "Minion headband, waterproof pouch for water rides (Jurassic Rapids)",
                    "photo_url": ""
                },
                "shaiwal": {
                    "dress_type": "Quick-dry Graphic Tee & Active Cargo Shorts with Zipper Pockets",
                    "color": "Black or Slate Grey Graphic Tee",
                    "color_hex": "#475569",
                    "footwear": "Grippy Running Shoes (Secured on rollercoasters)",
                    "accessories": "Sport cap, sunglasses strap, zipper pockets for phone & wallet",
                    "photo_url": ""
                },
                "style_notes": "Must have zipped pockets or cross-body bag for rollercoasters (Battlestar Galactica)!"
            },
            {
                "id": "outfit-d7-eve",
                "day": 7,
                "date": "Dec 19 (Sat)",
                "time_slot": "Evening (6 PM - 10:30 PM)",
                "occasion": "Mandai River Wonders / Night Safari & Rainforest Trail",
                "shaila": {
                    "dress_type": "Breathable Safari Linen Pants & Light Cotton Shirt",
                    "color": "Khaki Beige / Olive Green",
                    "color_hex": "#84CC16",
                    "footwear": "Closed-toe Cushioned Walking Shoes",
                    "accessories": "Mosquito repellant bracelet, mini torch, hair tie",
                    "photo_url": ""
                },
                "shaiwal": {
                    "dress_type": "Moisture-wicking Outdoor Crewneck & Cargo Chinos",
                    "color": "Forest Green or Camo Earth Tones",
                    "color_hex": "#15803D",
                    "footwear": "Waterproof Trail / Trekking Sneakers",
                    "accessories": "Pocket umbrella in backpack, insect spray",
                    "photo_url": ""
                },
                "style_notes": "Comfortable, mosquito-safe earth-tone clothing for evening outdoor zoo and boat rides."
            },
            {
                "id": "outfit-d9-fly",
                "day": 9,
                "date": "Dec 21 (Mon)",
                "time_slot": "Daytime (11 AM - 5 PM)",
                "occasion": "Jewel Changi Rain Vortex & Return Flight to Delhi",
                "shaila": {
                    "dress_type": "Comfortable Co-ord Knit Lounge Set or Stretch Trousers",
                    "color": "Cream / Almond / Oat Beige",
                    "color_hex": "#D97706",
                    "footwear": "Slip-on Travel Sneakers with Cushioned Soles",
                    "accessories": "Soft cashmere travel shawl (flight cabin is cold), luggage tag",
                    "photo_url": ""
                },
                "shaiwal": {
                    "dress_type": "Classic Oxford Shirt & Stretch Chino Joggers",
                    "color": "Clean White Shirt + Charcoal Joggers",
                    "color_hex": "#4B5563",
                    "footwear": "Clean Loafers / Easy-off Sneakers for Security",
                    "accessories": "Noise-cancelling headphones, passport wallet",
                    "photo_url": ""
                },
                "style_notes": "Effortlessly stylish for iconic Jewel waterfall photos, yet maximum comfort for the 6-hr flight home."
            }
        ]
    },

    # Comprehensive Honeymoon Travel Survival Guide
    "travel_survival_guide": {
        "esim_and_connectivity": {
            "title": "e-SIM & Connectivity (Stay Connected Seamlessly)",
            "options": [
                {"provider": "Klook Singtel / StarHub 5G eSIM (Recommended)", "desc": "Book on Klook beforehand (~₹950 for 10–20 GB or 100GB). Install the QR profile in Delhi; activates automatically as soon as your flight touches down at Changi Airport. No physical SIM swapping needed."},
                {"provider": "Changi Airport Physical SIM", "desc": "Available at Changi Airport arrival terminal (UOB/Travelex counter) for ~SGD 12 (~₹750) if phone lacks eSIM capability."},
                {"provider": "Cruise Note", "desc": "Cellular roaming turns off at sea. The Disney Cruise Line Navigator app works on the ship's FREE onboard Wi-Fi without any paid package."}
            ]
        },
        "currency_and_payments": {
            "title": "Currency, Forex Cards & Cash Rules",
            "points": [
                {"title": "Zero Forex Markup Card (Niyo / Scapia / Fi)", "desc": "95%+ of Singapore transactions are cashless. Tap directly for MRT, Grab, cafes, and shops with zero markup fees."},
                {"title": "Cash Requirement & Exchange Rates", "desc": "Carry only SGD 150–200 (~₹9,500–₹12,500) cash in total for hawker centers (Lau Pa Sat satay carts) or small local stalls. Note: Changi Airport money exchange counters give slightly lower rates ($100 USD = $123.8 SGD) than city money changers ($100 USD = $125 SGD). Withdraw from bank ATMs directly with your zero-forex debit card for the best interbank rate!"},
                {"title": "DCC Warning", "desc": "Always choose to be charged in SGD on card machines. Never select INR to avoid the 4–7% dynamic currency conversion penalty."}
            ]
        },
        "powerbanks_and_electronics": {
            "title": "Power Banks & Airline Aviation Rules",
            "rules": [
                {"rule": "Strict Carry-On Only", "detail": "Power banks are 100% FORBIDDEN in checked baggage by international aviation law (DGCA & Singapore CAAS). If found in checked bags, the bag will be opened and confiscated."},
                {"rule": "Capacity Limit", "detail": "Maximum 20,000mAh (under 100Wh) per power bank. Up to 2 per person in hand luggage."},
                {"rule": "Type G UK Plug Adapter", "detail": "Singapore uses standard Type G 3-pin plugs (UK style) at 230V 50Hz. Pack 1 or 2 universal travel adapters for hotels."}
            ]
        },
        "transportation_and_cars": {
            "title": "Taxis, Grab, Cars & MRT Logistics",
            "best_mode": "MRT, Public Bus 36, EZ-Link / Contactless VISA & Grab",
            "guide": [
                {"mode": "Public Bus No. 36 (Airport ➔ City Direct)", "desc": "Departs directly from the basement bus bays of Changi Airport (T1, T2, T3 & T4). Travels straight to the city center, including Marine Parade, Bras Basah (Carlton Hotel area), and Orchard Road (~SGD 2.00, scenic daylight ride into town)."},
                {"mode": "MRT Metro Network", "desc": "Singapore's world-class subway connecting Changi Airport, City Hall, Marina Bay, Chinatown, and HarbourFront. Fast, spotless, and fully air-conditioned (~SGD 1.50–2.20 per trip)."},
                {"mode": "Fare Payment: Contactless VISA & EZ-Link Card", "desc": "EZ-Link stored-value cards are available at MRT passenger service counters and 7-Eleven. However, foreign contactless VISA (and Mastercard) credit/debit cards or Apple/Google Pay are seamlessly accepted with tap-and-go convenience at all MRT gantries and bus readers!"},
                {"mode": "Grab & Gojek Ride-Hailing", "desc": "Download both apps before flying. Transparent fixed pricing (~SGD 15–28) with no surge taxi meter surprises. Ideal for heavy luggage transfers between airport, cruise terminal, and Sentosa."},
                {"mode": "Sentosa Express Monorail & Tickets ($4 Ticket, Thereafter FREE)", "desc": "HarbourFront MRT (NE1/CC29) brings you straight into VivoCity Mall Basement 2. Take the escalator up to Level 3 (Lobby L) to board the Sentosa Express monorail into Sentosa. Tickets cost SGD 4.00 per person for entry (purchase at Level 3 kiosks or tap contactless VISA/Mastercard/EZ-Link directly at gantries). AFTER this initial $4 ticket entry (or once checked into Oasia Resort Sentosa with your guest room keycard/QR pass), all monorail rides inside Sentosa island and returning back to VivoCity are 100% FREE OF COST! The monorail connects 4 stations: VivoCity ➔ Resorts World ➔ Imbiah Station (Stop 2, right at Oasia Resort Sentosa front door) ➔ Beach Station (Final Stop: Central Beach Bazaar, Wings of Time daily shows at 7:40 PM & 8:40 PM, beach shuttles & food street)."},
                {"mode": "Singapore Cable Car (HarbourFront Tower 2 ➔ Sentosa)", "desc": "Walk from HarbourFront MRT Exit B to HarbourFront Tower 2 (Level 15) to board the Mount Faber Line cable car soaring high across Keppel Bay directly into Sentosa (Imbiah Lookout). Breathtaking 360° romantic panoramic views of the entire island, sea, and cruise ship terminals."},
                {"mode": "Rental Cars (Do NOT Rent)", "desc": "Avoid self-drive car rentals due to ERP electronic toll gantries, $4–$8/hr parking rates, and strict left-hand traffic monitoring."}
            ],
            "car_rental_verdict": "Self-drive car rentals are completely unnecessary and stressful in Singapore. MRT trains, Bus 36, VivoCity Sentosa Monorail, Cable Car, Grab, and walking cover 100% of your honeymoon travel smoothly."
        },
        "must_eat_places": [
            {"name": "Trapizza (Siloso Beach, Sentosa)", "type": "Italian Wood-fired by the waves", "must_try": "Pizza Quattro Formaggi, Linguine Granchio, sunset spritz on the sand."},
            {"name": "Lau Pa Sat (Satay Street)", "type": "Historic Victorian Hawker Centre", "must_try": "Boon Tat Street open-air Satay stalls (stall 7 & 8), chicken/mutton satay with peanut dipping sauce under city lights ($5–10 SGD)."},
            {"name": "Little India Vegetarian Hotspots", "type": "Authentic Pure Indian Vegetarian", "must_try": "Gandhi Mess for $2 dosas on banana leaves, MTR for rava idlis, Jaggi's for Punjabi parathas, Ananda Bhavan."},
            {"name": "Cassia (Capella Singapore)", "type": "Heritage Cantonese Fine Dining", "must_try": "Truffle crystal dumplings, dim sum lunch in colonial heritage setting."},
            {"name": "CHIJMES Courtyards", "type": "Fairytale Gothic Chapel Dining", "must_try": "Tapas, pizza, craft beer right across from Carlton Hotel."},
            {"name": "Nalan Vegetarian (Capitol Singapore)", "type": "100% Pure Vegetarian Fine Dining", "must_try": "Paneer tikka masala, crispy masala dosas (2 mins from Carlton)."},
            {"name": "Cultivate Cafe (Maxwell Reserve)", "type": "Candlelit Library Plant-Based", "must_try": "Artisanal pastas & vegan desserts surrounded by antique books."},
            {"name": "Disney Rotational Dining", "type": "Disney Adventure Cruise", "must_try": "3 distinct themed restaurants with your personal Disney serving team."}
        ],
        "skip_places": [
            {"place": "Singapore Flyer", "reason": "Costly (~₹2,600–3,000/person) for a slow 30-min observation wheel. MBS SkyPark (57 levels high) and Cloud Forest have far superior romantic views and photos."},
            {"place": "Museum of Ice Cream", "reason": "Overpriced (~₹5,000/person) and geared towards kids/TikTok props rather than romantic honeymoon memories."},
            {"place": "Street Shopping at Bugis / Arab Street", "reason": "Basic cheap street stalls. Focus your souvenir shopping at Chinatown (Pagoda St) or branded outlets at IMM Mall instead."},
            {"place": "Singapore Zoo Daytime", "reason": "Skip daytime Zoo; your itinerary features Mandai River Wonders with pandas Jia Jia & Kai Kai which is fully sheltered, shaded, air-conditioned and far more romantic."},
            {"place": "Night Safari (Late Night Tram)", "reason": "Often overcrowded with 2-hour queue lines in pitch darkness. River Wonders daytime is 10x better."},
            {"place": "Universal Studios Singapore (USS) on Weekends without Express Pass", "reason": "If you visit on peak weekends, ride queues take 60–80 mins each. Skip or only go if booking Express Passes."},
            {"place": "Sentosa Merlion", "reason": "Permanently demolished. The original Merlion Park at Marina Bay Waterfront is where you take couple photos."}
        ],
        "singapore_dos_and_donts": {
            "donts": [
                "NEVER carry chewing gum, vapes, or e-cigarettes into Singapore (confiscated at customs, heavy fines up to SGD 2,000).",
                "Do NOT drink water or eat anything inside MRT trains or stations (SGD 500 fine).",
                "Do NOT jaywalk across roads within 50m of a crossing (SGD 50–1,000 fine).",
                "Do NOT buy tickets at venue counters (queues take 45+ mins; pre-book on Klook for 10–20% discounts).",
                "Do NOT assume all dishes in food courts are vegetarian — always ask if sauces contain fish sauce, oyster sauce, or chicken stock.",
                "Do NOT smoke on stateroom verandahs or public streets (only yellow box Designated Smoking Areas).",
                "Do NOT connect to unverified open public Wi-Fi networks (illegal under Computer Misuse Act)."
            ],
            "dos": [
                "DO drink the tap water everywhere in Singapore — it is 100% safe, filtered, and higher quality than bottled water (saves $2.50 SGD/bottle).",
                "DO claim your 8–9% GST tourist refund at Changi Airport for single-store purchases over SGD 100 (keep passport handy at checkout).",
                "DO carry 2 compact windproof umbrellas at all times for December monsoon showers.",
                "DO pre-submit the electronic SG Arrival Card within 72 hours before landing in Singapore (100% free at ica.gov.sg).",
                "DO dress modestly (covered knees/shoulders) when visiting heritage temples in Chinatown or Little India.",
                "DO book Disney Princess Royal Gathering on the Navigator app the moment you board the cruise!"
            ]
        }
    },

    # Generic Honeymoon Things to Do / Master Task Tracker (Fully Editable)
    "things_to_do": [
        {
            "id": "todo-1",
            "title": "Buy Singtel 5G Singapore Tourist eSIM",
            "category": "Connectivity",
            "link": "https://www.klook.com/en-IN/activity/176809-singtel-singapore-data-esim/",
            "notes": "Install QR code while on home Wi-Fi in Delhi before departure so it activates immediately at Changi.",
            "due_date": "Dec 5, 2026",
            "status": "Pending"
        },
        {
            "id": "todo-1b",
            "title": "Alternative: Singtel 4G/5G Physical Tourist SIM (Airport Pickup)",
            "category": "Connectivity",
            "link": "https://www.klook.com/en-IN/activity/77287-4g-travel-sim-card-singtel-singapore/?spm=SearchResult.SearchResult_LIST&clickId=752b002a05",
            "notes": "Collect at Changi Airport Terminal 1, 2, 3, or 4 arrival hall. 100GB high-speed local data.",
            "due_date": "Dec 5, 2026",
            "status": "Pending"
        },
        {
            "id": "todo-1c",
            "title": "Alternative: South East Asia Multi-Country eSIM (Singapore, Malaysia, Thailand)",
            "category": "Connectivity",
            "link": "https://www.klook.com/en-IN/activity/105381-south-east-asia-esim/",
            "notes": "Instant digital QR delivery. Works across South East Asia and international cruise waters near Malaysia/Indonesia.",
            "due_date": "Dec 5, 2026",
            "status": "Pending"
        },
        {
            "id": "todo-2",
            "title": "Apply for Electronic SG Arrival Card with Health Declaration (SGAC)",
            "category": "Mandatory Immigration",
            "link": "https://eservices.ica.gov.sg/sgarrivalcard/",
            "notes": "CRITICAL MANDATORY STEP: Must apply online within 72 hours (3 days) prior to landing in Singapore (apply Dec 10–12, 2026). It is 100% FREE on the official ICA website (never pay on third-party fake websites!). Fill individual declarations for Shaiwal & Shaila (passport details, flight info, Carlton Hotel address, and health declaration). Download the PDF acknowledgment barcodes onto your phones.",
            "due_date": "Dec 10–12, 2026 (Within 72 hrs of flight)",
            "status": "Pending"
        },
        {
            "id": "todo-3",
            "title": "Book SharePal DJI Osmo Pocket 3 Camera Gear",
            "category": "Photography",
            "link": "https://www.sharepal.in",
            "notes": "Zero-deposit Delhi doorstep delivery on Dec 12 for high quality romantic low-light videos.",
            "due_date": "Nov 15, 2026",
            "status": "Pending"
        },
        {
            "id": "todo-4",
            "title": "Download Disney Cruise Navigator App",
            "category": "Cruise",
            "link": "https://disneycruise.disney.go.com/guest-services/navigator-app/",
            "notes": "Download and link reservation #44985264. Book Royal Gathering Princess meet the moment you connect to ship Wi-Fi.",
            "due_date": "Dec 1, 2026",
            "status": "Pending"
        },
        {
            "id": "todo-5",
            "title": "Book Gardens by the Bay & MBS SkyPark on Klook",
            "category": "Attractions",
            "link": "https://www.klook.com/en-IN/activity/127-gardens-by-the-bay-singapore/",
            "notes": "Reserve prime sunset slot (5:30 PM - 6:00 PM) for Flower Dome & Cloud Forest.",
            "due_date": "Nov 20, 2026",
            "status": "Pending"
        }
    ],

    # Curated Travel Video Reference
    "reference_video": {
        "title": "India to Singapore: 6-Day Detailed Itinerary & Total Cost Breakdown",
        "channel": "YouTube Travel Guide",
        "url": "https://youtu.be/UITG7PTmgk4?si=LVUPqbjQe1qAEyun",
        "embed_url": "https://www.youtube.com/embed/UITG7PTmgk4",
        "description": "Essential Indian traveler reference guide breaking down flights, visas, MRT local transit via contactless cards, must-see sights (Universal Studios, S.E.A. Aquarium, Gardens by the Bay, Fort Siloso Skywalk, Jewel Changi Rain Vortex), and authentic food budgets.",
        "key_highlights": [
            "Little India & Chinatown walking routes and budget souvenir spots",
            "Mandai Wildlife / Singapore Zoo logistics and shuttle advice",
            "Sentosa Island free transport (Beach shuttle tram & Fort Siloso Skywalk)",
            "Marina Bay Sands, Spectra Light & Water show and Merlion Park",
            "Jewel Changi Rain Vortex & departure transit time management"
        ]
    }
}
