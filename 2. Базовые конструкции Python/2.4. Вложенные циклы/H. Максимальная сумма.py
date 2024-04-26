N = int(input())
winner_sum = 0
winner_name = str()
for i in range(N):
    name = input()
    number = int(input())
    sum = 0
    while number > 0:
        digit = number % 10
        sum = sum + digit
        number = number // 10
        if sum >= winner_sum:
            winner_sum = sum
            winner_name = name
print(winner_name)
