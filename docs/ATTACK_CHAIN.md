# Attack Chain and Stage Contracts

## Overview
DEAD AIR is an evidence-correlation campaign, not eight unrelated flags. Every stage must produce a concrete artifact, identifier, or fact needed by a later stage.

| Stage | Category | Input | Required output | Next dependency |
|---|---|---|---|---|
| 01 | OSINT | Fictional public snapshots | Station ID and recording timestamp | Select the relevant audio |
| 02 | Steganography | Audio and image | Key fragment and evidence hash | Locate/validate the forensic record |
| 03 | Digital forensics | Filesystem/disk artifact | Second key clue and firmware reference | Decrypt the dossier |
| 04 | Cryptography | Two independent clues | Internal service and test-record identifiers | Investigate the local portal |
| 05 | Web exploitation | Test account and record ID | Firmware manifest and device ID | Identify the correct package |
| 06 | Reverse engineering | Firmware-like package and manifest | Integrity discrepancy and network indicator | Filter the PCAP |
| 07 | Network forensics | PCAP and indicators | Verified timeline and command evidence | Build incident report |
| 08 | Incident response | Evidence from all stages | Validated incident reconstruction | Final flag |

## Dependency rules
- No stage should be solvable solely by guessing a predictable flag string.
- Earlier-stage outputs must be checked by artifact or integration tests.
- Decoys must be rejectable with evidence.
- Stage names and identifiers must be consistent across docs and generated assets.
- The final stage must validate multiple independent facts.
- Public artifacts may contain challenge clues but must not contain organizer answer keys.

## Evidence contract
For every stage, document:
- artifact names and hashes;
- intended analysis tools;
- input prerequisites;
- expected finding (organizer-only);
- player-facing output token or evidence identifier;
- hints and scoring;
- automated validation;
- safe deployment boundary.

## Current implementation status
This file defines the target design only. Do not treat the chain as implemented until all artifacts and end-to-end tests are present.
