# Вашему решению будет предоставлена функция func, которая не имеет параметров и результата.
# Однако во время её исполнения может произойти одна из ошибок: ValueError, TypeError или SystemError.
#
# Вызовите её, обработайте ошибку и выведите её название.
# Если ошибка не произойдёт, выведите сообщение "No Exceptions".
try:
    func()
except SystemError:
    print("SystemError")
except TypeError:
    print("TypeError")
except ValueError:
    print("ValueError")
else:
    print("No Exceptions")