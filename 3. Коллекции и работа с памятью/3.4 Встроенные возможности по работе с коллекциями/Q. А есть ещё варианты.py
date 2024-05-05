from itertools import product, combinations

suits = ["бубен", "пик", "треф", "червей"]
nominal = ["2", "3", "4", "5", "6", "7", "8",
           "9", "10", "валет", "дама", "король", "туз"]
needed = input()
if needed == "буби":
    new_needed = "бубен"
elif needed == "пики":
    new_needed = "пик"
elif needed == "трефы":
    new_needed = "треф"
else:
    new_needed = "червей"
del nominal[nominal.index(input())]
sorted_nominal = sorted(nominal)
values = list(product(sorted_nominal, suits))
values_for_combo = []
for element in values:
    values_for_combo.append(f"{element[0]} {element[1]}")
combo = (list(combinations(values_for_combo, 3)))
final_list = []
for line in combo:
    if new_needed in str(line):
        final_list.append(line)
previous_line = input()
previous_line_tuple = tuple(previous_line.split(', '))
if previous_line_tuple in final_list:
    index_previous_line = final_list.index(previous_line_tuple)
    next_line = final_list[index_previous_line + 1]
    print(", ".join(next_line))