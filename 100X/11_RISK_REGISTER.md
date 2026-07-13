# Risk register

| Risk | L | I | Leading indicator | Control | Owner required |
|---|---:|---:|---|---|---|
| Unsupported allegation published | M | Critical | claim without exact anchor | publication compiler + two reviewers | Editorial lead |
| PII/whistleblower exposure | M | Critical | raw upload reaches public projection | quarantine, redaction, allowlist | Privacy lead |
| Portal terms/access conflict | M | High | blocks, complaints, unstable scraping | source register, counsel review, rate limits | Connector owner |
| AI extraction hallucination | H | High | anchor mismatch, low abstention | candidate-only, benchmark, review diff | ML/evidence lead |
| Audit tampering | L | Critical | privileged update/delete path | append-only role, external checkpoints | Security lead |
| Defamatory product framing | M | Critical | guilt/corruption scoring language | language policy and review | Product/editorial |
| Incomplete data treated as complete | H | High | “missing” without search scope | search-scope ledger | Evidence lead |
| Malicious document | H | High | parser crash/exfiltration attempt | scanning, sandbox, no network/secrets | Security lead |
| OSS dependency abandonment/licence | M | High | stale releases/licence change | adapter boundaries, SBOM, alternatives | Maintainer |
| No adoption | H | High | pilots do not repeat workflow | design partners and kill criteria | Product lead |
| Founder/operator burnout | H | High | unresolved incidents/corrections | staffing, runbook, sustainable funding | Governing entity |
| Political or legal pressure | M | Critical | takedown/threats | counsel, transparent policy, safety plan | Legal/operator |

L = likelihood; I = impact. Review monthly and after every material incident.
