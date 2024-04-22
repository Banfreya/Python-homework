N = int(input())
a = int(input())
for i in range(N - 1):
    b = int(input())
    smallest_number = min(a, b)
    biggest_number = max(a, b)
    while (biggest_number % smallest_number) != 0:
        biggest_number_holder = biggest_number
        biggest_number = smallest_number
        smallest_number = biggest_number_holder % smallest_number
        a = smallest_number
print(smallest_number)
