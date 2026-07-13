# Architecture v2 — trust before scale

## Recommended stack
- **API:** FastAPI or equivalent typed Python service; keep domain logic framework-independent.
- **Database:** PostgreSQL with migrations, row-level authorization checks and append-only audit triggers.
- **Objects:** managed S3-compatible storage with versioning, encryption, retention and separate quarantine/public-redacted buckets.
- **Jobs:** PostgreSQL-backed queue initially; avoid Kafka until measured need.
- **Extraction:** deterministic PDF text first; Docling/OCRmyPDF/PaddleOCR behind isolated worker adapters.
- **Search:** PostgreSQL full-text first; add OpenSearch only after scale/query evidence.
- **Identity:** deployment-native OIDC with MFA; explicit reviewer/admin roles and short sessions.
- **Frontend:** server-rendered or lightweight React/Next.js application with accessible reviewer and public surfaces.
- **Observability:** OpenTelemetry-compatible structured logs/traces, metrics and error monitoring.
- **Supply chain:** pinned dependencies, SBOM, signed containers/releases and provenance attestations.

## Bounded contexts
1. **Registry:** projects, organizations, contracts and identifiers.
2. **Evidence vault:** immutable originals, retrieval events, hashes and redactions.
3. **Extraction:** parser/OCR jobs and candidate spans.
4. **Claims:** atomic claims, evidence links, contradictions and state transitions.
5. **Review:** assignments, decisions, separation of duties and corrections.
6. **Publication:** allowlisted public views, dossiers, reports and RTI drafts.
7. **Connectors:** source-specific retrieval with rate, licence and breakage metadata.
8. **Audit:** append-only events plus periodic externally anchored checkpoints.

## Data flow
`receive -> quarantine -> scan -> hash -> preserve -> extract -> candidate -> review-1 -> review-2 -> publish -> correct/withdraw`

No stage overwrites the prior artifact. Derived artifacts point backward through a lineage chain.

## Security properties
- Public API reads from an allowlisted projection, never raw tables.
- Worker has no publication permission.
- Parser has no credentials beyond one quarantined object and one result sink.
- AI adapter can create candidates only.
- Audit events are insert-only to the application role.
- Original objects are private; public exports include redacted derivatives.
- Every privileged write includes actor, request ID, reason and before/after digest.

## Scale posture
Start as a modular monolith plus isolated workers. Target 10k projects and 1m claims with indexes and cache. Microservices would add operational risk before they add value.
