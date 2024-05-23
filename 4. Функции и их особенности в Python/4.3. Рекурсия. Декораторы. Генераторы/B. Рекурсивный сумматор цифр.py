# Рекурсия – отличный способ избавиться от циклов,
# особенно от while. Давайте вспомним одну из наших
# старых задач и модернизируем её.
#
# Напишите функцию recursive_digit_sum, которая находит
# сумму всех цифр натурального числа.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций,
# за исключением рекурсивных.
# Трассировка вызова рекурсивной функции в обработке
# ответа не учитывается и показана для примера.


def recursive_digit_sum(number):
    if len(str(number)) == 1:
        return number
    return number % 10 + recursive_digit_sum(number // 10)
