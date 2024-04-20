landscape_number = int(input())
counter = 0
for i in range(landscape_number):
    landscape = input()
    if "зайка" in landscape:
        counter = counter + 1
    else:
        counter
print(counter)
