# Во всех без исключения учебных заведениях ведутся журналы успеваемости.
# Это отличный пример данных, подлежащих обработке.
#
# Рассмотрим журнал летней олимпиадной школы, в которой основными предметами выступают
# математика, физика и информатика. Данные об успеваемости представлены DataFrame со столбцами:
#
# name — имя;
# maths — оценка по математике;
# physics — оценка по физике;
# computer science — оценка по информатике.
# Напишите функцию best, которая фильтрует всех «ударников» в журнале.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

def best(data):
    return data[data['maths'] >= 4][data['physics'] >= 4][data['computer science'] >= 4]
