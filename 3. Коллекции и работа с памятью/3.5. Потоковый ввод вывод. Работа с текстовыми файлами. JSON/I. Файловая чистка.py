text = []
with open(input(), encoding='UTF-8') as file_in:
    for line in file_in:
        text.append(line.strip().replace("\t", "").split())
text = [word for word in text if len(word) > 0]
with open(input(), "w", encoding="UTF-8") as file_out:
    for line in text:
        print(" ".join(line), file=file_out)
