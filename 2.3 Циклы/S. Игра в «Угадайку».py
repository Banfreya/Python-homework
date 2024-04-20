lower_border = 0
upper_border = 1000
for attempt in range(1, 11):
    guess_number = lower_border + (upper_border - lower_border) // 2
    print(guess_number)
    answer = input()
    if answer == "Меньше":
        upper_border = guess_number
    elif answer == "Больше":
        lower_border = guess_number + 1 
    elif answer == "Угадал!":
        break
    if lower_border == upper_border:  
        print(lower_border)
        break