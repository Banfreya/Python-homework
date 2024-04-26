N = int(input())
last_hash = 0
answer = - 1
for i in range(N):
    b = int(input())
    h = b % 256
    r = (b // 256) % 256
    m = b // 256 ** 2
    next_hash = ((m + r + last_hash) * 37) % 256
    if next_hash != h or h >= 100:
        answer = i
        break
    last_hash = h
print(answer)
