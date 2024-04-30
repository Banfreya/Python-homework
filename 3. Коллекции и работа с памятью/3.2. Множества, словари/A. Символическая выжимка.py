word = input()
letters = set(word)
for i in range(len(word)):
    if word[i] in letters:
        print(word[i], end="")
        letters.remove(word[i])
