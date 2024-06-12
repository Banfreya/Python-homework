# Напишите функцию length_stats, которая получает текст,
# а возвращает объект Series со словами в качестве индексов и их длинами в качестве значений.
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
    word_lengths = {word: len(word) for word in sorted(set(words))}
    length_series = pd.Series(word_lengths)
    return length_series





