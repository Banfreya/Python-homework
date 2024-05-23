# Напишите функцию merge, которая принимает два
# отсортированных по возрастанию кортежа целых чисел,
# а возвращает один из всех переданных чисел.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
# В этой задаче отключены стандартные сортировки

def merge(first_tuple, second_tuple):
    final = [int(item) for item in first_tuple]
    for item in second_tuple:
        number = int(item)
        final.append(number)
    final.sort()
    new_tuple = tuple(final)
    return new_tuple
