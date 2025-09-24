import pytest
from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Apple") == "ppl"
    assert shorten("") == ""
    assert shorten("AEIOU") == ""
    assert shorten("Rand0mWord") == "Rnd0mWrd"
    assert shorten("CS50!") == "CS50!"
    assert shorten("Hello!") == "Hll!"
