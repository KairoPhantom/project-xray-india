# Interface registry

This registry is the integration contract for the synthetic alpha. Changes to database migrations, API contracts, evidence-state rules, or public projections require an ADR and contract tests.

| Boundary | Owner | Contract |
| --- | --- | --- |
| API and evidence policy | Integration | FastAPI/Pydantic request and response models under `/api/v1` |
| Persistence | Domain | Alembic migrations; PostgreSQL is the deployment target; SQLite is test-only |
| Object storage | Ingestion | Quarantine, private-original, and public-redacted namespaces; originals are never public |
| Extraction worker | Ingestion | Receives one quarantined object and writes candidate-only results; no publication permission |
| Public projection | Publication | Explicit allowlisted `PublicDossier` response; no raw ORM serialization |
| Identity and reviews | Security | OIDC roles and independent two-reviewer publication check |
| Exports | Publication | Redacted evidence report, editable RTI draft, and checksum-backed dossier capsule |
