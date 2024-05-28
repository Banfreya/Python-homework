# Давайте расширим функционал класса, написанного в прошлой задаче.
#
# Реализуйте методы:
#
# move, который перемещает точку на заданное расстояние по осям
# 𝑥
# x и
# 𝑦
# y;
# length, который определяет до переданной точки расстояние, округлённое до сотых.
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
