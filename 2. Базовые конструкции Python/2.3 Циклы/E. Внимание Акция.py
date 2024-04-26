counter = float(0.00)
while (price := float(input())) != 0:
    if price < 500:
        counter = counter + price
    else:
        counter = counter + price * 0.9
print(counter)
