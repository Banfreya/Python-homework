# Напишите функцию is_prime, которая принимает
# натуральное число, а возвращает булево значение:
# True — если переданное число простое, а иначе — False.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

def is_prime(number):
    if number <= 1 or number % 2 == 0:
        return False
    elif number == 2:
        return True
    else:
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                return False
        else:
            return True
