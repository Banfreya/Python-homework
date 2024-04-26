while (log := input()) != "":
    log = list(log)
    if ["@", "@", "@"] == log[-3:]:
        continue
    elif ['#', '#'] == log[0:2]:
        del log[0:2]
        print("".join(log))
    else:
        print("".join(log))
