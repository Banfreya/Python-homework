N = int(input())
M = int(input())
start = 1
for i in range(N):
    if i % 2 == 0:
        for j in range(M):
            if N * M < 10:
                print(start, end=" ")
                start += 1
            elif N * M < 100:
                print(f"{start:>2}", end=" ")
                start += 1
            else:
                print(f"{start:>3}", end=" ")
                start += 1
    else:
        start += M - 1
        for j in range(M):
            if N * M < 10:
                print(start, end=" ")
                start -= 1
            elif N * M < 100:
                print(f"{start:>2}", end=" ")
                start -= 1
            else:
                print(f"{start:>3}", end=" ")
                start -= 1
        start += M + 1
    print()