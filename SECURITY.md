# Security Policy

## Scope
DEAD AIR is an intentionally vulnerable cybersecurity training project. Deliberate weaknesses must exist only in explicitly designated challenge components and must use fabricated data.

## Safe use
- Run the lab only on systems and networks you own or are authorized to test.
- Prefer local-only port bindings and isolated Docker networks.
- Do not connect challenge services to production systems, public emergency infrastructure, or real devices.
- Do not add real credentials, personal data, or third-party secrets to artifacts.
- Keep organizer-only files and flag material outside player-facing images and static directories.

## Reporting a vulnerability
For an issue in the project infrastructure (rather than an intended challenge weakness), open a private security report through the repository's available GitHub security reporting features, if enabled. Otherwise contact the maintainer privately through an appropriate channel. Include affected component, impact, reproduction steps, and suggested mitigation. Do not publish real secrets or sensitive data in a public issue.

## Intended vulnerabilities
Challenge vulnerabilities should be labeled in documentation and tests. Where practical, provide a secure reference implementation or regression test demonstrating the correct behavior.
