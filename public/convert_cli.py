import json
import zlib
import os
from pathlib import Path

# Need to pack: library, enemy, mission
TARGET_FILES = ["library", "enemy", "mission"]
FOLDER = Path("c:/laragon/www/ninjasage/public/game_data")

def json_to_bin(src: Path, dst: Path):
    try:
        with open(src, "r", encoding="utf-8") as f:
            data = json.load(f)
        raw = json.dumps(data, separators=(",", ":")).encode("utf-8")
        compressed = zlib.compress(raw, level=zlib.Z_BEST_COMPRESSION)
        with open(dst, "wb") as f:
            f.write(compressed)
        ratio = 100 * len(compressed) / len(raw)
        print(f"Success: {src.name} -> {dst.name} | {len(raw):,} -> {len(compressed):,} bytes ({ratio:.1f}%)")
    except Exception as e:
        print(f"Failed {src.name}: {e}")

for name in TARGET_FILES:
    src_file = FOLDER / f"{name}.json"
    dst_file = FOLDER / f"{name}.bin"
    if src_file.exists():
        json_to_bin(src_file, dst_file)
    else:
        print(f"Missing: {src_file}")
