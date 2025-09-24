from cookiejar import Jar
import pytest

def test_init():
    jar = Jar(7)
    assert jar.capacity == 7
    assert jar.size == 0
    with pytest.raises(ValueError):
        Jar(-1) #not > 0
    with pytest.raises(ValueError):
        Jar("a") #not a number

def test_deposit():
    jar = Jar(8)
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(1)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.deposit(11)

def test_withdraw():
    jar = Jar(4)
    jar.deposit(3)
    jar.withdraw(2)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(6)

def test_str():
    jar = Jar(5)
    jar.deposit(2)
    assert str(jar) == "🍪🍪"

