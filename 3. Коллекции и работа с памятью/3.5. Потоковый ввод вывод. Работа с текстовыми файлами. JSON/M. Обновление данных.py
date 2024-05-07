import json

file = input()
update = input()
with open(update, encoding="UTF-8") as file_in:
    records = json.load(file_in)
with open(file, 'w', encoding="UTF-8") as file_out:
    json.dump(records, file_out, ensure_ascii=False, indent=2)
    for massive in records:
        key = massive["name"]
        massive.pop("name")
        records[key] = massive