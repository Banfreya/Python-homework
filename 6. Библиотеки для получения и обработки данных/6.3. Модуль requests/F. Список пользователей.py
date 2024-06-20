# Список пользователей
# На сервере по пути /users, доступен список пользователей, представленных JSON объектами с ключами:
#
# id — уникальный идентификатор пользователя;
# username — имя пользователя;
# last_name — фамилия;
# first_name — имя;
# email — адрес электронной почты.
# Формат ввода
# В первой строке вводится адрес сервера.
#
# Формат вывода
# Выведите список всех пользователей системы в алфавитном порядке.
from requests import get


def get_sorted_users(server_address):
    response = get(f"http://{server_address}/users")
    if response.status_code == 200:
        users = response.json()
        sorted_users = sorted(users, key=lambda x: (x['last_name'], x['first_name']))
        return sorted_users


if __name__ == "__main__":
    server_address = input()
    users = get_sorted_users(server_address)
    for user in users:
        print(f"{user['last_name']} {user['first_name']}")


