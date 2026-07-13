# Architecture

## Target production topology

```text
Browser/CDN/WAF
  -> Public web app
  -> API gateway
       -> application service
       -> job worker
       -> PostgreSQL
       -> private object storage (originals/quarantine)
       -> public redacted-object store
       -> append-only audit sink
       -> OCR/LLM provider through restricted adapter
```

## Trust boundaries
- Public browser is untrusted.
- Uploaded documents and crawled pages are hostile input.
- LLM output is untrusted candidate data.
- Reviewer identity is authenticated but actions remain auditable.
- Public exports must use an explicit allowlist.

## Evidence lifecycle
`received -> quarantined -> extracted -> candidate -> reviewed -> published -> corrected/withdrawn`

## Availability target for first release
- 99.5% monthly public-read availability.
- RPO 24 hours maximum; target 1 hour.
- RTO 4 hours maximum.
- Graceful read-only mode if write/worker dependencies fail.

## Scale assumptions
Initial: 10k projects, 1m claims, 100 concurrent public readers, 20 reviewer writes/minute. Optimize indexes and cache public dossiers; do not premature-microservice.
