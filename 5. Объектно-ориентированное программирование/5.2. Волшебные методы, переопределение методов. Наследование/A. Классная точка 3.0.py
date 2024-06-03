# Давайте расширим функционал класса, написанного вами в задаче «Классная точка 2.0».
#
# Создайте класс PatchedPoint — наследника уже написанного вами Point.
#
# Требуется реализовать следующие виды инициализации нового класса:
#
# параметров не передано — координаты точки равны 0;
# передан один параметр — кортеж с координатами точки;
# передано два параметра — координаты точки.
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
