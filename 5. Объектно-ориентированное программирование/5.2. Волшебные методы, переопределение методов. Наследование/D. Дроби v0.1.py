# Возможно, вы уже заметили, что дробные числа (float) недостаточно точные для некоторых задач. Для более точных математических расчётов иногда прибегают к созданию правильных рациональных дробей, описываемых числителем и знаменателем.
#
# Начнём разработку класса Fraction, который реализует предлагаемые дроби.
#
# Предусмотрите возможность инициализации дроби с помощью двух целых чисел или строки
# в формате <числитель>/<знаменатель>.
# В случаях наличия общего делителя у числителя и знаменателя, дробь следует сократить.
#
# А также реализуйте методы:
#
# numerator() — возвращает значение числителя;
# numerator(number) — изменяет значение числителя и производит сокращение дроби, если это необходимо;
# denominator() – возвращает значение знаменателя;
# denominator(number) — изменяет значение знаменателя и производит сокращение дроби, если необходимо;
# __str__ — возвращает строковое представление дроби в формате <числитель>/<знаменатель>;
# __repr__ — возвращает описание объекта в формате Fraction(<числитель>, <знаменатель>).
# Примечание
# Будем считать, что пользователь знает о запрете деления на ноль.
# Все числа в данной задаче будут положительными.
# Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть
# с использованием ведущих символов нижнего подчёркивания).
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

    def _reduce(self):
        gcd = math.gcd(self._x, self._y)
        self._x //= gcd
        self._y //= gcd

    def numerator(self, number=None):
        if number is None:
            return self._x
        else:
            self._x = number
            self._reduce()

    def denominator(self, number=None):
        if number is None:
            return self._y
        else:
            self._y = number
            self._reduce()

    def __str__(self):
        return f"{self._x}/{self._y}"

    def __repr__(self):
        return f"Fraction({self._x}, {self._y})"



