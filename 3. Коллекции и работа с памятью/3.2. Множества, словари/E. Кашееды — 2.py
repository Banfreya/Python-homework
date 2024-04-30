N = int(input())
M = int(input())
kids_set = set()
for i in range(N + M):
    kid = input()
    if kid not in kids_set:
        kids_set.add(kid)
    else:
        kids_set.remove(kid)
if len(kids_set) == 0:
    print("Таких нет")
else:
    print(len(kids_set))
