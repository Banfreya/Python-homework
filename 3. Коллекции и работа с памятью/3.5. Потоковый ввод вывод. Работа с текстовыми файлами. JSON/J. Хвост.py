with open(input(), encoding='UTF-8') as file_in:
    line_list = [line for line in file_in]
N = int(input())
tail = line_list[-N:]
for line in tail:
    print(line.strip())