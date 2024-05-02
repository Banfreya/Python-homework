N = int(input())
full_info = {}
for i in range(N):
    name, toys = input().split(": ")
    splitted_toys = toys.split(", ")
    full_info[name] = set(splitted_toys)
toys_count = {}
for toys in full_info.values():
    for toy in toys:
        if toy not in toys_count:
            toys_count[toy] = 0
        toys_count[toy] += 1
for toy, count in sorted(toys_count.items()):
    if count == 1:
        print(toy)
