final_line = ""
while (line := input()) != "ФИНИШ":
    final_line += line.lower().replace(" ", "")  
symbol = final_line[0]
symbol_count = final_line.count(final_line[0])
for i in sorted(set(final_line)):  
    if i != " ": 
        if final_line.count(i) > symbol_count:
            symbol = i
            symbol_count = final_line.count(i)
print(symbol)