# Zadanie 10.
# Proszę napisać program rozwiązujący rekurencyjnie Problem Skoczka Szachowego. Należy wskazać
# kolejne ruchy skoczka wypisując macierz.

import random
import os
import time
from colorama import init
init()

def draw_tab(tab):
    draw = ''    
    for i in range (0, len(tab)):
        for j in range (0, len(tab[i])):
            if(j == len(tab[i]) - 1):
                draw += ''.join(str(tab[i][j]))
                draw += ''.join("\n")
            else:
                draw += ''.join(str(tab[i][j]))
                draw += ''.join(" ") # •
    return draw

def get_start_position_knight(board):
    board[random.randint(0, len(board)) - 1][random.randint(0, len(board)) - 1] = '\u001b[32m♞\u001b[0m'
    # board[0][0] = '\u001b[32m♞\u001b[0m'
    return board

def knight_problem_solve(board):
    for i in range (0, len(board)):
        for j in range (0, len(board[i])):

            if board[i][j] == '\u001b[32m♞\u001b[0m':    
                for x, y in _moves:
                    if ((i + x >= 0 and i + x < len(board)) and (j + y >= 0 and j + y < len(board))):
                        if board[i + x][j + y] == '\u001b[31m♞\u001b[0m':
                            continue
                        else:
                            board[i][j] = '\u001b[31m♞\u001b[0m'
                            board[i + x][j + y] = '\u001b[32m♞\u001b[0m'
                            os.system('cls')
                            print(draw_tab(board))
                            time.sleep(0.1)
                            return knight_problem_solve(board)
    return board

_moves = [
    [2,-1],
    [2,1],  
    [1,2],
    [-1,2],
    [-2,-1],
    [1,-2],
    [-1,-2],
    [-2,1]
]

def start():
    for i in range(0, 1):
        board = [['•' for i in range(8)] for j in range(8)]
        knights_board = get_start_position_knight(board)
        checked_board = knight_problem_solve(knights_board)
        print(draw_tab(checked_board))

start()