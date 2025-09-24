from regular import count
import pytest

def test_empty_isolate():
    
    assert count("") == 0
    assert count("um") == 1
    assert count("um, um") == 2
    assert count(" um UM um ") ==3

def test_punct_bound():
    assert count("umido") != 1
    assert not count("uhm") == 2
    assert count("um?") != 0
    assert count("umano") == 0

def test_multi():
    assert count("um um um ") != 0
    assert count("uhm um, right, um") == 2
    assert count("umumus") == 0


