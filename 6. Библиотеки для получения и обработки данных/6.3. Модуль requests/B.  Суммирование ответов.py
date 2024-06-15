from requests import get


def sum_server_data(server_address):
    final_sum = 0
    while True:
        response = get(f"http://{server_address}")
        try:
            num = int(response.text.strip())
            if num == 0:
                break
            final_sum += num
        except ValueError:
            print("Данные не подходят для суммирования")
            break
    return final_sum


if __name__ == "__main__":
    server_address = input()
    result = sum_server_data(server_address)
    print(result)