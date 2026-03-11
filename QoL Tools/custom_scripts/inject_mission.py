import json

with open('c:/laragon/www/ninjasage/public/game_data/mission.json', 'r', encoding='utf-8') as f:
    mission_data = json.load(f)

fishing_mission = {
  "enemies": [
    "enemy_wild_fish"
  ],
  "bg": "mission_01",
  "id": "msn_fishing",
  "grade": "c",
  "type": "hunting",
  "name": "Memancing di Rawa",
  "level": 1,
  "description": "Tangkap Ikan Liar Raksasa yang bersembunyi di perairan ini! (Gunakan Umpan Cacing & Pancingan Pemula)",
  "premium": False,
  "dialogs": [
    {
      "character": "Shin-Left",
      "dialog": "Airnya sangat tenang hari ini. Semoga kamu mendapat tangkapan yang bagus!"
    }
  ],
  "rewards": {
    "tp": 0,
    "ss": 0,
    "xp": 50,
    "gold": 50,
    "item": "item_fish_gold"
  },
  "visible": True
}

existing_ids = {m.get('id') for m in mission_data if isinstance(m, dict)}
if fishing_mission['id'] not in existing_ids:
    mission_data.append(fishing_mission)
    with open('c:/laragon/www/ninjasage/public/game_data/mission.json', 'w', encoding='utf-8') as f:
        json.dump(mission_data, f, separators=(',', ':'))
    print("Added Fishing Mission to mission.json")
else:
    print("Fishing Mission already exists")
