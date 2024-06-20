# Продолжим работу с сервером из прошлых задач. При PUT запросе по пути /users/<id> доступна возможность изменение
# информации о пользователе. Для этого в данные запроса(data) требуется передать JSON объект с новой информацией
# (без указания идентификатора).
#
# Напишите программу, которая изменяет информацию о пользователе.
#
# Формат ввода
# В первой строке вводится адрес сервера.
# Во второй строке записан идентификатор пользователя, информацию о котором требуется изменить.
# В следующих строках вводятся данные для изменения в формате: <название поля>=<новое значение>.
import requests


def update_user(server_address, user_id, new_data):
    response = requests.put(f"http://{server_address}/users/{user_id}", json=new_data)
    response.raise_for_status()


def main():
    server_address = input()
    user_id = input()
    new_data = {}
    while True:
        try:
            data = input()
            if not data:
                break
            key, value = data.split('=', 1)
            new_data[key] = value
        except EOFError:
            break
    update_user(server_address, user_id, new_data)


if __name__ == "__main__":
    main()
