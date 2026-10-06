import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("installer", ROOT / "scripts/install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        self.source = ROOT / installer.NAME
        self.parent = self.base / "custom path" / "skills"

    def tearDown(self):
        self.tmp.cleanup()

    def test_install_complete_package(self):
        target, backup = installer.install(self.source, self.parent)
        self.assertIsNone(backup)
        self.assertEqual({str(p.relative_to(target)) for p in target.rglob("*") if p.is_file()}, set(installer.REQUIRED))
        for rel in installer.REQUIRED:
            self.assertEqual((target / rel).read_bytes(), (self.source / rel).read_bytes())

    def test_existing_install_untouched_without_update(self):
        target, _ = installer.install(self.source, self.parent)
        (target / "local-notes.txt").write_text("keep me")
        with self.assertRaises(FileExistsError):
            installer.install(self.source, self.parent)
        self.assertEqual((target / "local-notes.txt").read_text(), "keep me")

    def test_update_keeps_custom_files_in_backup(self):
        target, _ = installer.install(self.source, self.parent)
        (target / "local-notes.txt").write_text("keep me")
        _, backup = installer.install(self.source, self.parent, update=True)
        self.assertFalse(backup.is_relative_to(self.parent))
        self.assertEqual((backup / "local-notes.txt").read_text(), "keep me")
        self.assertFalse((target / "local-notes.txt").exists())

    def test_dry_run_changes_nothing(self):
        target, _ = installer.install(self.source, self.parent, dry_run=True)
        self.assertFalse(target.exists())
        self.assertFalse(self.parent.exists())

    def test_bad_source_does_not_disturb_install(self):
        target, _ = installer.install(self.source, self.parent)
        with self.assertRaises(ValueError):
            installer.install(self.base / "missing source", self.parent, update=True)
        self.assertTrue((target / "SKILL.md").is_file())

    def test_failed_copy_preserves_old_version(self):
        target, _ = installer.install(self.source, self.parent)
        before = (target / "SKILL.md").read_bytes()
        with patch.object(installer.shutil, "copy2", side_effect=OSError("copy failed")):
            with self.assertRaises(OSError):
                installer.install(self.source, self.parent, update=True)
        self.assertEqual((target / "SKILL.md").read_bytes(), before)
        self.assertFalse(list(self.parent.glob(".full-build-blueprint-*")))

    def test_failed_activation_restores_old_version(self):
        target, _ = installer.install(self.source, self.parent)
        (target / "local-notes.txt").write_text("keep me")
        real_rename = Path.rename
        def fail_staging(path, destination):
            if path.name.startswith(".full-build-blueprint-"):
                raise OSError("activation failed")
            return real_rename(path, destination)
        with patch.object(Path, "rename", fail_staging):
            with self.assertRaises(OSError):
                installer.install(self.source, self.parent, update=True)
        self.assertEqual((target / "local-notes.txt").read_text(), "keep me")


if __name__ == "__main__":
    unittest.main()
