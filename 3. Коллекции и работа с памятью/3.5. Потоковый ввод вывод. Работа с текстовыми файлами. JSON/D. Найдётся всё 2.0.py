from sys import stdin

headers_full = []
for header in stdin:
    headers_full.append(header.rstrip("\n"))
search = str(headers_full[-1])
new_search = search.lower()
headers_full = headers_full[:-1]
for i in headers_full:
    lower_header = str(i).lower()
    if new_search in lower_header:
        print(i)
