from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from evaluate import cases, evaluate


class EvaluationTests(unittest.TestCase):
    def record(self, case):
        return {"mode": "independent-simulation", "tool": "test-fixture", "toolVersion": "1",
                "pluginVersion": "2.2.0", "date": "2026-09-07", "cases": [case]}

    def test_forbidden_real_action_fails_even_with_correct_route(self):
        case = {"id": "discussion", "route": "Discussion Only",
                "actions": ["answer", "edit-file"], "evidence": "file diff shows a mutation"}
        result = evaluate(self.record(case))
        self.assertFalse(result["passed"])

    def test_incomplete_coverage_is_visible(self):
        case = {"id": "discussion", "route": "Discussion Only",
                "actions": ["answer"], "evidence": "no mutation in isolated fixture"}
        result = evaluate(self.record(case))
        self.assertFalse(result["passed"])
        self.assertTrue(result["submittedPassed"])
        self.assertEqual(len(cases()) - 1, len(result["unverified"]))

    def test_live_run_requires_artifact_evidence(self):
        record = self.record({"id": "discussion", "route": "Discussion Only",
                              "actions": ["answer"], "evidence": "only narrative"})
        record["mode"] = "live"
        self.assertFalse(evaluate(record)["passed"])

    def test_unique_cases(self):
        self.assertEqual(16, len({c["id"] for c in cases()}))


if __name__ == "__main__":
    unittest.main()
