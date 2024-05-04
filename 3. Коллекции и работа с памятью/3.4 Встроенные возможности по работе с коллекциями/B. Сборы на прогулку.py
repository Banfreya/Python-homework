first_group = input().split(", ")
second_group = input().split(", ")
pairs = [f"{x} - {y}" for x, y in list(zip(first_group, second_group))]
for i in pairs:
    print(i)
