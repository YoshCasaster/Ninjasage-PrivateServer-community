<?php
require __DIR__.'/vendor/autoload.php';
$app = require_once __DIR__.'/bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

use App\Models\Item;

try {
    $itemData = [
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
    ];
    Item::create($itemData);
    file_put_contents('debug_error.log', "Item inserted\n");
} catch (\Exception $e) {
    file_put_contents('debug_error.log', "ERROR: " . $e->getMessage() . "\n");
}
