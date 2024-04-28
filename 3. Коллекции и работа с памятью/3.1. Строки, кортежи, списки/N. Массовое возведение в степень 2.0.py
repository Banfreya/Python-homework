number_chain = input()
power = int(input())
remove_space = number_chain.split(" ")
change_to_num = list(map(int, remove_space))
elements_number = len(change_to_num)
for i in range(elements_number):
    powered_number = change_to_num[i] ** power
    print(powered_number, end=" ")
