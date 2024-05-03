numbers = [1, 2, 3, 4, 5]
squares = {number for number in numbers if int(number ** 0.5) ** 2 == number}
print(squares)