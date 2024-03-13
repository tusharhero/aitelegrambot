run: venv
	$(VENV)/python -m aitelegrambot
format: venv
	$(VENV)/python -m pip install black
	$(VENV)/python -m black src/aitelegrambot
build: venv
	rm -rf dist/*
	$(VENV)/python -m pip install build --upgrade
	$(VENV)/python -m build
upload: venv
	$(VENV)/python -m pip install --upgrade twine
	$(VENV)/python -m twine upload dist/*
include Makefile.venv
