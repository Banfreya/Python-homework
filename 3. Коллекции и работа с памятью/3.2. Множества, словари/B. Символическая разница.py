N = input()
M = input()
N_set = set(N)
M_set = set(M)
NM_intersection = N_set & M_set
for i in range(len(N)):
    if N[i] in NM_intersection:
        print(N[i], end="")
        NM_intersection.remove(N[i])
