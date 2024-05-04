from itertools import islice, cycle

M = int(input())
poridges = []
for i in range(M):
    poridge = input()
    poridges.append(poridge)
N = int(input())
final_list = islice(cycle(poridges), 0, N)
for poridge in final_list:
    print(poridge)
