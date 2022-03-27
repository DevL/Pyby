PYTHON_VERSION ?= 3.8

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
clean:
	rm -rf venv
	find . -name "*.pyc" -delete
