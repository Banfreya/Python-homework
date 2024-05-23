# Напишите функцию gcd, которая принимает два натуральных числа
# # и возвращает их наибольший общий делитель.

# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.


def gcd(first_number, second_number):

    smallest_number = min(first_number, second_number)
    biggest_number = max(first_number, second_number)

    while (biggest_number % smallest_number) != 0:
        biggest_number_holder = biggest_number
        biggest_number = smallest_number
        smallest_number = biggest_number_holder % smallest_number
    return smallest_number
