# Давайте перейдём к более сложным геометрическим фигурам.
#
# Разработайте класс Rectangle.
#
# При инициализации класс принимает два кортежа рациональных координат
# противоположных углов прямоугольника (со сторонами параллельными осям координат).
#
# Класс должен реализовывать методы:
#
# perimeter — возвращает периметр прямоугольника;
# area — возвращает площадь прямоугольника.
# Все результаты вычислений нужно округлить до сотых.
#
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.

class Rectangle:

    def __init__(self, first_coordinates, second_coordinates):
        self.first_coordinates = first_coordinates
        self.second_coordinates = second_coordinates
        self.first_side = abs(self.second_coordinates[0] - self.first_coordinates[0])
        self.second_side = abs(self.second_coordinates[1] - self.first_coordinates[1])

    def perimeter(self):
        return round(self.first_side * 2 + self.second_side * 2, 2)

    def area(self):
        return round(self.first_side * self.second_side, 2)