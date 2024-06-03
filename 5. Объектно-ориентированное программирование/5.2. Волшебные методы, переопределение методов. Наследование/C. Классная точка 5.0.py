# Согласитесь, что использовать операторы куда удобнее, чем обыкновенные методы. Давайте вспомним
# о реализованном нами методе move(x, y) и напишем ему альтернативу в виде операторов + и +=.
#
# При выполнении кода point + (x, y), создаётся новая точка, которая отличается от изначальной
# на заданное кортежем расстояние по осям x и y.
# При выполнении кода point += (x, y) производится перемещение изначальной точки.
#
# Напомним, что сейчас мы модернизируем только класс PatchedPoint.
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

    def __add__(self, other):
        return PatchedPoint(self.x + other[0], self.y + other[1])

    def __iadd__(self, other):
        self.move(other[0], other[1])
        return self
