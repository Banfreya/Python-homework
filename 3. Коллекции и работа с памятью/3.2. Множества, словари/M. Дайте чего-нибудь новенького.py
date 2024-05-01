N = int(input())
dishes = set()
coocked_dishes = set()
for i in range(N):
    dish = input()
    dishes.add(dish)
M = int(input())
for j in range(M):
    number = int(input())
    for j in range(number):
        element = input()
        coocked_dishes.add(element)
uncooked_dishes = dishes - coocked_dishes
uncooked_dishes_list = list(uncooked_dishes)
final_list = sorted(uncooked_dishes_list)
print(final_list)
