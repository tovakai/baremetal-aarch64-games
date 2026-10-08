# Standalone AArch64 downloads and test reports

Native ARM64 games are distributed outside Flatpak too, including developer-published ZIP packages on itch.io, GitHub `.tar.gz`/`.tar.xz` archives and AArch64 AppImages. The catalog tracks the **specific release and architecture** without claiming every archive will run on SteamOS VR.

## Evidence

- Confirm the publisher explicitly lists `linux-arm64`, `linux-aarch64` or equivalent **as an actual downloadable build**; don't rely on generic Linux platform flags.
- Record the **exact asset filename and released version** in `data/games.json`. If no version is shown, use `unversioned (itch.io)` rather than inventing one.
- For paid games, mention that **purchasing/access is required** in notes. Never redistribute commercial files, keys or extracted game assets.
- Differentiate official original games (`kind: upstream`) from community engine reimplementations (`kind: community`), and game engines needing original assets from complete games.
- A Linux ARM64 release for a **VR** game does **not** establish Steam Frame compatibility. The developer of Not Enough Fuel VR specifically marks its Frame ARM64 build as untested.

## Check the actual executable (after legally obtaining it)

```sh
file ./game-executable
readelf -h ./game-executable | grep -E 'Class:|Machine:'
# Expect ELF64, Machine: AArch64, not x86-64.
```

If the archive contains a launcher, identify the real executable first. Some builds depend on SDL, Java, specific OpenGL/Vulkan features, glibc versions, or a working X11/Wayland compositor. On Steam Frame, note whether you launched through Steam, a graphical session, or a custom overlay.

Only create a `device_tests` record once you can link a **dated, reproducible gameplay report** with the exact device, SteamOS version, title/build version, runtime and outcome. If you merely downloaded or inspected a release, leave `device_tests: []`.
