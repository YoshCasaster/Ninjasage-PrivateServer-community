import json

lib = json.load(open('c:/laragon/www/ninjasage/public/game_data/library.json', 'r', encoding='utf-8'))

output = []
for c in lib:
    if isinstance(c, dict):
        ctype = c.get('type')
        items = c.get('items', [])
        output.append({
            'type': ctype,
            'item_count': len(items),
            'sample_item': items[0] if len(items) > 0 else None
        })

with open('c:/laragon/www/ninjasage/all_categories.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=4)
