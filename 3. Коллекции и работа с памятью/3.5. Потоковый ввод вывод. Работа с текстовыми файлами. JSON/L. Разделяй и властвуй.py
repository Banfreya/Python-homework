with open(input(), encoding='UTF-8') as file_in:
    numbers = [line.strip() for line in file_in.readlines()]
    even_list = []
    odd_list = []
    eq_list = []

    for line in numbers:
        even_line = []
        odd_line = []
        eq_line = []
        for number_str in line.split(" "):
            number = int(number_str)
            even = 0
            odd = 0
            temp_number = number
            while temp_number > 0:
                if temp_number % 2 == 0:
                    even += 1
                else:
                    odd += 1
                temp_number = temp_number // 10
            if even > odd:
                even_line.append(number)
            elif even < odd:
                odd_line.append(number)
            else:
                eq_line.append(number)
        even_list.append(even_line)
        odd_list.append(odd_line)
        eq_list.append(eq_line)
with open(input(), 'w', encoding='UTF-8') as file_out:
    for line in even_list:
        file_out.write(' '.join(map(str, line)) + '\n')
with open(input(), 'w', encoding='UTF-8') as file_out:
    for line in odd_list:
        file_out.write(' '.join(map(str, line)) + '\n')
with open(input(), 'w', encoding='UTF-8') as file_out:
    for line in eq_list:
        file_out.write(' '.join(map(str, line)) + '\n')

