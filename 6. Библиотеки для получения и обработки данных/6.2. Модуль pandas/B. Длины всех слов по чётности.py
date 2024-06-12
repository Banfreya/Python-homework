# В этот раз продумайте функцию length_stats, которая получает текст,
# а возвращает пару объектов Series со словами в качестве индексов и их длинами в качестве значений.
#
# Все слова в тексте предварительно переведите в нижний регистр,
# избавьтесь от знаков препинания и цифр, а также отсортируйте в лексикографическом порядке.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

import pandas as pd
import re


def length_stats(text):
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    words = [word for word in text.split() if word]
    odd_words = [word for word in words if len(word) % 2 != 0]
    even_words = [word for word in words if len(word) % 2 == 0]
    odd_dict = {word: len(word) for word in sorted(set(odd_words))}
    even_dict = {word: len(word) for word in sorted(set(even_words))}
    odd = pd.Series(odd_dict, dtype='int64')
    even = pd.Series(even_dict, dtype='int64')

    return odd, even

