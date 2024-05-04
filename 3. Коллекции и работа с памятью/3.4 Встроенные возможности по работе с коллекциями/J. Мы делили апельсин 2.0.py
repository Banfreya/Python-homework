from itertools import product

N = int(input())
print("А Б В")
segments_per_kid = list(range(1, N))
values = list(product(segments_per_kid, repeat=2))
final = []
for element in values:
    c = N - sum(element)
    if c > 0:
        final.append(f"{element[0]} {element[1]} {c}")
for line in final:
    print(line)
