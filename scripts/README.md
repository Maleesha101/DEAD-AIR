# Scripts

Planned command-line scripts:
- `generate_artifacts.py`: create campaign artifacts from synthetic inputs.
- `verify_artifacts.py`: validate the artifact manifest and SHA-256 hashes.
- `healthcheck.sh`: verify expected local services after implementation.
- `reset_lab.sh`: stop services and remove only documented disposable lab state.

Scripts must fail safely, explain what they will change, avoid deleting arbitrary paths, and never depend on external services. Do not claim these commands are available until the corresponding scripts are implemented.
