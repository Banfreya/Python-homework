number = int(input())
i = 3
result = ""
while number % 2 == 0 and number > 1:
    multiplier = 2
    number = number / 2
    result = result + " * " + str(multiplier)
while i <= number:
    if number % i == 0:
        result = result + " * " + str(i)
        number = number / i
    else:
        i += 2
print(result[3:])
