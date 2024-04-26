start_number = int(input(""))
end_number = int(input(""))
if start_number < end_number:
    for counter in range(start_number, end_number + 1):
        print(counter, end=' ')
else:
    for counter in range(start_number, end_number - 1, -1):
        print(counter, end=' ')