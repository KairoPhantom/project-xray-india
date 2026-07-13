# Threat model

| Threat | Example | Control |
|---|---|---|
| Prompt injection | PDF tells extractor to ignore policy | Isolated extraction; fixed schema; no tool authority; human review |
| Defamation | Unsupported guilt claim | Taxonomy, reviewer gate, right to respond, corrections |
| PII exposure | whistleblower identity in upload | quarantine, redaction, allowlist, private originals |
| Evidence tampering | file silently replaced | SHA-256, immutable versions, audit events |
| Malicious upload | exploit PDF/archive | type/size limits, malware scan, sandboxed parser |
| Scraper poisoning | spoofed portal page | domain/source policy, signatures/hashes where available |
| Reviewer compromise | stolen token publishes claim | OIDC/MFA, short sessions, approval separation |
| Abuse/brigading | mass partisan submissions | rate limits, moderation, no auto-publication |
| Supply-chain attack | compromised dependency | lockfiles, SBOM, scans, minimal dependencies |
| Audit deletion | operator edits history | append-only external sink and restricted DB role |
