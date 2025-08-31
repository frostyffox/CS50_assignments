from assignments.L8_regex.numb3rs_dir.numb3rs import validate
import pytest

#test individual function
def test_validation():
    assert validate("22.11.33.44") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("1.22.3.44") == True

def test_invalid():
    assert validate("-1") == False
    assert validate("-2.-2.2") == False
    assert validate("abb.sss.fff.aaa") == False
    assert validate("") == False
    assert validate("23.1.44.3333") == False

def test_error():
    with pytest.raises(TypeError):
        validate()