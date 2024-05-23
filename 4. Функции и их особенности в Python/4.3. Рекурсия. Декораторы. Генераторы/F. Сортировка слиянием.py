# Мы уже реализовывали функцию merge, которая способна "слить" два
# отсортированных списка в один.
# Чаще всего её применяют в рекурсивном алгоритме сортировки слиянием.
#
# Напишите рекурсивную функцию merge_sort, которая производит сортировку списка.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций, за исключением рекурсивных.
# Трассировка вызова рекурсивной функции в обработке ответа не учитывается
# и показана для примера.


def merge(first_part, second_part):
    final = []
    first_counter = 0
    second_counter = 0
    while first_counter < len(first_part) and second_counter < len(second_part):
        if first_part[first_counter] < second_part[second_counter]:
            final.append(first_part[first_counter])
            first_counter += 1
        else:
            final.append(second_part[second_counter])
            second_counter += 1
    while first_counter < len(first_part):
        final.append(first_part[first_counter])
        first_counter += 1
    while second_counter < len(second_part):
        final.append(second_part[second_counter])
        second_counter += 1
    return final


def merge_sort(args):
    if len(args) <= 1:
        return args
    half = len(args) // 2
    first_part = merge_sort(args[:half])
    second_part = merge_sort(args[half:])
    return merge(first_part, second_part)
