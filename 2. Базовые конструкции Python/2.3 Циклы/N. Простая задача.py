number = int(input())
if number <= 1 or number % 2 == 0:
    print("NO")
elif number == 2:
    print("YES")
else:
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            print("NO")
            break
    else:
        print("YES")
