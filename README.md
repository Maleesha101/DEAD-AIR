# DEAD AIR: The Last Broadcast

**A narrative-driven, multi-stage CTF campaign** where players investigate a fictional emergency-broadcast incident by chaining OSINT, steganography, digital forensics, cryptography, web exploitation, reverse engineering, network forensics, and incident response.

> **Project status:** Initial documentation and architecture planning. The challenge services and artifacts are not yet implemented unless explicitly listed in the repository.

## Story

At 02:17 AM, the fictional Pelican Coastal Resilience Network (PCRN) broadcasts an evacuation order for a nonexistent tsunami. A senior radio engineer disappears after investigating a suspicious firmware update. Players reconstruct the incident from public clues, concealed media, deleted records, an exposed maintenance record, a firmware package, and a packet capture.

All people, organizations, systems, credentials, keys, domains, and artifacts are fictional and intended for an isolated lab.

## Campaign stages

| Stage | Category | Intended outcome |
|---|---|---|
| 01 | OSINT | Correlate public clues to identify a station and timestamp |
| 02 | Steganography | Recover hidden evidence from audio and an image |
| 03 | Digital forensics | Recover maintenance records and identify a firmware package |
| 04 | Cryptography | Combine evidence to decrypt a maintenance dossier |
| 05 | Web exploitation | Demonstrate a scoped IDOR/BOLA authorization flaw |
| 06 | Reverse engineering | Inspect a synthetic firmware-like package and verify an integrity failure |
| 07 | Network forensics | Reconstruct the unauthorized command from a synthetic PCAP |
| 08 | Incident response | Submit a defensible, evidence-backed incident timeline |

The stages must form one dependency chain; artifacts from earlier stages provide evidence required later.

## Planned architecture

- **Player portal:** challenge descriptions, downloads, hints, scoring, and progress.
- **Evidence API:** isolated, synthetic maintenance records and scoped challenge interactions.
- **Artifact generation:** reproducible scripts for audio, images, forensic records, firmware-like data, and packet captures.
- **Flag validation:** server-side validation using organizer-only configuration.
- **Container runtime:** Docker Compose with minimal privileges and no unnecessary outbound network access.

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [docs/ATTACK_CHAIN.md](docs/ATTACK_CHAIN.md), and [docs/CHALLENGE_DESIGN.md](docs/CHALLENGE_DESIGN.md).

## Current status

This repository begins with project documentation and implementation guidance. Do not assume that a runnable portal, generated artifacts, vulnerable endpoint, or complete challenge chain exists until implemented and tested.

## Planned local development

The runtime instructions will be finalized after the initial application and artifact generator are implemented. For now, inspect the docs and use [AGENTS.md](AGENTS.md) as the contributor/coding-agent guide.

## Safety

Run intentionally vulnerable services only in an isolated, disposable environment that you control. Never connect this lab to real emergency services, production networks, or real devices. Never place organizer solutions, real credentials, or the final flag in player-accessible assets.

See [docs/SAFETY.md](docs/SAFETY.md).

## Contributions

Contributions should preserve the narrative dependency chain, use fabricated data, include tests, and document both intended vulnerabilities and their mitigations. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

No license has been selected yet. Until a license is added, do not assume that the repository grants permission to reuse, distribute, or modify its contents.
