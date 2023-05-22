# ---------------------------- VARIABLE ----------------------------- #

BUILD  = .env/build
DEPLOY = .env/deploy

PY_PIP = bin/pip
PYTHON = bin/python

# ----------------------------- DEFAULT ----------------------------- #

.ONESHELL:
.DEFAULT_GOAL := make

make:
	make build
	make deploy
	make clean

# ------------------------------ BUILD ------------------------------ #

build:
	rm -rf $(BUILD)
	python -m venv $(BUILD)
	$(BUILD)/$(PY_PIP) install --quiet --upgrade pip build
	$(BUILD)/$(PYTHON) -m build -w

deploy:
	rm -rf $(DEPLOY)
	python -m venv $(DEPLOY)
	$(DEPLOY)/$(PY_PIP) install --quiet --upgrade pip -r requirements.txt
	$(DEPLOY)/$(PY_PIP) install --quiet --force-reinstall  dist/*.whl
	ls $(DEPLOY)/$(PY_PIP)

clean:
	rm -rf .env venv build *.egg-info .pytest_cache
	find . -name "*.pyc" -exec rm -f {} \;
	find . -name "__pycache__" -exec rmdir {} \;

# ----------------------------- INSTALL ----------------------------- #

system:
	which pip
	pip install --upgrade pip -r requirements.txt
	pip install --force-reinstall  dist/*.whl

# ------------------------------ SETUP ------------------------------ #

setup:
	python -m venv venv
	venv/$(PY_PIP) install --quiet --upgrade pip -r requirements-dev.txt
	venv/$(PY_PIP) install -e .
	rm -rf build *.egg-info
