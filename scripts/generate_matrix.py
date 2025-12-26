import json
from pathlib import Path

# === CONFIGURATION ===
# automatically find all *.keymap filenames under ../config/keymap
keymap_dir = Path(__file__).parent.parent / "config" / "keymap"
keymaps = sorted(p.stem for p in keymap_dir.glob("*.keymap"))

boards_to_short_names = {
    "nice_nano_v2": "nano",
    "seeeduino_xiao_ble": "xiao",
}

groups = []
board = "nice_nano_v2"
for keymap in keymaps:
    for fmt in ["bt", "dongle"]:
        groups.append(
            {
                "keymap": keymap,
                "format": fmt,
                "name": f"{keymap}-{fmt}-{boards_to_short_names[board]}",
                "board": board,
            }
        )

board = "seeeduino_xiao_ble"
for keymap in keymaps:
    for fmt in ["dongle_only"]:
        groups.append(
            {
                "keymap": keymap,
                "format": fmt,
                "name": f"{keymap}-{fmt}-{boards_to_short_names[board]}",
                "board": board,
            }
        )

for board in boards_to_short_names.keys():
    groups.append(
        {
            "keymap": "default",
            "format": "reset",
            "name": f"reset-{boards_to_short_names[board]}",
            "board": board,
        }
    )

# Dump matrix as compact JSON (GitHub expects it this way)
print(json.dumps(groups))
