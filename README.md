# Bare Metal AArch64 Games

An evidence-backed, community-maintained directory of **native Linux AArch64 (ARM64) games**. Built for people with ARM Linux systems, including Steam Frame tinkerers, without confusing a native binary with an x86 game running through translation.

> **Native ARM64 does not mean Steam Frame-tested.** An ARM64 Debian package, for example, is evidence that a Linux ARM64 build exists, *not* evidence it installs or runs on SteamOS. Device compatibility is recorded separately. "Bare Metal" is the project name, not a claim that these run without an operating system.

## Catalog

Each row describes a **specific build**, not a blanket promise about every version of a game. Links under **ARM64 evidence** point to a release or package listing that explicitly identifies the architecture.

<!-- catalog:start -->
**5 games · 5 native AArch64 builds cataloged**

| Game | Genre | Version | Origin · Format | Target | ARM64 evidence | Device tests |
| --- | --- | --- | --- | --- | --- | --- |
| [0 A.D.](https://play0ad.com/) | Real-time strategy | 0.27.0-2+b1 | [Distribution · deb](https://packages.debian.org/trixie/arm64/0ad) | Debian 13 (Trixie) | [Published](https://packages.debian.org/trixie/arm64/0ad) | — |
| [OpenTTD](https://www.openttd.org/) | Transport simulation | 14.1-1+b2 | [Distribution · deb](https://packages.debian.org/trixie/arm64/openttd) | Debian 13 (Trixie) | [Published](https://packages.debian.org/trixie/arm64/openttd) | — |
| [SuperTux](https://www.supertux.org/) | Platformer | 0.6.3-3 | [Distribution · deb](https://packages.debian.org/trixie/arm64/supertux) | Debian 13 (Trixie) | [Published](https://packages.debian.org/trixie/arm64/supertux) | — |
| [SuperTuxKart](https://supertuxkart.net/) | Kart racing | 1.4+dfsg-5+b1 | [Distribution · deb](https://packages.debian.org/trixie/arm64/supertuxkart) | Debian 13 (Trixie) | [Published](https://packages.debian.org/trixie/arm64/supertuxkart) | — |
| [The Battle for Wesnoth](https://www.wesnoth.org/) | Turn-based strategy | 1:1.18.5-1 | [Distribution · deb](https://packages.debian.org/trixie/arm64/wesnoth-1.18) | Debian 13 (Trixie) | [Published](https://packages.debian.org/trixie/arm64/wesnoth-1.18) | — |
<!-- catalog:end -->

**Verification labels:** `Published` means the linked ARM64 package/release exists. `Tested: works`, `Tested: partial`, and `Tested: broken` require a dated, reproducible device report. A dash means **no device test has been recorded**, not that the game is broken.

**Build origins:** `Upstream` = game developer; `Community` = third-party build/port; `Distribution` = Linux package maintainer. Formats and targets are listed explicitly, since `.deb` files are not generic SteamOS installers.

## Scope

- **Include:** Linux user-space **AArch64** game executables distributed as native binaries by upstream, community builders, or Linux distributions. Open-source and proprietary games are both welcome, as are clearly credited community ports, provided redistribution/legal requirements are respected.
- **Exclude:** Android-only APKs; ARM32-only builds; x86/x86-64 games that require emulation/translation (FEX, box64, QEMU, etc.); Proton/Wine-only Windows builds; source code that *might* compile for ARM64 but has no evidenced Linux ARM64 build.
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

The initial entries are **published Debian 13 ARM64 packages**, seeded from Debian's architecture-specific package index. They are **not** claimed to be personally tested on a Steam Frame. Contributions of upstream releases, standalone downloads, Flatpaks, and documented headset tests are especially welcome.
