# README
# options for pytest

pytest
py.test # equivalent
pytest -v # verbose
pytest test_math.py::test_add_strings # run only one
pytest -k "add and string"
pytest -k "add or prod"
pytest -m "number" #create pytest.ini for markers
pytest --markers #list all markers
pytest -x #exit after failure
pytest --tb 'no' #shows less
pytest -v -rsx #summary of skipping tests
pytest -s # show "print" statements
pytest -q # quiet run

pytest -v test_parameterize_decorator.py #mind to pass the argument as a single string