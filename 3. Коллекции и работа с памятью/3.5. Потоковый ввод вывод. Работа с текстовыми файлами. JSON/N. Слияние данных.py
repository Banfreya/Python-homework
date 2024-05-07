import json

old = input()
with open(old, encoding='UTF-8') as file:
    old_database = json.load(file)
with open(input()) as file:
    update = json.load(file)
searcher = 'name'
updated_json = {}
for massive in old_database:
    name = massive.pop(searcher)
    updated_json[name] = massive
for massive in update:
    name = massive.pop(searcher)
    if name not in updated_json: 
        updated_json[name] = {}
    for key, value in massive.items():
        if key not in updated_json[name] or value > updated_json[name][key]:
            updated_json[name][key] = value
with open(old, 'w') as file:
    json.dump(updated_json, file, sort_keys=False, indent=2, ensure_ascii=False)