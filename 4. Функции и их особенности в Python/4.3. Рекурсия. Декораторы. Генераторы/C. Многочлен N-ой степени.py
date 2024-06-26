# Напишите функцию make_equation, которая по заданным коэффициентам строит
# строку, описывающую валидное с точки зрения Python выражение без использования
# оператора возведения в степень.
# Многочлен второй степени с коэффициентами a,b и c, например, можно записать в виде:
# ((𝑎)∗𝑥+𝑏)∗𝑥+𝑐((a)∗x+b)∗x+c
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций, за исключением рекурсивных.
# Трассировка вызова рекурсивной функции в обработке ответа не учитывается и показана
# для примера.


def make_equation(*args):
    if len(args) == 1:
        return f"{args[0]}"
    else:
        return f"({make_equation(*args[:-1])}) * x + {args[-1]}"

