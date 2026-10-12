# 04 — The Split-Key Archive

- **Category:** Cryptography
- **Planned points:** 200
- **Prerequisites:** Stage 02 key fragment and Stage 03 clue
- **Output:** Internal service identifier and test-record reference

## Player objective
Combine two independently recovered clues to decrypt a fictional maintenance dossier.

## Design constraints
- Neither prerequisite alone should reveal the dossier.
- Use a documented, lab-specific cryptographic weakness or weak derivation scheme.
- Make solving deterministic; do not require timing-sensitive brute force.
- Verify the decrypted content's integrity.
- Keep organizer keys and expected answers out of player assets.

## Acceptance criteria
An automated test proves that the intended inputs recover the dossier and that incomplete or incorrect inputs fail.

## Implementation status
Design only. Archive, key derivation, hints, and tests are pending.
