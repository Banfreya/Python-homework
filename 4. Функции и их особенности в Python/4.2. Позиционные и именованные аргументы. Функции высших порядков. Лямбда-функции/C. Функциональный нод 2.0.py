import math
from functools import reduce
from collections.abc import Iterable

# Напишите функцию gcd, которая вычисляет наибольший
# общий делитель последовательности чисел.
# Параметрами функции выступают натуральные числа
# в произвольном количестве, но не менее одного.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.


def gcd(*args):
    if len(args) == 1 and isinstance(args[0], int):
        return args[0]
    elif len(args) == 1 and isinstance(args[0], Iterable):
        numbers = args[0]
    else:
        numbers = args
    return reduce(math.gcd, numbers)
