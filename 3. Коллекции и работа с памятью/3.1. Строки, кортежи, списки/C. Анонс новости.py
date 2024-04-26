L = int(input())
N = int(input())
for i in range(N):
    header = input()
    if len(header) <= L:
        print(header)
    else:
        print(header[0:L - 3] + "...")
