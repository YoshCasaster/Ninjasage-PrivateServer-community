<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\Item;
use App\Models\Enemy;
use App\Models\Mission;

class FishingSeeder extends Seeder
{
    public function run(): void
    {
        // 1. Insert Items based on $fillable: 'item_id', 'name', 'level', 'price_gold', 'price_tokens', 'category', 'premium', 'icon'
        $items = [
            [
                'item_id' => 'wpn_fishing_pole',
                'name' => 'Pancingan Pemula',
                'level' => 1,
                'price_gold' => 250,
                'price_tokens' => 0,
                'category' => 'weapon',
                'premium' => 0,
                'icon' => 'wpn_fishing_pole',
            ],
            [
                'item_id' => 'item_bait',
                'name' => 'Umpan Cacing',
                'level' => 1,
                'price_gold' => 25,
                'price_tokens' => 0,
                'category' => 'item',
                'premium' => 0,
                'icon' => 'item_bait',
            ],
            [
                'item_id' => 'item_fish_gold',
                'name' => 'Ikan Mas Segar',
                'level' => 1,
                'price_gold' => 0,
                'price_tokens' => 0,
                'category' => 'item',
                'premium' => 0,
                'icon' => 'item_fish_gold',
            ],
        ];

        foreach ($items as $itemData) {
            if (!Item::where('item_id', $itemData['item_id'])->exists()) {
                Item::create($itemData);
                $this->command->info("Inserted Item: {$itemData['name']}");
            }
        }

        // 2. Insert Enemy based on $fillable: 'enemy_id', 'name', 'level', 'hp', 'cp', 'agility', 'attacks'
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
            $this->command->info("Inserted Enemy: {$enemyData['name']}");
        }

        // 3. Insert Mission based on $fillable: 'mission_id', 'req_lvl', 'xp', 'gold'
        $missionData = [
            'mission_id' => 'msn_fishing',
            'req_lvl' => 1,
            'xp' => 50,
            'gold' => 50,
        ];

        if (!Mission::where('mission_id', $missionData['mission_id'])->exists()) {
            Mission::create($missionData);
            $this->command->info("Inserted Mission: {$missionData['mission_id']}");
        }

        $this->command->info("Fishing database sync completed.");
    }
}
