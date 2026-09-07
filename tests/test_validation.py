import importlib.util
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_plugin import inventory, release_files, validate
from build_bundle import build


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "plugin"
        for path in release_files(ROOT):
            dest = self.root / path.relative_to(ROOT)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, dest)

    def test_valid_release_and_line_endings(self):
        before = inventory(self.root)
        path = self.root / "README.md"
        path.write_bytes(path.read_bytes().replace(b"\r\n", b"\n").replace(b"\n", b"\r\n"))
        self.assertEqual(before, inventory(self.root))
        self.assertEqual(8, validate(self.root)["phaseCount"])

    def test_version_mismatch_is_rejected(self):
        path = self.root / ".claude-plugin/plugin.json"
        import json
        manifest = json.loads(path.read_text())
        manifest["version"] = "99.0.0"
        path.write_text(json.dumps(manifest), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "versions differ"):
            validate(self.root)

    def test_stale_readme_version_is_rejected(self):
        path = self.root / "README.md"
        path.write_text(path.read_text(encoding="utf-8").replace("`2.2.0`", "`0.0.0`"), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "README"):
            validate(self.root)

    def test_extra_discoverable_skill_is_rejected(self):
        path = self.root / "skills/extra/SKILL.md"
        path.parent.mkdir()
        path.write_text("---\nname: extra\ndescription: extra\n---\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "one public Router"):
            validate(self.root)

    def test_missing_resource_is_rejected(self):
        (self.root / "skills/ai-dev-protocol/phases/ai-handoff/PHASE.md").unlink()
        with self.assertRaisesRegex(ValueError, "unresolved"):
            validate(self.root)

    def test_link_cannot_escape_package(self):
        path = self.root / "skills/ai-dev-protocol/SKILL.md"
        with path.open("a", encoding="utf-8") as stream:
            stream.write("\n[escape](../../../outside.md)\n")
        with self.assertRaisesRegex(ValueError, "escaping"):
            validate(self.root)

    def test_phase_frontmatter_is_rejected(self):
        path = self.root / "skills/ai-dev-protocol/phases/ai-handoff/PHASE.md"
        path.write_text("---\nname: hidden\n---\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "frontmatter"):
            validate(self.root)

    def test_bundle_is_complete_and_does_not_overwrite(self):
        output = build(self.root, Path(self.temp.name) / "project")
        installed = output / "vendor/ai-dev-protocol"
        self.assertEqual(inventory(self.root), inventory(installed))
        self.assertTrue((output / ".cursor/rules/ai-dev-protocol.mdc").is_file())
        self.assertEqual(8, validate(installed)["phaseCount"])
        with self.assertRaisesRegex(ValueError, "already exists"):
            build(self.root, output)

    def test_bundle_cannot_be_created_inside_release_assets(self):
        with self.assertRaisesRegex(ValueError, "overlap"):
            build(self.root, self.root / "docs/project-bundle")

    def test_broken_installation_link_is_rejected(self):
        path = self.root / "README.md"
        with path.open("a", encoding="utf-8") as stream:
            stream.write("\n[missing](adapters/no-such-tool/install.md)\n")
        with self.assertRaisesRegex(ValueError, "unresolved"):
            validate(self.root)

    def test_symlinked_release_directory_is_rejected(self):
        directory = self.root / "docs"
        outside = Path(self.temp.name) / "outside-docs"
        directory.rename(outside)
        try:
            directory.symlink_to(outside, target_is_directory=True)
        except OSError:
            outside.rename(directory)
            self.skipTest("OS does not permit directory symlinks")
        with self.assertRaisesRegex(ValueError, "Linked release directory"):
            validate(self.root)


if __name__ == "__main__":
    unittest.main()
