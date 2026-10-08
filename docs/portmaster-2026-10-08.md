# PortMaster AArch64 candidate audit (2026-10-08)

Inspected official [PortMaster-New](https://github.com/PortsMaster/PortMaster-New) `port.json` architecture declarations, bundled port folders, and launcher scripts. **All twelve packages declare `aarch64` and call a native binary or native ARM64 engine runtime**. The two packages for existing games (OpenMW, OpenTTD) are second build entries, not new games.

| Community port | Native execution evidence | Porters | Source manifest |
| --- | --- | --- | --- |
| Balatro | Native LÖVE 11.5 runtime runs patched user-owned game Lua from Balatro.exe or Balatro.love; PortMaster controller/UI adaptations. Requires purchase. | nkahoang, Guandor, juanvillacortac | [balatro port.json](https://github.com/PortsMaster/PortMaster-New/blob/main/ports/balatro/port.json) |
| Celeste | ARM64 Mono squashfs runs managed Celeste.exe with FNA compatibility libraries. Requires DRM-free original retail files; not x86 translation. | Johnny on Flame | [celeste port.json](https://github.com/PortsMaster/PortMaster-New/blob/main/ports/celeste/port.json) |
| Stardew Valley (compatibility branch) | Native ARM64 Mono 6.12 plus game-specific MonoGame patches and loader. Requires the purchased compatibility version, not the default Stardew Valley build. | Johnny on Flame | [stardewvalley port.json](https://github.com/PortsMaster/PortMaster-New/blob/main/ports/stardewvalley/port.json) |
| Undertale | Bundled gmloadernext.aarch64 executes assets supplied by owner from legitimate retail Steam/GOG game. | krishenriksen, Jeod, Ganimoth, curious_idiot | [undertale port.json](https://github.com/PortsMaster/PortMaster-New/blob/main/ports/undertale/port.json) |
| Fallout (Community Edition) | Bundled native fallout-ce game engine; requires legally purchased Fallout 1 data (critter.dat, master.dat, data folder). | kloptops | [fallout1 port.json](https://github.com/PortsMaster/PortMaster-New/blob/main/ports/fallout1/port.json) |
| Fallout 2 (Community Edition) | Bundled native fallout2-ce game engine; requires legally purchased Fallout 2 data (critter.dat, master.dat, patch000.dat, data folder). | Orson | [fallout2 port.json](https://github.com/PortsMaster/PortMaster-New/blob/main/ports/fallout2/port.json) |
| fheroes2 (Heroes of Might and Magic II) | Bundled AArch64-native fheroes2 engine. Requires legitimate Heroes II data/maps/music/sounds, not included. | romadu, ddrsoul | [fheroes2 port.json](https://github.com/PortsMaster/PortMaster-New/blob/main/ports/fheroes2/port.json) |
| Star Wars Jedi Knight: Jedi Academy (OpenJK) | Bundled openjk_sp.aarch64 and rd-vanilla_aarch64.so; requires purchased Jedi Academy base game files. Handheld gl4es.aarch64 is environment-specific. | brooksytech | [jediacademy port.json](https://github.com/PortsMaster/PortMaster-New/blob/main/ports/jediacademy/port.json) |
| Star Wars Jedi Knight II: Jedi Outcast (OpenJK) | Bundled openjo_sp.aarch64 and rdjosp-vanilla_aarch64.so; requires purchased Jedi Outcast base game files. | brooksytech | [jedioutcast port.json](https://github.com/PortsMaster/PortMaster-New/blob/main/ports/jedioutcast/port.json) |
| Quake III Arena (Quake3e) | Bundled quake3e.aarch64 and handheld gl4es.aarch64 integration; requires original Quake III full game pak files and product key. | brooksytech | [quake3 port.json](https://github.com/PortsMaster/PortMaster-New/blob/main/ports/quake3/port.json) |
| OpenMW | Separate PortMaster ARM64 build of OpenMW, using openmw.aarch64 and a Linux aarch64 compilation recipe. Requires legally acquired Morrowind assets. | saint, kloptops, BinaryCounter, bmdhacks | [openmw port.json](https://github.com/PortsMaster/PortMaster-New/blob/main/ports/openmw/port.json) |
| OpenTTD | Separate PortMaster ARM64 packaging of OpenTTD that launches openttd.${DEVICE_ARCH} natively. Existing Debian package remains a separate build. | Slayer366, Cebion, romadu | [openttd port.json](https://github.com/PortsMaster/PortMaster-New/blob/main/ports/openttd/port.json) |

## PortMaster is a platform constraint, not a seal of SteamOS approval

- Source manifests advertise native **AArch64**, but target specific Rocknix, ArkOS, MuOS and similar handheld configurations. None of these twelve entries is a new Steam Frame device test.
- Balatro: native LÖVE 11.5, with source game scripts extracted from an owned copy. Celeste and Stardew Valley: managed .NET assemblies under a native AArch64 Mono 6.12 squashfs. Undertale: bundled `gmloadernext.aarch64`.
- Fallout 1/2: bundled native Community Edition executables. Jedi Academy, Jedi Outcast, Quake III: explicitly named `.aarch64` native binaries. Heroes II, OpenMW and OpenTTD: native engines. Many packages rely on handheld-only gl4es or PortMaster controller-mapper helpers.
- **Not included:** Iconoclasts (manifest only `armhf`), and TMNT: Shredder's Revenge / Axiom Verge (inspected metadata did not explicitly declare `aarch64`). Other packages requiring FEX/box64 translation must be excluded from a strictly native catalog.
- PortMaster packages do **not** include copyrighted full game files. Buy/own them, supply your own game data, and use the port team's original instructions. Do not transplant a handheld distribution's system libraries into SteamOS.

## Future Steam Frame tests

Try a native game binary in isolation or the corresponding ARM64 runtime in a controlled environment, then document exact OS, compatible library dependencies, compositor, graphics requirements and input behavior. Successful upstream handheld gameplay cannot be assumed on Steam Frame.
