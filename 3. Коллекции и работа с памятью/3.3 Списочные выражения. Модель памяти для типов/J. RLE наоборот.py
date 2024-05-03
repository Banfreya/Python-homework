rle = [('1', 1), ('0', 2), ('5', 1), ('0', 2)]
reversed_rle = "".join(element * counter for element, counter in rle)
print(reversed_rle)
