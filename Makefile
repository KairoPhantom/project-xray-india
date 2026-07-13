run:
	python3 app/server.py

test:
	python3 -m unittest discover -s tests -v

check:
	python3 scripts/check_release.py

package:
	./scripts/create_release.sh
