from itertools import chain

N = int(input())
wishlist = ()
for i in range(N):
    wishlist = sorted(list(chain(wishlist, input().split(", "))))
for index, value in enumerate(wishlist, 1):
    print(index, ". ", value, sep="")
