average_petya_speed = int(input())
average_vasya_speed = int(input())
average_tolya_speed = int(input())
if average_petya_speed > average_vasya_speed and average_petya_speed > average_tolya_speed:
    print("Петя")
elif average_vasya_speed > average_petya_speed and average_vasya_speed > average_tolya_speed:
    print("Вася")
else:
    print("Толя")
