import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/2") == 50
    assert convert("99/100") == 99
    assert convert("0/2") == 0
    assert convert("1/1") == 100

    with pytest.raises(ValueError):
        convert("4/2")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("b/2")
    with pytest.raises(ValueError):
        convert("4/-1")

    with pytest.raises(ValueError):
        convert("-1/4")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
