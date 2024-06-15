# Бесконечный морской бой
# Представьте себе поле морского боя, которое не имеет границ.
# Для простоты координаты выстрелов будем обозначать целыми координатами на плоскости.
#
# Бесконечное поле порождает большое количество данных, которые требуется проанализировать.
# Один из игроков для упрощения этой задачи просит вас написать программу,
# которая обрезает данные до ограниченного прямоугольника.
#
# Формат ввода
# В первой строке записано два числа — координаты верхнего левого угла. Во второй строке — правого нижнего.
#
# В файле data.csv находится датасет с координатами всех выстрелов противника.
#
# Формат вывода
# Часть датасета, ограниченная заданным прямоугольником.
#
# Примечание
# Скачать датасет из примера можно по этой ссылке.
# https://yastatic.net/s3/ml-handbook/admin/data171_4fcbd1f963.csv?updated_at=2022-11-04T09:07:51.186Z

import pandas as pd


top_left_corner = input().strip().split()
bottom_right_corner = input().strip().split()
top_x, top_y = int(top_left_corner[0]), int(top_left_corner[1])
bottom_x, bottom_y = int(bottom_right_corner[0]), int(bottom_right_corner[1])
data = pd.read_csv('data.csv')
filtered_data = data[(data['x'] >= top_x) & (data['x'] <= bottom_x) & (data['y'] >= bottom_y) & (data['y'] <= top_y)]
print(filtered_data)

