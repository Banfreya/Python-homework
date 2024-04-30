N = int(input())
all_kids_info = []
surnames = []
for i in range(N):
    kid_info = input()
    all_kids_info.append(kid_info)
search = input()
for kid_info in all_kids_info:
    if search in kid_info:
        kid_info_list = kid_info.split(' ')
        surnames.append(kid_info_list[0])
if len(surnames) == 0:
    print("Таких нет")
else:
    surnames.sort()
    print("\n".join(surnames))
