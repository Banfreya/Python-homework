N = int(input())
for i in range(N):
    landscape = input()
    if "зайка" not in landscape:
        print("Заек нет =(")
    else:
        rabbit_searcher = landscape.find("зайка")
        print(rabbit_searcher + 1)
