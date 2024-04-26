N = int(input())
M = int(input())
matrix = [[0] * M for _ in range(N)]
number = 1
for i in range(M):
    if i % 2 == 0:
        for j in range(N):
            matrix[j][i] = number
            number += 1
    else:
        for j in range(N - 1, -1, -1):
            matrix[j][i] = number
            number += 1
for i in range(N):
    for j in range(M):
        if N * M < 10:
            print(matrix[i][j], end=" ")
        elif N * M < 100:
            print(f"{matrix[i][j]:>2}", end=" ")
        else:
            print(f"{matrix[i][j]:>3}", end=" ")
    print()