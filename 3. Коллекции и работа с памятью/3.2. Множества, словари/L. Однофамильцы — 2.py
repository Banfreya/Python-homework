N = int(input())
surnames = {}
namesakes = []
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
        new_element = str(f"{surname} - {surnames[surname]}")
        namesakes.append(new_element)
if all(surnames[surname] == 1 for surname in surnames):
    print("Однофамильцев нет")
else:
    sorted_namesakes = sorted(namesakes)
    print("\n".join(sorted_namesakes))
