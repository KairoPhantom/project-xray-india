# Reuse, integrate or study — do not rebuild the ecosystem

| Need | Candidate | Decision | Boundary |
|---|---|---|---|
| Contract/project standards | OCDS + OC4IDS | Adopt schemas/mappings | Keep local evidence extensions namespaced. |
| Investigative entity model | FollowTheMoney | Integrate later | Use for organization/person relationships, not core project workflow. |
| Large investigative search | OpenAleph/Aleph patterns | Study/integrate | Do not recreate a general-purpose investigative data lake. |
| Document parsing | Docling | Adapter + benchmark | Never trust extraction without exact source anchors. |
| Searchable scan layer | OCRmyPDF | Reuse | Preserve original; OCR output is derivative. |
| Indic OCR | PaddleOCR/Tesseract options | Benchmark | Select per-language and document class, not hype. |
| Malware scanning | ClamAV + managed option | Defense layer | A clean verdict is not proof of safety; keep parser sandboxing. |
| Object storage | Managed S3; S3-compatible locally | Adopt interface | Avoid hard dependency on one self-hosted product/licence. |
| Tamper-evident release | Sigstore/Cosign/Rekor | Adopt for software artifacts | Evidence audit anchoring requires a separate privacy-aware design. |
| Immutable audit DB | PostgreSQL append-only + external checkpoints | Start simple | Evaluate immudb only if threat model justifies operational cost. |
| Sanctions/entity enrichment | OpenSanctions | Optional adapter | Never equate a match with wrongdoing; licence and false-positive review required. |
| Geospatial | PostGIS | Adopt when needed | Store source geometry and precision metadata. |

## Build ourselves
- evidence-state transition engine;
- publication compiler and public-field allowlist;
- search-scope ledger;
- contradiction and correction model;
- evidence envelope and dossier capsule;
- India infrastructure connector manifests;
- reviewer UX and policy-as-code;
- benchmark corpus for Indian public records.

## Dependency admission checklist
Before adding a repository: active maintenance, licence compatibility, security history, reproducible build, data egress, model weights/licence, deployment cost, graceful replacement and benchmark performance on our corpus.
