import json

with open('c:/laragon/www/ninjasage/public/game_data/enemy.json', 'r', encoding='utf-8') as f:
    enemy_data = json.load(f)

# The structure of enemy.json is likely a list or dictionary.
print(f"Type of enemy.json root: {type(enemy_data)}")
if isinstance(enemy_data, list) and len(enemy_data) > 0:
    print(json.dumps(enemy_data[0], indent=2))
elif isinstance(enemy_data, dict):
    first_key = list(enemy_data.keys())[0]
    print(f"First key: {first_key}")
    print(json.dumps(enemy_data[first_key], indent=2))
