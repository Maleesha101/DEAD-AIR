#!/usr/bin/env python3
"""CLI tool to verify campaign artifact integrity against an artifact manifest."""

import argparse
import sys
from pathlib import Path

# Add project root to sys.path so we can import artifacts package
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from artifacts.generation.manifest import verify_manifest


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify SHA-256 hashes and file integrity from an artifact manifest."
    )
    parser.add_argument(
        "--manifest",
        "-m",
        type=Path,
        required=True,
        help="Path to the JSON artifact manifest file.",
    )
    parser.add_argument(
        "--target-dir",
        "-d",
        type=Path,
        default=None,
        help="Base directory containing the artifacts (defaults to the manifest's parent directory).",
    )
    parser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        help="Suppress output except for errors.",
    )

    args = parser.parse_args()

    manifest_path = args.manifest.resolve()
    target_dir = (args.target_dir or manifest_path.parent).resolve()

    if not manifest_path.is_file():
        print(f"[ERROR] Manifest file does not exist: {manifest_path}", file=sys.stderr)
        return 2

    if not target_dir.is_dir():
        print(f"[ERROR] Target artifacts directory does not exist: {target_dir}", file=sys.stderr)
        return 2

    result = verify_manifest(manifest_path, target_dir)

    if result.is_valid:
        if not args.quiet:
            print(f"[OK] Verification succeeded: {result.matched_count}/{result.checked_count} artifact(s) match.")
        return 0

    print("[FAIL] Artifact verification failed!", file=sys.stderr)
    if result.errors:
        print("\nErrors:", file=sys.stderr)
        for err in result.errors:
            print(f"  - {err}", file=sys.stderr)

    if result.unsafe_paths:
        print("\nUnsafe / Path Traversal Attempts:", file=sys.stderr)
        for unsafe in result.unsafe_paths:
            print(f"  - {unsafe}", file=sys.stderr)

    if result.missing:
        print(f"\nMissing Files ({len(result.missing)}):", file=sys.stderr)
        for missing in result.missing:
            print(f"  - {missing}", file=sys.stderr)

    if result.mismatched:
        print(f"\nHash Mismatches ({len(result.mismatched)}):", file=sys.stderr)
        for item in result.mismatched:
            print(f"  - {item['path']}:", file=sys.stderr)
            print(f"      Expected: {item['expected_sha256']}", file=sys.stderr)
            print(f"      Actual:   {item['actual_sha256']}", file=sys.stderr)

    return 1


if __name__ == "__main__":
    sys.exit(main())
