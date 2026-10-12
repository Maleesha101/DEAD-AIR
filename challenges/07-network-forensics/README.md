# 07 — Who Sent the Order?

- **Category:** Network forensics
- **Planned points:** 250
- **Prerequisite:** Stage 06 network indicator
- **Output:** Verified timeline and unauthorized-command evidence

## Player objective
Analyze a synthetic PCAP/PCAPNG and correlate device check-ins, a maintenance session, an update request, and a suspicious application-level command.

## Planned traffic
- Benign background traffic
- Normal device check-ins
- Legitimate maintenance activity
- Suspicious update sequence
- Unauthorized simulated command

## Acceptance criteria
- Capture is synthetic and fully local.
- Wireshark/tshark can inspect the important fields.
- A script verifies the key packet-level facts.
- No traffic is sent to real systems.
- The evidence supports Stage 08's incident reconstruction.

## Implementation status
Design only. Capture, generator, hints, and tests are pending.
