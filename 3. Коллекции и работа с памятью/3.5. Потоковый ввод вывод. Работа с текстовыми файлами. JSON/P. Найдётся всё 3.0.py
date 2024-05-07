from sys import stdin

search = input().strip()
new_search = search.lower().replace(" ", " ")
names_holder = []
for name in stdin:
    filename = name.strip() 
    with open(filename, encoding='UTF-8') as file:
        file_content = " ".join(file.read().replace(" ", " ").lower().split())
        if new_search in file_content:
            names_holder.append(filename)      
if len(names_holder) == 0:
    print("404. Not Found")
else:
    for name in names_holder:
        print(name)

