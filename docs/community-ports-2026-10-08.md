# Native Linux AArch64 community ports verified on 2026-10-08

This seed batch includes **8 GitHub community port/recompilation projects** and **6 Flathub-packaged community ports**. These links were checked for specifically published Linux **arm64/aarch64** release assets (GitHub) or an explicit **Available Architectures: aarch64** listing (Flathub). **No new Steam Frame device tests were performed.**

## Published GitHub Linux ARM64 releases

| Community project | Tagged release | Verified ARM64 artifact(s) | Maintainer |
| --- | --- | --- | --- |
| [Dethrace (Carmageddon)](https://github.com/dethrace-labs/dethrace) | [v0.10.1](https://github.com/dethrace-labs/dethrace/releases/tag/v0.10.1) | `dethrace-v0.10.1-linux-arm64.tar.gz` | Dethrace contributors |
| [dhewm3 (Doom 3)](https://github.com/dhewm/dhewm3) | [1.5.5](https://github.com/dhewm/dhewm3/releases/tag/1.5.5) | `dhewm3-1.5.5_Linux_arm64.tar.gz` | dhewm3 contributors |
| [Little Big Adventure 2 Classic Community](https://github.com/LBALab/lba2-classic-community) | [v0.12.0](https://github.com/LBALab/lba2-classic-community/releases/tag/v0.12.0) | `lba2cc-0.12.0-anylinux-aarch64.AppImage`, `lba2cc-0.12.0-linux-aarch64.tar.gz` | LBALab contributors |
| [Pokémon Snap: Recompiled](https://github.com/JackandBeans/Snap64Recomp) | [v1.1.2](https://github.com/JackandBeans/Snap64Recomp/releases/tag/v1.1.2) | `Snap64Recomp-1.1.2-linux-arm64.tar.gz` | JackandBeans |
| [Donkey Kong 64: Recompiled](https://github.com/Rainchus/Donkey-Kong-64-Recompiled) | [v1.0.3](https://github.com/Rainchus/Donkey-Kong-64-Recompiled/releases/tag/v1.0.3) | `DK64Recompiled-Linux-ARM64-Release-1-0-3.zip` | Rainchus |
| [Star Fox 64: Recompiled](https://github.com/sonicdcer/Starfox64Recomp) | [1.0.3](https://github.com/sonicdcer/Starfox64Recomp/releases/tag/1.0.3) | `Starfox64Recompiled-v1.0.3-Linux-ARM64-Release.zip` | Sonic Dreamcaster |
| [G1R Deluxe (Gen1Recomp)](https://github.com/bryanthaboi/gen1recomp) | [v0.3.63](https://github.com/bryanthaboi/gen1recomp/releases/tag/v0.3.63) | `gen1recomp-0.3.63-linux-arm64.AppImage` | bryanthaboi |
| [Xash3D FWGS (Half-Life)](https://github.com/FWGS/xash3d-fwgs) | [continuous](https://github.com/FWGS/xash3d-fwgs/releases/tag/continuous) | `xash3d-fwgs-arm64.AppImage`, `xash3d-fwgs-linux-arm64.tar.gz` | FWGS contributors |

## ARM64 community source-port Flatpaks

| Game / engine | Flathub build version | App ID |
| --- | --- | --- |
| [Julius (Caesar III)](https://flathub.org/en/apps/com.github.bvschaik.julius) | 1.8.0 | `com.github.bvschaik.julius` |
| [Augustus (Caesar III)](https://flathub.org/en/apps/com.github.keriew.augustus) | 4.0.0 | `com.github.keriew.augustus` |
| [CorsixTH (Theme Hospital)](https://flathub.org/en/apps/com.corsixth.corsixth) | 0.70.1 | `com.corsixth.corsixth` |
| [DXX-Rebirth (Descent 1 & 2)](https://flathub.org/en/apps/io.github.dxx_rebirth.dxx-rebirth) | 0.60.0-beta2+a531f57 | `io.github.dxx_rebirth.dxx-rebirth` |
| [Hurrican](https://flathub.org/en/apps/io.github.hurricangame.hurrican) | 1.0.1 | `io.github.hurricangame.hurrican` |
| [ZeroSpades](https://flathub.org/en/apps/io.github.zerospades.ZeroSpades) | 0.0.9 | `io.github.zerospades.ZeroSpades` |

## What was intentionally excluded

- **OpenLara:** the release shows `OpenLara_rpi.zip`, but does not establish 64-bit ARM ELF; Raspberry Pi alone is insufficient architecture evidence.
- **TRX (Tomb Raider), Augustus/Julius GitHub binaries, CorsixTH GitHub binaries:** no specifically named Linux AArch64 asset in the inspected latest GitHub releases. Julius, Augustus, CorsixTH enter via *their independently verified ARM64 Flatpaks* instead.
- **Gen2Recomped:** project documentation advertises a Linux ARM64 AppImage, but inspected latest release assets do not include it; do not infer existence from a build workflow.
- **ET: Legacy, OpenSpades, original Zandronum:** inspected Flathub listings were x86_64-only; excluded as ARM64 Flatpaks. ZeroSpades, a distinct fork, has an AArch64 Flatpak.
- **PortMaster wrappers:** [JeodC/RHH-Ports](https://github.com/JeodC/RHH-Ports) and [Pixelforge Ports](https://github.com/Pixelforge-Ports) are worth investigating, but handheld-specific PortMaster recipes often depend on a specific firmware/runtime. A game needs explicit Linux AArch64 binary evidence (and any necessary runtime caveats) before entering the main catalog.

## Important limitations

- Native **static recompilations** are different from emulators. They often need a legally obtained source ROM even though the host binary runs natively on AArch64.
- **Port** and **source port** may require original game assets; publisher rights remain with the original owners.
- ARM64 artifacts establish availability, **not** successful play on Steam Frame. Linux desktop dependencies and GPU capabilities can be dealbreakers.
- Source-port maintainers are credited separately from original game authors. Flathub is a distribution format, not proof of project-owner endorsement.
