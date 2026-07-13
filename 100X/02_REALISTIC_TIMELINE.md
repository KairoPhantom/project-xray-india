# Realistic timeline using frontier AI and existing open source

## Assumptions
- Six coordinated agent workstreams operate continuously with one integration lead.
- Managed PostgreSQL, S3-compatible storage, OIDC and a deployment target are available on day one.
- Two human source reviewers, one technical reviewer and one security/operator owner respond daily.
- Scope is one production-quality vertical slice and two launch dossiers—not nationwide automation.

## Elapsed-time estimate
| Outcome | Aggressive | Responsible |
|---|---:|---:|
| Local end-to-end engineering slice | 5–7 days | 7–10 days |
| Hardened staging | 10–14 days | 14–21 days |
| First controlled production pilot | 21–28 days | 4–6 weeks |
| Repeatable v1 with 3–5 partners | 8–12 weeks | 12–16 weeks |
| Multi-state connector platform | 6–9 months | 9–18 months |

## Why 72 hours is not production readiness
AI can compress implementation, test authoring and documentation. It cannot responsibly compress independent factual review, cloud permissions, DNS, security testing, restore drills, incident ownership, legal decisions, partner onboarding and real production observation.

## Critical path
1. Evidence invariants and public/private data boundary.
2. Production persistence, migrations and object storage.
3. Authentication, two-person publication gate and immutable audit path.
4. Secure document intake and extraction.
5. Public dossier/export/correction workflow.
6. Recovery, red-team, load and accessibility evidence.
7. Two real dossiers reviewed by humans.

## Staffing ceiling
Six to eight agents is useful. Beyond that, interface churn and merge conflicts dominate. Parallelize by bounded context; serialize schema, security policy and release decisions.

## Brutal promise
Do not promise “100% production-ready” on a date. Promise a dated evidence package showing which release gates passed on the target environment.
