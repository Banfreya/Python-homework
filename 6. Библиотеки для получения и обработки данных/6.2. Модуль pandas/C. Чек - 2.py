# В местном магазине решили добавить анализ данных и каждый чек представлять в виде DataFrame.
# Прайс-лист уже сформирован в виде объекта Series, где индексами являются названия, а значениями — цены.
#
# Напишите функцию, cheque, которая принимает прайс-лист и список покупок в виде неопределённого количества
# именованных параметров (ключ — название товара, значение — количество).
#
# Функция должна вернуть объект DataFrame со столбцами:
#
# наименование продукта (product);
# цена за единицу (price);
# количество (number);
# итоговая цена (cost).
# Строки чека должны быть отсортированы по названию продуктов в лексикографическом порядке.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

import pandas as pd


def cheque(price_list, **purchases):
    product_list = []
    price_list_for_cheque = []
    number_list = []
    cost_list = []
    for product, number in sorted(purchases.items()):
        price = price_list[product]
        cost = price * number
        product_list.append(product)
        price_list_for_cheque.append(price)
        number_list.append(number)
        cost_list.append(cost)
    final = pd.DataFrame({
        'product': product_list,
        'price': price_list_for_cheque,
        'number': number_list,
        'cost': cost_list
    })

    return final
