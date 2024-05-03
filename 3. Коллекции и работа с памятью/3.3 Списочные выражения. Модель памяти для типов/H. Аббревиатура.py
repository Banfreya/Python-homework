string = 'открытое акционерное общество'
abbreviation = "".join(word[0].capitalize() for word in string.split())
print(abbreviation)
