# Напишите функцию multiplication_matrix, которая принимает размер матрицы (N)
# и возвращает массив описывающий таблицу умножения
# 𝑁
# N на
# 𝑁
# N.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
import numpy as np


def multiplication_matrix(N):
    matrix = np.zeros((N, N), dtype="int32")
    for column in range(1, N + 1):
        for raw in range(1, N + 1):
            matrix[column - 1, raw - 1] = column * raw
    return matrix


