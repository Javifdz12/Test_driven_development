import pytest
from factorial import factorial
def test_myfactorial():
    assert factorial(3) == 6
def test_myfactorialneg():
    assert factorial(-1)=='No existe el factorial de un numero negativo'
