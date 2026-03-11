import json

with open('c:/laragon/www/ninjasage/public/game_data/enemy.json', 'r', encoding='utf-8') as f:
    enemy_data = json.load(f)

output = ""
output += f"Type of enemy.json root: {type(enemy_data)}\n"
if isinstance(enemy_data, list) and len(enemy_data) > 0:
    output += json.dumps(enemy_data[0], indent=2)
elif isinstance(enemy_data, dict):
    first_key = list(enemy_data.keys())[0]
    output += f"First key: {first_key}\n"
    output += json.dumps(enemy_data[first_key], indent=2)

with open('c:/laragon/www/ninjasage/sample_enemy.txt', 'w', encoding='utf-8') as f:
    f.write(output)
