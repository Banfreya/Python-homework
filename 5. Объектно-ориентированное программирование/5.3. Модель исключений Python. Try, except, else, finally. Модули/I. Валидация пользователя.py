# Используйте две предыдущих функции валидации и напишите функцию user_validation,
# которая принимает именованные аргументы:
#
# last_name — фамилия;
# first_name — имя;
# username — имя пользователя.
# Если функции был передан неизвестный параметр или не передан один из обязательных, то вызовите исключение KeyError.
#
# Если один из параметров не является строкой, то вызовите исключение TypeError.
#
# Обработка данных должна происходить в порядке: фамилия, имя, имя пользователя.
#
# Если поле заполнено верно, функция возвращает словарь с данными пользователя.
#
# Примечание
# В решении не должно быть вызовов требуемых функций.
import re


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def username_validation(name):
    if not isinstance(name, str):
        raise TypeError
    if not re.match("^[A-Za-z0-9_]+$", name):
        raise BadCharacterError
    if name[0].isdigit():
        raise StartsWithDigitError
    return name


def name_validation(string):
    if not isinstance(string, str):
        raise TypeError
    for letter in string:
        if not ('\u0400' <= letter <= '\u04FF'):
            raise CyrillicError
    if not string[0].isupper() or not string[1:].islower():
        raise CapitalError
    return string


def user_validation(*args, last_name, first_name, username, **kwargs):
    fields = (last_name, first_name, username)
    if any(_ == '' for _ in fields):
        raise KeyError
    if args or kwargs:
        raise KeyError
    if not all(isinstance(_, str) for _ in (last_name, first_name, username)):
        raise TypeError
    name_validation(last_name)
    name_validation(first_name)
    username_validation(username)
    return {"last_name": last_name, "first_name": first_name, "username": username}