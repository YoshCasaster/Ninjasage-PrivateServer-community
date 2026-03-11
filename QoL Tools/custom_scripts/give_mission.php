<?php
require __DIR__.'/vendor/autoload.php';
$app = require_once __DIR__.'/bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

use App\Models\Character;
use Illuminate\Support\Facades\DB;

try {
    $char = Character::orderBy('updated_at', 'desc')->first();
    
    if (!$char) {
        echo "No character found!\n";
        exit;
    }

    echo "Targeting character: {$char->name} (ID: {$char->id})\n";

    // Although missions are stateless in NS, there's often a character_missions or similar table.
    // Wait, the Hunting House or Mission list is determined merely by Level in NS.
    // If the mission is not showing up, the grade might literally require 'c' or 'hunting' correctly.
    // Let's modify the mission in DB just in case.
    $mission = \App\Models\Mission::where('mission_id', 'msn_fishing')->first();
    if ($mission) {
        $mission->req_lvl = 1;
        $mission->save();
        echo "Ensured fishing mission is level 1.\n";
    }

    // Is there a mission unlock table? Let's check schema.
} catch (\Exception $e) {
    echo "ERROR: " . $e->getMessage() . "\n";
}
