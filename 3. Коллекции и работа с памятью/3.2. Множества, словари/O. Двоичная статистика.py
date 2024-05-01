line = input()
line_list = []
splitted_line = line.split()
for token in splitted_line:
    binary_token = bin(int(token))
    token_dictionary = {}
    digit_counter = len(binary_token) - 2
    token_dictionary["digits"] = digit_counter
    unit_counter = 0
    zero_counter = 0
    for digit in binary_token[2:]:
        if digit == '0':
            zero_counter += 1
        if digit == '1':
            unit_counter += 1
    token_dictionary["units"] = unit_counter
    token_dictionary["zeros"] = zero_counter
    line_list.append(token_dictionary)
print(line_list)
