from itertools import permutations

N = int(input())
names = []
for i in range(N):
    names.append(input())
values = list(permutations(sorted(names)))
for line in values:
    print(", ".join(line))
    