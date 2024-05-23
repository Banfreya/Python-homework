#Разработайте функцию modern_print, которая принимает
# строку и выводит её, если она не была выведена ранее.

# Примечание
# В решении не должно быть вызовов требуемых функций

def modern_print(string, _printed=set()):
    if string not in _printed:
        _printed.add(string)
        print(string)
