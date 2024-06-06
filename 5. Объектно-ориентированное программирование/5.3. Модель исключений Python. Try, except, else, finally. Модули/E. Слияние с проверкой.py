# Когда-то вы уже писали функцию merge, которая производит слияние двух отсортированных кортежей.
#
# Давай-те её немного переработаем.
#
# Введём систему проверок:
#
# если один из параметров не является итерируемым объектом, то вызовите исключение StopIteration;
# если значения входных параметров содержат «неоднородные» данные, то вызовите исключение TypeError;
# если один из параметров не отсортирован, то вызовите исключение ValueError.
# Проверки следует проводить в указанном порядке.
#
# Если параметры прошли все проверки, верните итерируемый объект, являющийся слиянием двух переданных.
#
# Примечание
# В решении не должно быть вызовов требуемых функций.

def merge(first_tuple, second_tuple):
    if not hasattr(first_tuple, '__iter__') or not hasattr(second_tuple, '__iter__'):
        raise StopIteration
    first_tuple = tuple(first_tuple)
    second_tuple = tuple(second_tuple)
    if not first_tuple or not all([isinstance(x, type(first_tuple[0])) for x in first_tuple + second_tuple]):
        raise TypeError
    if first_tuple != tuple(sorted(first_tuple)) or second_tuple != tuple(sorted(second_tuple)):
        raise ValueError
    merged_list = sorted(first_tuple + second_tuple)
    return tuple(merged_list)

