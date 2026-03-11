<?php
require __DIR__.'/vendor/autoload.php';
$app = require_once __DIR__.'/bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

use App\Models\Character;
use App\Models\AdminCommand;
use App\Services\AdminCommandService;

try {
    // Determine the character to target (first character of user 1, etc.)
    // Let's get the most recently active character or ID 1
    $char = Character::orderBy('updated_at', 'desc')->first();
    
    if (!$char) {
        echo "No character found!\n";
        exit;
    }

    echo "Targeting character: {$char->name} (ID: {$char->id})\n";

    $service = new AdminCommandService();
    $command = new AdminCommand();
    $command->command_type = 'give_fishing_gear';
    
    $result = $service->execute($command, $char);
    
    if ($result['success']) {
        echo "SUCCESS: " . $result['message'] . "\n";
    } else {
        echo "FAILED: " . ($result['message'] ?? 'Unknown error') . "\n";
    }
} catch (\Exception $e) {
    echo "ERROR: " . $e->getMessage() . "\n";
}
