import json

lib = json.load(open('c:/laragon/www/ninjasage/public/game_data/library.json', 'r', encoding='utf-8'))
samples = {}

for cat_name, cat_data in lib.items() if isinstance(lib, dict) else enumerate(lib):
    if isinstance(cat_data, dict):
        ctype = cat_data.get('type')
        items = cat_data.get('items', [])
        if ctype and len(items) > 0:
            samples[ctype] = items[0]
            print(f"Found sample for {ctype}")

with open('c:/laragon/www/ninjasage/sample_objects.json', 'w', encoding='utf-8') as f:
    json.dump(samples, f, indent=4)
