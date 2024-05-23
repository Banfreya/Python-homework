# Ключевой секрет
# Вася любит секреты и шифрование. Он часто пользуется
# шифром на основе замен и просит разработать вас функцию,
# которая позволит ему быстро шифровать сообщения.
#
# Напишите функцию secret_replace(text, **replaces), которая принимает:
#
# текст требующий шифрования;
# именованные аргументы — правила замен, представляющие собой кортежи
# из одного или нескольких значений.
# Функция должна вернуть зашифрованный текст.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
#
# Обратите внимание, что позиционный аргумент требуемой функции не
# должен иметь однобуквенного имени. Для понимания ошибки исследуйте следующих код:
#
# def func(a, **b):
#     ...
#
# func(1, **{'a': 2})


def secret_replace(text, **replaces):
    replace_dict = dict()
    final_text = ""
    for key, value in replaces.items():
        replace_dict[key] = list(value)
    for letter in text:
        if letter in replace_dict:
            letter_change = replace_dict[letter].pop(0)
            replace_dict[letter] += {letter_change}
            final_text += letter_change
        else:
            final_text += letter

    return final_text
