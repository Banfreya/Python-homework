number = int(input())
counter = 0
width = 1
max_length = 0
while counter <= number:
    string_length = 0
    for position in range(width):
        counter += 1
        if counter <= number:
            string_length += len(str(counter))
        if position < width - 1 and counter < number:
            string_length += 1
    if max_length < string_length:
        max_length = string_length
    width += 1
counter = 0
width = 1
while counter <= number:
    string = ''
    for position in range(width):
        counter += 1
        if counter <= number:
            string += str(counter)
        if position < width - 1 and counter < number:
            string += ' '
    width += 1
    print(f'{string:^{max_length}}')