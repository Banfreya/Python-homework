N = int(input())
M = int(input())
semolina_lovers_set = set()
oatmeal_lovers_set = set()
for i in range(N):
    kid = input()
    semolina_lovers_set.add(kid)
for j in range(M):
    kid = input()
    oatmeal_lovers_set.add(kid)
kids_intersection = semolina_lovers_set & oatmeal_lovers_set
if len(kids_intersection) == 0:
    print("Таких нет")
else:
    print(len(kids_intersection))
