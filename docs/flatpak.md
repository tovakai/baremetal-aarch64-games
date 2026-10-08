# Testing Flathub AArch64 games

Flathub lists native `aarch64` builds for many games, but that **does not prove they launch on Steam Frame**. GPU APIs, OS runtime, desktop session, input, asset acquisition and media codecs may still matter.

## Install and check architecture

```sh
# Confirm you are running on an aarch64 Linux host:
uname -m

# Configure Flathub if it is not already available (no root required for user installs):
flatpak remotes
flatpak remote-add --if-not-exists --user flathub https://flathub.org/repo/flathub.flatpakrepo

# Example: open source Morrowind engine (original game assets required):
flatpak remote-info --arch=aarch64 flathub org.openmw.OpenMW
flatpak install --user flathub org.openmw.OpenMW
flatpak run org.openmw.OpenMW

# See the installed app's architecture and runtime:
flatpak info org.openmw.OpenMW
```

**Caution:** Flatpak may be preconfigured system-wide. If `flatpak remote-info` fails, check `flatpak remotes` and local configuration first. Do not copy over x86_64 Flatpaks or assume a generic Linux download is ARM64. Flatpak being available does not imply the app's specific sandbox permissions or device input work on the Frame.

## Submit a Steam Frame gameplay report

Record the exact app ID, version, `flatpak info` details, SteamOS VR version, session/windowing method, launch command, controller behavior, graphics issues, and **whether you actually reached gameplay**. Link to your report in `device_tests`. No personal test should be fabricated from a store page, review, or package listing.

As always, never redistribute commercial assets. For source ports (OpenMW, OpenRCT2, Raze, Odamex, etc.), obtain the required game data from legitimate sources.
