from itertools import chain

first_wishlist = input().split(", ")
second_wishlist = input().split(", ")
third_wishlist = input().split(", ")
wishlist = sorted(list(chain(first_wishlist, second_wishlist, third_wishlist)))
for index, value in enumerate(wishlist, 1):
    print(index, ". ", value, sep="")
