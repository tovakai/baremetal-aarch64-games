# Celeste

**Genre:** Precision platformer

**Game/project website:** [https://www.celestegame.com/](https://www.celestegame.com/)

[← All games](../../README.md)

## AArch64 builds

### 1. PortMaster package (rolling; retail game version user-supplied)

- **Origin:** Community
- **Format:** portmaster
- **Target:** PortMaster handheld Linux AArch64 (device-specific)
- **Build/download page:** [Open link](https://github.com/PortsMaster/PortMaster-New/tree/main/ports/celeste)
- **Architecture evidence:** [Verify source](https://github.com/PortsMaster/PortMaster-New/blob/main/ports/celeste/port.json)
- **Evidence checked:** 2026-10-08
- **Maintainer/porter:** Johnny on Flame

#### Notes

PortMaster port.json declares aarch64, with launch script/native engine inspected. ARM64 Mono squashfs runs managed Celeste.exe with FNA compatibility libraries. Requires DRM-free original retail files; not x86 translation. Requires PortMaster and applicable native runtime or controller/graphics libraries. NOT tested on Steam Frame; do not assume this package works directly on SteamOS.

#### Device compatibility

No device tests recorded. An AArch64 release is not a confirmed Steam Frame test.

---

This page is generated from [game.json](game.json).
To correct metadata or add a build, edit game.json and run python3 scripts/catalog.py --write from the repository root.
Game assets and proprietary ROMs are not distributed here. See [contribution guidelines](../../CONTRIBUTING.md).
