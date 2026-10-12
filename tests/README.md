# Test Strategy

Organize tests by scope:
- `unit/`: pure logic, parsers, manifest validation, key derivation, and schema checks.
- `integration/`: interactions between services and artifact generators.
- `security/`: authorization boundaries, organizer-file exposure, input limits, and flag handling.
- `end_to_end/`: the full eight-stage dependency chain from generated artifacts to final validation.

Tests must assert observable behavior, not merely that modules import or endpoints return HTTP 200. Do not use placeholder assertions to represent unfinished work.

For each test command recorded in documentation, report the actual environment and result. The test suite is not implemented yet.
