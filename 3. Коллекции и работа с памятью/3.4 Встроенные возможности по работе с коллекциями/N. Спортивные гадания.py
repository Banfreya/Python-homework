from itertools import permutations

N = int(input())
names = []
for i in range(N):
    names.append(input())
values = list(permutations(sorted(names), 3))
for line in values:
    print(", ".join(line))
    