test:
	pipenv run python -m pytest tests/

install:
	python3 -m pip install . --user

uninstall:
	python3 -m pip uninstall coinhandler
