from itertools import count

numbers = input().split()
start = float(numbers[0])
step = float(numbers[2])
end = float(numbers[1])
for value in count(start, step):
    if value <= end:
        print(round(value, 1))
    else:
        break
