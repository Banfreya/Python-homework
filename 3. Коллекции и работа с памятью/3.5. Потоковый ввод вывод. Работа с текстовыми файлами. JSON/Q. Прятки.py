normal_text = []
with open("secret.txt", encoding='UTF-8') as file:
    for line in file:
        stripped_line = line.strip()
        for i in range(len(stripped_line)):
            char = stripped_line[i]
            char_number = ord(char)
            if char_number < 128:
                normal_text.append(char)
            else:
                binary_number = bin(char_number)
                new_binary = binary_number[-1]
                new_number = int(new_binary, 2)
                new_char = chr(new_number)
                normal_text.append(new_char)
    print("".join(normal_text))