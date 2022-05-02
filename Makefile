PYTHON_VERSION ?= 3.8

dist: clean-dist
	python3 setup.py sdist bdist_wheel

venv: dev-packages.txt
	virtualenv venv --python=${PYTHON_VERSION}
	. venv/bin/activate && pip3 install --upgrade pip && pip3 install -r dev-packages.txt

.PHONY: test
test: venv
	@ . venv/bin/activate && PYTHONPATH=src/ pytest -rsx tests/ src/ --doctest-modules --doctest-continue-on-failure
	@ . venv/bin/activate && flake8 src tests --exclude '#*,~*,.#*'

.PHONY: focus-test
focus-test: venv
	@ . venv/bin/activate && PYTHONPATH=src/ pytest -vv -m focus -rsx tests/
	@ . venv/bin/activate && flake8 src tests --exclude '#*,~*,.#*'

.PHONY: clean
clean: clean-dist
	rm -rf venv
	find . -name "*.pyc" -delete

.PHONY: clean-dist
clean-dist:
	rm -rf build
	rm -rf src/pyby.egg-info
	rm -rf dist
