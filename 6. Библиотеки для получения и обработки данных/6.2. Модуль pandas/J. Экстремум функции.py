# Экстремум в математике — максимальное или минимальное значение функции на заданном множестве.
#
# Чаще всего математики для поиска экстремума функции прибегают к её дифференцированию.
# Однако мы можем обойти этот трудоёмкий процесс и схитрить.
#
# Напишите три функции:
#
# values(func, start, end, step), строящую Series значений функции в точках диапазона и принимающую:
# функцию одной переменной;
# начало диапазона;
# конец диапазона;
# шаг вычисления;
# min_extremum(data) возвращает точку, в которой был достигнут минимум на диапазоне;
# max_extremum(data) возвращает точку, в который был достигнут максимум на диапазоне.
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
import pandas as pd
import numpy as np


def values(func, start, end, step):
    x_values = np.arange(start, end + step, step)
    y_values = [func(x) for x in x_values]
    return pd.Series(y_values, index=x_values)


def min_extremum(data):
    return data.idxmin()


def max_extremum(data):
    return data.idxmax()
