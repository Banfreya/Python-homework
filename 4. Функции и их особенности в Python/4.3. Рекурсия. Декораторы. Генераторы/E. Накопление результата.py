# В некоторых случаях полезно накапливать результат, а затем
# получать его единым списком.
#
# Реализуйте декоратор result_accumulator, который модернизирует
# функцию с неопределенным количеством позиционных параметров следующим образом:
#
# Добавляет именованный параметр method со значением по умолчанию accumulate;
# При вызове функции с параметром method равным accumulate, результат
# сохраняется в очередь (для каждой функции в собственную), а функция ничего не возвращает;
# При вызове функции с параметром method равным drop, возвращается все
# накопленные результаты, а очередь сбрасывается.
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

def result_accumulator(func):
    queue = list()

    def wrapper(*args, method="accumulate"):
        result = func(*args)
        if method == "accumulate":
            queue.append(result)
        elif method == "drop":
            queue.append(result)
            queue_for_return = list(queue)
            queue.clear()
            return queue_for_return
    return wrapper
