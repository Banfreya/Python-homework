number = int(input())
first_digit = number // 100
second_digit = number // 10 % 10
third_digit = number % 10
min_digit = min(first_digit, second_digit, third_digit)
max_digit = max(first_digit, second_digit, third_digit)
mid_digit = first_digit + second_digit + third_digit - min_digit - max_digit
if max_digit + min_digit == mid_digit * 2:
    print("YES")
else:
    print("NO")
