number = int(input())
max_sum = 0
beneficial_basis = 0
for basis in range(2, 10 + 1):
    digit_sum = 0
    tempo = number
    while tempo:
        digit_sum += tempo % basis
        tempo = tempo // basis
    if digit_sum > max_sum:
        max_sum = digit_sum
        beneficial_basis = basis
print(beneficial_basis)
