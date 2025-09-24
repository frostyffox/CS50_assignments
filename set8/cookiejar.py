
class Jar:

    #Initialise the jar
    def __init__(self, capacity=12):
        #capacity: int, >0
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError()
        self._capacity = capacity
        self._cookies = 0 #init to 0

    #method: return cookies size times
    def __str__(self):
        return "🍪" * self._cookies

    #ADD AND REMOVE COOKIES TO THE JAR
    #pay attention to capacity and min number
    def deposit(self, n):
        if self._cookies + n > self._capacity:
            raise ValueError("too many cookies")
        self._cookies += n

    def withdraw(self, n):
        if n > self._cookies:
            raise ValueError("too few cookies")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies

