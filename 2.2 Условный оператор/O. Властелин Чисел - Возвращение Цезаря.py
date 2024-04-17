first_def_num = int(input())
second_def_num = int(input())
first_digit_1num = first_def_num // 10
second_digit_1num = first_def_num % 10
first_digit_2num = second_def_num // 10
second_digit_2num = second_def_num % 10
max_digit = max(first_digit_1num, first_digit_2num,
                second_digit_2num, second_digit_1num)
min_digit = min(first_digit_1num, first_digit_2num,
                second_digit_2num, second_digit_1num)
other_digit_sum = first_digit_1num + second_digit_1num + \
    first_digit_2num + second_digit_2num - max_digit - min_digit
other_digit_sum_modified = other_digit_sum % 10
if other_digit_sum < 10:
    print(max_digit, other_digit_sum, min_digit, sep="")
else:
    print(max_digit, other_digit_sum_modified, min_digit, sep="")
