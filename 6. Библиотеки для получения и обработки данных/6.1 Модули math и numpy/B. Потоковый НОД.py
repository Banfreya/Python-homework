# Напишите программу, находящую наибольшие общие делители для всех переданных
# в стандартный поток последовательностей чисел.
#
# Формат ввода
# Вводятся строки чисел, разделённых пробелами.
#
# Формат вывода
# Последовательность чисел — наибольшие общие делители всех последовательностей.

import sys
import math


def gcd_multiple(numbers):
    current_gcd = numbers[0]
    for num in numbers[1:]:
        current_gcd = math.gcd(current_gcd, num)
    return current_gcd


def main():
    input = sys.stdin
    output = []
    for line in input:
        numbers = list(map(int, line.split()))
        if numbers:
            result = gcd_multiple(numbers)
            output.append(result)
    for res in output:
        print(res)


if __name__ == "__main__":
    main()
