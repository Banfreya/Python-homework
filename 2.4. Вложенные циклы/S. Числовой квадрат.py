N = int(input())
max_length = len(str(N))

for i in range(N):
    row = ""
    for j in range(N):
        if N < 19:
            distance_to_border = min(i, j, N - i - 1, N - j - 1)
            value = distance_to_border + 1
            cell = f"{value:^{max_length}}"
            row += cell + " "
    print(row)