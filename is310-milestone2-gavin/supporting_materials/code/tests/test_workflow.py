"""Meaningful checks for math, sample selection, preservation and review gates."""
import csv
import math
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from project import ROOT, build_rows, inputs, keyed, read_csv, select, spearman, write_csv


class WorkflowTests(unittest.TestCase):
    def test_sample_is_order_invariant_and_ignores_outcomes(self):
        players, _, _ = inputs()
        expected = [p["id"] for p in select(players)]
        altered = [dict(p, goals_scored="999", expected_goals="999") for p in reversed(players)]
        self.assertEqual(expected, [p["id"] for p in select(altered)])
        self.assertEqual(Counter(p["element_type"] for p in select(players)), {"2": 20, "3": 20, "4": 20})

    def test_independent_per90_calculation_and_source_link(self):
        rows = keyed(build_rows(), "fpl_id")
        players, _, _ = inputs()
        source = keyed(players, "id")["351"]
        row = rows["351"]
        self.assertEqual(row["player_name"], "Erling Haaland")
        self.assertEqual(row["ea_id"], "239085")
        self.assertTrue(math.isclose(row["goals_p90"], int(source["goals_scored"]) / (int(source["minutes"]) / 90), abs_tol=0.00000051))

    def test_tied_spearman_and_constant_series(self):
        self.assertAlmostEqual(spearman([1, 2, 2, 4], [4, 3, 3, 1]), -1)
        self.assertIsNone(spearman([2, 2, 2], [1, 2, 3]))
        self.assertIsNone(spearman([1, 2], [2, 1]))

    def test_duplicate_identity_key_is_rejected(self):
        with self.assertRaises(ValueError):
            keyed([{"id": "1"}, {"id": "1"}], "id")

    def test_no_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "review.csv"
            write_csv(target, [{"id": "1", "note": "original"}])
            original = target.read_bytes()
            with self.assertRaises(FileExistsError):
                write_csv(target, [{"id": "2", "note": "replacement"}])
            self.assertEqual(target.read_bytes(), original)

    def test_candidate_validation_and_final_gate(self):
        candidate = subprocess.run([sys.executable, str(ROOT / "supporting_materials/code/validate.py")], capture_output=True, text=True)
        self.assertEqual(candidate.returncode, 0, candidate.stdout + candidate.stderr)
        final = subprocess.run([sys.executable, str(ROOT / "supporting_materials/code/validate.py"), "--final"], capture_output=True, text=True)
        self.assertEqual(final.returncode, 1)
        self.assertIn("NOT READY", final.stdout)

    def test_tampered_output_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            rows = read_csv(ROOT / "dataset.csv")
            rows[0]["minutes"] = "9999"
            target = Path(directory) / "tampered.csv"
            write_csv(target, rows)
            result = subprocess.run([sys.executable, str(ROOT / "supporting_materials/code/validate.py"), "--dataset", str(target)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn("stale or altered minutes", result.stdout)


if __name__ == "__main__":
    unittest.main()
