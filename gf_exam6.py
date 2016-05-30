# coding: utf-8

from __future__ import print_function
from random import choice


board = dict([(x, x) for x in range(1, 10)])

# --------------------------------------------------
# Helper functionsч
# --------------------------------------------------

def get_n(x, y):
    "It calculates the cell number using x and y."
    return (y - 1) * 3 + x


# --------------------------------------------------
# Main functions
# --------------------------------------------------

def draw_board(board):
    "It draws the game board."
    print("\n+---+---+---+")
    for y in range(1, 4):
        print("|", end='')
        for x in range(1, 4):
            n = get_n(x, y)
            print(" %s |" % board[n], end='')
        print("\n+---+---+---+")
    return


def users_input(sign):
    """
    Функция запускает игру и спрашивает, что игроки вводят.
    Используйте цикл while и raw_input.
    Проверяем, что: введённый символ число, число больше 1 и
    меньше 9, выбранная клетка не занята.
    """
    while True:
        v = raw_input('Куда ставим %s - ' % sign)
        try:
            v = int(v)
        except ValueError:
            print(u'Введёное значение должно быть цифрой.')
            continue
        else:
            if v < 1 or v > 9:
                print(u'Значение должно быть болше 1 и меньше 9.')
                continue
            elif str(board[v]) in 'XO':
                print(u'Клетка уже занята.')
                continue
            else:
                board[v] = sign
                break


def inputs_check(board):
    """
    Функия проверки выигрыша. Проверяет выиграшные комбинации.
    """
    wins = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
            (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]]:
            return board[w[0]]
    return False


def bot_move(sign):
    """
    1. Проверим, есть ли выигрышный ход у бота;
    2. Проверим, есть ли выигрышный ход у соперника;
    3. Ходим в "удачные" клетки;
    4. Выбираем ход рандомно.
    """
    board_copy = board.copy()
    empty_cells = [k for k, v in board.items() if str(v) not in 'XO']
    for i in empty_cells:
        board_copy[i] = sign
        win = inputs_check(board_copy)
        board_copy[i] = i
        if win:
            return i
    for i in empty_cells:
        board_copy[i] = "O"
        win = inputs_check(board_copy)
        board_copy[i] = i
        if win:
            return i
    good_cells = [1, 9, 3, 7]
    good = [i for i in good_cells if i in empty_cells]
    if good:
        return choice(good)
    return choice(empty_cells)


def main(board):
    for c in range(9):
        draw_board(board)
        if c % 2 == 0:
            i = bot_move("X")
            board[i] = "X"
            print('Ход бота %s' % i)
        else:
            users_input("O")
        if c >= 4:
            ans = inputs_check(board)
            if ans:
                draw_board(board)
                print(ans, 'победил')
                break
    else:
        print('Ничья')


main(board)
