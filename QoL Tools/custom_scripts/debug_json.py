import json
import os

game_data_path = 'c:/laragon/www/ninjasage/public/game_data'
library_path = os.path.join(game_data_path, 'library.json')

library = json.load(open(library_path, 'r', encoding='utf-8'))

for c in library:
    if c.get('type') == 'weapon':
        print("Keys in weapon category:", c.keys())
        for k in c.keys():
            if k != 'type' and isinstance(c[k], list) and len(c[k]) > 0:
                print(f"Sample from list '{k}':", json.dumps(c[k][0], indent=2))
                break
        break
