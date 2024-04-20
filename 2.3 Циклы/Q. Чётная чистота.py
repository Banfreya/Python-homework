number = int(input())
final = ""
while number > 0:
    digit = number % 10
    number = number // 10
    if digit % 2 == 0:
        final
    else:
        final = str(digit) + final
print(final)
