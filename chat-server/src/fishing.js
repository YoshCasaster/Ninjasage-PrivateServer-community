'use strict';

const db = require('./db');

// Konfigurasi Sistem Pancingan
const FISHING_COST_STAMINA = 10;
const COOLDOWN_MS = 5000; // 5 detik antar lemparan pancing

// Kamus Cooldown per pemain (di memori)
const cooldowns = {};

/**
 * Logika RNG (Random Number Generator) Memancing
 * Mengembalikan objek hadiah dan pesannya.
 */
function rollTangkapan() {
    const chance = Math.random() * 100;

    if (chance < 40) {
        // 40% Zonk / Sampah
        const gold = Math.floor(Math.random() * 50) + 10; // 10 - 60 gold
        return {
            type: 'gold',
            amount: gold,
            msg: `Kamu hanya mendapat sepatu rombeng, tapi laku dijual seharga ${gold} Gold.`
        };
    } else if (chance < 70) {
        // 30% Ikan Biasa
        const xp = Math.floor(Math.random() * 100) + 50; // 50 - 150 xp
        return {
            type: 'xp',
            amount: xp,
            msg: `Berhasil! Kamu menangkap Ikan Mas dan mendapatkan ${xp} XP.`
        };
    } else if (chance < 90) {
        // 20% Ikan Besar
        const gold = Math.floor(Math.random() * 500) + 200; // 200 - 700 gold
        return {
            type: 'gold',
            amount: gold,
            msg: `Luar Biasa! Kamu menangkap Ikan Hiu mini. Dijual seharga ${gold} Gold!`
        };
    } else {
        // 10% Jackpot
        const token = Math.floor(Math.random() * 5) + 1; // 1 - 5 token
        return {
            type: 'token',
            amount: token,
            msg: `JACKPOT! Kamu memancing peti harta karun berisi ${token} Token!`
        };
    }
}

/**
 * Handle perintah /mancing dari ChatNamespace
 */
async function handleFishingCommand(socket, socketChar) {
    const charId = socketChar.id;
    const now = Date.now();

    // Cek Cooldown supaya tidak di-spam
    if (cooldowns[charId] && (now - cooldowns[charId]) < COOLDOWN_MS) {
        const sisa = Math.ceil((COOLDOWN_MS - (now - cooldowns[charId])) / 1000);
        sendSystemMsg(socket, `Air sedang keruh. Tunggu ${sisa} detik lagi.`);
        return;
    }

    try {
        // 1. Ambil data asli dari database untuk validasi stamina terkini
        const charData = await db.queryOne('SELECT id, name, stamina, gold, session_tokens, xp FROM characters WHERE id = ?', [charId]);

        if (!charData) {
            sendSystemMsg(socket, "Gagal memancing. Data karakter tidak ditemukan.");
            return;
        }

        if (charData.stamina < FISHING_COST_STAMINA) {
            sendSystemMsg(socket, `Stamina tidak cukup! Butuh ${FISHING_COST_STAMINA} stamina untuk memancing.`);
            return;
        }

        // Terapkan cooldown
        cooldowns[charId] = now;

        // 2. Tentukan Hasil Pancingan RNG
        const hasil = rollTangkapan();

        // 3. Update Database (Potong stamina dan tambah hadiah)
        let sqlUpdate = '';
        let params = [];

        if (hasil.type === 'gold') {
            sqlUpdate = 'UPDATE characters SET stamina = stamina - ?, gold = gold + ? WHERE id = ?';
            params = [FISHING_COST_STAMINA, hasil.amount, charId];
        } else if (hasil.type === 'xp') {
            sqlUpdate = 'UPDATE characters SET stamina = stamina - ?, xp = xp + ? WHERE id = ?';
            params = [FISHING_COST_STAMINA, hasil.amount, charId];
        } else if (hasil.type === 'token') {
            sqlUpdate = 'UPDATE characters SET stamina = stamina - ?, session_tokens = session_tokens + ? WHERE id = ?';
            params = [FISHING_COST_STAMINA, hasil.amount, charId];
        }

        await db.query(sqlUpdate, params);

        // 4. Kirim balasan ke pemain
        sendSystemMsg(socket, hasil.msg + " (-10 Stamina)");

    } catch (error) {
        console.error(`[Fishing] Error for charId ${charId}:`, error);
        sendSystemMsg(socket, "Terjadi kesalahan sistem saat memancing.");
    }
}

/**
 * Fungsi helper untuk mengirim pesan system ke pemancing saja (bukan global)
 */
function sendSystemMsg(socket, text) {
    const systemMsg = {
        character: {
            id: 0,
            name: '[Memancing]',
            level: 0,
            rank: 0,
            premium: 0,
        },
        message: text,
    };
    socket.emit('message', systemMsg);
}

module.exports = {
    handleFishingCommand
};
