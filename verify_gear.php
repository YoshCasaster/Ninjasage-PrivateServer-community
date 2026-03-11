<?php
require __DIR__.'/vendor/autoload.php';
$app = require_once __DIR__.'/bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

use App\Models\Character;
use App\Models\CharacterItem;

try {
    $char = Character::orderBy('updated_at', 'desc')->first();
    
    if (!$char) {
        echo "No character found!\n";
        exit;
    }

    $pole = CharacterItem::where('character_id', $char->id)->where('item_id', 'wpn_fishing_pole')->first();
    $bait = CharacterItem::where('character_id', $char->id)->where('item_id', 'item_bait')->first();
    
    echo "Check for Character: {$char->name}\n";
    echo "Fishing Pole: " . ($pole ? "Found (Qty: {$pole->quantity})" : "Not Found") . "\n";
    echo "Bait: " . ($bait ? "Found (Qty: {$bait->quantity})" : "Not Found") . "\n";

} catch (\Exception $e) {
    echo "ERROR: " . $e->getMessage() . "\n";
}
