# Test Strategy

Organize tests by scope:
- `unit/`: pure logic, parsers, manifest validation, key derivation, and schema checks.
- `integration/`: interactions between services and artifact generators.
- `security/`: authorization boundaries, organizer-file exposure, input limits, and flag handling.
- `end_to_end/`: the full eight-stage dependency chain from generated artifacts to final validation.

Tests must assert observable behavior, not merely that modules import or endpoints return HTTP 200. Do not use placeholder assertions to represent unfinished work.

## Running Tests

Run the test suite using standard Python `unittest`:
```bash
python3 -m unittest discover -s tests -v
```

Unit tests under `tests/unit/test_artifacts.py` cover:
- Deterministic manifest generation and formatting
- SHA-256 chunked calculation
- Safe path containment and path traversal protection (`..`, absolute paths, Windows separators)
- Verification success, missing file detection, and hash mismatch detection
- Reproducibility across multiple generator runs
- Subprocess CLI execution for `generate_artifacts.py` and `verify_artifacts.py`

