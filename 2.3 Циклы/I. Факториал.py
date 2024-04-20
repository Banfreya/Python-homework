number = int(input())
start = 1
for i in range(number):
    factorial = start * (i + 1)
    start = factorial
print(factorial)
