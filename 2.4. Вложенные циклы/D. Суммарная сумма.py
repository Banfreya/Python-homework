N = int(input())
total_sum = 0
while True:
    for i in range(N):
        number = (input())
        digits = sum(map(int, str(number)))
        total_sum += digits
    print(total_sum)
    break
