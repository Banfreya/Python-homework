segments = int(input())
print("A Б В")
for A in range(1, segments):
    for B in range(1, segments - A):
        C = segments - A - B
        if C >= 1:
            print(A, B, C)
