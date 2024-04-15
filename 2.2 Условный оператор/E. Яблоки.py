petya_apple_balance = 7
vasya_apple_balance = 6
petya_apple_balance - 3
vasya_apple_balance + 3
petya_apple_balance + 2
final_dima_apples_to_petya = int(input())
final_dima_apples_to_vasya = int(input())
final_petya_balance = petya_apple_balance + final_dima_apples_to_petya
final_vasya_balance = vasya_apple_balance + final_dima_apples_to_vasya
if final_vasya_balance < final_dima_apples_to_petya:
    print("Петя")
else:
    print("Вася")
