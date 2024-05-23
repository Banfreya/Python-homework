# Напишите функцию can_eat, которая принимает положение
# коня и другой фигуры в виде кортежей из двух координат,
# а возвращает булево значение: True если конь съедает
# фигуру и False иначе.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций

def can_eat(knight_coordinates, figure_coordinates):
    knight_x = knight_coordinates[0]
    knight_y = knight_coordinates[1]
    figure_x = figure_coordinates[0]
    figure_y = figure_coordinates[1]
    min_y = min(knight_y, figure_y)
    max_y = max(knight_y, figure_y)
    min_x = min(knight_x, figure_x)
    max_x = max(knight_x, figure_x)
    if (max_y - min_y) > 2 or (max_x - min_x) > 2:
        return False
    elif (max_y - min_y) == 1 and (max_x - min_x) == 1:
        return False
    elif (max_y - min_y) == 1 or (max_x - min_x) == 1:
        return True
    elif (max_y - min_y) == 2 and (max_x - min_x) == 0:
        return True
    elif (max_y - min_y) == 0 and (max_x - min_x) == 2:
        return True
    else:
        return False

