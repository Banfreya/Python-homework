# Во многих задачах требуется контроль входных данных,
# в частности, несмотря на динамическую типизацию, их типов.
#
# Разработайте декоратор same_type, который производит
# проверку переменного количества позиционных параметров.
# В случае получения не одинаковых типов выводит сообщение
# "Обнаружены различные типы данных" и прерывает выполнение функции.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

def same_type(func):
    def wrapper(*args):
        if len(set(type(arg) for arg in args)) != 1:
            print("Обнаружены различные типы данных")
            return False
        return func(*args)
    return wrapper


