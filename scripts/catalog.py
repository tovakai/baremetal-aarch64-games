#!/usr/bin/env python3
"""Validate the JSON catalog and render its README table (stdlib only)."""

from __future__ import annotations

import argparse
import datetime as dt
import difflib
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "games.json"
README = ROOT / "README.md"
START = "<!-- catalog:start -->"
END = "<!-- catalog:end -->"
KINDS = {"upstream", "community", "distribution"}
FORMATS = {"deb", "rpm", "flatpak", "appimage", "tarball", "standalone", "other", "steam", "conversion"}
RESULTS = {"works", "partial", "broken"}
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


class CatalogError(ValueError):
    """Invalid catalog data or generated README."""


def require(condition: bool, location: str, explanation: str) -> None:
    if not condition:
        raise CatalogError(f"{location}: {explanation}")


def fields(obj: object, location: str, required: set[str], optional: set[str] = frozenset()) -> dict:
    require(isinstance(obj, dict), location, "must be an object")
    missing = required - obj.keys()
    extra = obj.keys() - required - optional
    require(not missing, location, f"missing keys: {', '.join(sorted(missing))}")
    require(not extra, location, f"unknown keys: {', '.join(sorted(extra))}")
    return obj


def text_field(obj: dict, key: str, location: str) -> str:
    value = obj[key]
    require(isinstance(value, str) and bool(value.strip()), location, f"{key} must be a non-empty string")
    require(value == value.strip(), location, f"{key} has surrounding whitespace")
    return value


def https_field(obj: dict, key: str, location: str) -> None:
    value = text_field(obj, key, location)
    url = urlsplit(value)
    require(url.scheme == "https" and bool(url.netloc) and not url.username and not url.password,
            location, f"{key} must be an HTTPS URL without credentials")
    require(not any(c.isspace() for c in value), location, f"{key} contains whitespace")


def date_field(obj: dict, key: str, location: str) -> None:
    value = text_field(obj, key, location)
    require(bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", value)), location, f"{key} must use YYYY-MM-DD")
    try:
        dt.date.fromisoformat(value)
    except ValueError as exc:
        raise CatalogError(f"{location}: {key} must be a valid date") from exc


def validate_catalog(data: object) -> tuple[int, int]:
    root = fields(data, "catalog", {"schema_version", "games"})
    require(type(root["schema_version"]) is int and root["schema_version"] == 1,
            "catalog", "unsupported schema_version (expected 1)")
    games = root["games"]
    require(isinstance(games, list), "catalog.games", "must be an array")
    ids: set[str] = set()
    build_count = 0
    for i, item in enumerate(games):
        loc = f"games[{i}]"
        game = fields(item, loc, {"id", "title", "genre", "homepage", "builds"})
        game_id = text_field(game, "id", loc)
        require(bool(SLUG.fullmatch(game_id)), loc, "id must be a lower-case hyphenated slug")
        require(game_id not in ids, loc, f"duplicate game id '{game_id}'")
        ids.add(game_id)
        text_field(game, "title", loc)
        text_field(game, "genre", loc)
        https_field(game, "homepage", loc)
        builds = game["builds"]
        require(isinstance(builds, list) and len(builds) > 0, loc, "builds must be a non-empty array")
        seen_builds: set[tuple[str, str, str, str]] = set()
        for j, b in enumerate(builds):
            where = f"{loc}.builds[{j}]"
            build = fields(b, where,
                           {"version", "kind", "format", "target", "url", "evidence_url", "last_checked", "device_tests"},
                           {"notes", "maintainer"})
            for key in ("version", "kind", "format", "target"):
                text_field(build, key, where)
            require(build["kind"] in KINDS, where, f"kind must be one of {sorted(KINDS)}")
            require(build["format"] in FORMATS, where, f"format must be one of {sorted(FORMATS)}")
            for key in ("url", "evidence_url"):
                https_field(build, key, where)
            date_field(build, "last_checked", where)
            if "notes" in build:
                require(isinstance(build["notes"], str), where, "notes must be a string")
            if "maintainer" in build:
                text_field(build, "maintainer", where)
            fingerprint = tuple(build[k] for k in ("version", "kind", "format", "target"))
            require(fingerprint not in seen_builds, where, "duplicate build identity")
            seen_builds.add(fingerprint)
            tests = build["device_tests"]
            require(isinstance(tests, list), where, "device_tests must be an array")
            for k, t in enumerate(tests):
                test_where = f"{where}.device_tests[{k}]"
                test = fields(t, test_where, {"device", "os", "date", "result", "report_url"})
                for key in ("device", "os", "result"):
                    text_field(test, key, test_where)
                require(test["result"] in RESULTS, test_where, f"result must be one of {sorted(RESULTS)}")
                date_field(test, "date", test_where)
                https_field(test, "report_url", test_where)
            build_count += 1
    return len(games), build_count


def md(value: str) -> str:
    """Escape untrusted catalog labels in a Markdown table."""
    return (value.replace("\\", "\\\\").replace("|", "\\|")
            .replace("[", "\\[").replace("]", "\\]")
            .replace("\n", " ").replace("\r", " "))


def render_catalog(data: dict) -> str:
    game_count, build_count = validate_catalog(data)
    lines = [
        f"**{game_count} games · {build_count} native AArch64 builds cataloged**",
        "",
        "| Game | Genre | Version | Origin · Format | Target | ARM64 evidence | Device tests |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for game in sorted(data["games"], key=lambda g: g["title"].casefold()):
        for build in sorted(game["builds"], key=lambda b: (b["target"], b["version"])):
            title = f"[{md(game['title'])}]({game['homepage']})"
            source = f"[{md(build['kind'].title())} · {md(build['format'])}]({build['url']})"
            if build.get("maintainer"):
                source += f" · {md(build['maintainer'])}"
            label = "Verified conversion" if build["format"] == "conversion" else "Published"
            evidence = f"[{label}]({build['evidence_url']})"
            test_info = ", ".join(
                f"[{md(t['device'])}: {md(t['result'])}]({t['report_url']})"
                for t in build["device_tests"]
            ) or "—"
            lines.append(f"| {title} | {md(game['genre'])} | {md(build['version'])} | {source} | "
                         f"{md(build['target'])} | {evidence} | {test_info} |")
    return "\n".join(lines)


def sync_readme(data: dict, write: bool) -> bool:
    content = README.read_text(encoding="utf-8")
    require(content.count(START) == 1 and content.count(END) == 1,
            "README.md", "catalog markers must appear exactly once")
    pattern = re.compile(re.escape(START) + r"\n.*?" + re.escape(END), re.DOTALL)
    require(bool(pattern.search(content)), "README.md", "catalog markers must be on separate lines and ordered")
    desired = START + "\n" + render_catalog(data) + "\n" + END
    updated = pattern.sub(lambda _: desired, content, count=1)
    if updated == content:
        return True
    if write:
        README.write_text(updated, encoding="utf-8")
        return True
    print("README catalog is not in sync. Run: python3 scripts/catalog.py --write", file=sys.stderr)
    print("".join(difflib.unified_diff(content.splitlines(keepends=True), updated.splitlines(keepends=True),
                                      fromfile="README.md", tofile="README.md (generated)")), file=sys.stderr)
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_mutually_exclusive_group(required=True)
    actions.add_argument("--write", action="store_true", help="validate JSON and refresh README table")
    actions.add_argument("--check", action="store_true", help="validate JSON and check README table")
    args = parser.parse_args()
    try:
        data = json.loads(DATA.read_text(encoding="utf-8"))
        counts = validate_catalog(data)
        if not sync_readme(data, write=args.write):
            return 1
    except (CatalogError, json.JSONDecodeError, OSError) as exc:
        print(f"Catalog validation error: {exc}", file=sys.stderr)
        return 1
    print(f"Catalog valid; README synchronized ({counts[0]} games, {counts[1]} builds).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
