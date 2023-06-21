run:
	python3 void/VOID.python

install:
	pip3 install -r requirements.txt

build:
	python3 setup.py build

clean:
	rm /s /q build
	rm /s /q VOID.egg_info

