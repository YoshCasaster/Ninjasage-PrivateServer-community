import json

lib = json.load(open('c:/laragon/www/ninjasage/public/game_data/library.json', 'r', encoding='utf-8'))
samples = {}

for item in lib:
    if isinstance(item, dict):
        itype = item.get('type')
        if itype and itype not in samples:
            samples[itype] = item

with open('c:/laragon/www/ninjasage/sample_objects.json', 'w', encoding='utf-8') as f:
    json.dump(samples, f, indent=4)
