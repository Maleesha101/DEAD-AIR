# Safety and Isolation

## Intended use
DEAD AIR is a controlled cybersecurity training lab. All identities, organizations, hosts, credentials, devices, and evidence must be fabricated. Use the project only on systems and networks you own or are authorized to test.

## Deployment requirements
- Prefer local-only published ports for development.
- Do not deploy intentionally vulnerable services on a public interface.
- Use isolated container networks and disable outbound connectivity for challenge services where feasible.
- Run as non-root and avoid privileged containers.
- Never mount the Docker socket or sensitive host directories into player-facing containers.
- Keep organizer secrets and answer keys in runtime-only configuration or an organizer-only service.
- Apply resource limits and request-size limits.
- Use disposable volumes and document cleanup/reset steps.

Docker is not a complete security boundary. A public or multi-user deployment requires a separate security review, host hardening, network policy, monitoring, and explicit operator authorization.

## Challenge constraints
- The web vulnerability must be scoped to a synthetic maintenance-record endpoint.
- The reverse-engineering artifact must be harmless and must not include real firmware secrets or destructive behavior.
- Network captures must be generated or synthesized for this campaign.
- No challenge should require contacting real emergency systems, public infrastructure, or unrelated third-party services.
- Do not include malware, persistence, destructive actions, or unrestricted host access.

## Secret handling
- Never commit real secrets or local `.env` files.
- Keep final flags and expected answers out of player assets, source maps, public JSON, and challenge images.
- Use unique flags per deployment.
- Rotate any secret accidentally committed; deleting the latest copy alone does not remove it from Git history.

## Reporting
Report accidental secret exposure or unintended vulnerabilities privately to the maintainer where possible. Do not publish real sensitive data in an issue.
