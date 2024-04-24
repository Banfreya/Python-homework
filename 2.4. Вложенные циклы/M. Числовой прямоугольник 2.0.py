N = int(input())
M = int(input())
last_number = N * M
for i in range(N):
    start = 1 + i
    for i in range(M):
        if N * M < 10:
            print(start, end=" ")
            if start <= last_number:
                start += N
        elif N * M < 100:
            if start <= last_number:
                print(f"{start:>2}", end=" ")
                start += N
        else:
            print(f"{start:>3}", end=" ")
            if start <= last_number:
                start += N
    print()
