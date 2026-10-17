# Artifact Generation

Artifact generators and deterministic input fixtures belong here or under `scripts/`, depending on whether they are reusable libraries or command-line entry points.

## Architecture

- `manifest.py`: Implements deterministic SHA-256 manifest generation, path traversal validation, and artifact verification.
- `base.py`: Defines the `BaseArtifactGenerator` interface and `GeneratorRegistry` for orchestrating stage artifact generators.

## Requirements
- Work offline with zero external network dependencies.
- Use synthetic data only.
- Be deterministic given a numeric seed.
- Constrain all file outputs strictly within the chosen output directory (enforced by `validate_safe_path`).
- Never read or package local secrets.
- Emit a sorted JSON manifest with SHA-256 hashes.
- Fail non-zero if files are missing or hashes mismatch.

