# Напишите генератор cycle, который принимает список
# и работает аналогично итератору itertools.cycle.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.


def cycle(args):
    final_list = []
    for arg in args:
        yield arg
        final_list.append(arg)
    while final_list:
        for item in final_list:
            yield item
