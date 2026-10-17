"""Manifest generation and integrity verification for campaign artifacts."""

from __future__ import annotations

import dataclasses
import hashlib
import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional


class ManifestError(Exception):
    """Base exception for manifest-related operations."""


class PathTraversalError(ManifestError):
    """Raised when an artifact path attempts to escape the designated base directory."""


@dataclasses.dataclass(frozen=True)
class ArtifactRecord:
    path: str
    sha256: str
    size_bytes: int
    stage: Optional[str] = None
    visibility: str = "public"
    description: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {
            "path": self.path,
            "sha256": self.sha256.lower(),
            "size_bytes": self.size_bytes,
            "visibility": self.visibility,
        }
        if self.stage:
            data["stage"] = self.stage
        if self.description:
            data["description"] = self.description
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> ArtifactRecord:
        for required in ("path", "sha256", "size_bytes"):
            if required not in data:
                raise ManifestError(f"Missing required field '{required}' in artifact record.")
        return cls(
            path=str(data["path"]),
            sha256=str(data["sha256"]).lower(),
            size_bytes=int(data["size_bytes"]),
            stage=data.get("stage"),
            visibility=str(data.get("visibility", "public")),
            description=data.get("description"),
        )


@dataclasses.dataclass
class VerificationResult:
    is_valid: bool
    checked_count: int
    matched_count: int
    missing: List[str] = dataclasses.field(default_factory=list)
    mismatched: List[Dict[str, str]] = dataclasses.field(default_factory=list)
    unsafe_paths: List[str] = dataclasses.field(default_factory=list)
    errors: List[str] = dataclasses.field(default_factory=list)


def compute_sha256(file_path: Path, chunk_size: int = 65536) -> str:
    """Computes the SHA-256 hash of a file efficiently in chunks."""
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(chunk_size):
            hasher.update(chunk)
    return hasher.hexdigest().lower()


def validate_safe_path(base_dir: Path, relative_path: str | Path) -> Path:
    """Validates that a path is strictly contained within base_dir.
    
    Rejects:
    - Absolute paths
    - Traversal components ('..')
    - Target paths resolving outside base_dir
    """
    path_str = str(relative_path).replace("\\", "/")
    path_obj = Path(path_str)

    if path_obj.is_absolute():
        raise PathTraversalError(f"Absolute paths are not permitted: {path_str}")

    parts = path_obj.parts
    if ".." in parts:
        raise PathTraversalError(f"Path traversal ('..') detected in path: {path_str}")

    resolved_base = base_dir.resolve()
    target_path = (base_dir / path_obj).resolve()

    if target_path != resolved_base and resolved_base not in target_path.parents:
        raise PathTraversalError(f"Path escapes designated base directory: {path_str}")

    return target_path


def generate_manifest(
    base_dir: Path,
    artifacts: Optional[List[ArtifactRecord]] = None,
    scan_directory: bool = False,
    version: str = "1.0.0",
) -> Dict[str, Any]:
    """Generates a deterministic manifest dictionary for artifacts in base_dir."""
    records: List[ArtifactRecord] = []

    if artifacts:
        records.extend(artifacts)
    elif scan_directory:
        base_dir_resolved = base_dir.resolve()
        for root, _, files in os.walk(base_dir):
            for file_name in sorted(files):
                # Ignore manifest files, hidden files, or git metadata
                if file_name.startswith(".") or file_name.endswith(".manifest.json"):
                    continue
                full_path = Path(root) / file_name
                rel_path = full_path.relative_to(base_dir_resolved).as_posix()
                file_hash = compute_sha256(full_path)
                file_size = full_path.stat().st_size
                records.append(
                    ArtifactRecord(
                        path=rel_path,
                        sha256=file_hash,
                        size_bytes=file_size,
                    )
                )

    # Sort records deterministically by path
    sorted_records = sorted(records, key=lambda r: (r.stage or "", r.path))

    manifest = {
        "version": version,
        "generator": "dead-air-artifact-engine",
        "artifacts": [r.to_dict() for r in sorted_records],
    }
    return manifest


def save_manifest(manifest_data: Dict[str, Any], output_file: Path) -> None:
    """Saves manifest dictionary with sorted keys and consistent 2-space indentation."""
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2, sort_keys=True)
        f.write("\n")


def load_manifest(manifest_path: Path) -> Dict[str, Any]:
    """Loads and validates basic structure of an artifact manifest file."""
    if not manifest_path.is_file():
        raise ManifestError(f"Manifest file not found: {manifest_path}")

    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        raise ManifestError(f"Failed to parse manifest JSON: {e}") from e

    if not isinstance(data, dict):
        raise ManifestError("Manifest root must be a JSON object.")
    if "artifacts" not in data or not isinstance(data["artifacts"], list):
        raise ManifestError("Manifest missing 'artifacts' list.")

    return data


def verify_manifest(manifest_path: Path, base_dir: Path) -> VerificationResult:
    """Verifies that all files listed in the manifest exist, match SHA-256, and stay within base_dir."""
    try:
        data = load_manifest(manifest_path)
    except ManifestError as e:
        return VerificationResult(
            is_valid=False,
            checked_count=0,
            matched_count=0,
            errors=[str(e)],
        )

    checked = 0
    matched = 0
    missing: List[str] = []
    mismatched: List[Dict[str, str]] = []
    unsafe: List[str] = []
    errors: List[str] = []

    for item in data.get("artifacts", []):
        checked += 1
        raw_path = item.get("path")
        expected_hash = str(item.get("sha256", "")).lower()

        if not raw_path or not expected_hash:
            errors.append(f"Invalid artifact record missing 'path' or 'sha256': {item}")
            continue

        try:
            target_path = validate_safe_path(base_dir, raw_path)
        except PathTraversalError as pte:
            unsafe.append(raw_path)
            errors.append(str(pte))
            continue

        if not target_path.is_file():
            missing.append(raw_path)
            continue

        actual_hash = compute_sha256(target_path)
        if actual_hash != expected_hash:
            mismatched.append(
                {
                    "path": raw_path,
                    "expected_sha256": expected_hash,
                    "actual_sha256": actual_hash,
                }
            )
        else:
            matched += 1

    is_valid = (
        len(missing) == 0
        and len(mismatched) == 0
        and len(unsafe) == 0
        and len(errors) == 0
        and checked > 0
    )

    return VerificationResult(
        is_valid=is_valid,
        checked_count=checked,
        matched_count=matched,
        missing=missing,
        mismatched=mismatched,
        unsafe_paths=unsafe,
        errors=errors,
    )
