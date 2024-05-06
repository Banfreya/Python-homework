from sys import stdin

lines = []
palindromes = set()
for line in stdin:
    lines.append(line.rstrip("\n").split(" "))
for line in lines:
    for element in line:
        lower_element = str(element).lower()
        if lower_element == lower_element[::-1]:
            palindromes.add(element)
print("\n".join(sorted(palindromes)))
