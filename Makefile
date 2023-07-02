#TODO: Add venv
#TODO: Add user input for venv

ifeq ($(OS), Windows_NT)

.ONESHELL:

.DEFAULT_GOAL := run

run:
	python void/VOID.py

install:
	pip install -r requirements.txt

build:
	python setup.py build

clean:
	if exist "./build" rd /s /q build
	if exist "./VOID.egg_info" rd /s /q VOID.egg_info
else
.ONESHELL:

.DEFAULT_GOAL := run
#venv/bin/activate: requirements.txt
#	VENV ?= $(shell bash -c 'read -p "venv name: " venv;')
#	python3 -m venv VENV
#	chmod +x venv/bin/activate
#	$(PIP) install -r requirements.txt

#venv: venv/bin/activate
#	. .venv/bin/activate
run: 
	python3 void/VOID.py

install:
	pip3 install -r requirements.txt

build:
	python3 setup.py build

clean:
	rm -rf build
	rm -rf VOID.egg_info
endif
