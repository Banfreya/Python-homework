normalNumber = int(input())
thousands = normalNumber // 1000
hundreds = normalNumber // 100 % 10
tens = normalNumber // 10 % 10
units = normalNumber % 10
print(hundreds, thousands, units, tens, sep="")
