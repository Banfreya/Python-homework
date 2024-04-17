average_petya_speed = int(input())
average_vasya_speed = int(input())
average_tolya_speed = int(input())
if average_petya_speed > average_vasya_speed \
        and average_petya_speed > average_tolya_speed \
        and average_vasya_speed > average_tolya_speed:
    print(f"{'Петя':^24}\n{'  Вася':<24}\n{'Толя  ':>24}")
    print(f"{'   II':<8}{'I':^8}{'III   ':>8}")
elif average_petya_speed > average_vasya_speed \
        and average_petya_speed > average_tolya_speed \
        and average_tolya_speed > average_vasya_speed:
    print(f"{'Петя':^24}\n{'  Толя':<24}\n{'Вася  ':>24}")
    print(f"{'   II':<8}{'I':^8}{'III   ':>8}")
elif average_tolya_speed > average_vasya_speed \
        and average_tolya_speed > average_petya_speed \
        and average_petya_speed > average_vasya_speed:
    print(f"{'Толя':^24}\n{'  Петя':<24}\n{'Вася  ':>24}")
    print(f"{'   II':<8}{'I':^8}{'III   ':>8}")
elif average_tolya_speed > average_vasya_speed \
        and average_tolya_speed > average_petya_speed \
        and average_petya_speed < average_vasya_speed:
    print(f"{'Толя':^24}\n{'  Вася':<24}\n{'Петя  ':>24}")
    print(f"{'   II':<8}{'I':^8}{'III   ':>8}")
elif average_tolya_speed < average_vasya_speed \
        and average_tolya_speed > average_petya_speed \
        and average_petya_speed < average_vasya_speed:
    print(f"{'Вася':^24}\n{'  Толя':<24}\n{'Петя  ':>24}")
    print(f"{'   II':<8}{'I':^8}{'III   ':>8}")
else:
    print(f"{'Вася':^24}\n{'  Петя':<24}\n{'Толя  ':>24}")
    print(f"{'   II':<8}{'I':^8}{'III   ':>8}")
