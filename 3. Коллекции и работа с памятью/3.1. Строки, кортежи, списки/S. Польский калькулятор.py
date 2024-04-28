N = input()
modified_N = N.split()
operands = []
for token in modified_N:
    if token.isdigit():
        operands.append(int(token))
    elif token in ['+', '-', '*']:
        operand_two = operands.pop()
        operand_one = operands.pop()
        if token == '+':
            result = operand_one + operand_two
        elif token == '-':
            result = operand_one - operand_two
        elif token == '*':
            result = operand_one * operand_two
        operands.append(result)
print(operands[0])
