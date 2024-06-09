# Математика — круто, но это не точно
# Давайте вспомним начало нашего задачника, когда всё было просто: мы не использовали ни циклы,
# ни коллекции, ни объектно-ориентированное программирование. Перед нами были только входные данные
# и требовалось предоставить результат.
#
# Напишите программу, которая вычисляет значение функции:
# https://nexters.gyazo.com/0a86ab8afeef2b751328c84b82520f76
# Формат ввода
# Вводится действительное число х
# Формат вывода
# Одно число — значение функции в заданной точке.

import math
import sys


def f(x):
    first_value = math.log(x**(3 / 16)) / math.log(32)
    exponent = math.cos((math.pi * x) / (2 * math.e))
    second_value = x ** exponent
    third_value = math.sin(x / math.pi) ** 2
    return first_value + second_value - third_value


if __name__ == "__main__":

    input = sys.stdin.read
    x = float(input())
    result = f(x)
    print(f"{result:.15f}")
