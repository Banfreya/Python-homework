N = int(input())
max_number = ""
for i in range(N):
    number = int(input())
    tempo = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        final = max(digit, tempo)
        tempo = final
    max_number += str(final)
print(max_number)
