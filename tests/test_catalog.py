"""A small regression suite for catalog data validation."""

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from catalog import (  # noqa: E402
    CatalogError, validate_catalog, render_catalog,
    load_directory_catalog, render_game_readme, sync_aggregate
)


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = json.loads((ROOT / "data" / "games.json").read_text(encoding="utf-8"))

    def fresh(self):
        return copy.deepcopy(self.original)

    def test_seed_is_valid(self):
        self.assertEqual(validate_catalog(self.fresh()), (126, 133))

    def test_generated_table_and_device_test_provenance(self):
        result = render_catalog(self.fresh())
        self.assertEqual(result.count("[Published]("), 119)
        self.assertEqual(result.count("[PortMaster package]("), 12)
        self.assertEqual(result.count("[Verified conversion]("), 2)
        self.assertIn("tovakai", result)
        self.assertNotIn("Tovakai (Anthon)", result)
        self.assertEqual(result.count("Steam Frame: works"), 4)

    def test_folder_data_rebuilds_aggregate(self):
        directory_data = load_directory_catalog()
        self.assertEqual(validate_catalog(directory_data), (126, 133))
        self.assertEqual(
            {g["id"] for g in directory_data["games"]},
            {g["id"] for g in self.original["games"]},
        )
        self.assertTrue(sync_aggregate(directory_data, write=False))

    def test_all_game_pages_match_metadata(self):
        for game in load_directory_catalog()["games"]:
            folder = ROOT / "games" / game["id"]
            self.assertEqual(
                (folder / "README.md").read_text(encoding="utf-8"),
                render_game_readme(game),
            )

    def test_reject_mismatched_folder_id(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / "different-id"
            folder.mkdir()
            (folder / "game.json").write_text(
                json.dumps(self.original["games"][0]), encoding="utf-8"
            )
            with self.assertRaisesRegex(CatalogError, "game id must exactly match directory"):
                load_directory_catalog(Path(tmp))

    def test_reject_folder_without_game_json(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "not-a-game").mkdir()
            with self.assertRaisesRegex(CatalogError, "missing game.json"):
                load_directory_catalog(Path(tmp))

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
