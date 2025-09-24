import pytest
from bank import value

def test_value():
    assert value("hello") ==0
    assert value("Hello") ==0 #case sensitivity
    assert value("HELLO") ==0 #cs pt2
    assert value("hi") == 20 #startswith h
    assert value("hola") == 20
    assert value("goodmorning") == 100
    assert value("BYE") == 100
