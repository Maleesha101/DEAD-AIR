# Architecture

## Status
This document describes the intended architecture. Components remain planned until source code and tests exist.

## Logical components

### Player portal
Serves campaign introduction, challenge descriptions, permitted downloads, hints, scoring, and player progress. It must never serve organizer write-ups, answer keys, signing secrets, or the final flag source.

### Evidence API
Provides only the synthetic records required for the web challenge. The intentionally vulnerable IDOR/BOLA behavior must be restricted to one documented endpoint and a small fabricated dataset. Other endpoints should enforce authorization normally.

### Artifact generator
Creates repeatable challenge files, including audio, images, forensic records, an encrypted dossier, a firmware-like package, and a PCAP/PCAPNG. Each artifact should be listed in a manifest with its expected hash and challenge dependency.

### Flag validator
Validates the final incident-response submission server-side. The answer key and flag configuration must be loaded from organizer-only runtime configuration, never frontend code or player downloads. Errors should not reveal which individual answer field was wrong.

### Container orchestration
Docker Compose is the planned local development and deployment mechanism. Services should run as non-root where practical, use minimal capabilities, avoid host-sensitive mounts, and expose only necessary ports.

## Trust boundaries
1. **Player browser → portal:** all submitted input is untrusted.
2. **Player → challenge API:** authenticated identity does not imply access to every record.
3. **Player containers → organizer assets:** no route or mount should permit access.
4. **Public artifacts → organizer validator:** artifacts may reveal clues, but never the final answer key.
5. **Container network → host/external network:** restrict connectivity and document remaining platform-level risks.

## Planned data flow
OSINT clue → recording selection → hidden payload → forensic record → archive decryption → scoped maintenance record → firmware analysis → PCAP reconstruction → evidence submission → final flag.

## Implementation requirements
- Define API schemas and request-size limits.
- Store player progress by player/team identifier when that feature is implemented.
- Keep logs useful but free of secrets.
- Add health checks and reproducible startup/reset commands.
- Add tests for cross-user authorization, organizer-file exposure, and incorrect flag submissions.
