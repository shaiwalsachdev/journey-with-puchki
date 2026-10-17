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

    # Disney Cruise Special Zones & Features
    "disney_features": [
        {
            "zone": "Town Square (Disney Princess Realm) 👑",
            "desc": "A fairytale realm celebrating Disney Royalty (Cinderella, Belle, Ariel, Jasmine, Rapunzel, Elsa & Anna). Royal shops, magical salons, and enchanting princess meet-and-greets.",
            "icon": "auto_awesome",
            "color": "from-purple-500 to-pink-500"
        },
        {
            "zone": "Disney Imagination Garden ✨",
            "desc": "The enchanted heart of the ship with Sorcerer Mickey, open-air castle courtyard performance stage, and storybook garden walkways.",
            "icon": "castle",
            "color": "from-blue-500 to-indigo-600"
        },
        {
            "zone": "Mickey & Minnie Captain's Gala 🐭🎀",
            "desc": "Meet Mickey and Minnie in their finest maritime captain attire! Take fairytale honeymoon couple photos together on the grand staircase.",
            "icon": "favorite",
            "color": "from-rose-500 to-red-600"
        },
        {
            "zone": "Disney Rotational Dining 🍽️",
            "desc": "Experience Hollywood Spotlight Club, Navigator's Club, and Animator's Palate with dedicated Disney servers traveling with you each night.",
            "icon": "restaurant",
            "color": "from-amber-500 to-orange-500"
        },
        {
            "zone": "Remember Stage Musical & Sky Fireworks 🎆",
            "desc": "Exclusive Broadway-caliber theatrical stage shows at Walt Disney Theatre and fireworks lighting up the open sea starry night.",
            "icon": "theater_comedy",
            "color": "from-pink-500 to-rose-500"
        },
        {
            "zone": "Wayfinder Bay & Adults Retreat 🌴",
            "desc": "Moana-inspired open-air poolside oasis with sweeping ocean vistas, couple daybeds, and tropical cocktails under the stars.",
            "icon": "pool",
            "color": "from-teal-500 to-emerald-600"
        }
    ],

    # Visa Timeline & Requirements
    "visa": {
        "apply_date": "November 1, 2026",
        "target_decision": "Within 3–5 working days (issued as e-Visa)",
        "processing_window": "Must apply within 30 days of arrival (Nov 1 is the perfect date!)",
        "fee": "SGD 30 ICA fee + authorized visa agent service fee (~₹1,200 - ₹1,800)",
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

    # Day-by-Day Itinerary with Real-time Options
    "days": [
        {
            "day": 1,
            "date": "Sunday, 13 December 2026",
            "title": "Welcome to Singapore & City Lights",
            "location": "Changi Airport ➔ Carlton Hotel",
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
        {"id": "t0", "date": "13 Dec 2026 (Arrival)", "due_date": "Book by Dec 5, 2026 📱 (Install QR in Delhi)", "name": "Singapore High-Speed 5G Tourist eSIM (Singtel / StarHub)", "status": "To Book", "link": "https://www.klook.com/en-IN/activity/80673-singtel-singapore-data-esim/", "booked": False, "price": "~₹950 / person (10–20 GB)"},
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
            {"title": "No Connecting to Open Unsecured Wi-Fi", "desc": "Legally considered unauthorized network access under Computer Misuse Act."}
        ],
        "dos": [
            {"title": "Tap Water is 100% Safe", "desc": "Singapore tap water is cleaner than bottled water. Carry reusable insulated flasks."},
            {"title": "Tap Credit/Debit Card for MRT", "desc": "No need to buy transit cards! Simply tap any contactless Visa/Mastercard directly at MRT gates."},
            {"title": "Tipping is NOT Customary", "desc": "10% service charge and 9% GST are already included in hotel and restaurant bills."},
            {"title": "Modest Temple Attire", "desc": "Cover shoulders and knees when entering Hindu, Buddhist, or Muslim places of worship."},
            {"title": "Download Grab App", "desc": "Grab is Southeast Asia's Uber. Seamless for booking taxis and island rides."}
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
            "status": "Shortlisted"
        },
        {
            "id": "d2",
            "name": "Cassia (Capella Singapore)",
            "area": "Sentosa Heritage",
            "cuisine": "Ultra-Luxury Cantonese / Dim Sum",
            "highlight": "Heritage 1880s manor. Exceptional vegetarian black truffle crystal dumplings.",
            "status": "Must Visit"
        },
        {
            "id": "d3",
            "name": "Quayside Isle (Sentosa Cove)",
            "area": "Sentosa Marina",
            "cuisine": "Mediterranean & Italian Waterfront",
            "highlight": "Miska Café and Sole Pomodoro facing luxury yachts. Very romantic evening walk.",
            "status": "Shortlisted"
        },
        {
            "id": "d4",
            "name": "CHIJMES Courtyards",
            "area": "City Hall (Opp. Carlton)",
            "cuisine": "Gothic Chapel Outdoor Dining",
            "highlight": "Lit with fairy lights. Great tapas, wood-fired pizza, and craft drinks across from Carlton.",
            "status": "Day 1 Dinner"
        },
        {
            "id": "d5",
            "name": "Nalan Vegetarian (Capitol Singapore)",
            "area": "City Hall",
            "cuisine": "100% Pure Vegetarian Fine Dining",
            "highlight": "2 mins from Carlton Hotel. High quality North & South Indian curries and dosas.",
            "status": "Shortlisted"
        },
        {
            "id": "d6",
            "name": "Cultivate Cafe (Maxwell Reserve)",
            "area": "Tanjong Pagar / Chinatown",
            "cuisine": "Candlelit Library Plant-Based",
            "highlight": "Candlelit library setting with artisanal pastas and plant-based fine dining.",
            "status": "Shortlisted"
        }
    ],

    # Live Expense Tracker Items (Fully Editable with actual expense tracking)
    "expenses": [
        {"id": "exp-1", "category": "Visa", "item": "Singapore e-Visa (2 Adults)", "amount": 6500, "actual_amount": 0, "currency": "INR", "status": "Pending", "notes": "Submit Nov 1"},
        {"id": "exp-2", "category": "Flights", "item": "Roundtrip Delhi - Singapore (Air India / Singapore Airlines)", "amount": 65000, "actual_amount": 64200, "currency": "INR", "status": "Booked", "notes": "Confirmed roundtrip"},
        {"id": "exp-3", "category": "Hotels", "item": "Carlton Hotel (1 Night) + Oasia Resort Sentosa (4 Nights)", "amount": 85000, "actual_amount": 85000, "currency": "INR", "status": "Booked", "notes": "Carlton + Oasia Deluxe"},
        {"id": "exp-4", "category": "Cruise", "item": "Disney Adventure Cruise (3-Night Balcony Stateroom)", "amount": 85000, "actual_amount": 85000, "currency": "INR", "status": "Booked", "notes": "Disney Adventure Sailing"},
        {"id": "exp-5", "category": "Activities", "item": "All 7 Klook Sightseeing Passes (2 Adults)", "amount": 34000, "actual_amount": 0, "currency": "INR", "status": "To Book", "notes": "Cable Car, River Wonders, Gardens, MBS"},
        {"id": "exp-6", "category": "Food & Dining", "item": "Romantic Dinners, Cafes, Gelato & Street Food", "amount": 40000, "actual_amount": 0, "currency": "INR", "status": "Budget", "notes": "Trapizza, CHIJMES, Rotational dining tips"}
    ],

    # Uploaded Tickets, Vouchers & PDF Documents
    "documents": [
        {
            "id": "doc-dcl",
            "name": "Disney Adventure Cruise Confirmation",
            "category": "Cruise",
            "filename": "Disney_Adventure_Reservation_44985264.pdf",
            "url": "https://pub-2849c719e70146059d0fc1f31f9b33a5.r2.dev/honeymoon/docs/disney_cruise_confirmation.pdf",
            "size": "Deluxe Verandah #11680",
            "uploaded_at": "Paid in Full · Dec 14-17"
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
            {"category": "Sightseeing & Walking Days", "count": "4 Outfits", "suggestion": "Moisture-wicking tees, comfortable stretch chino shorts, and UV sunglasses for Mandai River Safari & Marina Bay."},
            {"category": "Swimwear", "count": "2–3 Pairs", "suggestion": "Quick-dry board shorts for cruise swimming pools, Sentosa Siloso beach & Oasia resort pool."},
            {"category": "Footwear", "count": "3 Pairs", "suggestion": "1 pair supportive walking sneakers, 1 pair waterproof pool slides/sandals, 1 pair smart loafers/boat shoes for dinner."}
        ]
    },

    # Comprehensive Honeymoon Travel Survival Guide
    "travel_survival_guide": {
        "esim_and_connectivity": {
            "title": "e-SIM & Connectivity (Stay Connected Seamlessly)",
            "options": [
                {"provider": "Airalo / Nomad e-SIM (Recommended)", "desc": "Buy online before departure (e.g. 10GB for ~₹1,100). Activates automatically as soon as your flight touches down at Changi Airport. No physical SIM swapping needed."},
                {"provider": "Singtel Tourist SIM (Physical)", "desc": "Available at Changi Airport arrival terminal (Travelex counter). 100GB 4G/5G data for SGD 12 (~₹750) valid for 14 days."},
                {"provider": "Cruise Note", "desc": "Cellular roaming turns off at sea. The Disney Cruise Line Navigator app works on the ship's FREE onboard Wi-Fi without any paid package."}
            ]
        },
        "currency_and_payments": {
            "title": "Currency, Forex Cards & Cash Rules",
            "points": [
                {"title": "Zero Forex Markup Card (Niyo / Scapia / Fi)", "desc": "95%+ of Singapore transactions are cashless. Tap directly for MRT, Grab, cafes, and shops with zero markup fees."},
                {"title": "Cash Requirement", "desc": "Carry only SGD 150–200 (~₹9,500–₹12,500) cash in total for hawker centers or small local stalls. Withdraw at any DBS/UOB ATM at Changi Airport."},
                {"title": "Indian Currency Tip", "desc": "Do not exchange INR to SGD in Singapore city centers at poor rates. Carry a clean debit/forex card or exchange a small amount at Delhi Airport before departure."}
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
                {"mode": "Grab App (Southeast Asia's Uber)", "desc": "Download & verify the Grab app in India beforehand. Add credit card. Seamless for Changi-to-Carlton, hotel-to-cruise, and evening rides back to Sentosa."},
                {"mode": "MRT & Public Buses (Contactless Tap)", "desc": "No need for transit cards (EZ-Link)! Simply tap your contactless Visa/Mastercard or Apple Pay directly at the turnstiles."},
                {"mode": "Sentosa Express Monorail", "desc": "Complimentary unlimited passes provided by Oasia Resort Sentosa during your 4-night stay."},
                {"mode": "Rental Cars (Do NOT Rent)", "desc": "Avoid self-drive car rentals! Singapore has expensive Electronic Road Pricing (ERP), steep parking fees ($3–$6/hr), and left-hand driving with strict speed cameras."}
            ]
        },
        "must_eat_places": [
            {"name": "Trapizza (Siloso Beach, Sentosa)", "type": "Italian Wood-fired by the waves", "must_try": "Pizza Quattro Formaggi, Linguine Granchio, sunset spritz on the sand."},
            {"name": "Cassia (Capella Singapore)", "type": "Heritage Cantonese Fine Dining", "must_try": "Truffle crystal dumplings, dim sum lunch in colonial heritage setting."},
            {"name": "CHIJMES Courtyards", "type": "Fairytale Gothic Chapel Dining", "must_try": "Tapas, pizza, craft beer right across from Carlton Hotel."},
            {"name": "Nalan Vegetarian (Capitol Singapore)", "type": "100% Pure Vegetarian Fine Dining", "must_try": "Paneer tikka masala, crispy masala dosas (2 mins from Carlton)."},
            {"name": "Cultivate Cafe (Maxwell Reserve)", "type": "Candlelit Library Plant-Based", "must_try": "Artisanal pastas & vegan desserts surrounded by antique books."},
            {"name": "Disney Rotational Dining", "type": "Disney Adventure Cruise", "must_try": "3 distinct themed restaurants with your personal Disney serving team."}
        ],
        "skip_places": [
            {"place": "Singapore Zoo Daytime", "reason": "Skip daytime Zoo; your itinerary features Mandai River Wonders with pandas Jia Jia & Kai Kai which is fully sheltered, shaded, and far more romantic."},
            {"place": "Orchard Road Mega Malls", "reason": "Skip wasting whole days in generic malls. High prices due to 9% GST. Enjoy Sentosa beach, nature, and scenic spots instead."},
            {"place": "Night Safari (Late Night Tram)", "reason": "Often overcrowded with 2-hour queue lines in pitch darkness. River Wonders daytime is 10x better."},
            {"place": "Sentosa Merlion", "reason": "Permanently demolished. The original Merlion Park at Marina Bay Waterfront is where you take couple photos."}
        ],
        "singapore_dos_and_donts": {
            "donts": [
                "NEVER carry chewing gum, vapes, or e-cigarettes into Singapore (confiscated at customs, heavy fines).",
                "Do NOT drink water or eat anything inside MRT trains or stations (SGD 500 fine).",
                "Do NOT jaywalk across roads within 50m of a crossing (SGD 50–1,000 fine).",
                "Do NOT smoke on stateroom verandahs or public streets (only yellow box Designated Smoking Areas).",
                "Do NOT connect to unverified open public Wi-Fi networks (illegal under Computer Misuse Act)."
            ],
            "dos": [
                "DO drink the tap water everywhere in Singapore — it is 100% safe, filtered, and higher quality than bottled water.",
                "DO carry 2 compact windproof umbrellas at all times for December monsoon showers.",
                "DO pre-submit the electronic SG Arrival Card within 72 hours before landing in Singapore (free at ica.gov.sg).",
                "DO dress modestly (covered knees/shoulders) when visiting heritage temples in Chinatown or Little India.",
                "DO book Disney Princess Royal Gathering on the Navigator app the moment you board the cruise!"
            ]
        }
    }
}
