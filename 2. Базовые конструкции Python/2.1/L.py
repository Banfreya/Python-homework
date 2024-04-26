firstNumber = int(input())
secondNumber = int(input())
firstNumberHundreds = firstNumber // 100
secondNumberHundreds = secondNumber // 100
firstNumberTens = firstNumber // 10 % 10
secondNumberTens = secondNumber // 10 % 10
firstNumberUnits = firstNumber % 10
secondNumberUnits = secondNumber % 10
print((firstNumberHundreds + secondNumberHundreds) % 10, (firstNumberTens +
      secondNumberTens) % 10, (firstNumberUnits + secondNumberUnits) % 10, sep="")
