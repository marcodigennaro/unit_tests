import math_funct
import pytest

@pytest.mark.parametrize('n1, n2, result',
                         [
                             (7, 3, 10),
                             ('Hello', 'World', 'HelloWorld'),
                             (1.3, 2.7, 4.0),
                         ])
def test_add(n1, n2, result):
    assert math_funct.add(n1, n2) == result