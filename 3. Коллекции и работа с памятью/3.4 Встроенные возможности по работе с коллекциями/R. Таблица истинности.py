expression = input()
print('a b c f')
for a, b, c in [(a, b, c) for a in range(2) for b in range(2) for c in range(2)]:
    result = eval(expression, {'a': a, 'b': b, 'c': c})
    print('{} {} {} {}'.format(a, b, c, int(result)))