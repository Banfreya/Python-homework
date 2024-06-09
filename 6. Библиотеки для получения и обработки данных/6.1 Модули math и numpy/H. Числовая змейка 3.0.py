# Когда-то вы помогали детсадовцам с различными змейками. Давайте реализуем её на основе массивов.
#
# Напишите функцию snake, которая принимает ширину (M) и высоту (N) змейки, а также именованный параметр direction.
#
# Параметр direction могут принимать значения:
#
# H — горизонтальная змейка, используется по умолчанию;
# V — вертикальная змейка.
# Функция должна вернуть матрицу, представляющую змейку, с ячейками типа int16.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
import numpy as np


def snake(M, N, direction='H'):
    matrix = np.zeros((N, M), dtype="int16")
    num = 1
    if direction == 'H':
        for column in range(N):
            if column % 2 == 0:
                for line in range(M):
                    matrix[column, line] = num
                    num += 1
            else:
                for line in range(M - 1, -1, -1):
                    matrix[column, line] = num
                    num += 1
    else:
        for line in range(M):
            if line % 2 == 0:
                for column in range(N):
                    matrix[column, line] = num
                    num += 1
            else:
                for column in range(N - 1, -1, -1):
                    matrix[column, line] = num
                    num += 1
    return matrix
