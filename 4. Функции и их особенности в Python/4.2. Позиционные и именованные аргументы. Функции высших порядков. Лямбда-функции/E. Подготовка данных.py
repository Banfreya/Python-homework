# Напишите функцию to_string, которая формирует
# из последовательности данных строку.
# Функция должна принимать:
#
# неопределённое количество данных;
# необязательный параметр sep (по умолчанию пробел);
# необязательный параметр end (по умолчанию \n).
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.


def to_string(*data, sep=" ", end="\n"):
    final_string = sep.join(str(item) for item in data)
    final_string += end
    return final_string
