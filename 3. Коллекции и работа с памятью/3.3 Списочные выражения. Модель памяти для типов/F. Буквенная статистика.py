text = 'Мама мыла раму!'
char_counter = {char: text.lower().count(char) for char in set(text.lower()) if char.isalpha()}
print(char_counter)