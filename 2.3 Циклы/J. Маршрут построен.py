x = 0
y = 0
while (direction := input()) != "СТОП":
    steps = int(input())
    if direction == "СЕВЕР":
        x = x + steps
    elif direction == "ЮГ":
        x = x - steps
    elif direction == "ЗАПАД":
        y = y - steps
    else:
        y = y + steps
print(x)
print(y)
