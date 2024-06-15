# Сервер отвечает на несколько путей, каждый из которых возвращает свой JSON список. Напишите программу,
# которая произведёт сбор и суммирование всех данных по заданным путям.
#
# Формат ввода
# Вводится адрес сервера и список анализируемых путей.
#
# Формат вывода
# Одно число — сумма всех чисел из полученных списков.
from requests import get


def sum_server_data(server_address, paths):
    final_sum = 0

    def sum_list(data):
        nonlocal final_sum
        for item in data:
            if isinstance(item, int):
                final_sum += item
            elif isinstance(item, list):
                sum_list(item)

    for path in paths:
        response = get(f"http://{server_address}{path}")
        if response.status_code == 200:
            json_data = response.json()
            sum_list(json_data)
    return final_sum


if __name__ == "__main__":
    server_address = input()
    paths = []
    while True:
        try:
            path = input().strip()
            if path:
                paths.append(path)
            else:
                break
        except EOFError:
            break
    result = sum_server_data(server_address, paths)
    print(result)
