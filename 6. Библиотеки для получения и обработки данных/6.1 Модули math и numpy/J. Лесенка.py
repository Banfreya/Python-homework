# Напишите функцию stairs, принимающую вектор и возвращающую матрицу,
# в которой каждая строка является копией вектора со смещением.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

import numpy as np


def stairs(vector):
    length = len(vector)
    result = np.zeros((length, length), dtype=vector.dtype)
    for number in range(length):
        result[number] = np.roll(vector, number)
    return result
