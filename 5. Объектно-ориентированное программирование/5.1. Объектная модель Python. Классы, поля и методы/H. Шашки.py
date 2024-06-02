# Шашки очень занимательная игра, которую достаточно легко моделировать.
#
# Правила подразумевают наличие двух классов: игральная доска и шашка.
# Однако мы немного упростим себе задачу и вместо шашки будем манипулировать клетками,
# которые могут находиться в трех состояниях: пустая, белая шашка и чёрная шашка.
#
# Разработайте два класса: Checkers и Cell.
#
# Объекты класса Checkers при инициализации строят игральную доску со стандартным
# распределением клеток и должны обладать методами:
#
# move(f, t) — перемещает шашку из позиции f в позицию t;
# get_cell(p) — возвращает объект «клетка» в позиции p.
# Объекты класса Cell при инициализации принимают одно из трех состояний: W — белая шашка,
# B — чёрная шашка, X — пустая клетка, а также обладают методом status() возвращающим заложенное в ней состояние.
#
# Координаты клеток описываются строками вида PQ, где:
#
# P — столбец игральной доски, одна из заглавных латинских букв: ABCDEFGH;
# Q — строка игральной доски, одна из цифр: 12345678.
# Будем считать, что пользователь всегда ходит правильно и контролировать возможность хода не требуется.
#
# Примечание
# Ваше решение должно содержать только классы и функции.
# В решении не должно быть вызовов инициализации требуемых классов.

class Checkers:
    def __init__(self):
        self.board = {}
        checker_board = 'XBXBXBXB' + 'BXBXBXBX' + 'XBXBXBXB' + 'XXXXXXXX' + \
            'XXXXXXXX' + 'WXWXWXWX' + 'XWXWXWXW' + 'WXWXWXWX'
        counter = 0
        for row in '87654321':
            for column in 'ABCDEFGH':
                self.board[column + row] = Cell(checker_board[counter])
                counter += 1

    def get_cell(self, p_position):
        return self.board[p_position]

    def move(self, f_position, t_position):
        old_state = self.board[f_position].status()
        self.board[f_position].state = 'X'
        self.board[t_position].state = old_state
        return old_state


class Cell:
    def __init__(self, cell='X') -> None:
        self.state = cell

    def status(self):
        return self.state





