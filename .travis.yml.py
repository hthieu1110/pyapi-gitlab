language: python
python:
  - "2.6"
  - "2.7"
# command to install dependencies
install: "python setup.py install"
# command to run tests
script: "python tests/test.py"