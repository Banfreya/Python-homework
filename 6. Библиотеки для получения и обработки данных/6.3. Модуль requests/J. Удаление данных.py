# Завершим эпопею с сервером из прошлых задач. При DELETE запросе по пути /users/<id> производится удаление
# пользователя с заданным идентификатором.
#
# Напишите программу, которая удаляет пользователя из системы.
#
# Формат ввода
# В первой строке вводится адрес сервера.
# Во второй строке записан идентификатор пользователя, информацию о котором требуется удалить.
#
# Формат вывода
# Ничего выводить не требуется.
import requests


def delete_user(server_address, user_id):
    response = requests.delete(f"http://{server_address}/users/{user_id}")
    response.raise_for_status()


def main():
    server_address = input()
    user_id = input()

    delete_user(server_address, user_id)


if __name__ == "__main__":
    main()

