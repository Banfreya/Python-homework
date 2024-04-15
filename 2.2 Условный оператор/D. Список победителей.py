average_petya_speed = int(input())
average_vasya_speed = int(input())
average_tolya_speed = int(input())
if average_petya_speed > average_vasya_speed \
        and average_petya_speed > average_tolya_speed \
        and average_vasya_speed > average_tolya_speed:
    print("1. Петя\n2. Вася\n3. Толя")
elif average_petya_speed > average_vasya_speed \
        and average_petya_speed > average_tolya_speed \
        and average_tolya_speed > average_vasya_speed:
    print("1. Петя\n2. Толя\n3. Вася")
elif average_tolya_speed > average_vasya_speed \
        and average_tolya_speed > average_petya_speed \
        and average_petya_speed > average_vasya_speed:
    print("1. Толя\n2. Петя\n3. Вася")
elif average_tolya_speed > average_vasya_speed \
        and average_tolya_speed > average_petya_speed \
        and average_petya_speed < average_vasya_speed:
    print("1. Толя\n2. Вася\n3. Петя")
elif average_tolya_speed < average_vasya_speed \
        and average_tolya_speed > average_petya_speed \
        and average_petya_speed < average_vasya_speed:
    print("1. Вася\n2. Толя\n3. Петя")
else:
    print("1. Вася\n2. Петя\n3. Толя")
