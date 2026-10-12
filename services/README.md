# Services

Planned services:
- `player-portal/`: player-facing campaign UI and challenge downloads.
- `evidence-api/`: isolated synthetic maintenance portal with one scoped intentional authorization flaw.
- `flag-validator/`: server-side evidence validation and final flag issuance.

Keep organizer-only answers and secrets out of player-facing images and static directories. Prefer separate service identities, minimal privileges, internal networks, bounded input sizes, and tests for cross-boundary access.

These services have not been implemented yet.
