from sys import stdin

for line in stdin:
    if "#" not in line:
        print(line.strip('\n'))
    else:
        comment_searcher = line.find("#")
        if comment_searcher == 0:
            continue
        else:
            line = list(line.strip("\n"))
            del line[comment_searcher:]
            print("".join(line))