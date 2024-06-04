import math


class Fraction:
    def __init__(self, x, y=None):
        if isinstance(x, str):
            x, y = map(int, x.split('/'))
        self._x = x
        self._y = y
        self._reduce()

    def numerator_sign(self):
        return -1 if self._x < 0 else 1

    def _reduce(self):
        gcd = math.gcd(self._x, self._y)
        self._x //= gcd
        self._y //= gcd
        if self._y < 0:
            self._x = -self._x
            self._y = abs(self._y)

    def numerator(self, number=None):
        if number is None:
            return self._x * self._grebanyi_numerator_sign()
        else:
            self._x = number * self._grebanyi_numerator_sign()
        self._reduce()

    def denominator(self, number=None):
        if number is None:
            return self._y
        else:
            self._y = number
            self._reduce()

    def __neg__(self):
        return Fraction(-self._x, self._y)

    def __str__(self):
        return f"{self._x}/{self._y}"

    def __repr__(self):
        return f"Fraction('{self.__str__()}')"
