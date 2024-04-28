text = input()
text_modified = list(text.lower())
for i in range(len(text_modified)):
    space_counter = text_modified.count(' ')
    for j in range(space_counter):
        j = text_modified.index(' ')
        del text_modified[j]
if text_modified == text_modified[::-1]:
    print("YES")
else:
    print("NO")
