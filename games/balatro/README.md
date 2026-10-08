# Balatro

**Genre:** Roguelike deckbuilder

**Game/project website:** [https://store.steampowered.com/app/2379780/Balatro/](https://store.steampowered.com/app/2379780/Balatro/)

[← All games](../../README.md)

## AArch64 builds

### 1. PortMaster package (rolling; retail game version user-supplied)

- **Origin:** Community
- **Format:** portmaster
- **Target:** PortMaster handheld Linux AArch64 (device-specific)
- **Build/download page:** [Open link](https://github.com/PortsMaster/PortMaster-New/tree/main/ports/balatro)
- **Architecture evidence:** [Verify source](https://github.com/PortsMaster/PortMaster-New/blob/main/ports/balatro/port.json)
- **Evidence checked:** 2026-10-08
- **Maintainer/porter:** nkahoang, Guandor, juanvillacortac

#### Notes

PortMaster port.json declares aarch64, with launch script/native engine inspected. Native LÖVE 11.5 runtime runs patched user-owned game Lua from Balatro.exe or Balatro.love; PortMaster controller/UI adaptations. Requires purchase. Requires PortMaster and applicable native runtime or controller/graphics libraries. NOT tested on Steam Frame; do not assume this package works directly on SteamOS.

#### Device compatibility

No device tests recorded. An AArch64 release is not a confirmed Steam Frame test.

---

This page is generated from [game.json](game.json).
To correct metadata or add a build, edit game.json and run python3 scripts/catalog.py --write from the repository root.
Game assets and proprietary ROMs are not distributed here. See [contribution guidelines](../../CONTRIBUTING.md).
