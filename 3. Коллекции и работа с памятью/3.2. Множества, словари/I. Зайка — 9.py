full_landscape = []
animals = {}
while landscape := input():
    if landscape == "":
        break
    else:
        splitted_landscape = landscape.split()
        full_landscape.append(splitted_landscape)
for landscape in full_landscape:
    for i in range(len(landscape)):
        if landscape[i] not in animals:
            counter = 1
            animals[landscape[i]] = counter
        else:
            counter = int(animals.pop(landscape[i])) + 1
            animals[landscape[i]] = counter
for landscape in animals:
    print(f"{landscape} {animals[landscape]}")
