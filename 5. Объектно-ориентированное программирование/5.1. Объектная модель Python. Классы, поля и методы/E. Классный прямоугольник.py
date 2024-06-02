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
        self.first_coordinates = (round(first_coordinates[0], 2), round(first_coordinates[1], 2))
        self.second_coordinates = (round(second_coordinates[0], 2), round(second_coordinates[1], 2))
        self.up_left_x = min(self.first_coordinates[0], self.second_coordinates[0])
        self.up_left_y = max(self.first_coordinates[1], self.second_coordinates[1])
        self.bottom_right_x = max(self.first_coordinates[0], self.second_coordinates[0])
        self.bottom_right_y = min(self.first_coordinates[1], self.second_coordinates[1])

    def get_size(self):
        first_side = round(abs(self.up_left_x - self.bottom_right_x), 2)
        second_side = round(abs(self.up_left_y - self.bottom_right_y), 2)
        return first_side, second_side

    def perimeter(self):
        first_side, second_side = self.get_size()
        return round(first_side * 2 + second_side * 2, 2)



