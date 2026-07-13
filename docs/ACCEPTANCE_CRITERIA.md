# Definition of done

A release is not complete until all P0 checks pass.

## Functional
- Complete create-to-public-dossier-to-export path works.
- Real persistence survives restart.
- Backup restore is demonstrated.
- Every public claim has provenance and review metadata.
- Official responses can be linked and displayed.
- Corrections are versioned.

## Security/privacy
- Deployed writes require real authentication and authorization.
- No default credentials.
- HTTPS and secure headers verified.
- Upload limits/quarantine/scanning configured.
- Secrets/static/dependency scans pass or documented risk is accepted.
- Public API allowlist prevents private fields.
- Incident and privacy contacts exist.

## Reliability
- Health/readiness endpoints; structured logs; alert tested.
- Migration and rollback tested.
- RPO/RTO restore tested.
- Load test meets declared launch capacity.

## Editorial
- Two launch dossiers receive two-person source review.
- No synthetic content is presented as real.
- Every “missing” record includes search scope/date.
- Right-to-respond and correction route visible.

## Open source
- Clean clone starts from README.
- Licence, contribution, governance, security and code-of-conduct files present.
- SBOM/checksums/release notes generated.
- Third-party licences reviewed.
