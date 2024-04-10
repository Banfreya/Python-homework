childName = input()
lockerNumber = int(input())
groupNumber = lockerNumber // 100
bedNumber = lockerNumber // 10 % 10
childNumber = lockerNumber % 10
print(f"Группа №{groupNumber}.\n{childNumber}. {childName}.\nШкафчик: {lockerNumber}.\nКроватка: {bedNumber}.")