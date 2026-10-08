# Undertale

**Genre:** RPG

**Game/project website:** [https://undertale.com/](https://undertale.com/)

[← All games](../../README.md)

## AArch64 builds

### 1. PortMaster package (rolling; retail game version user-supplied)

- **Origin:** Community
- **Format:** portmaster
- **Target:** PortMaster handheld Linux AArch64 (device-specific)
- **Build/download page:** [Open link](https://github.com/PortsMaster/PortMaster-New/tree/main/ports/undertale)
- **Architecture evidence:** [Verify source](https://github.com/PortsMaster/PortMaster-New/blob/main/ports/undertale/port.json)
- **Evidence checked:** 2026-10-08
- **Maintainer/porter:** krishenriksen, Jeod, Ganimoth, curious_idiot

#### Notes

PortMaster port.json declares aarch64, with launch script/native engine inspected. Bundled gmloadernext.aarch64 executes assets supplied by owner from legitimate retail Steam/GOG game. Requires PortMaster and applicable native runtime or controller/graphics libraries. NOT tested on Steam Frame; do not assume this package works directly on SteamOS.

#### Device compatibility

No device tests recorded. An AArch64 release is not a confirmed Steam Frame test.

---

This page is generated from [game.json](game.json).
To correct metadata or add a build, edit game.json and run python3 scripts/catalog.py --write from the repository root.
Game assets and proprietary ROMs are not distributed here. See [contribution guidelines](../../CONTRIBUTING.md).
