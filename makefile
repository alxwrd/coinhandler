test:
	pipenv run python -m pytest tests/

install:
	python3 -m pip install . --user

uninstall:
	python3 -m pip uninstall coinhandler

clean:
	rm -rf build/ dist/ ety.egg-info/  __pycache__/ */__pycache__/ .pytest_cache/
	rm -f *.pyc */*.pyc

build:
	pipenv run python setup.py sdist bdist_wheel

upload:
	pipenv run twine upload dist/*
