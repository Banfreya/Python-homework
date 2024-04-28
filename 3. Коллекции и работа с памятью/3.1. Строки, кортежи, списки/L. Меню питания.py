N = int(input())
counter = 0
poridges = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
for i in range(N):
    print(poridges[counter])
    counter += 1
    if counter == 5:
        counter = 0
