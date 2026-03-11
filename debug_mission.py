import json

with open('c:/laragon/www/ninjasage/public/game_data/mission.json', 'r', encoding='utf-8') as f:
    mission_data = json.load(f)

if isinstance(mission_data, list) and len(mission_data) > 0:
    for m in mission_data:
        if isinstance(m, dict):
            with open('c:/laragon/www/ninjasage/sample_mission.txt', 'w', encoding='utf-8') as out:
                out.write(json.dumps(m, indent=2))
            break
