N = int(input())
surnames = {}
final_counter = 0
for i in range(N):
    surname = input()
    if surname not in surnames:
        surnames[surname] = 1
    else:
        surnames[surname] = surnames.get(surname, []) + 1
for surname in surnames:
    if surnames.get(surname) == 1:
        continue
    else:
        final_counter += surnames.get(surname, [])
print(final_counter)
