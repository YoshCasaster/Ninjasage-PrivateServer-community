<?php

use App\Models\Item;
use App\Models\Enemy;
use App\Models\Mission;

// 1. Insert Items
$items = [
    [
        'item_id' => 'wpn_fishing_pole',
        'type' => 'weapon',
        'name' => 'Pancingan Pemula',
        'description' => 'Tongkat kayu biasa dengan benang yang kuat.',
        'level' => 1,
        'damage' => 5,
        'buyable' => 1,
        'sellable' => 1,
        'price_gold' => 250,
        'price_token' => 0,
        'sell_price' => 50,
    ],
    [
        'item_id' => 'item_bait',
        'type' => 'item',
        'name' => 'Umpan Cacing',
        'description' => 'Umpan cacing tanah yang lezat.',
        'level' => 1,
        'damage' => 0,
        'buyable' => 1,
        'sellable' => 1,
        'price_gold' => 25,
        'price_token' => 0,
        'sell_price' => 5,
    ],
    [
        'item_id' => 'item_fish_gold',
        'type' => 'item',
        'name' => 'Ikan Mas Segar',
        'description' => 'Daging Ikan Mas berukuran besar!',
        'level' => 1,
        'damage' => 0,
        'buyable' => 0,
        'sellable' => 1,
        'price_gold' => 0,
        'price_token' => 0,
        'sell_price' => 300,
    ],
];

foreach ($items as $itemData) {
    if (!Item::where('item_id', $itemData['item_id'])->exists()) {
        Item::create($itemData);
        echo "Inserted Item: {$itemData['name']}\n";
    }
}

// 2. Insert Enemy
$enemyData = [
    'enemy_id' => 'enemy_wild_fish',
    'name' => 'Ikan Mas Liar',
    'level' => 1,
    'hp' => 50,
    'cp' => 10,
    'agility' => 3,
    'attacks' => [
        [
            "cooldown" => 0,
            "animation" => "attack_01",
            "posType" => "melee_1",
            "dmg" => 2,
            "multi_hit" => false,
            "effects" => [],
            "anims" => ["hit" => [36]]
        ]
    ]
];

if (!Enemy::where('enemy_id', $enemyData['enemy_id'])->exists()) {
    Enemy::create($enemyData);
    echo "Inserted Enemy: {$enemyData['name']}\n";
}

// 3. Insert Mission
$missionData = [
    'mission_id' => 'msn_fishing',
    'req_lvl' => 1,
    'xp' => 50,
    'gold' => 50,
];

if (!Mission::where('mission_id', $missionData['mission_id'])->exists()) {
    Mission::create($missionData);
    echo "Inserted Mission: {$missionData['mission_id']}\n";
}

echo "Database injection completed.\n";
