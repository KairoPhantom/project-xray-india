# Evidence and AI protocol

## AI authority ceiling
AI may classify, extract, translate, summarize, compare and suggest. AI may **not** publish, delete originals, approve evidence, infer guilt or decide that a record does not exist.

## Candidate contract
Every model output must include:
- model/provider/version and prompt-template digest;
- input artifact digest and page/span references;
- structured candidate values;
- confidence as model metadata, never truth probability;
- extraction warnings and unsupported fields;
- timestamp and run ID;
- reviewer status.

## Claim publication compiler
A claim is renderable publicly only when:
1. claim type and language policy are valid;
2. source record exists and is preserved;
3. exact passage/page anchor exists;
4. public derivative passes PII/redaction review;
5. reviewer one approves;
6. independent reviewer two approves real cases;
7. technical wording has qualified review when required;
8. contradictions and relevant official responses are linked;
9. actor and review timestamps are auditable.

## Prompt-injection boundary
- Documents are data, never instructions.
- Extraction runs with fixed schemas and no tools/network/publication authority.
- Document text is delimited and never concatenated into system instructions.
- Output is schema-validated and stored as candidate.
- Adversarial fixtures include “ignore policy,” tool-call requests and fabricated citations.

## Evaluation suite
Build a versioned corpus stratified by born-digital/scanned, English/Hindi/Marathi, tables, stamps, low resolution and mixed scripts. Measure page-anchor accuracy, field precision/recall, table fidelity, abstention, citation validity, PII leakage and reviewer correction time. Do not select a model on one aggregate score.

## Model portability
Use a provider-neutral adapter. Store normalized candidate output and run metadata, not provider-specific reasoning. Require an offline/degraded deterministic path for critical reads.
