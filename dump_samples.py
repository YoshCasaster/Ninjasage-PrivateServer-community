import json

lib = json.load(open('c:/laragon/www/ninjasage/public/game_data/library.json', 'r', encoding='utf-8'))
samples = {}

for c in lib:
    t = c.get('type')
    if t in ('weapon', 'material', 'item'):
        if 'items' in c and len(c['items']) > 0:
            samples[t] = c['items'][0]

with open('c:/laragon/www/ninjasage/sample_objects.json', 'w', encoding='utf-8') as f:
    json.dump(samples, f, indent=4)
