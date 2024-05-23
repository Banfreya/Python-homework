# Разработайте функцию number_length, которая принимает
# одно целое число и возвращает его длину без учёта знака.

# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

def number_length(number):
    length = 0
    string = str(number)
    for n in string:
        if n.isdigit():
            length += 1
    return length
