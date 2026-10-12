# Deployment Guide

## Status
The repository currently contains initial documentation. A runnable application and Docker Compose configuration have not yet been implemented, so there are no verified startup commands at this stage.

## Development deployment target
The intended first deployment is a local, single-host lab:
- player portal bound to loopback;
- evidence API reachable only through the required internal network;
- organizer validator and answer material separated from player-facing services;
- synthetic artifacts generated locally;
- no runtime dependency on external services.

## Before running a future build
1. Review the Compose configuration and every published port.
2. Copy `.env.example` to `.env` and replace all placeholders with deployment-specific values.
3. Confirm no real credentials or sensitive host paths are mounted.
4. Build images from reviewed source.
5. Verify that organizer-only material is absent from player images and static directories.
6. Run unit, integration, and security tests.
7. Confirm that only the intended player-facing port is published.
8. Use a disposable environment and snapshot/backup strategy appropriate to the host.

## Production or multi-user hosting
Do not expose an intentionally vulnerable development build directly to the public Internet. A hosted event requires a separate threat model, host hardening, resource limits, monitoring, abuse controls, isolation review, and an operator-approved network design.

Docker networking reduces exposure but does not by itself guarantee containment.

## Future operator runbook
Once the runtime exists, update this document with commands that have been tested from a clean checkout:
- build;
- start;
- health check;
- stop;
- reset;
- regenerate artifacts;
- inspect logs;
- remove disposable volumes.

Do not document unverified commands as working.
