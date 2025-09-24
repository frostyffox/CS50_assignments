from seasons import number_to_words

def test_number_to_words_basic():
    assert number_to_words(0) == "Zero"
    assert number_to_words(1) == "One"
    assert number_to_words(10) == "Ten"
    assert number_to_words(15) == "Fifteen"

def test_number_to_words_tens():
    assert number_to_words(20) == "Twenty"
    assert number_to_words(25) == "Twenty-five"
    assert number_to_words(30) == "Thirty"
    assert number_to_words(42) == "Forty-two"

def test_number_to_words_hundreds():
    assert number_to_words(100) == "One hundred"
    assert number_to_words(101) == "One hundred one"
    assert number_to_words(115) == "One hundred fifteen"
    assert number_to_words(365) == "Three hundred sixty-five"

def test_number_to_words_thousands():
    assert number_to_words(1000) == "One thousand"
    assert number_to_words(1001) == "One thousand one"
    assert number_to_words(2010) == "Two thousand ten"

def test_number_to_words_large_numbers():
    assert number_to_words(525600) == "Five hundred twenty-five thousand, six hundred"
    assert number_to_words(1051200) == "One million, fifty-one thousand, two hundred"
