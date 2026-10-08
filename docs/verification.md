# Native AArch64 verification and device reports

## Evidence tiers

1. **Architecture listed:** an official or distro release lists a Linux `aarch64` / `arm64` build. This is sufficient for a `builds` entry when the listing identifies an actual published binary package. This is **not** an execution test.
2. **Binary inspected:** a downloaded executable is confirmed as Linux AArch64 by `file` and/or `readelf`. Mention this in the report, including source URL and version.
3. **Conversion verified:** a user-owned game is converted with a documented AArch64-native engine/runtime, with a version-specific test showing **actual gameplay** (not just detection or package output). Link the converter/recipe and the report; do not host commercial game assets.
4. **Device tested:** that exact build is run on identified hardware and OS, with result and reproduction details. Only this level earns a `Tested` label in the catalog.

Do not silently promote a build from tier 1 to tier 3. A community build can be just as native as an upstream build, but record its maintainer and whether an artifact is actually distributed versus locally generated. A *verified conversion* does not imply a publicly available game download.

## Inspect a Linux binary

```sh
file ./game-binary
readelf -h ./game-binary | grep -E 'Class:|Machine:'
# Expected ELF64 and Machine: AArch64, not x86-64.

# When troubleshooting native library dependencies:
readelf -d ./game-binary | grep NEEDED
```

Archives may contain launcher scripts and multiple binaries: inspect the actual executable. `file` can also identify non-Linux formats, such as Windows PE or Android-only executables. Shared libraries and runtime dependencies may still prevent a native AArch64 game from running on another distro.

## Device test checklist

- **Exact build:** release/version, URL, origin, installation method, and any checksums you have.
- **System:** device, OS version, GPU driver, display server/compositor, and runtime/container if relevant.
- **Launch:** precise command or Steam shortcut/launch options; controller/input setup if relevant.
- **Result:** `works`, `partial`, or `broken` with reproducible symptoms, logs/screenshots where appropriate, and date.
- **Restrictions:** missing assets, network login, DRM, performance, VR-vs-2D expectations, audio or video bugs.

Create a GitHub issue containing the report, then add its link in `device_tests[].report_url` in the JSON. Never label a title Steam Frame-compatible merely because its CPU instruction set matches.

**Safety:** Don't execute untrusted binaries as root or upload proprietary game files while collecting evidence.
