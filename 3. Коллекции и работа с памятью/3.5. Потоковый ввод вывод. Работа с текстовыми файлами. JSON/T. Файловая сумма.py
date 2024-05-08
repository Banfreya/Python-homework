from itertools import islice

final_sum = 0


def batched(content, n):
    it = iter(content)
    while batch := tuple(islice(it, n)):
        yield batch  # неведомая хрень, скопировала с итертулс,
# поскольку эта штука делает то, что мне нужно, но в моей версии ее нет


with open("numbers.num", mode='rb') as file_in:
    content = file_in.read()
    n = 2
    for item in batched(content, n):
        number = int.from_bytes(item, 'big')
        final_sum += number
print(final_sum % 0x10000)
