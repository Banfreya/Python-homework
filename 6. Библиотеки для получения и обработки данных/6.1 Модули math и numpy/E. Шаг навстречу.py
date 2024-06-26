# Два выдуманных человечка Дека и Поля, пользуются каждый своей системой координат.
# Деке нравится представлять себя в декартовом пространстве, а Поле — в полярном.
#
# Напишите программу, определяющую кратчайшее расстояние, которое нужно пройти Деке и Поле, чтобы встретиться.
#
# Формат ввода
# В первой строке записаны координаты Деки: два рациональных числа — x и y
# Во второй строке записаны координаты Поли: два рациональных числа — 𝜌 и 𝜙
#
# Формат вывода
# Одно число — расстояние между Декой и Полей.
#
# Примечание
# Дека и Поля живут на одной плоскости с общим центром.
#
# 𝜙 — измеряется в радианах.
import math

deka_x, deka_y = map(float, input().split())
polya_x, polya_y = map(float, input().split())
normal_polya_x = polya_x * math.cos(polya_y)
normal_polya_y = polya_x * math.sin(polya_y)
distance = math.sqrt((normal_polya_x - deka_x) ** 2 + (normal_polya_y - deka_y) ** 2)
print(distance)

