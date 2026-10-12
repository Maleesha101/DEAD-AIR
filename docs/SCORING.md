# Scoring and Hints

## Planned score table

| Stage | Challenge | Points |
|---|---|---:|
| 01 | Find the Ghost Engineer — OSINT | 100 |
| 02 | The Silent Signal — Steganography | 150 |
| 03 | The Deleted Maintenance Log — Digital forensics | 200 |
| 04 | The Split-Key Archive — Cryptography | 200 |
| 05 | The Control Portal — Web exploitation | 250 |
| 06 | The False Update — Reverse engineering | 250 |
| 07 | Who Sent the Order? — Network forensics | 250 |
| 08 | Prove the Breach — Incident response | 400 |
| | **Total** | **1,800** |

This is the target scoring design, not a claim that scoring is implemented.

## Hint policy
Each stage should have three progressively more specific hints:
1. **Nudge:** points toward a useful technique or artifact.
2. **Direction:** narrows the relevant evidence.
3. **Near-solution:** explains the decisive correlation without disclosing the final flag.

The implementation must choose and document one scoring policy:
- fixed points regardless of hints; or
- a documented point deduction for each hint.

Do not silently change scores based on hints. Display the policy before players start.

## Validation rules
- A stage is complete only after server-side validation of its expected output.
- Client-side state must not be authoritative.
- The final stage must validate multiple evidence-backed fields.
- Incorrect answers must not reveal which field is correct.
- The final campaign flag must not be awarded from a client-side-only check.
