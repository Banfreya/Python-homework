L = int(input())
N = int(input())
headers_full = []
sum_length = L - 3
elements_number = 0
for i in range(N):
    header = input()
    headers_full.append(header)
    elements_number += len(header)
if elements_number <= L - 3:
    print(headers_full, sep="\n")
else:
    for header in headers_full:
        header_length = len(header)
        if header_length >= sum_length:
            print(header[0:sum_length] + "...")
            break
        else:
            print(header)
            sum_length -= header_length
