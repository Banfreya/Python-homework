# Остался последний штрих!" Правда звучит как издевательство?
#
# Мы «научили» наши дроби работать с целыми числами и вот теперь надо
# провернуть обратное действие. Реализуйте функционал, который позволит
# производить все арифметические операции с дробями и числами, независимо
# от их положения (слева или справа) в операторе.
#
# Примечание
# Будем считать, что пользователь знает о запрете деления на ноль.
# Все поля и методы, не требуемые в задаче, следует инкапсулировать
# (называть с использованием ведущих символов нижнего подчёркивания).
#
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.
import math


class Fraction:
    def __init__(self, x, y=None):
        if isinstance(x, str):
            if '/' in x:
                x, y = map(int, x.split('/'))
            else:
                x, y = int(x), 1
        elif y is None:
            x, y = x, 1
        self._x = x
        self._y = y
        self._reduce()

    def _grebanyi_numerator_sign(self):
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

    def __add__(self, other) -> 'Fraction':
        if isinstance(other, int):
            other = Fraction(other)
        x = self._x * other._y + other._x * self._y
        y = self.denominator() * other.denominator()
        return Fraction(x, y)

    def __sub__(self, other) -> 'Fraction':
        if isinstance(other, int):
            other = Fraction(other)
        x = self._x * other._y - other._x * self._y
        y = self.denominator() * other.denominator()
        return Fraction(x, y)

    def __iadd__(self, other) -> 'Fraction':
        if isinstance(other, int):
            other = Fraction(other)
        self._x = self._x * other._y + other._x * self._y
        self._y = self.denominator() * other.denominator()
        self._reduce()
        return self

    def __isub__(self, other) -> 'Fraction':
        if isinstance(other, int):
            other = Fraction(other)
        self._x = self._x * other._y - other._x * self._y
        self._y = self.denominator() * other.denominator()
        self._reduce()
        return self

    def reverse(self) -> 'Fraction':
        return Fraction(self._y, self._x)

    def __mul__(self, other) -> 'Fraction':
        if isinstance(other, int):
            other = Fraction(other)
        new_fraction = Fraction(1, 1)
        new_fraction._x = self._x * other._x
        new_fraction._y = self._y * other._y
        new_fraction._reduce()
        return new_fraction

    def __truediv__(self, other) -> 'Fraction':
        if isinstance(other, int):
            other = Fraction(other)
        new_fraction = Fraction(self._x, self._y)
        new_fraction._reduce()
        return new_fraction.__mul__(other.reverse())

    def __imul__(self, other) -> 'Fraction':
        if isinstance(other, int):
            other = Fraction(other)
        self._x = self._x * other._x
        self._y = self._y * other._y
        self._reduce()
        return self

    def __itruediv__(self, other) -> 'Fraction':
        if isinstance(other, int):
            other = Fraction(other)
        return self.__imul__(other.reverse())

    def __gt__(self, other) -> bool:
        if isinstance(other, int):
            other = Fraction(other)
        return self._x * other._y > other._x * self._y

    def __lt__(self, other) -> bool:
        if isinstance(other, int):
            other = Fraction(other)
        return self._x * other._y < other._x * self._y

    def __ge__(self, other) -> bool:
        if isinstance(other, int):
            other = Fraction(other)
        return self._x * other._y >= other._x * self._y

    def __le__(self, other) -> bool:
        if isinstance(other, int):
            other = Fraction(other)
        return self._x * other._y <= other._x * self._y

    def __eq__(self, other) -> bool:
        if isinstance(other, int):
            other = Fraction(other)
        return self._x * other._y == other._x * self._y

    def __ne__(self, other) -> bool:
        if isinstance(other, int):
            other = Fraction(other)
        return self._x * other._y != other._x * self._y

    def __radd__(self, other) -> 'Fraction':
        return self.__add__(other)

    def __rsub__(self, other) -> 'Fraction':
        return -self.__sub__(other)

    def __rmul__(self, other) -> 'Fraction':
        return self.__mul__(other)

    def __rtruediv__(self, other) -> 'Fraction':
        return self.__truediv__(other).reverse()

    def __rgt__(self, other) -> bool:
        return self.__gt__(other)

    def __rlt__(self, other) -> bool:
        return self.__lt__(other)

    def __rge__(self, other) -> bool:
        return self.__ge__(other)

    def __rle__(self, other) -> bool:
        return self.__le__(other)

    def __req__(self, other) -> bool:
        return self.__eq__(other)

    def __rne__(self, other) -> bool:
        return self.__ne__(other)