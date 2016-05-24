# coding: utf-8

from __future__ import print_function

board = dict([(x, x) for x in range(1, 10)])


# --------------------------------------------------
# Helper functionsч
# --------------------------------------------------

def get_y(n):
    "It calculates the cell y using number."
    return (n - 1) // 3 + 1


def get_x(n, y):
    "It calculates the cell x using number"
    return n - (y - 1) * 3


def get_n(x, y):
    "It calculates the cell number using x and y."
    return (y - 1) * 3 + x


# --------------------------------------------------
# Main functions
# --------------------------------------------------

def draw_board(board):
    "It draws the game board."
    print("\n-------------")
    for y in range(1, 4):
        print("|", end='')
        for x in range(1, 4):
            n = get_n(x, y)
            print(" %s |" % board[n], end='')
        print("\n-------------")
    return


def users_input():
    """
    Функция запускает игру и спрашивает, что игроки вводят.
    Используйте цикл while и raw_input.
    """
    pass


def inputs_check(user_n, cell_n):
    """
    Функия проверки. Проверяем, что: введённый символ число,
    число больше 1 и меньше 9, выбранная клетка не занята и
    в конце проверим выиграшные комбинации.
    """
    pass


draw_board(board)
