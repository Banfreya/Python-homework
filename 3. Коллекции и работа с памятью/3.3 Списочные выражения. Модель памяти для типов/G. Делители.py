numbers = {1, 2, 3, 4, 5}
divisors = {number: [divider for divider in range(1, number + 1) if number % divider == 0] for number in numbers}
print(divisors)