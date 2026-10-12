# 02 — The Silent Signal

- **Category:** Steganography
- **Planned points:** 150
- **Prerequisite:** Stage 01
- **Output:** Key fragment and evidence hash

## Player objective
Use the station and timestamp from Stage 01 to select and inspect a synthetic radio recording. Follow the audio clue to a PNG containing a concealed payload.

## Planned evidence
- WAV recording and metadata
- Decoy recording
- Spectrogram clue
- PNG with recoverable hidden payload
- Hash used to identify the related forensic evidence

## Acceptance criteria
- A documented, reproducible generator embeds the payload.
- Automated tests recover the expected payload from generated media.
- The clue is not plainly exposed by a filename or simple metadata field.
- The output is required by Stage 04.

## Implementation status
Design only. Artifact files, generator, hints, and automated checks are pending.
