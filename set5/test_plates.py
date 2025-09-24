import pytest
from plates import is_valid

def test_is_valid():
    assert is_valid("CS50") is True
    assert is_valid("CS05") is False
    assert is_valid("CS50P") is False
    assert is_valid("OUTATIME") is False
    assert is_valid("PI3.14") is False
    assert is_valid("C") is False
    assert is_valid("Y44") is False
    assert is_valid("CS500") is True
