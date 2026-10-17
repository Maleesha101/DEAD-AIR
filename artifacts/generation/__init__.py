"""Artifact generation and verification framework for DEAD AIR."""

from .manifest import (
    ArtifactRecord,
    VerificationResult,
    PathTraversalError,
    ManifestError,
    compute_sha256,
    validate_safe_path,
    generate_manifest,
    load_manifest,
    save_manifest,
    verify_manifest,
)
from .base import BaseArtifactGenerator, GeneratorRegistry

__all__ = [
    "ArtifactRecord",
    "VerificationResult",
    "PathTraversalError",
    "ManifestError",
    "compute_sha256",
    "validate_safe_path",
    "generate_manifest",
    "load_manifest",
    "save_manifest",
    "verify_manifest",
    "BaseArtifactGenerator",
    "GeneratorRegistry",
]
