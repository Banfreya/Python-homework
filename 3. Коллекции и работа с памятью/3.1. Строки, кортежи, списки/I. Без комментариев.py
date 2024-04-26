while (code := input()) != "":
    if "#" not in code:
        print(code)
    else:
        comment_searcher = code.find("#")
        if comment_searcher == 0:
            continue
        else:
            code = list(code)
            del code[comment_searcher:]
            print("".join(code))
