ifeq ($(OS), Windows_NT)
run:
	python void/VOID.python

install:
	pip install -r requirements.txt

build:
	python setup.py build

clean:
	if exist "./build" rd /s /q build
	if exist "./VOID.egg_info" rd /s /q VOID.egg_info
else
run:
	python3 void/VOID.python

install:
	pip3 install -r requirements.txt

build:
	python3 setup.py build

clean:
	rm -rf build
	rm -rf VOID.egg_info

endif
