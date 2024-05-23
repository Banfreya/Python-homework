# Напишите функцию is_palindrome, которая принимает
# натуральное число, строку, кортеж или список, а
# возвращает логическое значение: True — если передан
# палиндром, а в противном случае — False.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
#
# Для определения типа параметра можно воспользоваться
# функцией type или более продвинутой isinstance.

def is_palindrome(something):
    if isinstance(something, int):
        something = str(something)
    elif isinstance(something, (str, list, tuple)):
        pass
    return something == something[::-1]



