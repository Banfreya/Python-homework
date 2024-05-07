import json

with open(input(), encoding='UTF-8') as file_in:
    numbers = [int(number) for number in file_in.read().split()]
    number_sum = sum(numbers)
    positive_length = len([number for number in numbers if number > 0])
    records = {"count": len(numbers),
               "positive_count": positive_length,
               "min": min(numbers),
               "max": max(numbers),
               "sum": sum(numbers),
               "average": float(sum(numbers) / len(numbers))}
with open(input(), "w", encoding="UTF-8") as file_out:
    json.dump(records, file_out, ensure_ascii=False, indent=2)
