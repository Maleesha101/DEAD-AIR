# AGENTS.md — DEAD AIR

## Mission
Build **DEAD AIR: The Last Broadcast**, a safe, reproducible, narrative-driven CTF campaign connecting eight disciplines into one evidence-led investigation.

## Before changing code
1. Inspect the existing repository, Git status, and current implementation.
2. Read this file and the relevant documents under `docs/`.
3. Propose a small implementation plan based on the actual codebase.
4. Preserve existing user changes. Never reset, force-push, or overwrite unrelated work.
5. Do not claim that a build, test, or challenge has passed unless it was actually run.

## Core rules
- Synthetic data only: all people, organizations, hosts, credentials, device IDs, keys, and incident records must be fictional.
- Offline-first: challenge solving must not depend on third-party websites or services.
- Connected chain: each stage must consume a clue or artifact from an earlier stage.
- Reproducibility: generated artifacts should be deterministic where practical and accompanied by hashes/manifests.
- Separation: organizer solutions, answer keys, signing material, and final flags must never be shipped in player-facing images, static assets, or public API responses.
- Scope: intentional vulnerabilities must be narrowly scoped to the designated challenge endpoint and synthetic records.
- Verification: include automated tests for artifact integrity, challenge dependencies, authorization behavior, and flag validation.
- Documentation must match the implementation. Mark unimplemented features as planned, not complete.

## Planned stack
Prefer Python with FastAPI for a lightweight local API, a static HTML/CSS/JavaScript player interface, and Docker Compose for orchestration. Adapt to established repository choices rather than introducing unnecessary frameworks.

## Security boundaries
- Never mount the Docker socket or sensitive host directories into challenge containers.
- Do not use privileged containers.
- Do not include malware, persistence, destructive actions, or real infrastructure targeting.
- Avoid arbitrary command execution, unrestricted file access, and uncontrolled SSRF.
- Keep organizer services and secrets out of player networks and images.
- Validate all untrusted inputs and cap request sizes.
- Treat Docker network isolation as a layer, not a complete security boundary.

## Code quality
- Keep modules small and responsibilities clear.
- Use descriptive names, type hints where useful, and comments for non-obvious security decisions.
- Add tests alongside new behavior.
- Pin dependency versions where practical.
- Keep generated binary artifacts out of Git when they are large or reproducible; document the generation command instead.
- Do not commit real secrets, local environment files, caches, or generated runtime state.

## Suggested workflow
1. Implement one stage or infrastructure component at a time.
2. Add/update tests.
3. Run targeted tests and applicable lint/build checks.
4. Inspect the diff and update docs.
5. Use focused commits with conventional messages, such as `feat: add artifact manifest validator` or `docs: describe PCAP challenge`.

## Definition of done
A feature is done only when it is implemented, tested, documented, and does not leak organizer-only data. For a challenge stage, verify its artifact, expected solve path, prerequisite, hints, scoring, and safe deployment boundary.
