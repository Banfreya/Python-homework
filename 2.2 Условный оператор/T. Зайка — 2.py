landscape1 = input()
landscape2 = input()
landscape3 = input()
if "зайка" in landscape1 and "зайка" in landscape2 and "зайка" in landscape3:
    min_landscape = min(landscape1, landscape2, landscape3)
    print(min_landscape, len(min_landscape))
elif "зайка" in landscape1 and "зайка" in landscape2:
    min_landscape = min(landscape1, landscape2)
    print(min_landscape, len(min_landscape))
elif "зайка" in landscape1 and "зайка" in landscape3:
    min_landscape = min(landscape1, landscape3)
    print(min_landscape, len(min_landscape))
elif "зайка" in landscape2 and "зайка" in landscape3:
    min_landscape = min(landscape2, landscape3)
    print(min_landscape, len(min_landscape))
elif "зайка" in landscape1:
    print(landscape1, len(landscape1))
elif "зайка" in landscape2:
    print(landscape2, len(landscape2))
else:
    print(landscape3, len(landscape3))
