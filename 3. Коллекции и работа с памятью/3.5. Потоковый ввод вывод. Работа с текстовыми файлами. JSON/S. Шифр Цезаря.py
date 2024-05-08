alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = int(input()) % len(alphabet)
ciphered_alphabet = alphabet[shift:] + alphabet[:shift]
cipher = ''
with open("public.txt", encoding='UTF-8') as file_in:
    for char in file_in.read():
        if char.lower() in alphabet:
            new_number = alphabet.find(char.lower())
            new_char = ciphered_alphabet[new_number]
            cipher += new_char.upper() if char.isupper() else new_char
        else:
            cipher += char
with open("private.txt", 'w', encoding="UTF-8") as file_out:
    file_out.write(cipher)
