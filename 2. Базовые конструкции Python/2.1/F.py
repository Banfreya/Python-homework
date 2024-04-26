name = input()
price = int(input())
weight = int(input())
cash = int(input())
finalPrice = price * weight
balance = cash - weight * price
print(f"Чек\n{name} - {weight}кг - {price}руб/кг\nИтого: {finalPrice}руб\nВнесено: {cash}руб\nСдача: {balance}руб")