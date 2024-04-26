N = int(input())
counter = 0
for i in range(N):
    word = input()
    if word[0] in ("абв"):
        counter += 1
if counter == N:
    print("YES")
else:
    print("NO")
