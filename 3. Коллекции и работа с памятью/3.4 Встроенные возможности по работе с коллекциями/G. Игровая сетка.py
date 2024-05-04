from itertools import combinations

N = int(input())
names = []
for i in range(N):
    name = input()
    names.append(name)
pairs = [f"{x} - {y}" for x, y in list(combinations(names, 2))]
for i in pairs:
    print(i)
