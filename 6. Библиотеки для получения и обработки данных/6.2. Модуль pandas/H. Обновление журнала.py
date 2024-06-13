# Продолжим обрабатывать DataFrame из прошлых задач.
#
# Напишите функцию update, которая добавляет к данным столбец average,
# содержащий среднюю оценку ученика, а также сортирует данные по убыванию
# этого столбца, а при равенстве средних — по имени лексикографически.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

def update(data):
    average_mark = data.assign(average=lambda x: (x["maths"] + x['physics'] + x['computer science']) / 3)
    return average_mark.sort_values(by=["average", "name"], ascending=[False, True])
