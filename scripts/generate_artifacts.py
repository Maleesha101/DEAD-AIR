#!/usr/bin/env python3
"""CLI tool to deterministically generate campaign artifacts and emit SHA-256 manifest."""

import argparse
import sys
from pathlib import Path

# Add project root to sys.path so we can import artifacts package
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from artifacts.generation.base import GeneratorRegistry, SyntheticSampleGenerator
from artifacts.generation.manifest import generate_manifest, save_manifest


def build_default_registry() -> GeneratorRegistry:
    registry = GeneratorRegistry()
    registry.register(SyntheticSampleGenerator())
    return registry


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deterministically generate campaign artifacts and SHA-256 manifest."
    )
    parser.add_argument(
        "--output-dir",
        "-o",
        type=Path,
        required=True,
        help="Target directory where artifacts will be generated.",
    )
    parser.add_argument(
        "--seed",
        "-s",
        type=int,
        default=1337,
        help="Deterministic generation seed (default: 1337).",
    )
    parser.add_argument(
        "--manifest-filename",
        "-m",
        type=str,
        default="artifacts.manifest.json",
        help="Name of the manifest file to write (default: artifacts.manifest.json).",
    )
    parser.add_argument(
        "--scan-existing",
        action="store_true",
        help="Scan and hash pre-existing files in output-dir instead of running generators.",
    )

    args = parser.parse_args()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.scan_existing:
        print(f"[*] Scanning pre-existing files in {output_dir}...")
        manifest_data = generate_manifest(output_dir, scan_directory=True)
    else:
        print(f"[*] Generating synthetic artifacts in {output_dir} with seed {args.seed}...")
        registry = build_default_registry()
        records = registry.generate_all(output_dir, seed=args.seed)
        manifest_data = generate_manifest(output_dir, artifacts=records)

    manifest_path = output_dir / args.manifest_filename
    save_manifest(manifest_data, manifest_path)
    count = len(manifest_data.get("artifacts", []))
    print(f"[OK] Generated {count} artifact record(s). Manifest written to {manifest_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
