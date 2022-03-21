# ----------------------------------
#          INSTALL & TEST
# ----------------------------------
install_requirements:
	@pip install -r requirements.txt

check_code:
	@flake8 tftemplates/**.py

black:
	@black tftemplates/**

test:
	@coverage erase
	@coverage run -m pytest tests -W ignore::DeprecationWarning
	@coverage report -m -i
ftest:
	@Write me

clean:
	@rm -f */version.txt
	@rm -f .coverage
	@rm -fr */__pycache__ */*.pyc __pycache__
	@rm -fr build dist
	@rm -fr tftemplates-*.dist-info
	@rm -fr tftemplates.egg-info

install:
	@pip install . -U

all: clean test black check_code
