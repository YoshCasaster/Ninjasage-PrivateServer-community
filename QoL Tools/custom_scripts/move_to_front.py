import json

# 1. Update library.json
with open('c:/laragon/www/ninjasage/public/game_data/library.json', 'r', encoding='utf-8') as f:
    library_data = json.load(f)

# Find and extract fishing pole and bait
fishing_pole = None
bait = None
fish = None

filtered_library = []
for item in library_data:
    if isinstance(item, dict):
        if item.get('id') == 'wpn_fishing_pole':
            fishing_pole = item
        elif item.get('id') == 'item_bait':
            bait = item
        elif item.get('id') == 'item_fish_gold':
            fish = item
        else:
            filtered_library.append(item)
    else:
        filtered_library.append(item)

# Insert at the beginning of the list, after some basic structural items if necessary.
# Let's just insert at index 0
if fish: filtered_library.insert(0, fish)
if fishing_pole: filtered_library.insert(0, fishing_pole)
if bait: filtered_library.insert(0, bait)

with open('c:/laragon/www/ninjasage/public/game_data/library.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_library, f, separators=(',', ':'))


# 2. Update mission.json
with open('c:/laragon/www/ninjasage/public/game_data/mission.json', 'r', encoding='utf-8') as f:
    mission_data = json.load(f)

fishing_mission = None
filtered_missions = []
for m in mission_data:
    if isinstance(m, dict):
        if m.get('id') == 'msn_fishing':
            fishing_mission = m
        else:
            filtered_missions.append(m)
    else:
        filtered_missions.append(m)

if fishing_mission:
    filtered_missions.insert(0, fishing_mission)

with open('c:/laragon/www/ninjasage/public/game_data/mission.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_missions, f, separators=(',', ':'))

print("Items and Missions moved to the front successfully.")
