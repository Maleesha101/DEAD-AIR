# 03 — The Deleted Maintenance Log

- **Category:** Digital forensics
- **Planned points:** 200
- **Prerequisite:** Stage 02 evidence reference
- **Output:** Second archive-key clue and firmware reference

## Player objective
Inspect a synthetic filesystem archive or disk image, recover a deleted maintenance record, and correlate its timestamps with the incident evidence.

## Planned evidence
- Synthetic filesystem image/archive
- Maintenance records and timestamps
- Recoverable deleted record or file fragment
- Firmware update reference
- Plausible decoy record
- Integrity manifest

## Acceptance criteria
- The supplied evidence is genuinely inspectable with documented tools.
- Hashes can be independently verified.
- Recovery does not depend on unstable host-specific metadata.
- The second key clue is required by Stage 04.

## Implementation status
Design only. Artifact files, generator, hints, and automated checks are pending.
