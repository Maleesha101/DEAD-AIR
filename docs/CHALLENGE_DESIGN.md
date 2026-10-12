# Challenge Design

## Scoring
Planned fixed scoring: OSINT 100, steganography 150, digital forensics 200, cryptography 200, web exploitation 250, reverse engineering 250, network forensics 250, incident response 400. Total: **1,800 points**.

Scoring is a design target, not an implemented feature yet.

## Difficulty and learning outcomes

### 01 — Find the Ghost Engineer (OSINT)
Correlate offline fictional pages, notices, and repository snapshots. Learn source validation, timeline correlation, and metadata awareness.

### 02 — The Silent Signal (Steganography)
Analyze WAV metadata and spectrograms, then inspect a PNG for concealed data. Learn to distinguish hidden payloads from ordinary media content.

### 03 — The Deleted Maintenance Log (Digital forensics)
Inspect a synthetic filesystem archive or small disk image, recover a record, and correlate timestamps. Learn integrity preservation and evidence handling.

### 04 — The Split-Key Archive (Cryptography)
Combine clues from two earlier stages to recover a lab-only archive key. Learn how weak key construction and poor key management undermine confidentiality.

### 05 — The Control Portal (Web exploitation)
Demonstrate a deliberately scoped IDOR/BOLA flaw using a synthetic maintenance record. Learn object-level authorization and secure regression testing.

### 06 — The False Update (Reverse engineering)
Inspect a harmless firmware-like package, compare manifest hashes, and identify an unsafe trust decision. Learn static analysis and integrity verification.

### 07 — Who Sent the Order? (Network forensics)
Analyze a synthetic PCAP and correlate protocol events with recovered indicators. Learn filtering, timeline reconstruction, and evidence-backed attribution.

### 08 — Prove the Breach (Incident response)
Submit a structured incident timeline, root cause, and supporting evidence. Learn to distinguish a plausible story from a defensible conclusion.

## Progressive hints
Each challenge should provide three hints:
1. **Nudge:** suggests a technique or artifact worth inspecting.
2. **Direction:** narrows the relevant field, timestamp, file, or protocol.
3. **Near-solution:** explains the decisive correlation without directly exposing the final flag.

## Author write-up requirements
For each stage, document tools, commands, expected observations, why the finding matters, common false leads, the output token, and a defensive lesson.

## Fairness requirements
- No external account or paid tool is required.
- Every necessary artifact is downloadable or bundled locally.
- Tool versions and assumptions are documented.
- Decoys should be plausible but not arbitrary.
- All timestamps specify timezone or explicitly use a campaign-relative clock.
