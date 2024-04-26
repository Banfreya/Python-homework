N = int(input())
counter = 0
for i in range(N):
    landscape = input()
    rabbit_searcher = landscape.count("зайка")
    counter += rabbit_searcher
print(counter)
