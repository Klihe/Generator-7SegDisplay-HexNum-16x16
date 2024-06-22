SRC = src//main.py
OS := $(shell uname -s)

ifeq ($(OS),Windows_NT)
	PYTHON = python
else
	PYTHON = python3
endif

all: run

run:
	$(PYTHON) $(SRC)