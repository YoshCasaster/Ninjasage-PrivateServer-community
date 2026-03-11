import json

def generate_items():
    try:
        with open('c:/laragon/www/ninjasage/public/game_data/library.json', 'r', encoding='utf-8') as f:
            library = json.load(f)

        fishing_rod = {
            "price_pvp": 0,
            "attack_type": "attack_01",
            "buyable_clan": False,
            "description": "Tongkat kayu biasa dengan benang yang kuat. Cocok untuk menangkap monster air di rawa Konoha.",
            "level": 1,
            "damage": 5,
            "sell_price": 50,
            "type": "wpn",
            "price_tokens": 0,
            "id": "wpn_fishing_pole",
            "price_gold": 250,
            "name": "Pancingan Pemula",
            "buyable": True,
            "premium": False,
            "price_prestige": 0,
            "sellable": True,
            "price_merit": 0
        }

        bait = {
            "attack_type": "item",
            "buyable_clan": False,
            "description": "Umpan cacing tanah yang lezat. Taruh di tas agar monster Misi Pancingan mau keluar.",
            "level": 1,
            "damage": 0,
            "sell_price": 5,
            "type": "item",
            "price_tokens": 0,
            "id": "item_bait",
            "price_gold": 25,
            "name": "Umpan Cacing",
            "buyable": True,
            "premium": False,
            "price_prestige": 0,
            "sellable": True,
            "price_pvp": 0,
            "price_merit": 0
        }

        fish = {
            "attack_type": "item",
            "buyable_clan": False,
            "description": "Daging Ikan Mas berukuran besar! Dapat dijual ke Shop dengan harga yang sangat mahal.",
            "level": 1,
            "damage": 0,
            "sell_price": 300,
            "type": "item",
            "price_tokens": 0,
            "id": "item_fish_gold",
            "price_gold": 0,
            "name": "Ikan Mas Segar",
            "buyable": False,
            "premium": False,
            "price_prestige": 0,
            "sellable": True,
            "price_pvp": 0,
            "price_merit": 0
        }

        # Check if they exist to prevent duplication
        existing_ids = {item.get('id') for item in library if isinstance(item, dict)}
        
        added = 0
        for new_item in [fishing_rod, bait, fish]:
            if new_item['id'] not in existing_ids:
                library.append(new_item)
                added += 1
                
        with open('c:/laragon/www/ninjasage/public/game_data/library.json', 'w', encoding='utf-8') as f:
            json.dump(library, f, separators=(',', ':')) # compact format
            
        print(f"Successfully added {added} fishing items to library.json")
    except Exception as e:
        print(f"Error: {e}")

generate_items()
