# Contributing

Thanks for helping build DEAD AIR.

## Contribution principles
- Keep the eight-stage incident narrative coherent.
- Use only fictional identities, services, credentials, and datasets.
- Make each clue independently verifiable and relevant to a later stage.
- Prefer realistic analysis workflows over isolated payload guessing.
- Include tests and update the relevant documentation with each feature.

## Suggested workflow
1. Open an issue describing the stage, bug, or infrastructure change.
2. Create a focused branch, for example `feat/steganography-artifact-generator`.
3. Implement the smallest useful change.
4. Run relevant tests and inspect generated artifacts.
5. Update docs and include reproduction steps in the pull request.
6. Submit a pull request with the problem, solution, test evidence, and security implications.

## Challenge contribution checklist
- [ ] Uses synthetic, locally controlled data.
- [ ] Has a clear objective and learning outcome.
- [ ] Has a real dependency on the campaign chain.
- [ ] Includes expected output and organizer write-up.
- [ ] Includes progressive hints and scoring.
- [ ] Includes artifact integrity checks or tests.
- [ ] Does not expose answer keys or final flags to players.
- [ ] Documents intended vulnerabilities and mitigations.
- [ ] Works offline and stays within the lab scope.

## Commit style
Use focused conventional commit messages:
- `docs: document campaign attack chain`
- `feat: generate synthetic audio artifact`
- `test: validate firmware manifest integrity`
- `fix: enforce maintenance record scope`

## Safety
Do not submit real secrets, personal information, malware, or instructions targeting real emergency infrastructure. Report suspected accidental secret exposure promptly and do not reproduce exposed secrets in issues.
