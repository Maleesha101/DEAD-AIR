# Scripts

Command-line scripts:

### Implemented

#### `generate_artifacts.py`
Deterministically creates campaign artifacts and produces an `artifacts.manifest.json` file.
```bash
python3 scripts/generate_artifacts.py --output-dir <path> [--seed 1337] [--manifest-filename artifacts.manifest.json]
```

#### `verify_artifacts.py`
Validates artifacts against an artifact manifest, checking SHA-256 integrity and catching path traversal attempts. Exits non-zero (`1`) on any missing, modified, or unsafe artifact.
```bash
python3 scripts/verify_artifacts.py --manifest <path/to/artifacts.manifest.json> [--target-dir <path>]
```

### Planned
- `healthcheck.sh`: verify expected local services after implementation.
- `reset_lab.sh`: stop services and remove only documented disposable lab state.

Scripts must fail safely, explain what they will change, avoid deleting arbitrary paths, and never depend on external services.

