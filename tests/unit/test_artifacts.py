"""Unit tests for artifact manifest generation and verification framework."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

# Add project root to sys.path
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT_DIR))

from artifacts.generation.base import SyntheticSampleGenerator
from artifacts.generation.manifest import (
    ArtifactRecord,
    PathTraversalError,
    compute_sha256,
    generate_manifest,
    load_manifest,
    save_manifest,
    validate_safe_path,
    verify_manifest,
)


class TestArtifactManifest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.base_dir = Path(self.temp_dir.name).resolve()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_compute_sha256(self) -> None:
        sample_file = self.base_dir / "test.txt"
        sample_file.write_text("DEAD AIR TRANSMISSION TEST\n", encoding="utf-8")
        h = compute_sha256(sample_file)
        self.assertEqual(len(h), 64)
        # Verify idempotency
        self.assertEqual(h, compute_sha256(sample_file))

    def test_validate_safe_path_valid(self) -> None:
        safe_rel = "stage01/audio/broadcast.wav"
        resolved = validate_safe_path(self.base_dir, safe_rel)
        expected = (self.base_dir / safe_rel).resolve()
        self.assertEqual(resolved, expected)

    def test_validate_safe_path_rejects_absolute(self) -> None:
        with self.assertRaises(PathTraversalError):
            validate_safe_path(self.base_dir, "/etc/passwd")

    def test_validate_safe_path_rejects_parent_traversal(self) -> None:
        with self.assertRaises(PathTraversalError):
            validate_safe_path(self.base_dir, "../escaped.txt")

        with self.assertRaises(PathTraversalError):
            validate_safe_path(self.base_dir, "sub/../../escaped.txt")

    def test_validate_safe_path_rejects_windows_traversal(self) -> None:
        with self.assertRaises(PathTraversalError):
            validate_safe_path(self.base_dir, "..\\escaped.txt")

    def test_generate_and_save_manifest_deterministic(self) -> None:
        file1 = self.base_dir / "file_b.txt"
        file2 = self.base_dir / "file_a.txt"
        file1.write_text("B content", encoding="utf-8")
        file2.write_text("A content", encoding="utf-8")

        manifest = generate_manifest(self.base_dir, scan_directory=True)
        manifest_file = self.base_dir / "artifacts.manifest.json"
        save_manifest(manifest, manifest_file)

        loaded = load_manifest(manifest_file)
        self.assertEqual(loaded["version"], "1.0.0")
        self.assertEqual(len(loaded["artifacts"]), 2)
        # Must be sorted by path deterministically
        self.assertEqual(loaded["artifacts"][0]["path"], "file_a.txt")
        self.assertEqual(loaded["artifacts"][1]["path"], "file_b.txt")

    def test_verification_success(self) -> None:
        gen = SyntheticSampleGenerator()
        records = gen.generate(self.base_dir, seed=42)
        manifest = generate_manifest(self.base_dir, artifacts=records)
        manifest_file = self.base_dir / "artifacts.manifest.json"
        save_manifest(manifest, manifest_file)

        result = verify_manifest(manifest_file, self.base_dir)
        self.assertTrue(result.is_valid)
        self.assertEqual(result.matched_count, 1)
        self.assertEqual(result.checked_count, 1)
        self.assertEqual(len(result.missing), 0)
        self.assertEqual(len(result.mismatched), 0)
        self.assertEqual(len(result.unsafe_paths), 0)

    def test_verification_fails_on_missing_file(self) -> None:
        gen = SyntheticSampleGenerator()
        records = gen.generate(self.base_dir, seed=42)
        manifest = generate_manifest(self.base_dir, artifacts=records)
        manifest_file = self.base_dir / "artifacts.manifest.json"
        save_manifest(manifest, manifest_file)

        # Remove the generated file
        target_file = self.base_dir / records[0].path
        target_file.unlink()

        result = verify_manifest(manifest_file, self.base_dir)
        self.assertFalse(result.is_valid)
        self.assertIn(records[0].path, result.missing)

    def test_verification_fails_on_modified_content(self) -> None:
        gen = SyntheticSampleGenerator()
        records = gen.generate(self.base_dir, seed=42)
        manifest = generate_manifest(self.base_dir, artifacts=records)
        manifest_file = self.base_dir / "artifacts.manifest.json"
        save_manifest(manifest, manifest_file)

        # Modify the generated file
        target_file = self.base_dir / records[0].path
        target_file.write_text("TAMPERED CONTENT", encoding="utf-8")

        result = verify_manifest(manifest_file, self.base_dir)
        self.assertFalse(result.is_valid)
        self.assertEqual(len(result.mismatched), 1)
        self.assertEqual(result.mismatched[0]["path"], records[0].path)

    def test_verification_detects_path_traversal(self) -> None:
        manifest_data = {
            "version": "1.0.0",
            "artifacts": [
                {
                    "path": "../../secret.txt",
                    "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
                    "size_bytes": 10,
                }
            ],
        }
        manifest_file = self.base_dir / "artifacts.manifest.json"
        save_manifest(manifest_data, manifest_file)

        result = verify_manifest(manifest_file, self.base_dir)
        self.assertFalse(result.is_valid)
        self.assertIn("../../secret.txt", result.unsafe_paths)

    def test_reproducibility(self) -> None:
        with tempfile.TemporaryDirectory() as dir1, tempfile.TemporaryDirectory() as dir2:
            p1 = Path(dir1)
            p2 = Path(dir2)

            gen = SyntheticSampleGenerator()
            rec1 = gen.generate(p1, seed=9999)
            rec2 = gen.generate(p2, seed=9999)

            m1 = generate_manifest(p1, artifacts=rec1)
            m2 = generate_manifest(p2, artifacts=rec2)

            self.assertEqual(m1, m2)
            content1 = (p1 / rec1[0].path).read_bytes()
            content2 = (p2 / rec2[0].path).read_bytes()
            self.assertEqual(content1, content2)

    def test_cli_scripts_execution(self) -> None:
        gen_script = ROOT_DIR / "scripts" / "generate_artifacts.py"
        ver_script = ROOT_DIR / "scripts" / "verify_artifacts.py"

        # 1. Run generate_artifacts.py
        cmd_gen = [
            sys.executable,
            str(gen_script),
            "--output-dir",
            str(self.base_dir),
            "--seed",
            "1234",
        ]
        proc_gen = subprocess.run(cmd_gen, capture_output=True, text=True)
        self.assertEqual(proc_gen.returncode, 0, msg=proc_gen.stderr)
        self.assertTrue((self.base_dir / "artifacts.manifest.json").exists())

        # 2. Run verify_artifacts.py -> expected 0
        cmd_ver = [
            sys.executable,
            str(ver_script),
            "--manifest",
            str(self.base_dir / "artifacts.manifest.json"),
            "--target-dir",
            str(self.base_dir),
        ]
        proc_ver = subprocess.run(cmd_ver, capture_output=True, text=True)
        self.assertEqual(proc_ver.returncode, 0, msg=proc_ver.stderr)
        self.assertIn("[OK] Verification succeeded", proc_ver.stdout)

        # 3. Modify artifact and run verify_artifacts.py -> expected 1 (fail)
        sample_file = self.base_dir / "00-bootstrap" / "sample_signal.txt"
        sample_file.write_text("CORRUPTED", encoding="utf-8")
        proc_ver_fail = subprocess.run(cmd_ver, capture_output=True, text=True)
        self.assertEqual(proc_ver_fail.returncode, 1)
        self.assertIn("[FAIL] Artifact verification failed!", proc_ver_fail.stderr)


if __name__ == "__main__":
    unittest.main()
