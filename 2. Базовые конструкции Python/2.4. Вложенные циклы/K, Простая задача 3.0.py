N = int(input())
counter = 0
for _ in range(N):
    number = int(input())
    if number <= 1:
        continue
    elif number == 2:
        counter += 1
    elif number % 2 == 0:
        continue
    else:
        simple_number = True
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                simple_number = False
                break
        if simple_number:
            counter += 1
print(counter)
