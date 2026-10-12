# 08 — Prove the Breach

- **Category:** Incident response
- **Planned points:** 400
- **Prerequisite:** Evidence from Stages 01–07
- **Output:** Validated campaign completion flag

## Player objective
Submit a structured reconstruction of the incident, including the compromised component, authorization weakness, firmware integrity failure, command sequence, timeline, and supporting evidence identifiers.

## Validation requirements
- Validate structured input server-side.
- Check multiple independent facts against organizer-only expected values.
- Bound request sizes and validate types.
- Use generic failure messages that do not reveal which field was correct.
- Issue a configurable unique flag only after complete validation.
- Never expose expected answers or the flag source to the player portal.

## Acceptance criteria
Tests cover incorrect, incomplete, malformed, and correct submissions. Organizer-only files are not accessible over HTTP.

## Implementation status
Design only. Validator, answer schema, flag configuration, hints, and integration tests are pending.
