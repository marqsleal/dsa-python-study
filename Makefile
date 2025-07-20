PROJECT_NAME = warhammer-damage-calc
PYTHON_VERSION = 3.12
PYTHON_INTERPRETER = python


.PHONY: start
start:
	$(PYTHON_INTERPRETER)$(PYTHON_VERSION) -m venv venv
	. .venv/bin/activate && $(PYTHON_INTERPRETER) -m pip install -U pip
	. .venv/bin/activate && $(PYTHON_INTERPRETER) -m pip install -r requirements.txt


.PHONY: requirements
requirements:
	$(PYTHON_INTERPRETER) -m pip install -U pip
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt


.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +