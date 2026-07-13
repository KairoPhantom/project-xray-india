run:
	python3 app/server.py

test:
	python3 -m unittest discover -s tests -v

check:
	python3 scripts/check_release.py

smoke:
	python3 scripts/smoke_e2e.py

verify-audit:
	python3 scripts/verify_audit.py $${DB_PATH:-data/project_xray.db}

backup:
	python3 scripts/recovery.py backup $${DB_PATH:-data/project_xray.db} backups/project_xray.db

package:
	./scripts/create_release.sh
