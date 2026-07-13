# Parallel-agent operating system

## Workstreams
A. Domain/data model; B. API/auth; C. ingestion/workers; D. reviewer/public UX; E. infrastructure/observability; F. tests/security/release.

## Rules
- one integration lead owns architecture and release gate;
- one branch/worktree per issue;
- no two agents edit the same migration or API contract concurrently;
- state acceptance test before coding;
- deterministic tests before model-assisted features;
- every integration change runs smoke, migration and public-field-leak tests;
- agents cannot self-approve factual content or security risk acceptance;
- merge only green commits with a brief evidence record;
- keep a live interface registry and decision log;
- stop the line on unsupported publication, PII leak, mutable audit, broken restore or undocumented startup.

## Checkpoint cadence
- every 2 hours: branch status and blockers;
- every 6 hours: integrate, full suite and smoke path;
- daily: clean-environment deploy and release-gate snapshot;
- twice weekly after launch: restore drill or failure injection;
- after material schema change: threat-model and migration review.

## Human decision queue
Domain language, source policy, legal basis, privacy/redaction, production risk acceptance, release label and real-case publication always require named humans.

## Agent deliverable format
Issue, acceptance test, files changed, commands/results, security/evidence implications, migration/rollback, known limits and next dependency.
