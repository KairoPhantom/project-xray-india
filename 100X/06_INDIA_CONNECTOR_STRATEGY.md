# India source connector strategy

## Start narrow
Choose one state/authority and one infrastructure class. Map the complete document lifecycle before adding breadth.

## Source tiers
1. Official project/authority pages and signed records.
2. CPPP/eProcurement/GeM tender and award records.
3. Audit, legislature, court and regulator records.
4. RTI disclosures and authority correspondence.
5. Credible reporting and expert reports.
6. Public submissions, retained privately until verified.

## Connector contract
Each connector declares owner, lawful basis/terms review, robots/rate policy, source timezone, identifiers, pagination, expected document types, field mapping, retry behavior, change detector, parser version, coverage limits and last successful verification.

## Connector observatory
Publish operational facts, not blame:
- retrieval success rate;
- schema-change incidents;
- median staleness;
- percentage with award documents;
- percentage with machine-readable identifiers;
- known blind spots;
- terms/licensing status.

## Anti-overclaim controls
Portal disclaimers and source incompleteness must be preserved. “No result” becomes “not located in connector X using query Y at time Z.” Cross-portal mismatches become review prompts, not accusations.

## First connector sequence
1. Manual upload and URL snapshot.
2. CPPP project/tender metadata adapter.
3. One selected state e-procurement adapter.
4. Authority website snapshot adapter.
5. RTI response intake.
6. OC4IDS export and validation.

Every automated source requires fixture-based contract tests and a kill switch.
