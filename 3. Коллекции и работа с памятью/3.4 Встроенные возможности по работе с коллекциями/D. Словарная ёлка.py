from itertools import accumulate

text = input().split()
modified_text = ['{} '.format(element) for element in text]
for value in accumulate(modified_text):
    print(value)
