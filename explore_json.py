import json
import os

game_data_path = 'c:/laragon/www/ninjasage/public/game_data'
library_path = os.path.join(game_data_path, 'library.json')
enemy_path = os.path.join(game_data_path, 'enemy.json')
mission_path = os.path.join(game_data_path, 'mission.json')

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

print("Loading library...")
library = load_json(library_path)

# Find categories
categories = [c.get('type') for c in library if isinstance(c, dict)]
print("Library categories:", categories)

# Find weapon and material sample
weapon_sample = None
material_sample = None

for c in library:
    if not isinstance(c, dict): continue
    if c.get('type') == 'weapon' and 'items' in c and len(c['items']) > 0:
        weapon_sample = c['items'][0]
    if c.get('type') == 'material' and 'items' in c and len(c['items']) > 0:
        material_sample = c['items'][0]

print("Weapon sample:", json.dumps(weapon_sample, indent=2) if weapon_sample else "None")
print("Material sample:", json.dumps(material_sample, indent=2) if material_sample else "None")
