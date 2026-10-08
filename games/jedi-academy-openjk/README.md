# Star Wars Jedi Knight: Jedi Academy (OpenJK)

**Genre:** Third-person action / FPS

**Game/project website:** [https://github.com/JACoders/OpenJK](https://github.com/JACoders/OpenJK)

[← All games](../../README.md)

## AArch64 builds

### 1. PortMaster package (rolling; retail game version user-supplied)

- **Origin:** Community
- **Format:** portmaster
- **Target:** PortMaster handheld Linux AArch64 (device-specific)
- **Build/download page:** [Open link](https://github.com/PortsMaster/PortMaster-New/tree/main/ports/jediacademy)
- **Architecture evidence:** [Verify source](https://github.com/PortsMaster/PortMaster-New/blob/main/ports/jediacademy/port.json)
- **Evidence checked:** 2026-10-08
- **Maintainer/porter:** brooksytech

#### Notes

PortMaster port.json declares aarch64, with launch script/native engine inspected. Bundled openjk_sp.aarch64 and rd-vanilla_aarch64.so; requires purchased Jedi Academy base game files. Handheld gl4es.aarch64 is environment-specific. Requires PortMaster and applicable native runtime or controller/graphics libraries. NOT tested on Steam Frame; do not assume this package works directly on SteamOS.

#### Device compatibility

No device tests recorded. An AArch64 release is not a confirmed Steam Frame test.

---

This page is generated from [game.json](game.json).
To correct metadata or add a build, edit game.json and run python3 scripts/catalog.py --write from the repository root.
Game assets and proprietary ROMs are not distributed here. See [contribution guidelines](../../CONTRIBUTING.md).
