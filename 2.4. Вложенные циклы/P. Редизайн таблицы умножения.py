size = int(input())
width = int(input())
for i in range(1, size + 1):
    for j in range(1, size + 1):
        if j == 1:
            print(f" {i * j:^{width - 2}}", end="")
        else:
            print(f"{i * j:^{width - 2}}", end="")
        if j < size:
            print(" | ", end="")
    print()
    if i < size:
        print("-" * (width * size + j - 1))
