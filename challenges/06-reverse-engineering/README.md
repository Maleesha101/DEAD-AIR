# 06 — The False Update

- **Category:** Reverse engineering
- **Planned points:** 250
- **Prerequisite:** Stage 05 manifest and device identifier
- **Output:** Integrity discrepancy and network-analysis indicator

## Player objective
Analyze a harmless synthetic firmware-like package, compare it with the maintenance manifest, and identify an integrity discrepancy and a clue for the packet capture.

## Design constraints
- Prefer a custom structured package or harmless compiled artifact.
- Support basic tools such as `file`, `strings`, and `hexdump`; document any specialist tools.
- Do not include real vendor firmware, secrets, malware, persistence, or destructive behavior.
- Verify hashes and package consistency with scripts.

## Acceptance criteria
The discrepancy is independently reproducible and the extracted indicator is consumed by Stage 07.

## Implementation status
Design only. Package, generator, hints, and tests are pending.
