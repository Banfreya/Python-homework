number_chain = input()
remove_space = number_chain.split(" ")
change_to_num = list(map(int, remove_space))
NOD = change_to_num[0]
for number in change_to_num[1:]:
    while number != 0:
        NOD_holder = NOD
        NOD = number
        number = NOD_holder % number
print(NOD)
