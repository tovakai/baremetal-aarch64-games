## Summary

Which `games/<slug>/game.json` file(s) changed, and why?

## Evidence

Link a published Linux AArch64 binary/package listing (not source-only or x86 emulation):

## Validation

- [ ] Canonical game.json updated; generated catalog files not hand-edited
- [ ] `python3 scripts/catalog.py --write`
- [ ] `python3 scripts/catalog.py --check`
- [ ] `python3 -m unittest discover -s tests`
- [ ] Device tests (if any) have dated, reproducible report URLs
- [ ] No proprietary game files added
