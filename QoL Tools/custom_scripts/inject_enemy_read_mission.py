import json

# Fix Enemy.json
with open('c:/laragon/www/ninjasage/public/game_data/enemy.json', 'r', encoding='utf-8') as f:
    enemy_data = json.load(f)

wild_fish = {
  "id": "enemy_wild_fish",
  "level": 1,
  "name": "Ikan Mas Liar",
  "hp": 50,
  "cp": 10,
  "dodge": 0,
  "critical": 5,
  "purify": 5,
  "accuracy": 0,
  "agility": 3,
  "reactive": 0,
  "combustion": 0,
  "description": "Ikan raksasa yang hidup di lumpur rawa Konoha.",
  "size_x": 0.45,
  "size_y": 0.45,
  "attacks": [
    {
      "cooldown": 0,
      "animation": "attack_01",
      "posType": "melee_1",
      "dmg": 2,
      "multi_hit": False,
      "effects": [],
      "anims": {
        "hit": [
          36
        ]
      }
    }
  ]
}

existing_ids = {e.get('id') for e in enemy_data if isinstance(e, dict)}
if wild_fish['id'] not in existing_ids:
    enemy_data.append(wild_fish)
    with open('c:/laragon/www/ninjasage/public/game_data/enemy.json', 'w', encoding='utf-8') as f:
        json.dump(enemy_data, f, separators=(',', ':'))
    print("Added Wild Fish to enemy.json")

# Inspect Mission.json
with open('c:/laragon/www/ninjasage/public/game_data/mission.json', 'r', encoding='utf-8') as f:
    mission_data = json.load(f)

if isinstance(mission_data, list) and len(mission_data) > 0:
    for m in mission_data:
        if isinstance(m, dict) and 'type' in m and m.get('type') == 'hunting':
            with open('c:/laragon/www/ninjasage/sample_mission.txt', 'w', encoding='utf-8') as out:
                out.write(json.dumps(m, indent=2))
            print("Dumped hunting mission sample to sample_mission.txt")
            break
