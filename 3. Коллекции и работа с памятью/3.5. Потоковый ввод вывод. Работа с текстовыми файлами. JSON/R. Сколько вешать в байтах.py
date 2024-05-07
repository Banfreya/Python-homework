import os
import math

file = input()
size = os.path.getsize(file)
if size >= 1073741824:
    gigabyte = math.ceil(9.3132257461548E-10 * size)
    print(str(gigabyte) + 'ГБ')
elif size >= 1048576:
    megabyte = math.ceil(9.5367431640625E-7 * size)
    print(str(megabyte) + 'МБ')

elif size >= 1024:
    kilobyte = math.ceil(0.0009765625 * size)
    print(str(kilobyte) + 'КБ')
elif size >= 1:
    byte = math.ceil(size)
    print(str(byte) + 'Б')
else:
    bit = size / 0.125
    print(str(bit) + 'б')
