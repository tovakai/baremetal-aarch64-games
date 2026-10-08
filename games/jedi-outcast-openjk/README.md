# Star Wars Jedi Knight II: Jedi Outcast (OpenJK)

**Genre:** Third-person action / FPS

**Game/project website:** [https://github.com/JACoders/OpenJK](https://github.com/JACoders/OpenJK)

[← All games](../../README.md)

## AArch64 builds

### 1. PortMaster package (rolling; retail game version user-supplied)

- **Origin:** Community
- **Format:** portmaster
- **Target:** PortMaster handheld Linux AArch64 (device-specific)
- **Build/download page:** [Open link](https://github.com/PortsMaster/PortMaster-New/tree/main/ports/jedioutcast)
- **Architecture evidence:** [Verify source](https://github.com/PortsMaster/PortMaster-New/blob/main/ports/jedioutcast/port.json)
- **Evidence checked:** 2026-10-08
- **Maintainer/porter:** brooksytech

#### Notes

PortMaster port.json declares aarch64, with launch script/native engine inspected. Bundled openjo_sp.aarch64 and rdjosp-vanilla_aarch64.so; requires purchased Jedi Outcast base game files. Requires PortMaster and applicable native runtime or controller/graphics libraries. NOT tested on Steam Frame; do not assume this package works directly on SteamOS.

#### Device compatibility

No device tests recorded. An AArch64 release is not a confirmed Steam Frame test.

---

This page is generated from [game.json](game.json).
To correct metadata or add a build, edit game.json and run python3 scripts/catalog.py --write from the repository root.
Game assets and proprietary ROMs are not distributed here. See [contribution guidelines](../../CONTRIBUTING.md).
