
# Лаборанты проводят эксперимент и запросили разработку
# системы обработки данных. Результатами эксперимента
# должны стать пары рациональных чисел.
#
# Для работы им требуются функции:
#
# enter_results(first, second, ...) — добавление данных
# одного или нескольких результатов (гарантируется, что
# количество параметров будет чётным);
# get_sum() — возвращает пару сумм результатов экспериментов;
# get_average() — возвращает пару средних арифметических з
# начений результатов экспериментов.
# Все вычисления производятся с точностью до сотых.
#
# Примечание
# В решении не должно быть вызовов требуемых функций.



values = []
odd_indices = []
even_indices = []


def enter_results(*nums):
    global values, odd_indices, even_indices
    values.extend(nums)
    odd_indices = values[::2]
    even_indices = values[1::2]


def get_sum():
    return round(sum(odd_indices), 2), round(sum(even_indices), 2)


def get_average():
    odd_avg = round(sum(odd_indices) / len(odd_indices), 2) if odd_indices else 0
    even_avg = round(sum(even_indices) / len(even_indices), 2) if even_indices else 0
    return odd_avg, even_avg
