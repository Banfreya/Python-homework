N = int(input())
numbers = []
for i in range(N):
    number = int(input())
    numbers.append(number)
power = int(input())
for number in numbers:
    powered_number = number ** power
    print(powered_number)
