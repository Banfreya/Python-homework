from itertools import chain, permutations

N = int(input())
wishlist = ()
for i in range(N):
    wishlist = sorted(list(chain(wishlist, input().split(", "))))
poor_wishlist = (permutations(wishlist, 3))
for line in poor_wishlist:
    print(" ".join(line))
