# Длинная сортировка
# Напишите lambda выражение для сортировки списка
# слов сначала по длине, а затем по алфавиту без
# учёта регистра.
#
# Примечание
# В решении не должно быть ничего, кроме выражения.


lambda line: (len(line), line.lower())