# Release gates v2

## Gate A — reproducible build
Clean clone, pinned install, tests, migration, SBOM, signed artifact and documented rollback all pass.

## Gate B — evidence safety
Unsupported-publication tests, two-person gate, exact-anchor integrity, contradiction display, correction versioning and synthetic labels pass.

## Gate C — privacy/security
OIDC/MFA, least privilege, upload quarantine, parser isolation, public allowlist, rate/body limits, secret/dependency/static scans and PII red-team pass.

## Gate D — reliability
Readiness distinguishes dependencies; backup and restore meet declared RPO/RTO; alerts reach an on-call human; load test meets declared capacity; failure injection has a tested runbook.

## Gate E — editorial/legal
Named operator, privacy/retention/correction/takedown policies, right-to-respond process, source terms review and two reviewed launch dossiers exist.

## Gate F — adoption
At least three design partners, one repeated unsupervised workflow and measured time/citation-quality improvement.

## Honest labels
- `alpha`: synthetic/local, workflow changing.
- `controlled beta`: real users, limited publication, disclosed failed gates.
- `production pilot`: all P0 technical and operational gates pass for a bounded audience.
- `v1 production`: all gates pass and named operator accepts ongoing responsibility.

No percentage-complete claim substitutes for gate evidence.
