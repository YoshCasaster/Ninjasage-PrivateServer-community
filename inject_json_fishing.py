import json
import os

game_data_path = 'c:/laragon/www/ninjasage/public/game_data'

def load_json(filename):
    with open(os.path.join(game_data_path, filename), 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filename, data):
    with open(os.path.join(game_data_path, filename), 'w', encoding='utf-8') as f:
        json.dump(data, f, separators=(',', ':'))

# 1. Inject Library (Items & Weapons)
library = load_json('library.json')

wpn_fishing_pole = {
    "id": "wpn_fishing_pole",
    "name": "Pancingan Pemula",
    "description": "Tongkat pancing kayu. Gunakan untuk memancing di danau.",
    "type": "weapon",
    "level": 1,
    "damage": 5,
    "chakra": 0,
    "agility": 0,
    "price": 250,
    "token": 0,
    "sellable": True,
    "swf": "wpn_fishing_pole"
}

item_bait = {
    "id": "item_bait",
    "name": "Umpan Cacing",
    "description": "Umpan untuk memancing ikan.",
    "type": "item",
    "level": 1,
    "price": 50,
    "token": 0,
    "sellable": True,
    "swf": "item_bait"
}

item_fish_gold = {
    "id": "item_fish_gold",
    "name": "Ikan Mas Konoha",
    "description": "Ikan tangkapan berharga yang bisa dijual mahal.",
    "type": "item",
    "level": 1,
    "price": 0,
    "sell_price": 500,
    "token": 0,
    "sellable": True,
    "swf": "item_fish_gold"
}

# Append directly to appropriate categories or at top level if not categorized
# library is usually a list of categories
for cat in library:
    if cat.get('type') == 'weapon':
        # check if not exist
        if 'items' not in cat:
            cat['items'] = []
        if not any(i.get('id') == 'wpn_fishing_pole' for i in cat['items']):
            cat['items'].insert(0, wpn_fishing_pole)
    if cat.get('type') == 'item':
        if 'items' not in cat:
            cat['items'] = []
        if not any(i.get('id') == 'item_bait' for i in cat['items']):
            cat['items'].insert(0, item_bait)
        if not any(i.get('id') == 'item_fish_gold' for i in cat['items']):
            cat['items'].insert(0, item_fish_gold)
save_json('library.json', library)

# 2. Inject Enemy
enemy_list = load_json('enemy.json')
enemy_wild_fish = {
    "id": "enemy_wild_fish",
    "name": "Ikan Mas Liar",
    "level": 1,
    "hp": 150,
    "cp": 100,
    "agility": 3,
    "swf": "enemy_wild_fish",
    "taijutsu_id": 1,
    "weapon_id": "wpn_01",
    "skills": ["1", "2"]
}
if not any(e.get('id') == 'enemy_wild_fish' for e in enemy_list):
    enemy_list.insert(0, enemy_wild_fish)
save_json('enemy.json', enemy_list)

# 3. Inject Mission
mission_list = load_json('mission.json')
msn_fishing = {
    "id": "msn_fishing",
    "name": "Memancing di Rawa",
    "description": "Pergi ke Rawa Mistik dan tangkap ikan langka dengan pancinganmu. Butuh umpan cacing.",
    "type": 1,
    "req_lvl": 1,
    "boss": 1,
    "enemies": ["enemy_wild_fish", "enemy_wild_fish", "enemy_wild_fish"],
    "bg": "mission_01",
    "rewards": {
        "xp": 50,
        "gold": 100,
        "items": []
    }
}
if not any(m.get('id') == 'msn_fishing' for m in mission_list):
    mission_list.insert(0, msn_fishing)
save_json('mission.json', mission_list)

print("Fishing Data Re-Injected Successfully.")
