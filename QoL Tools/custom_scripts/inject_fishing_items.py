import json
import os

game_data_path = 'c:/laragon/www/ninjasage/public/game_data'
library_path = os.path.join(game_data_path, 'library.json')

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

library = load_json(library_path)

# Extract samples and inject new custom items
weapon_sample = None
material_sample = None
item_sample = None

for c in library:
    if c.get('type') == 'weapon' and len(c.get('items', [])) > 0:
        weapon_sample = c['items'][0].copy()
    if c.get('type') == 'material' and len(c.get('items', [])) > 0:
        material_sample = c['items'][0].copy()
    if c.get('type') == 'item' and len(c.get('items', [])) > 0:
        item_sample = c['items'][0].copy()

# Print samples to a file for review
with open('sample_output.txt', 'w') as f:
    f.write(json.dumps({'weapon': weapon_sample, 'material': material_sample, 'item': item_sample}, indent=2))
