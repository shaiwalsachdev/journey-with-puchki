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
                "fare": "~SGD 2.05 (Tap zero-forex card directly)",
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
            "title": "Sentosa Island, Cable Car & Wings of Time",
            "location": "Oasia Resort Sentosa & Siloso/Palawan Beach",
            "mrt_guide": {
                "start": "Marina South Pier MRT (NS28)",
                "end": "Imbiah Station (Sentosa Express) / HarbourFront MRT (NE1 / CC29)",
                "lines": "North-South Line ➔ Dhoby Ghaut ➔ North-East Line (Purple) to HarbourFront ➔ Sentosa Express Monorail",
                "route_desc": "From Cruise Centre walk to Marina South Pier (NS28) ➔ Take North-South Line to Dhoby Ghaut (NS24) ➔ Transfer to North-East Line (Purple) to HarbourFront (NE1, VivoCity) ➔ Board Sentosa Express monorail to Imbiah Station (Oasia Resort Sentosa is right outside the station exit!).",
                "fare": "~SGD 2.10 MRT + Monorail (Free Monorail once checked in at Oasia).",
                "taxi_alternative": "Grab/Taxi ~18 mins (SGD 16–22) with suitcases directly to Oasia Resort lobby."
            },
            "schedule": [
                {"time": "7:00 AM – 8:30 AM", "title": "Cruise Disembarkation", "desc": "Follow cruise exit instructions. Clear customs at Marina Bay Cruise Centre.", "icon": "exit_to_app"},
                {"time": "8:30 AM – 9:30 AM", "title": "Taxi to Oasia Resort Sentosa", "desc": "Arrive at Oasia Resort Sentosa. Leave luggage with concierge (check-in at 3 PM).", "icon": "hotel"},
                {"time": "10:00 AM – 12:00 PM", "title": "Singapore Cable Car SkyPass", "desc": "Ride the Mount Faber Line & Sentosa Line. Panoramic 360-degree aerial views of the harbor.", "icon": "flight_takeoff"},
                {"time": "12:00 PM – 3:00 PM", "title": "Beachside Lunch & Siloso / Palawan Beach", "desc": "Cross the rope bridge to the Southernmost Point of Continental Asia. Relax on pristine sand.", "icon": "beach_access"},
                {"time": "3:00 PM – 5:00 PM", "title": "Check-in at Oasia Resort & Unwind", "desc": "Settle into your sanctuary room at Oasia. Refresh and take romantic resort photos.", "icon": "bed"},
                {"time": "7:40 PM / 8:40 PM", "title": "Wings of Time Night Show", "desc": "Spectacular multi-sensory laser, fire, water, and music show set against the open sea.", "icon": "auto_awesome"}
            ],
            "options": [
                {"title": "Lunch Option A (Beachfront Italian):", "desc": "Trapizza on Siloso Beach — wood-fired pizza and cocktails right by the waves."},
                {"title": "Lunch Option B (Chic Beach Club):", "desc": "Tipsy Unicorn or Ola Beach Club for tropical mocktails and relaxing beach loungers."},
                {"title": "Dinner Option:", "desc": "Quayside Isle waterfront dining at Sentosa Cove (overlooking private yachts)."}
            ]
        },
        {
            "day": 6,
            "date": "Friday, 18 December 2026",
            "title": "Oceanarium Wonders & Harry Potter Magic",
            "location": "Resorts World Sentosa",
            "mrt_guide": {
                "start": "Imbiah Station (Sentosa Express, outside Oasia)",
                "end": "Resorts World Station (Sentosa Express)",
                "lines": "Sentosa Express Monorail (1 stop, 2 mins)",
                "route_desc": "Hop on Sentosa Express at Imbiah Station ➔ Ride 1 stop (2 mins) to Resorts World Station. Walk 3 mins through the festive plaza to S.E.A. Aquarium & Harry Potter: Visions of Magic exhibition.",
                "fare": "Free with Oasia Resort Sentosa guest pass!"
            },
            "schedule": [
                {"time": "9:30 AM – 12:30 PM", "title": "Singapore Oceanarium (S.E.A. Aquarium)", "desc": "Walk through giant glass tunnels surrounded by manta rays, sharks, and vibrant coral reefs.", "icon": "water"},
                {"time": "12:30 PM – 2:00 PM", "title": "Lunch Break at Resorts World", "desc": "Enjoy lunch at Malaysian Food Street or Din Tai Fung / gourmet burger spots.", "icon": "restaurant"},
                {"time": "2:00 PM – 4:30 PM", "title": "Harry Potter: Visions of Magic", "desc": "Step into the magical interactive wizarding world art experience (timed entry).", "icon": "magic_button"},
                {"time": "5:30 PM – Late", "title": "Evening at Leisure in Sentosa", "desc": "Stroll around the island, ride the Sentosa Express, or book a sunset cocktail.", "icon": "nightlife"}
            ],
            "options": [
                {"title": "Alternative Thrill:", "desc": "Skyline Luge Sentosa (4 exhilarating downhill tracks) if you finish Harry Potter early!"},
                {"title": "Romantic Dinner Choice:", "desc": "Cassia at Capella Singapore for upscale Cantonese fine dining in a colonial manor."}
            ]
        },
        {
            "day": 7,
            "date": "Saturday, 19 December 2026",
            "title": "River Wonders Pandas & Culture Shopping",
            "location": "Mandai Wildlife Reserve ➔ Little India ➔ Chinatown",
            "mrt_guide": {
                "start": "HarbourFront MRT (NE1)",
                "end": "Khatib MRT (NS14) ➔ Mandai Shuttle ➔ Farrer Park (NE8) ➔ Chinatown (NE4)",
                "lines": "North-East Line (Purple) ➔ North-South Line (Red) ➔ Mandai Khatib Shuttle Bus",
                "route_desc": "1. To Mandai: Monorail to HarbourFront (NE1) ➔ Purple line to Dhoby Ghaut ➔ Red line northbound to Khatib (NS14 Exit A) ➔ Mandai Khatib Shuttle (SGD 1, every 10 min) directly to River Wonders. (Grab ~25 mins is very convenient here!).\n2. To Little India: Red Line south from Khatib ➔ Dhoby Ghaut ➔ Purple line to Farrer Park (NE8 Exit I for Mustafa Centre) or Little India (NE7).\n3. To Chinatown: Purple line direct from Little India (NE7) ➔ Chinatown MRT (NE4 Exit A directly into Pagoda Street market).",
                "fare": "~SGD 2.20 per MRT leg."
            },
            "schedule": [
                {"time": "8:00 AM – 9:00 AM", "title": "Taxi to Mandai Wildlife Reserve", "desc": "Head north to Mandai for the river safari experience.", "icon": "directions_car"},
                {"time": "9:00 AM – 12:00 PM", "title": "River Wonders & Giant Panda Forest", "desc": "Visit adorable Kai Kai and Jia Jia in their climate-controlled forest, Amazon Flooded Forest, and reservoir cruise.", "icon": "pets"},
                {"time": "12:00 PM – 1:00 PM", "title": "Lunch at Mandai", "desc": "Cute panda bao and snacks at Mama Panda Kitchen.", "icon": "lunch_dining"},
                {"time": "1:00 PM – 3:30 PM", "title": "Taxi to Little India & Mustafa Centre", "desc": "Mustafa Centre (24/7 shopping for electronics, chocolates, perfumes) and colorful Serangoon Road.", "icon": "shopping_bag"},
                {"time": "3:30 PM – 6:30 PM", "title": "Chinatown Street Market & Souvenirs", "desc": "Pagoda Street, Buddha Tooth Relic Temple, authentic bubble tea, gifts and souvenirs.", "icon": "storefront"},
                {"time": "7:30 PM", "title": "Return to Sentosa & Rest", "desc": "Dinner and peaceful night at Oasia Resort.", "icon": "night_shelter"}
            ],
            "options": [
                {"title": "Shopping Alternative:", "desc": "If tired of street shopping, head to Bugis Junction or Orchard Road malls for luxury & fashion brands."},
                {"title": "Foodie Treat in Chinatown:", "desc": "Chinatown Complex Hawker Centre for Michelin-rated street food."}
            ]
        },
        {
            "day": 8,
            "date": "Sunday, 20 December 2026",
            "title": "Gardens by the Bay, Marina Bay SkyPark & Light Show",
            "location": "Marina Bay & Gardens by the Bay",
            "mrt_guide": {
                "start": "HarbourFront MRT (NE1 / CC29)",
                "end": "Gardens by the Bay MRT (TE22) & Bayfront MRT (CE1 / DT16)",
                "lines": "Circle Line (Yellow) to Marina Bay (CE2) ➔ Thomson-East Coast Line (Brown) to TE22 OR Downtown Line (Blue)",
                "route_desc": "Monorail from Oasia to VivoCity / HarbourFront ➔ Circle Line (Yellow) to Marina Bay (CE2) ➔ Transfer 1 stop on Thomson-East Coast Line to Gardens by the Bay MRT (TE22 Exit 1 right outside Flower Dome!). For evening SkyPark & Spectra: Walk through Dragonfly Bridge to Bayfront MRT (DT16/CE1 Exit B). Returning to Sentosa: Bayfront (Downtown line) ➔ Chinatown (Purple line) ➔ HarbourFront.",
                "fare": "~SGD 1.90 each way."
            },
            "schedule": [
                {"time": "10:00 AM – 1:00 PM", "title": "Flower Dome & Cloud Forest", "desc": "World's largest glass greenhouse with indoor waterfall and mist walk.", "icon": "local_florist"},
                {"time": "1:00 PM – 2:00 PM", "title": "Lunch at Marina Bay Sands", "desc": "Dine at The Shoppes at Marina Bay Sands or waterfront dining.", "icon": "restaurant"},
                {"time": "2:00 PM – 3:30 PM", "title": "Outdoor Gardens & Supertree Boardwalk", "desc": "Walk among the towering 50-meter Supertrees and sculpture gardens.", "icon": "park"},
                {"time": "5:00 PM – 6:15 PM", "title": "Marina Bay Sands SkyPark Observation Deck", "desc": "57 levels high! Catch the golden hour sunset over Singapore skyline.", "icon": "apartment"},
                {"time": "6:15 PM – 7:15 PM", "title": "Merlion Park & Waterfront Photos", "desc": "Iconic photos with the Singapore Merlion against the skyline.", "icon": "photo_camera"},
                {"time": "7:45 PM – 8:15 PM", "title": "Garden Rhapsody Light & Sound Show", "desc": "Lie under the Supertrees as they dance with synchronized lights and music (free to watch!).", "icon": "auto_awesome"},
                {"time": "8:30 PM – Late", "title": "Grand Honeymoon Finale Dinner", "desc": "Romantic waterfront dinner celebrating your final night.", "icon": "celebration"}
            ],
            "options": [
                {"title": "Light Show Bonus:", "desc": "Catch the Spectra Marina Bay water-and-laser fountain show at 9:00 PM from the MBS Event Plaza!"},
                {"title": "Dining Option A (Rooftop):", "desc": "CÉ LA VI or Spago atop Marina Bay Sands for jaw-dropping skyline drinks."},
                {"title": "Dining Option B (Colonial Library Vegan Fine Dining):", "desc": "Cultivate Cafe at Maxwell Reserve — intimate, candlelit library setting."}
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
                {"time": "9:00 AM", "title": "Check-out of Oasia Resort Sentosa", "desc": "Take taxi to Changi Airport (~25–35 min).", "icon": "luggage"},
                {"time": "10:00 AM – 12:30 PM", "title": "Jewel Changi & Rain Vortex", "desc": "Marvel at the world's tallest indoor waterfall (HSBC Rain Vortex) and lush Shiseido Forest Valley.", "icon": "water_drop"},
                {"time": "1:00 PM", "title": "Check-in at Terminal & Baggage Drop", "desc": "Complete airline check-in for flight to Delhi.", "icon": "how_to_reg"},
                {"time": "1:30 PM – 3:30 PM", "title": "Duty-Free Shopping & Airport Lunch", "desc": "Bengawan Solo pandan cakes, TWG tea, cosmetics, and duty-free gifts.", "icon": "shopping_cart"},
                {"time": "4:40 PM", "title": "Flight to Delhi", "desc": "Board flight. Estimated landing at Delhi IGI Airport around 8:00 PM IST.", "icon": "flight_takeoff"}
            ],
            "options": [
                {"title": "Luggage Tip at Jewel:", "desc": "Use Early Check-in (if your airline supports it) or the Left Baggage counter on Level 1 to walk around hands-free!"}
            ]
        }
    ],

    # Tickets to Book (Klook Checklist) with Due Dates
    "klook_tickets": [
        {"id": "t0", "date": "13 Dec 2026 (Arrival)", "due_date": "Book by Dec 5, 2026 📱 (Install QR in Delhi)", "name": "Singtel Singapore 5G High-Speed Data Tourist eSIM", "status": "To Book", "link": "https://www.klook.com/en-IN/activity/176809-singtel-singapore-data-esim/", "booked": False, "price": "~₹950 / person (10–20 GB)"},
        {"id": "t0-sea", "date": "13 Dec 2026 (Arrival)", "due_date": "Book by Dec 5, 2026 (Multi-Country / Cruise Waters)", "name": "South East Asia Multi-Country High-Speed Data eSIM (Singapore, Malaysia, Thailand, Indonesia)", "status": "To Book", "link": "https://www.klook.com/en-IN/activity/105381-south-east-asia-esim/", "booked": False, "price": "~₹450 - ₹1,200 / person (Flexible Data/Days)"},
        {"id": "t0-physical", "date": "13 Dec 2026 (Arrival)", "due_date": "Book by Dec 5, 2026 (Pickup at Changi T1/T2/T3/T4)", "name": "Singtel 4G/5G Physical Tourist SIM Card (Changi Airport Pickup)", "status": "To Book", "link": "https://www.klook.com/en-IN/activity/77287-4g-travel-sim-card-singtel-singapore/?spm=SearchResult.SearchResult_LIST&clickId=752b002a05", "booked": False, "price": "~₹750 - ₹950 / person (100 GB)"},
        {"id": "t1", "date": "17 Dec 2026", "due_date": "Book by Nov 20, 2026", "name": "Singapore Cable Car SkyPass", "status": "To Book", "link": "https://www.klook.com/en-IN/activity/132-singapore-cable-car-sky-pass-singapore/", "booked": False, "price": "~₹2,200 / person"},
        {"id": "t2", "date": "17 Dec 2026", "due_date": "Book by Nov 20, 2026", "name": "Wings of Time (Sentosa)", "status": "To Book", "link": "https://www.klook.com/en-IN/activity/124-wings-of-time-singapore/", "booked": False, "price": "~₹1,100 / person"},
        {"id": "t3", "date": "18 Dec 2026", "due_date": "Book by Nov 25, 2026", "name": "Singapore Oceanarium (S.E.A. Aquarium)", "status": "To Book", "link": "https://www.klook.com/en-IN/activity/119-sea-aquarium-singapore/", "booked": False, "price": "~₹2,800 / person"},
        {"id": "t4", "date": "18 Dec 2026", "due_date": "Book by Nov 20, 2026 ⚠️ (Slots Fill Fast)", "name": "Harry Potter: Visions of Magic", "status": "To Book", "link": "https://www.klook.com/en-IN/activity/112678-harry-potter-visions-of-magic-singapore/", "booked": False, "price": "~₹3,200 / person"},
        {"id": "t5", "date": "19 Dec 2026", "due_date": "Book by Nov 25, 2026", "name": "River Wonders (with Giant Panda Forest)", "status": "To Book", "link": "https://www.klook.com/en-IN/activity/123-river-safari-singapore/", "booked": False, "price": "~₹2,600 / person"},
        {"id": "t6", "date": "20 Dec 2026", "due_date": "Book by Nov 20, 2026 ⚠️ (Prime Sunset Domes)", "name": "Gardens by the Bay (Flower Dome + Cloud Forest)", "status": "To Book", "link": "https://www.klook.com/en-IN/activity/127-gardens-by-the-bay-singapore/", "booked": False, "price": "~₹3,100 / person"},
        {"id": "t7", "date": "20 Dec 2026", "due_date": "Book by Nov 20, 2026 ⚠️ (Sunset Slot 5:30 PM)", "name": "Marina Bay Sands SkyPark Observation Deck", "status": "To Book", "link": "https://www.klook.com/en-IN/activity/148-skypark-observation-deck-singapore/", "booked": False, "price": "~₹2,100 / person"}
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
            {"title": "Tap Credit/Debit Card for MRT", "desc": "No need to buy transit cards (EZ-Link)! Simply tap any contactless Visa/Mastercard directly at MRT gates."},
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
            "guide": [
                {"mode": "MRT & Public Buses (Contactless Tap)", "desc": "The fastest, cleanest, and most budget-friendly transport in Singapore (~SGD 1.50–2.00 / ₹100–150 per trip). Simply tap your contactless Visa/Mastercard directly at turnstiles. No need to buy an EZ-Link card."},
                {"mode": "Grab & Gojek Apps", "desc": "Download & verify both apps before flying. Street taxis charge airport surcharge and midnight fees. Grab/Gojek offer clear upfront fixed pricing ($15–$25 SGD / ₹1,500–2,000). Use for luggage transfers and late night rides back to Sentosa."},
                {"mode": "Sentosa Express Monorail", "desc": "Complimentary unlimited passes provided by Oasia Resort Sentosa during your 4-night stay."},
                {"mode": "Rental Cars (Do NOT Rent)", "desc": "Avoid self-drive car rentals! Singapore has expensive Electronic Road Pricing (ERP), steep parking fees ($3–$6/hr), and left-hand driving with strict speed cameras."}
            ]
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
            "title": "Fill & Submit Electronic SG Arrival Card (ICA)",
            "category": "Immigration",
            "link": "https://eservices.ica.gov.sg/sgarrivalcard/",
            "notes": "100% Free online submission strictly within 72 hours before arrival in Singapore.",
            "due_date": "Dec 10–12, 2026",
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
    ]
}
