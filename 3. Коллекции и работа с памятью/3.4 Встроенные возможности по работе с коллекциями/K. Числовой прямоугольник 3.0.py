from itertools import product

N = int(input())
M = int(input())
last_number_length = len(str(N * M))
rectangle = [(row_num - 1) * M + col_num for row_num,
             col_num in product((range(1, N + 1)), (range(1, M + 1)))]
for element in rectangle:
    if element % M == 0:
        print(f"{element: >{last_number_length}}")
    else:
        print(f"{element: >{last_number_length}}", end=" ")
