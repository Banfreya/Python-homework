# Продолжим разработку класса Fraction, который реализует предлагаемые дроби.
#
# Реализуйте бинарные операторы:
#
# + — сложение дробей, создаёт новую дробь;
# - — вычитание дробей, создаёт новую дробь;
# += — сложение дробей, изменяет дробь, переданную слева;
# -= — вычитание дробей, изменяет дробь, переданную слева.
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
            x, y = map(int, x.split('/'))
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
        x = self._x * other._y + other._x * self._y
        y = self.denominator() * other.denominator()
        return Fraction(x, y)

    def __sub__(self, other) -> 'Fraction':
        x = self._x * other._y - other._x * self._y
        y = self.denominator() * other.denominator()
        return Fraction(x, y)

    def __iadd__(self, other) -> 'Fraction':
        self._x = self._x * other._y + other._x * self._y
        self._y = self.denominator() * other.denominator()
        self._reduce()
        return self

    def __isub__(self, other) -> 'Fraction':
        self._x = self._x * other._y - other._x * self._y
        self._y = self.denominator() * other.denominator()
        self._reduce()
        return self

