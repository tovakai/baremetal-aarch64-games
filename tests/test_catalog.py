"""A small regression suite for catalog data validation."""

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from catalog import CatalogError, validate_catalog, render_catalog  # noqa: E402


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = json.loads((ROOT / "data" / "games.json").read_text(encoding="utf-8"))

    def fresh(self):
        return copy.deepcopy(self.original)

    def test_seed_is_valid(self):
        self.assertEqual(validate_catalog(self.fresh()), (5, 5))

    def test_generated_table_has_five_entries_and_no_fake_tests(self):
        result = render_catalog(self.fresh())
        self.assertEqual(result.count("[Published]("), 5)
        self.assertNotIn("Steam Frame: works", result)

    def test_rejects_duplicate_game_id(self):
        data = self.fresh()
        data["games"].append(copy.deepcopy(data["games"][0]))
        with self.assertRaisesRegex(CatalogError, "duplicate game id"):
            validate_catalog(data)

    def test_rejects_missing_evidence(self):
        data = self.fresh()
        data["games"][0]["builds"][0]["evidence_url"] = ""
        with self.assertRaisesRegex(CatalogError, "evidence_url"):
            validate_catalog(data)

    def test_rejects_invalid_dates(self):
        data = self.fresh()
        data["games"][0]["builds"][0]["last_checked"] = "2026-02-30"
        with self.assertRaisesRegex(CatalogError, "valid date"):
            validate_catalog(data)

    def test_rejects_unsubstantiated_device_tests(self):
        data = self.fresh()
        data["games"][0]["builds"][0]["device_tests"] = [{
            "device": "Steam Frame", "os": "SteamOS VR 0.4.2", "date": "2026-10-08", "result": "works"
        }]
        with self.assertRaisesRegex(CatalogError, "report_url"):
            validate_catalog(data)

    def test_rejects_invalid_build_origin(self):
        data = self.fresh()
        data["games"][0]["builds"][0]["kind"] = "official-ish"
        with self.assertRaisesRegex(CatalogError, "kind must be one of"):
            validate_catalog(data)


if __name__ == "__main__":
    unittest.main()
