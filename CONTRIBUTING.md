# Contributing

Thanks for helping build an accurate Linux AArch64 game catalog. The goal is a useful source of truth, not the longest possible list.

## Add a game or build

1. Check whether the game is already present in `data/games.json`. Add a new `builds` entry rather than duplicating a game if only the build or packaging differs.
2. Link a release asset, package index, or archived build page that **explicitly identifies Linux AArch64/arm64**. For a *player-owned conversion*, link a reproducible conversion recipe and a real native ARM64 gameplay report (with exact game/runtime versions). Source-only claims or a build that has never launched do not count.
3. Specify the **origin** (`upstream`, `community`, or `distribution`) and **format** (`deb`, `rpm`, `flatpak`, `appimage`, `tarball`, `standalone`, or `other`; additionally, `steam` for a Steam-native build and `conversion` for a locally generated native game). Don't describe a distro package as upstream. For conversions, set `kind` to `community`, `format` to `conversion`, and `maintainer` to the credited converter/maintainer.
4. Record the exact version, distribution/runtime target, evidence URL, and date you checked the link. If it needs proprietary game files, say so in `notes` and link only legal acquisition paths.
5. Run `python3 scripts/catalog.py --write`, `python3 scripts/catalog.py --check`, and `python3 -m unittest discover -s tests` before opening a PR.

## Schema at a glance

```json
{
  "id": "example-game",
  "title": "Example Game",
  "genre": "Puzzle",
  "homepage": "https://example.org/game",
  "builds": [
    {
      "version": "1.2.3",
      "kind": "upstream",
      "format": "tarball",
      "target": "Generic Linux AArch64 (glibc)",
      "url": "https://example.org/releases/v1.2.3",
      "evidence_url": "https://example.org/releases/v1.2.3",
      "last_checked": "2026-10-08",
      "device_tests": [],
      "notes": "Optional details about requirements or assets."
    }
  ]
}
```

The example above is **illustrative, not an actual submission**. Both `url` and `evidence_url` must be actual HTTPS links. `maintainer` is optional but strongly encouraged for credited community conversions. `notes` is optional. `device_tests` must be an array (empty is fine).

## Record a test separately

An ARM64 package listing establishes **availability**, not performance or compatibility. A `conversion` entry instead requires the **successful native execution of a user-produced build** and cannot imply the proprietary converted game is publicly downloadable. Only add `device_tests` when you ran that exact build on the named hardware/software. Include a link to a public GitHub issue or other reproducible report, and state whether it works, partially works, or fails.

```json
"device_tests": [
  {
    "device": "Steam Frame",
    "os": "SteamOS VR 0.x.y",
    "date": "2026-10-08",
    "result": "partial",
    "report_url": "https://github.com/owner/repository/issues/123"
  }
]
```

Include install method, display stack, graphics driver/runtime, launch command, and errors or limitations in the report. **Never fill in a device test from a guess.** The example above is not a verified test.

## What counts as native?

A Linux ELF `AArch64` executable running on the ARM CPU is native even if it is a community port or uses an ARM64 game engine/runtime with legitimately acquired, game-specific assets. The build's *origin* must still be identified. x86 executable translation is not native, even when the game happens to work great.

No game archives, unauthorized assets, cracks, or redistribution of copyrighted content in issues/PRs. Keep the catalog links and evidence clean.
