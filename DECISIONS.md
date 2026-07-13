# Architecture decision log

## ADR-001 — Evidence engine, not corruption detector
**Date:** 2026-07-12  
**Decision:** Classify and connect evidence; do not predict guilt.  
**Reason:** Reduces defamation, hallucination and false-positive risk.

## ADR-002 — No real payment movement in v0.1
**Date:** 2026-07-12  
**Decision:** Generate payment-readiness evidence only in later phases.  
**Reason:** Payment authority, financial regulation and oracle verification are outside a 72-hour scope.

## ADR-003 — Standards-first
**Date:** 2026-07-12  
**Decision:** Plan compatibility with OCDS, OC4IDS and FollowTheMoney.  
**Reason:** Avoid a closed India-only ontology.

## ADR-004 — Dependency-light reference slice
**Date:** 2026-07-12  
**Decision:** Ship an offline-runnable SQLite/stdlib reference implementation with migration path.  
**Reason:** Guarantees reproducible startup while Codex builds the hardened target stack.
