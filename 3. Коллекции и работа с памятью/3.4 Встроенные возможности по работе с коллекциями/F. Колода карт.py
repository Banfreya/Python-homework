from itertools import product

suits = ["пик", "треф", "бубен", "червей"]
nominal = [2, 3, 4, 5, 6, 7, 8, 9, 10, "валет", "дама", "король", "туз"]
for_delete = suits.index(input())
del suits[for_delete]
values = list(product(nominal, suits))
for nominal, suits in values:
    print(nominal, suits, sep=" ")
