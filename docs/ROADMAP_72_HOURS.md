# 72-hour production roadmap

**Sprint starts:** 12 July 2026 IST  
**Target release:** 14 July 2026 IST  
**Principle:** working vertical slice first; factual trust before feature breadth.

No responsible team can guarantee production readiness from elapsed time alone. The release is ready only when every P0 acceptance gate passes on the target environment.

## Team model

- **Human product/evidence lead:** scope, legal judgment, source review and launch authority.
- **Codex implementation lead:** code, tests, migrations, infrastructure and documentation.
- **Second human reviewer:** independent source and UX review.
- **Civil engineer/adviser:** validates technical language for launch cases.
- **Security/reliability reviewer:** deployment and incident gate, even if part-time.

Codex may work continuously; humans must rotate. No unreviewed overnight factual publication.

## Day 1 — trustworthy vertical slice (hours 0–24)

### H0–2: release contract
- Read repository instructions.
- Confirm the one-line product promise and no-guilt/no-payment boundaries.
- Create issue board from `BACKLOG.md`.
- Assign human owners and checkpoint times.
- Record exact target domain, hosting region and privacy contact.

**Exit:** signed scope; no unresolved P0 ambiguity.

### H2–6: data and evidence foundation
- Implement production schema/migrations for projects, organizations, sources, documents, claims, gaps, responses, reviews and audit events.
- Enforce evidence states and allowed transitions.
- Add immutable IDs, timestamps and soft-delete/tombstone behavior.
- Add document hashing and retrieval provenance.

**Tests:** invalid evidence state rejected; published claim cannot lack source/reviewer; deletion creates tombstone.

### H6–10: authenticated API
- Implement read API and reviewer/admin write API.
- Add OIDC or deployment-appropriate authentication; token mode is local-only.
- Add authorization, request IDs, validation, rate limits and audit logging.
- Document API contract.

**Tests:** unauthenticated writes fail; public reads cannot expose private fields; all writes create audit events.

### H10–14: ingestion
- URL/manual/PDF intake.
- Preserve original bytes and hash.
- Extract born-digital text with page anchors.
- Queue OCR for scans; failures remain visible.
- Store LLM outputs as candidates only.
- Add prompt-injection-safe extraction boundary.

**Tests:** malicious document text cannot alter policy; unsupported file rejected; duplicate hash detected.

### H14–18: public dossier UI
- Build responsive, accessible project page.
- Show facts, allegations, official responses, gaps and corrections distinctly.
- Add timeline, source drawer and exact citations.
- Add empty, loading, error and withdrawn-evidence states.

**Tests:** keyboard navigation; 390px mobile; no color-only status; source opens exact record.

### H18–21: report and RTI workflow
- Generate evidence report with provenance.
- Generate editable RTI draft from selected gaps.
- Add explicit “draft—not legal advice” language.
- Log exports without recording sensitive content.

### H21–24: first full checkpoint
- Execute full smoke path.
- Restart and verify persistence.
- Backup and restore in clean environment.
- Freeze architecture unless a P0 blocker remains.

**Day 1 deliverable:** complete local vertical slice; no public case launch.

## Day 2 — hardening and real case production (hours 24–48)

### H24–28: deployment infrastructure
- Provision managed PostgreSQL/object storage or equivalent.
- HTTPS, DNS, secret manager, least-privilege service account.
- Staging and production separation.
- Structured logs, metrics, uptime checks and alert destinations.

### H28–32: security hardening
- CSP, HSTS, frame restrictions and secure cookies.
- Upload quarantine and malware-scanning integration.
- Dependency/SBOM/secret/static scans.
- Backup encryption and restoration test.
- Abuse, correction and takedown routes.

### H32–38: launch case 1
- Collect original/official sources first.
- Extract candidates.
- Human reviewer validates every published claim.
- Engineer reviews technical wording.
- Record search scope for every “not located” gap.
- Invite authority/contractor response before or at publication according to counsel.

### H38–42: launch case 2
- Repeat independently; do not copy assumptions.
- Explicitly include official clarification and what evidence does not establish.

### H42–45: quality and accessibility
- Contract tests, API tests, migration test, browser tests.
- Mobile/desktop visual review.
- WCAG AA critical checks.
- Load test expected launch traffic and set capacity limits.

### H45–48: second checkpoint
- Staging smoke test using real reviewed records.
- Independent editorial review.
- Resolve all P0 defects; defer P1 visibly.

**Day 2 deliverable:** hardened staging, two reviewed dossiers, tested restore.

## Day 3 — production gate and accountable launch (hours 48–72)

### H48–54: operations
- Finalize runbook, incident response, rollback and data-retention policy.
- Test on-call alert and failure injection.
- Verify data export and correction workflows.
- Confirm legal entity/contact details and privacy notice.

### H54–59: reproducible open-source release
- Clean-room clone and startup.
- Run tests and release checker.
- Generate SBOM, checksums and signed/tagged release.
- Verify licence compatibility and third-party notices.
- Remove sample secrets and unreviewed real data.

### H59–63: production deployment
- Deploy immutable version.
- Run migrations once with backup.
- Execute smoke path against production.
- Verify HTTPS, headers, logs, backups and rollback artifact.

### H63–67: launch materials
- Publish methodology, limitations and correction policy before promotion.
- Record a real workflow—not fabricated results.
- Create two source-grounded case explainers.
- Prepare audience-specific messages for journalists, engineers and civic groups.

### H67–70: red-team launch
- Attempt unsupported publication, PII exposure, token abuse, oversized upload, malicious PDF text, citation breakage and audit tampering.
- Fix or block release.

### H70–72: go/no-go
Release only if all P0 gates pass. Otherwise publish the repository as a **public beta** with failed gates disclosed; do not relabel it production-ready.

**Day 3 deliverable:** tagged open-source release, working production service, two reviewed dossiers, incident/rollback/backup capability, public methodology.

## Hourly Codex loop

1. Pull one P0 issue.
2. State measurable acceptance test.
3. Implement smallest vertical change.
4. Run targeted test.
5. Run smoke path if integration changed.
6. Commit with evidence.
7. Update issue and decision log.
8. Never self-approve factual content.
