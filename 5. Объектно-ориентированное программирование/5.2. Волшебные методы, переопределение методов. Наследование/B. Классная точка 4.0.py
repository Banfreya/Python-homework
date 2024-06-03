# А теперь модернизируем уже новый класс PatchedPoint. Реализуйте магические методы _str__ и _repr__.
#
# При преобразовании в строку точка представляется в формате (x, y).
# Репрезентация же должна возвращать строку для инициализации точки двумя параметрами.
#
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.

import math


class Point:
    def __init__(self, x, y, distance=0):
        self.x = x
        self.y = y
        self.distance = distance

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y
        return self.x, self.y

    def length(self, point):
        self.distance = round(math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2), 2)
        return self.distance


class PatchedPoint(Point):
    def __init__(self, x=0, y=0):
        if isinstance(x, tuple):
            x, y = x
        super().__init__(x, y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"

