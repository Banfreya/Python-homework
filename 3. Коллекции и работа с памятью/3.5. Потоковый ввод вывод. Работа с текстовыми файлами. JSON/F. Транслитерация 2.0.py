transliteration = {
    "А": "A", "Б": "B", "В": "V", "Г": "G", "Д": "D", "Е": "E", "Ё": "E", "Ж": "Zh", "З": "Z",
    "И": "I", "Й": "I", "К": "K", "Л": "L", "М": "M", "Н": "N", "О": "O", "П": "P", "Р": "R",
    "С": "S", "Т": "T", "У": "U", "Ф": "F", "Х": "Kh", "Ц": "Tc", "Ч": "Ch", "Ш": "Sh", "Щ": "Shch",
    "Ы": "Y", "Э": "E", "Ю": "Iu", "Я": "Ia"
}
transliterated_text = []
with open('cyrillic.txt', encoding='UTF-8') as file_in:
    for line in file_in:
        for symbol in line:
            if symbol.isalpha():
                searched_char = symbol.capitalize()
                if searched_char in ["Ъ", "Ь"]:
                    continue
                elif searched_char in transliteration:
                    if symbol.isupper():
                        transliterated_text.append(
                            transliteration[searched_char])
                    else:
                        small_char = transliteration[searched_char].lower()
                        transliterated_text.append(small_char)
                else:
                    transliterated_text.append(symbol)
            else:
                transliterated_text.append(symbol)
with open("transliteration.txt", "w", encoding="UTF-8") as file_out:
    print("".join(transliterated_text), file=file_out)
