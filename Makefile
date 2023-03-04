# Settings
PYTHON_VERS = 3.9 # Need to respect the XX.X format
VENV_DIR = .venv # Virtual environnement's folder name

# /!\ DO NOT CHANGE THOSE
PYTHON = python$(PYTHON_VERS)
MAIN = src/main.py
VENV_BIN = $(VENV_DIR)/bin/activate
VENV_ON = . $(VENV_BIN);
REQUIREMENTS = .py_requirements

.PHONY: all game help print venv clean

all: game

game: venv
	@echo "make: Launching game"
	@$(VENV_ON) python $(MAIN)

help:
	@echo "~ Useful ~"
	@echo "$$ make          - Launch the game"
	@echo "$$ make game     - Same as '$$ make'"
	@echo "$$ make help     - Prints out all make commands"
	@echo "$$ make clean    - Cleanse all trash files and the virtual environnement"
	
	@echo ""
	@echo "~ Advanced ~"
	@echo "$$ make print    - Display the python version of your virtual environnement"
	@echo "$$ make venv     - Create the virtual environnement and install all the requirements"

print:
	@$(VENV_ON) python --version

venv:
	@$(PYTHON) -m venv $(VENV_DIR) > /dev/null
	@echo "make: Virtual environnement created at '$(VENV_DIR)' with '$(PYTHON)'."
	@$(VENV_ON) pip install --upgrade pip setuptools wheel > /dev/null
	@echo "make: Virtual environnement's pip, setuptools and wheel updated."
	@$(VENV_ON) pip install -r $(REQUIREMENTS) > /dev/null
	@echo "make: Virtual environnement's requierements installed."

clean:
	@$(RM) -r $(VENV_DIR)
	@echo "make: Virtual environnement directory cleaned."
	@find -iname "*.pyc" -delete > /dev/null
	@find -iname "__pycache__" -delete > /dev/null
	@echo "make: '__pycache__' directories and '*.pyc' files cleaned."
