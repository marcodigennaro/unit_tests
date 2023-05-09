import math_funct
import pytest
import sys
print(sys.version)
@pytest.mark.number
def test_add():
    assert math_funct.add(7, 3) == 10

@pytest.mark.number
def test_add_one_arg():
    assert math_funct.add(7) == 9

@pytest.mark.number
def test_prod():
    assert math_funct.product(2, 6) == 12
    print('--- test_prod() executed ---')

@pytest.mark.skipif(sys.version_info > (2, 5), reason='skip if version is older than (2,5)')
def test_prod_one_arg():
    assert math_funct.product(4) == 8

@pytest.mark.string
def test_add_strings():
    assert math_funct.add('Hello', 'World') == 'HelloWorld'

@pytest.mark.string
def test_add_strings_is_string():
    assert type(math_funct.add('x'  , 'y')) is str

@pytest.mark.skip(reason='demonstrate skipping marker')
def test_prod_strings():
    assert math_funct.product('Hello') == 'HelloHello'