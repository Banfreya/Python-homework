# Необходимо ещё немного доработать предыдущую задачу.
#
# Разработайте методы:
#
# turn() — поворачивает прямоугольник на 90&deg; по часовой стрелке вокруг его центра;
# scale(factor) — изменяет размер в указанное количество раз, тоже относительно центра.
# Все вычисления производить с округлением до сотых.
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

    def area(self):
        first_side, second_side = self.get_size()
        return round(first_side * second_side, 2)

    def get_pos(self):
        return self.up_left_x, self.up_left_y

    def move(self, dx, dy):
        self.up_left_x = round(self.up_left_x + dx, 2)
        self.up_left_y = round(self.up_left_y + dy, 2)
        self.bottom_right_x = round(self.bottom_right_x + dx, 2)
        self.bottom_right_y = round(self.bottom_right_y + dy, 2)

    def resize(self, width, height):
        self.bottom_right_x = round(self.up_left_x + width, 2)
        self.bottom_right_y = round(self.up_left_y - height, 2)
        if self.up_left_x > self.bottom_right_x:
            self.up_left_x, self.bottom_right_x = self.bottom_right_x, self.up_left_x
        if self.up_left_y < self.bottom_right_y:
            self.up_left_y, self.bottom_right_y = self.bottom_right_y, self.up_left_y

    def turn(self):
        center_x = round((self.up_left_x + self.bottom_right_x) / 2, 2)
        center_y = round((self.up_left_y + self.bottom_right_y) / 2, 2)
        first_side, second_side = self.get_size()
        self.up_left_x = round(center_x - second_side / 2, 2)
        self.up_left_y = round(center_y + first_side / 2, 2)
        self.bottom_right_x = round(center_x + second_side / 2, 2)
        self.bottom_right_y = round(center_y - first_side / 2, 2)

    def scale(self, factor):
        center_x = round((self.up_left_x + self.bottom_right_x) / 2, 2)
        center_y = round((self.up_left_y + self.bottom_right_y) / 2, 2)
        first_side, second_side = self.get_size()
        new_first_side = round(first_side * factor, 2)
        new_second_side = round(second_side * factor, 2)
        self.up_left_x = round(center_x - new_first_side / 2, 2)
        self.up_left_y = round(center_y + new_second_side / 2, 2)
        self.bottom_right_x = round(center_x + new_first_side / 2, 2)
        self.bottom_right_y = round(center_y - new_second_side / 2, 2)
