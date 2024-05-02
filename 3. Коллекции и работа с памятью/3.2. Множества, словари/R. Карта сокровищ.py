N = int(input())
treasures = {}
for _ in range(N):
    x, y = input().split()
    index = (int(x) // 10, int(y) // 10)
    treasures[index] = treasures.get(index, 0) + 1
max_count = max(treasures.values())
print(max_count)