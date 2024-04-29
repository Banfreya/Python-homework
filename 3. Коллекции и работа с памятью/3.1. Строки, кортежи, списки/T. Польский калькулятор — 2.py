N = input()
modified_N = N.split()
operands = []
for token in modified_N:
    if token.isdigit():
        operands.append(int(token))
    elif token == '~':
        operands.append(operands.pop() * -1)
    elif token == '!':
        number = operands.pop()
        start = 1
        factorial = 1
        for i in range(number):
            factorial = start * (i + 1)
            start = factorial
        operands.append(factorial)
    elif token == '#':
        a = operands.pop()
        operands.append(a)
        operands.append(a)
    elif token == '+':
        a = operands.pop()
        b = operands.pop()
        operands.append(a + b)
    elif token == '-':
        a = operands.pop()
        b = operands.pop()
        operands.append(b - a)
    elif token == '*':
        a = operands.pop()
        b = operands.pop()
        operands.append(a * b)
    elif token == '/':
        a = operands.pop()
        b = operands.pop()
        operands.append(b // a)
    elif token == '@':
        a = operands.pop()
        b = operands.pop()
        c = operands.pop()
        operands.append(b)
        operands.append(a)
        operands.append(c)
print(operands[0])
