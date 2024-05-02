N = input()
numbers = set(N.split("; "))
sorted_number_list = sorted(map(int, numbers))

for number in sorted_number_list:
    simple_numbers_list = []
    for next_number in sorted_number_list:
        if number != next_number:
            smallest_number = min(int(number), int(next_number))
            biggest_number = max(int(number), int(next_number))
            while (biggest_number % smallest_number) != 0:
                biggest_number_holder = biggest_number
                biggest_number = smallest_number
                smallest_number = biggest_number_holder % smallest_number
                if smallest_number == 1:
                    simple_numbers_list.append(str(next_number))
    if len(simple_numbers_list) != 0:  
        print(f"{number} - {', '.join(sorted(simple_numbers_list, key=int))}")