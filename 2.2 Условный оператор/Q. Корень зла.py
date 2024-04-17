a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4 * a * c
if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
elif a == 0 and b == 0 and c != 0 or D < 0:
    print("No solution")
elif a == 0 and b != 0 and c != 0:
    x1 = -(c / b)
    print(f"{x1:.2f}")
elif a == 0 and b != 0 and c == 0:
    x1 = 0
    print(f"{x1:.2f}")
elif D == 0:
    print(f"{- b / (2 * a):.2f}")
else:
    x1 = (- b + D ** 0.5) / (2 * a)
    x2 = (- b - D ** 0.5) / (2 * a)
    min_root = min(x1, x2)
    max_root = max(x1, x2)
    print(f"{min_root:.2f}", f"{max_root:.2f}")
