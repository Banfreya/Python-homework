# Продолжим работу с сервером из прошлой задачи. По пути /users/<id> доступен JSON объект пользователя с заданным id.
#
# Подготовьте текст письма для отправки важной рассылки.
#
# Если пользователь с заданным идентификатором не найден, выведите сообщение «Пользователь не найден».
#
# Формат ввода
# В первой строке вводится адрес сервера.
# Во второй строке вводится id пользователя, которому требуется отправить письмо.
# В последующих строках записано содержание сообщения с форматированными вставками любого из полей объекта.
#
# Формат вывода
# Выведите подготовленное сообщение.
import requests
from sys import stdin


def get_user_data(server_address, user_id):
    try:
        response = requests.get(f"http://{server_address}/users/{user_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None


def format_message(template, user_data):
    return template.format(**user_data)


def main():
    server_address = input()
    user_id = input()
    message_template = ''.join(i for i in stdin)
    user_data = get_user_data(server_address, user_id)
    if user_data:
        formatted_message = format_message(message_template, user_data)
        print(formatted_message)
    else:
        print("Пользователь не найден")


if __name__ == "__main__":
    main()
