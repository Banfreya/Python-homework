from sys import stdin

lines = []
difference = []
for line in stdin:
    lines.append(line.rstrip("\n").split(" "))
for line in lines:
    change = int(line[2]) - int(line[1])
    difference.append(change)
difference_average = round(sum(difference) / len(difference))
print(difference_average)
