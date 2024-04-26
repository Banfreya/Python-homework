size = int(input())
for column in range(size):
    for line in range(size):
        print((line + 1), "*", (column + 1),
              "=", ((line + 1) * (column + 1)))
