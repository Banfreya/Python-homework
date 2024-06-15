# Сервер отвечает на запрос JSON объект.
# Выведите значение, находящееся в объекте по заданному ключу.
# Если такое значение не обнаружено, то выведите сообщение «No data».
#
# Формат ввода
# В первой строке вводится адрес сервера. Во второй строке — имя ключа.
#
# Формат вывода
# Одна строка — значение, полученное по заданному ключу, или сообщение «No data».
from requests import get


def find_value(server_address, key_to_find):
    response = get(f"http://{server_address}")
    json_data = response.json()
    for key in json_data:
        if key == key_to_find:
            return json_data[key]
    return "No data"


server_address = input()
key_to_find = input()
result = find_value(server_address, key_to_find)
print(result)
