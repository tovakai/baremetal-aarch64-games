# OpenTTD

**Genre:** Transport simulation

**Game/project website:** [https://www.openttd.org/](https://www.openttd.org/)

[← All games](../../README.md)

## AArch64 builds

### 1. 14.1-1+b2

- **Origin:** Distribution
- **Format:** deb
- **Target:** Debian 13 (Trixie)
- **Build/download page:** [Open link](https://packages.debian.org/trixie/arm64/openttd)
- **Architecture evidence:** [Verify source](https://packages.debian.org/trixie/arm64/openttd)
- **Evidence checked:** 2026-10-08

#### Notes

Debian arm64 package; SteamOS and Steam Frame compatibility not established.

#### Device compatibility

No device tests recorded. An AArch64 release is not a confirmed Steam Frame test.

### 2. PortMaster package (rolling; retail game version user-supplied)

- **Origin:** Community
- **Format:** portmaster
- **Target:** PortMaster handheld Linux AArch64 (device-specific)
- **Build/download page:** [Open link](https://github.com/PortsMaster/PortMaster-New/tree/main/ports/openttd)
- **Architecture evidence:** [Verify source](https://github.com/PortsMaster/PortMaster-New/blob/main/ports/openttd/port.json)
- **Evidence checked:** 2026-10-08
- **Maintainer/porter:** Slayer366, Cebion, romadu

#### Notes

PortMaster port.json declares aarch64, with launch script/native engine inspected. Separate PortMaster ARM64 packaging of OpenTTD that launches openttd.${DEVICE_ARCH} natively. Existing Debian package remains a separate build. Requires PortMaster and applicable native runtime or controller/graphics libraries. NOT tested on Steam Frame; do not assume this package works directly on SteamOS.

#### Device compatibility

No device tests recorded. An AArch64 release is not a confirmed Steam Frame test.

---

This page is generated from [game.json](game.json).
To correct metadata or add a build, edit game.json and run python3 scripts/catalog.py --write from the repository root.
Game assets and proprietary ROMs are not distributed here. See [contribution guidelines](../../CONTRIBUTING.md).
