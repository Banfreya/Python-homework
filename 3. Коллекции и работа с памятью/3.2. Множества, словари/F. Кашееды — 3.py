N = int(input())
M = int(input())
kids_set = set()
for i in range(N + M):
    kid = input()
    if kid not in kids_set:
        kids_set.add(kid)
    else:
        kids_set.remove(kid)
kids_list = list(kids_set)
sorted_kid_list = sorted(kids_list)
if len(sorted_kid_list) == 0:
    print("Таких нет")
else:
    print("\n".join(sorted_kid_list))
