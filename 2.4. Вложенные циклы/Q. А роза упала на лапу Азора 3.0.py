N = int(input())
counter = 0
for i in range(N):
    number = input()
    if number == number[::-1]:
        counter += 1
print(counter)
