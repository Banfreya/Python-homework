# Напишите функцию only_positive_even_sum, которая принимает два параметра и возвращает их сумму.
#
# Если один из параметров не является целым числом, то следует вызвать исключение TypeError.
# Если один из параметров не является положительным чётным числом, то следует вызвать исключение ValueError.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

def only_positive_even_sum(*args):
    for arg in args:
        if not isinstance(arg, int):
            raise TypeError
    for arg in args:
        if arg <= 0 or arg % 2 != 0:
            raise ValueError
    return sum(args)

