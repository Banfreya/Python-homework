# Продолжим работу с сервером из прошлых задач. При POST запросе по пути /users
# доступна возможность создания новых пользователей.
# Для этого в данные запроса (data) требуется передать JSON объект с информацией о пользователе
# (без указания идентификатора).
#
# Напишите программу, которая добавляет нового пользователя в систему.
#
# Формат ввода
# В первой строке вводится адрес сервера.
# В следующих строках вводятся: имя пользователя, фамилия, имя и адрес электронной почты.
#
# Формат вывода
# Ничего выводить не требуется.

import requests


def add_user(server_address, user_info):
    response = requests.post(f"http://{server_address}/users", json=user_info)
    response.raise_for_status()


def main():
    server_address = input()

    user_info = {
        "username": input(),
        "last_name": input(),
        "first_name": input(),
        "email": input()
    }

    add_user(server_address, user_info)


if __name__ == "__main__":
    main()
