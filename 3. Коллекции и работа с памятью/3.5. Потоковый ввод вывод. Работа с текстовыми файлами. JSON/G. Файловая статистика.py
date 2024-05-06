with open(input(), encoding='UTF-8') as file_in:
    numbers = [int(number) for number in file_in.read().split()]
    length = len(numbers)
    print(length)
    positive_length = len([number for number in numbers if number > 0])
    print(positive_length)
    print(min(numbers))
    print(max(numbers))
    number_sum = sum(numbers)
    print(number_sum)
    average = float(number_sum / length)
    print(average)