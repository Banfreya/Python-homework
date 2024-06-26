# Объектно-ориентированное программирование — популярная парадигма
# в современном мире. Это вполне очевидно, ведь любой объект реального
# мира мы теперь можем представить в виде цифрового набора полей и методов.
# Давайте приступим к проектированию классов.
#
# Разработайте класс Point, который при инициализации принимает координаты
# точки на декартовой плоскости и сохраняет их в поля x и y соответственно.
#
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
