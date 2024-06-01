# Рассмотрим объект «Программист», который задаётся именем, должностью
# и количеством отработанных часов. Каждая должность имеет собственный оклад
# (заработную плату за час работы). В нашей импровизированной компании существуют 3 должности:
#
# Junior — с окладом 10 тугриков в час;
# Middle — с окладом 15 тугриков в час;
# Senior — с окладом 20 тугриков в час по умолчанию и +1 тугрик за каждое новое повышение.
# Напишите класс Programmer, который инициализируется именем и должностью (отработка у
# нового работника равна нулю). Класс реализует следующие методы:
#
# work(time) — отмечает новую отработку в количестве часов time;
# rise() — повышает программиста;
# info() — возвращает строку для бухгалтерии в формате: <имя> <количество отработанных
# часов>ч. <накопленная зарплата>тгр.
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.

class Programmer:

    def __init__(self, name, rank, hours=0, senior_counter=0, money=0):
        self.name = name
        self.rank = rank
        self.hours = hours
        self.senior_counter = senior_counter
        self.money = money

    def work(self, time):
        self.hours += time
        if self.rank == "Junior":
            self.money += time * 10
        elif self.rank == "Middle":
            self.money += time * 15
        elif self.rank == "Senior":
            self.money += time * (15 + self.senior_counter)
        return self.hours, self.money

    def rise(self):
        if self.rank == "Junior":
            self.rank = "Middle"
        elif self.rank == "Middle":
            self.rank = "Senior"
        elif self.rank == "Senior":
            self.senior_counter += 1

        return self.rank

    def info(self):
        return f"{self.name} {self.hours}ч. {self.money}тгр."



