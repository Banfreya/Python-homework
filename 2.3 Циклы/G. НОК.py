first_number = int(input())
second_number = int(input())
smallest_number = min(first_number, second_number)
biggest_number = max(first_number, second_number)

while (biggest_number % smallest_number) != 0:
    biggest_number_holder = biggest_number
    biggest_number = smallest_number
    smallest_number = biggest_number_holder % smallest_number
print(int(first_number * second_number / smallest_number))
