# Напишите функцию rotate, принимающую двумерную матрицу и один из углов поворота: 90°, 180°, 270° и 360°.
#
# Функция должна вернуть новую матрицу соответствующую заданному повороту по часовой стрелке.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

import numpy as np


def rotate(matrix, angle):
    if angle == 90:
        return np.rot90(matrix, -1)
    elif angle == 180:
        return np.rot90(matrix, 2)
    elif angle == 270:
        return np.rot90(matrix, 1)
    elif angle == 360:
        return np.array(matrix)
