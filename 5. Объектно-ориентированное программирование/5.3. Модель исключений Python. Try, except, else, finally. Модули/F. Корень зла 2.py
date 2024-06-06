# В одной из первых лекций вы уже решали задачу о поиске корней уравнения. Давайте модернизируем её.
#
# Напишите функцию find_roots, принимающую три параметра: коэффициенты уравнения и возвращающую его корни
# в виде кортежа из двух значений.
#
# Так же создайте два собственных исключения NoSolutionsError и InfiniteSolutionsError, которые будут вызваны
# в случае отсутствия и бесконечного количества решений уравнения соответственно.
#
# Если переданные коэффициенты не являются рациональными числами, вызовите исключение TypeError.
#
# Примечание
# В решении не должно быть вызовов требуемых функций.

from fractions import Fraction


class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    if not all(isinstance(_, (int, float)) for _ in (a, b, c)):
        raise TypeError

    if a == 0 and b == 0 and c == 0:
        raise InfiniteSolutionsError

    if a == 0 and b == 0:
        raise NoSolutionsError

    if a == 0:
        root = -c / b
        return (root, root)

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        raise NoSolutionsError

    if discriminant == 0:
        root = -b / (2 * a)
        return (root, root)

    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    return tuple(sorted((x1, x2)))
