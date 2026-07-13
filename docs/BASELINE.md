# Verified reference baseline

Captured on 2026-07-14 IST from `project-xray-india-100x-2026-07-12.zip`.

- Archive SHA-256: `41dea6876f599190fc4568c473ea12a470c74cba31b269a6f66d5dc842710ba6` (matches the supplied checksum).
- Reference tests: `2 passed` using `python -m unittest discover -s tests -v`.
- Reference release checker: passed using `python scripts/check_release.py`.
- Readiness checker: `0/10` production checks passed; this is expected for the supplied reference implementation.

The reference service is a Python stdlib/SQLite application. It is not a production deployment and must remain labelled as a synthetic alpha until the applicable release evidence exists.
