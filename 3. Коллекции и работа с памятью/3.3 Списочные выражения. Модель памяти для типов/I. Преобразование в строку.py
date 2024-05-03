numbers = [3, 1, 2, 3, 2, 2, 1]
sorted_numbers = " - ".join(str(number) for number in sorted(list(set(numbers))))
print(sorted_numbers)