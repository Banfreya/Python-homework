from itertools import product, islice

N = int(input())
multiplier_table = [x * y for x, y in product(range(1, N + 1), repeat=2)]
for i in range(N):
    row = list(islice(multiplier_table, i * N, (i + 1) * N))
    for element in row:
        print(element, end=" ")
    print()
