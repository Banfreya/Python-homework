N = int(input())
full_landscape_set = set()
for i in range(N):
    landscape = input()
    landscape_words = landscape.split(" ")
    landscape_set = set(landscape_words)
    full_landscape_set = full_landscape_set | landscape_set
print("\n".join(full_landscape_set))
