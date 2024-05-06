with open(input(), encoding='UTF-8') as file_in_one:
    first_set = set([word for word in file_in_one.read().split()])
with open(input(), encoding='UTF-8') as file_in_two:
    second_set = set([word for word in file_in_two.read().split()])
symmetric_difference = first_set ^ second_set
with open(input(), "w", encoding="UTF-8") as file_out:
    print("\n".join(sorted(symmetric_difference)), file=file_out)