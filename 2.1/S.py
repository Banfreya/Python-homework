name = input()
price = int(input())
weight = int(input())
cash = int(input())
final_price = price * weight
balance = cash - weight * price
string_weight = str(weight)
string_price = str(price)
print(f"{'Чек':=^35}")
table = {"Товар:": str(name), "Цена:": string_weight + "кг * " + string_price + "руб/кг",
         "Итого:": str(final_price) + "руб", "Внесено:": str(cash) + "руб", "Сдача:": str(balance) + "руб"}
for naming, data in table.items():
    print(f'{naming:<10}{data:>25}')
print("=" * 35)
