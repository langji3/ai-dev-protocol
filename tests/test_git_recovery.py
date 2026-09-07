"""Exercise raw Git recovery fixtures, not a simulated agent implementation."""
from pathlib import Path
import subprocess
import tempfile
import unittest


class GitRecoveryFixtures(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        self.root.mkdir()
        self.git("init", "-b", "developer/lin")
        self.git("config", "user.name", "Fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        (self.root / "app.txt").write_text("base\n")
        self.git("add", ".")
        self.git("commit", "-m", "base")
        self.base = self.git("rev-parse", "HEAD")

    def git(self, *args, cwd=None):
        path = cwd or self.root
        result = subprocess.run(["git", "-c", f"safe.directory={path}", *args],
                                cwd=path, check=True, capture_output=True, text=True)
        return result.stdout.strip()

    def test_independent_worktree_and_advanced_target_combination(self):
        ai = Path(self.temp.name) / "ai"
        self.git("worktree", "add", "-b", "ai/fixture", str(ai), self.base)
        (ai / "feature.txt").write_text("new feature\n")
        self.git("add", ".", cwd=ai)
        self.git("commit", "-m", "feature", cwd=ai)
        (self.root / "team.txt").write_text("teammate\n")
        self.git("add", ".")
        self.git("commit", "-m", "target advanced")
        target = self.git("rev-parse", "HEAD")
        self.assertNotEqual(self.base, target)
        self.git("merge", "--no-edit", "developer/lin", cwd=ai)
        self.assertTrue((ai / "feature.txt").exists())
        self.assertTrue((ai / "team.txt").exists())
        self.assertEqual(target, self.git("rev-parse", "HEAD"))
        self.assertFalse((self.root / "feature.txt").exists())

    def test_integration_conflict_stays_in_isolated_worktree(self):
        ai = Path(self.temp.name) / "ai-conflict"
        self.git("worktree", "add", "-b", "ai/conflict", str(ai), self.base)
        (ai / "app.txt").write_text("AI change\n")
        self.git("add", ".", cwd=ai)
        self.git("commit", "-m", "AI change", cwd=ai)
        (self.root / "app.txt").write_text("Developer change\n")
        self.git("add", ".")
        self.git("commit", "-m", "Developer change")
        target = self.git("rev-parse", "HEAD")
        with self.assertRaises(subprocess.CalledProcessError):
            self.git("merge", "--no-edit", "developer/lin", cwd=ai)
        self.assertIn("UU app.txt", self.git("status", "--porcelain", cwd=ai))
        self.assertEqual("", self.git("status", "--porcelain"))
        self.assertEqual(target, self.git("rev-parse", "HEAD"))
        self.assertEqual("Developer change\n", (self.root / "app.txt").read_text())

    def test_changed_spec_blob_is_detectable_after_resume(self):
        spec = self.root / "docs/specs/order.md"
        spec.parent.mkdir(parents=True)
        spec.write_text("Only add filtering\n")
        self.git("add", ".")
        self.git("commit", "-m", "reviewed spec")
        reviewed = self.git("rev-parse", "HEAD:docs/specs/order.md")
        spec.write_text("Add filtering and remove auth\n")
        self.git("add", ".")
        self.git("commit", "-m", "changed spec")
        self.assertNotEqual(reviewed, self.git("rev-parse", "HEAD:docs/specs/order.md"))


if __name__ == "__main__":
    unittest.main()
