N = int(input())
timer_counter = 3
for i in range(N):
    tempo = timer_counter
    while tempo != 0:
        print("До старта", tempo, "секунд(ы)")
        tempo -= 1
    print("Старт", str(i + 1) + "!!!")
    timer_counter += 1
