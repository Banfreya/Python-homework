# Магазин, для которого вы писали функцию в предыдущей задаче, проводит акцию:
#
# При покупке больше двух товаров — скидка 50%
#
# мелкий шрифт: скидка распространяется только на товары купленные в количестве более двух штук
#
# Напишите функцию discount, принимающую чек из прошлой задачи и возвращающую новый с учётом акции.
#
# Примечание
# Не удаляйте функцию cheque, она потребуется для тестирования.
#
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


def discount(final):
    discounted_cheque = final.copy()
    if len(discounted_cheque) > 2:
        discounted_cheque.loc[discounted_cheque['number'] > 2, 'cost'] *= 0.5
    return discounted_cheque
