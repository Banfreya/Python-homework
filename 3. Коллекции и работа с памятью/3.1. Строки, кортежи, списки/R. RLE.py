N = input()
number = N[0]
number_counter = 1
for i in N[1:]:
    if number == i:
        number_counter += 1
    else:
        print(number, number_counter)
        number = i
        number_counter = 1
print(number, number_counter)
