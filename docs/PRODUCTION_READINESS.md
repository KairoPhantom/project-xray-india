# Production readiness gate

## P0 checklist
- [ ] Named product, evidence, security and incident owners.
- [ ] Domain/HTTPS/WAF and secrets configured.
- [ ] Production database is not SQLite; migrations and connection pooling tested.
- [ ] Object storage encryption, lifecycle and quarantine enabled.
- [ ] OIDC/MFA for reviewers; least privilege.
- [ ] Rate limits, body limits and abuse controls.
- [ ] Backups and clean restore tested.
- [ ] Monitoring, alerting and on-call test completed.
- [ ] Privacy notice, retention schedule and correction/takedown process published.
- [ ] Threat model reviewed.
- [ ] Two-person factual review for each launch case.
- [ ] Clean-room install, tests and smoke path pass.
- [ ] Rollback artifact and procedure tested.
- [ ] SBOM, checksums, licence scan and release notes published.

## Honest release labels
- `alpha`: schema/workflow may change; not for real publication.
- `public beta`: working real service with disclosed limitations, not all production gates met.
- `v1 production`: every P0 gate passed and named operator accepts responsibility.
