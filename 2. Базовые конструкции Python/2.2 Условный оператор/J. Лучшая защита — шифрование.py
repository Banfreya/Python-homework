number = int(input())
first_code = number % 10 + number // 10 % 10
second_code = number // 10 % 10 + number // 100
if first_code > second_code:
    print(first_code, second_code, sep="")
else:
    print(second_code, first_code, sep="")
