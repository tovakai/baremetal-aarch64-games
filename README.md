# Bare Metal AArch64 Games

An evidence-backed, community-maintained directory of **native Linux AArch64 (ARM64) games**. Built for people with ARM Linux systems, including Steam Frame tinkerers, without confusing a native binary with an x86 game running through translation.

> **Native ARM64 does not mean Steam Frame-tested.** An ARM64 Debian package, for example, is evidence that a Linux ARM64 build exists, *not* evidence it installs or runs on SteamOS. Device compatibility is recorded separately. "Bare Metal" is the project name, not a claim that these run without an operating system.

## Catalog

Each row describes a **specific build**, not a blanket promise about every version of a game. Links under **ARM64 evidence** identify either a published ARM64 release/package or a documented, reproducible native ARM64 conversion.

<!-- catalog:start -->
**9 games · 9 native AArch64 builds cataloged**

| Game | Genre | Version | Origin · Format | Target | ARM64 evidence | Device tests |
| --- | --- | --- | --- | --- | --- | --- |
| [0 A.D.](https://play0ad.com/) | Real-time strategy | 0.27.0-2+b1 | [Distribution · deb](https://packages.debian.org/trixie/arm64/0ad) | Debian 13 (Trixie) | [Published](https://packages.debian.org/trixie/arm64/0ad) | — |
| [Brotato](https://store.steampowered.com/app/1942280/Brotato/) | Arena survival / roguelite | 1.1.14.6 | [Community · conversion](https://github.com/tovakai/multi-engine-game-conversion-framework-by-tovakai) · Tovakai (Anthon) | Steam Frame · Linux AArch64 | [Verified conversion](https://github.com/tovakai/multi-engine-game-conversion-framework-by-tovakai#tested-game-compatibility) | [Steam Frame: works](https://github.com/tovakai/multi-engine-game-conversion-framework-by-tovakai#tested-game-compatibility) |
| [Factorio](https://factorio.com/) | Factory building / automation | 2.1.21 (experimental) | [Upstream · steam](https://factorio.com/download/experimental) · Wube Software | Linux AArch64 · Steam experimental / standalone | [Published](https://www.factorio.com/blog/post/fff-446) | [Steam Frame: works](https://www.factorio.com/blog/post/fff-446) |
| [Half-Life: Alyx](https://store.steampowered.com/app/546560/HalfLife_Alyx/) | VR first-person shooter | 2026-09-14 ARM64 update | [Upstream · steam](https://store.steampowered.com/app/546560/HalfLife_Alyx/) · Valve | Steam Frame · standalone Linux AArch64 VR | [Published](https://steamcommunity.com/app/546560/announcements/) | [Steam Frame: works](https://www.computerbase.de/artikel/gaming/valve-steam-frame-half-life-alyx-arm64-port.99351/) |
| [My Pig Princess](https://www.patreon.com/CyanCapsule) | Visual novel | 0.10.1 | [Community · conversion](https://github.com/tovakai/multi-engine-game-conversion-framework-by-tovakai) · Tovakai (Anthon) | Steam Frame · Linux AArch64 | [Verified conversion](https://github.com/tovakai/multi-engine-game-conversion-framework-by-tovakai#tested-game-compatibility) | [Steam Frame: works](https://github.com/tovakai/multi-engine-game-conversion-framework-by-tovakai#tested-game-compatibility) |
| [OpenTTD](https://www.openttd.org/) | Transport simulation | 14.1-1+b2 | [Distribution · deb](https://packages.debian.org/trixie/arm64/openttd) | Debian 13 (Trixie) | [Published](https://packages.debian.org/trixie/arm64/openttd) | — |
| [SuperTux](https://www.supertux.org/) | Platformer | 0.6.3-3 | [Distribution · deb](https://packages.debian.org/trixie/arm64/supertux) | Debian 13 (Trixie) | [Published](https://packages.debian.org/trixie/arm64/supertux) | — |
| [SuperTuxKart](https://supertuxkart.net/) | Kart racing | 1.4+dfsg-5+b1 | [Distribution · deb](https://packages.debian.org/trixie/arm64/supertuxkart) | Debian 13 (Trixie) | [Published](https://packages.debian.org/trixie/arm64/supertuxkart) | — |
| [The Battle for Wesnoth](https://www.wesnoth.org/) | Turn-based strategy | 1:1.18.5-1 | [Distribution · deb](https://packages.debian.org/trixie/arm64/wesnoth-1.18) | Debian 13 (Trixie) | [Published](https://packages.debian.org/trixie/arm64/wesnoth-1.18) | — |
<!-- catalog:end -->

**Verification labels:** `Published` means upstream/distribution evidence identifies an ARM64 release or package; `Verified conversion` means a reproducible, player-owned native ARM64 conversion has actually been tested, **not** that a prebuilt game is distributed. `Device: works`, `partial`, and `broken` are linked to dated test reports. A dash means **no device test recorded**, not that a game is broken. A gameplay test may be less extensive than a complete playthrough.

**Build origins:** `Upstream` = game developer; `Community` = third-party native port/conversion; `Distribution` = Linux package maintainer. `Steam` indicates a Steam-distributed native build; `conversion` indicates a package generated locally from legally obtained game files, **not** a downloadable redistributed game. Formats and targets are explicit since `.deb` files are not generic SteamOS installers.

## Community conversion spotlight

**Brotato 1.1.14.6** and **My Pig Princess 0.10.1** were converted and gameplay-tested on Steam Frame by **Tovakai (Anthon)**, using the [Tovakai multi-engine conversion framework](https://github.com/tovakai/multi-engine-game-conversion-framework-by-tovakai). Brotato completed a full run using the custom GodotSteam ARM64 runtime; My Pig Princess reached playable gameplay using Ren'Py 8.3.7 ARM64. These are **player-owned conversions**, not upstream ARM64 releases or downloads of the copyrighted games. See the [version-specific compatibility reports](https://github.com/tovakai/multi-engine-game-conversion-framework-by-tovakai#tested-game-compatibility).

## Scope

- **Include:** Linux user-space **AArch64** games distributed as native binaries by upstream, community builders, or Linux distributions **and** documented, successfully tested conversions that users can reproduce locally from legitimately acquired game files. Open-source and proprietary games are welcome, with explicit origin, attribution, and rights boundaries.
- **Exclude:** Android-only APKs; ARM32-only builds; x86/x86-64 games needing FEX, box64, QEMU, etc.; Proton/Wine-only Windows builds; hypothetical source-only compatibility and **unverified conversion attempts**. Native ARM64 engines running a converted game's original assets count only after documented gameplay testing.
- **Separate questions:** CPU architecture, distribution availability, runtime dependencies, and real-world compatibility. We do **not** infer Steam Frame support from a Debian/Flatpak listing, or VR support from a desktop game.
- **Game assets:** Link to the rights holder's legitimate distribution. Do not upload commercial game assets, keys, or copyrighted build artifacts to this repository.

## Contribute

Please use the [game submission form](https://github.com/tovakai/baremetal-aarch64-games/issues/new?template=add-game.yml) to suggest a build, or open a PR editing [`data/games.json`](data/games.json). Read [CONTRIBUTING.md](CONTRIBUTING.md) for the exact format, evidence requirements, and how to record a device test. No need to rewrite the table by hand.

```sh
python3 scripts/catalog.py --write   # regenerate the README catalog
python3 scripts/catalog.py --check   # validate data + generated table
python3 -m unittest discover -s tests
```

The catalog is generated from JSON using Python's standard library. CI rejects malformed data or an out-of-sync table.

## How to verify an AArch64 binary

See [the verification guide](docs/verification.md) for `file`/`readelf` commands, evidence examples, and reproducible Steam Frame test reports.

## Project status

Seed entries include **five Debian ARM64 packages** (no device tests), **two official native ARM64 releases** (with third-party/developer Steam Frame testing), and **two Tovakai player-owned conversions** (personally gameplay-tested on Steam Frame). The repo does not host copyrighted game binaries or assets. Further official releases, reproducible conversion reports, and documented device tests are welcome.
