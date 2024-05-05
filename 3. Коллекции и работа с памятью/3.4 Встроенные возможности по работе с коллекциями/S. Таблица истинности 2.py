from itertools import product

expression = input()
variables = [item for item in sorted(
    set(expression.split())) if item.isupper()]
length = len(variables)
print(" ".join(variables), "F")
for values in product([False, True], repeat=length):
    globals = {}
    for i in range(length):
        key = variables[i]
        value = values[i]
        globals[key] = value
    result = int(eval(expression, globals))
    numbers = [str(int(element)) for element in values]
    print(" ".join(numbers), str(result))
