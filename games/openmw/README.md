# OpenMW

**Genre:** RPG / Morrowind engine

**Game/project website:** [https://openmw.org/](https://openmw.org/)

[← All games](../../README.md)

## AArch64 builds

### 1. 0.51.0

- **Origin:** Distribution
- **Format:** flatpak
- **Target:** Flathub · Linux AArch64
- **Build/download page:** [Open link](https://flathub.org/en/apps/org.openmw.OpenMW)
- **Architecture evidence:** [Verify source](https://flathub.org/en/apps/org.openmw.OpenMW)
- **Evidence checked:** 2026-10-08

#### Notes

Flathub lists aarch64 in Available Architectures. App ID: org.openmw.OpenMW. Native engine replacement, not a free copy of The Elder Scrolls III: Morrowind. Legally acquired Morrowind data is required. Steam Frame not tested.

#### Device compatibility

No device tests recorded. An AArch64 release is not a confirmed Steam Frame test.

### 2. PortMaster package (rolling; retail game version user-supplied)

- **Origin:** Community
- **Format:** portmaster
- **Target:** PortMaster handheld Linux AArch64 (device-specific)
- **Build/download page:** [Open link](https://github.com/PortsMaster/PortMaster-New/tree/main/ports/openmw)
- **Architecture evidence:** [Verify source](https://github.com/PortsMaster/PortMaster-New/blob/main/ports/openmw/port.json)
- **Evidence checked:** 2026-10-08
- **Maintainer/porter:** saint, kloptops, BinaryCounter, bmdhacks

#### Notes

PortMaster port.json declares aarch64, with launch script/native engine inspected. Separate PortMaster ARM64 build of OpenMW, using openmw.aarch64 and a Linux aarch64 compilation recipe. Requires legally acquired Morrowind assets. Requires PortMaster and applicable native runtime or controller/graphics libraries. NOT tested on Steam Frame; do not assume this package works directly on SteamOS.

#### Device compatibility

No device tests recorded. An AArch64 release is not a confirmed Steam Frame test.

---

This page is generated from [game.json](game.json).
To correct metadata or add a build, edit game.json and run python3 scripts/catalog.py --write from the repository root.
Game assets and proprietary ROMs are not distributed here. See [contribution guidelines](../../CONTRIBUTING.md).
