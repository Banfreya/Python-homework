# Напишите функцию make_matrix, которая создаёт,
# заполняет и возвращает матрицу заданного размера.
#
# Параметры функции:
#
# size — кортеж (ширина, высота) или одно число
# (для создания квадратной матрицы);
# value — значение элементов списка (по-умолчанию 0).
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций

def make_matrix(size, value=0):
    if isinstance(size, int):
        return [[value for i in range(size)] for j in range(size)]
    elif isinstance(size, tuple):
        return [[value for i in range(size[0])] for j in range(size[1])]

