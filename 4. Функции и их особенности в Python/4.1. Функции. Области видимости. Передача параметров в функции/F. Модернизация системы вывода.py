#Разработайте функцию modern_print, которая принимает
# строку и выводит её, если она не была выведена ранее.

# Примечание
# В решении не должно быть вызовов требуемых функций

def modern_print(string, string_set=set()):
    if string not in string_set:
        string_set.add(string)
        print(string)

