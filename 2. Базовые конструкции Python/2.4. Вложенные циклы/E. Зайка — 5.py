N = int(input())
final_counter = 0
for i in range(N):
    landscape = input()
    rabbit_counter = 0
    while landscape != "ВСЁ":
        if landscape == "зайка":
            rabbit_counter += 1
        landscape = input()
    if rabbit_counter > 0:
        final_counter += 1
print(final_counter)
