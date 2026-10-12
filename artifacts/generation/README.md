# Artifact Generation

Artifact generators and deterministic input fixtures belong here or under `scripts/`, depending on whether they are reusable libraries or command-line entry points.

## Requirements
- Work offline.
- Use synthetic data.
- Be deterministic where practical.
- Write outputs only to an explicitly selected output directory.
- Never read or package local secrets.
- Emit a manifest with SHA-256 hashes.
- Fail clearly if required inputs are missing.
- Include tests for generated artifact structure and recovery.

No generator is implemented yet; this file defines the initial convention.
