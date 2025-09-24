from working import convert
import pytest

#check if conversion works
def test_conversions():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("4:10 AM to 9:50 PM") == "04:10 to 21:50"

#raise errors because of format
def test_format():
    #separators
    #missing period
    #invalid period
    #missing separator
    with pytest.raises(ValueError):
        convert("3AM-4AM")
    with pytest.raises(ValueError):
        convert("3 to 7")
    with pytest.raises(ValueError):
        convert("3 NM to 4 LN")
    with pytest.raises(ValueError):
        convert("3AMtoAM")

#raise errors because of values
def test_values():
    with pytest.raises(ValueError):
        convert("0 AM to 55 PM")
    with pytest.raises(ValueError):
        convert("3:59 AM to 77:00 PM")
  