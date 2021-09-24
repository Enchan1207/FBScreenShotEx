#
# makefile
#

.PNONY: __dummy__ build

__dummy__:
	@echo "make {build}"

build:
	pip install -r requirements.txt
