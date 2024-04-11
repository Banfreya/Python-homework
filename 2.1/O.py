hours = int(input())
minutes = int(input())
minutesToDeliver = int(input())
minutesFinal = (hours * 60 + minutes + minutesToDeliver) % 60
hoursFinal = (hours * 60 + minutes + minutesToDeliver) // 60 % 24
timerFirstHourDigit = str(hoursFinal // 10)
timerSecondHourDigit = str(hoursFinal % 10)
timerFirstMinuteDigit = str(minutesFinal // 10)
timerSecondMinutesDigit = str(minutesFinal % 10)
print(timerFirstHourDigit + timerSecondHourDigit + ":" +
      timerFirstMinuteDigit + timerSecondMinutesDigit, sep="")
