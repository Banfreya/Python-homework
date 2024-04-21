number = int(input())
rows = 0
element = 0
while element < number:
    rows += 1
    element += rows
last_number = number - (element - rows)
counter = 0
elements_printed = 0
for i in range(1, rows + 1):
    for j in range(i):
        counter += 1
        print(counter, end=" ")
        elements_printed += 1
        if elements_printed == number:
            break
    if elements_printed == number:
        break
    print()
