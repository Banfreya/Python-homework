number = int(input())
first_digit = number // 100
second_digit = number // 10 % 10
third_digit = number % 10
min_digit = min(first_digit, second_digit, third_digit)
max_digit = max(first_digit, second_digit, third_digit)
mid_digit = first_digit + second_digit + third_digit - min_digit - max_digit
if second_digit != 0 and third_digit != 0:
    print(min_digit, mid_digit, " ", max_digit, mid_digit, sep="")
elif second_digit == 0 and third_digit == 0:
    print(max_digit, min_digit, " ", max_digit, mid_digit, sep="")
else:
    print(mid_digit, min_digit, " ", max_digit, mid_digit, sep="")
