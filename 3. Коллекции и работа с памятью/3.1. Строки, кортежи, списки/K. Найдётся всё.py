N = int(input())
headers_full = []
for i in range(N):
    header = input()
    headers_full.append(header)
search = input()
search = search.lower()
for header in headers_full:
    lower_header = header.lower()
    if search in lower_header:
        print(header)