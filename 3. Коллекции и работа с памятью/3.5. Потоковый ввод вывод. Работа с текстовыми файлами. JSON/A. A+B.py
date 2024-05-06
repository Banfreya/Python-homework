from sys import stdin

sum = 0
for line in stdin:
    crop = line.replace("\n", "").split(" ")
    for element in crop:
        sum += int(element)
print(sum)