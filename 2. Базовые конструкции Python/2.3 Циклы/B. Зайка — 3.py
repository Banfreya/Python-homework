rabbit_str_counter = 0
while (landscape := input()) != "Приехали!":
    if "зайка" in landscape:
        rabbit_str_counter = rabbit_str_counter + 1
print(rabbit_str_counter)