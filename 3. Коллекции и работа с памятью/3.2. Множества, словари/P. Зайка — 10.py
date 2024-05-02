near_rabbit = set()
while (landscape := input()) != "":
    splitted_landscape = landscape.split()
    for index in range(len(splitted_landscape)):
        if splitted_landscape[index] == "зайка":
            if 0 < index < len(splitted_landscape) - 1:
                previous_element = splitted_landscape[index - 1]
                next_element = splitted_landscape[index + 1]
                near_rabbit.add(previous_element)
                near_rabbit.add(next_element)
                index += 1
            elif index == 0:
                next_element = splitted_landscape[index + 1]
                near_rabbit.add(next_element)
                index += 1
            elif index == len(splitted_landscape) - 1:
                previous_element = splitted_landscape[index - 1]
                near_rabbit.add(previous_element)
                index += 1
print("\n".join(near_rabbit))
