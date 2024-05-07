import json
from sys import stdin

lines = []
for line in stdin:
    lines.append(line.strip()) 

with open("scoring.json", encoding='UTF-8') as file_in:
    scoring = json.load(file_in)
final_score = 0
for test_group in scoring:
    full_points = test_group.get("points")
    points_per_item = full_points / len(test_group["tests"])
    for test in test_group["tests"]:
        pattern = test.get("pattern")
        if pattern in lines: 
            final_score += points_per_item
print(int(final_score))

