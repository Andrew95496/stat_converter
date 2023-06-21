ifeq ($(OS), Windows_NT)
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
.DEFAULT_GOAL := run

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
