# Сервер отвечает на запрос JSON списком.
# Выведите сумму чисел в полученном списке.
#
# Формат ввода
# Вводится адрес сервера
#
# Формат вывода
# Одно число — сумма всех чисел в полученном списке.
from requests import get


def sum_server_data(server_address):
    response = get(f"http://{server_address}")
    json_data = response.json()
    final_sum = 0

    def sum_list(data):
        nonlocal final_sum
        for item in data:
            if isinstance(item, int):
                final_sum += item
            elif isinstance(item, list):
                sum_list(item)

    sum_list(json_data)
    return final_sum


if __name__ == "__main__":
    server_address = input().strip()
    result = sum_server_data(server_address)
    print(result)
