import json

lib = json.load(open('c:/laragon/www/ninjasage/public/game_data/library.json', 'r', encoding='utf-8'))
for c in lib:
    t = c.get('type')
    print(f"Category: {t}, keys: {list(c.keys())}")
    if 'items' in c:
        print(f"  items count: {len(c['items'])}")
        if len(c['items']) > 0:
            print(f"  first item type: {type(c['items'][0])}")
            if isinstance(c['items'][0], dict):
                print(f"  first item keys: {list(c['items'][0].keys())}")
                print(f"  first item sample: {json.dumps(c['items'][0])[:200]}")
    print()
