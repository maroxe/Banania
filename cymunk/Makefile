.PHONY: build all

all: build 

build:
	rm __init__.py || true
	python setup.py build_ext --inplace -f
	touch __init__.py
