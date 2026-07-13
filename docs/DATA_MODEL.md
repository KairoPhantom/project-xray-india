# Data model

## Core entities
- `project`: stable dossier identity, authority, location, lifecycle state.
- `source`: publisher, URL, publication/retrieval dates, source class.
- `document`: source artifact, media type, hash, storage and redaction status.
- `claim`: atomic statement with type, evidence state and source passage.
- `event`: dated project milestone linked to claims.
- `evidence_gap`: required/expected record not located in declared search scope.
- `response`: authority/contractor/subject reply linked to claims.
- `review`: reviewer decision and rationale.
- `audit_event`: append-only actor/action/object record.

## Claim types
`verified_fact`, `reported_allegation`, `official_claim`, `expert_assessment`, `data_inconsistency`, `audit_finding`, `court_finding`.

## Publication states
`candidate`, `reviewed`, `published`, `disputed`, `corrected`, `withdrawn`.

## Critical invariant
A published claim requires source ID, exact passage or document page, reviewer ID and review timestamp. “Verified fact” additionally requires source-class policy satisfaction.

## Standards mapping
Contracting records should export to OCDS; project records to OC4IDS; organization/person relationship investigations to FollowTheMoney. Keep local fields in namespaced extensions.
