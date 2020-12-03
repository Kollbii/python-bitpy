# Zadanie 10.
# Proszę napisać program rozwiązujący rekurencyjnie Problem Skoczka Szachowego. Należy wskazać
# kolejne ruchy skoczka wypisując macierz.

import random
import os
import time

GREEN = "\u001b[32m"
RED = "\u001b[31m"
RESET = "\u001b[0m"

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
    board[random.randint(0, len(board)) - 1][random.randint(0, len(board)) - 1] = f'{GREEN}♞{RESET}'
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
                            time.sleep(0.2)
                            return knight_problem_solve(board)
    return board

def find_next_pos(pos):
    if pos == 63:
        return [4, 3]       # Środek boardu, pozycja 0
    for i in range(0, len(solution)):
        for j in range(0, len(solution[i])):
            if solution[i][j] == pos + 1:
                return [i, j]

def knight_problem_solve_from_solution(board, c):
    if c == 63:
        return True

    for i in range (0, len(board)):
        for j in range (0, len(board[i])):
            if board[i][j] == f'{GREEN}♞{RESET}':
                pos = solution[i][j]
                next_pos = find_next_pos(pos)
                board[i][j] = f'{RED}♞{RESET}'
                board[next_pos[0]][next_pos[1]] = f'{GREEN}♞{RESET}'
                
                os.system('cls')
                print(next_pos)
                print(draw_tab(board))
                time.sleep(0.2)
                
                c += 1
                return knight_problem_solve_from_solution(board, c)

def knight_problem_2nd(board, x, y, move_x, move_y, pos):
    if pos == 64:
        return True

    for i in range (len(board)):
        new_x = x + move_x[i]
        new_y = y + move_y[i]
        if (new_x >= 0 and new_x < len(board) and new_y >= 0 and new_y < len(board) and board[new_x][new_y] == '•'):
            board[new_x][new_y] = f'{GREEN}♞{RESET}'
            board[x][y] = f'{RED}♞{RESET}'

            os.system('cls')
            print(draw_tab(board))
            time.sleep(0.01)

            if(knight_problem_2nd(board, new_x, new_y, move_x, move_y, pos+1)):
                return True

            board[new_x][new_y] = '•'
    return False

solution = [        
    [ 5, 18, 57, 36,  3, 16, 59, 46],
    [56, 37,  4, 17, 58, 47, 14, 61],
    [19,  6, 35,  2, 15, 60, 45, 48],
    [38, 55, 28, 31, 34,  1, 62, 13], 
    [ 7, 20, 33,  0, 29, 26, 49, 44],
    [54, 39, 30, 27, 32, 63, 12, 25], 
    [21,  8, 41, 52, 23, 10, 43, 50],
    [40, 53, 22,  9, 42, 51, 24, 11],
]

_moves = [
    [2,1],
    [1,2],
    [-1,2],
    [-2,1],
    [-2,-1],
    [-1,-2],
    [1,-2],
    [2,-1],
]

def start():
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board = [['•' for i in range(8)] for j in range(8)]
    # knights_board = get_start_position_knight(board)
    # knight_problem_solve(knights_board)
    # if knight_problem_solve_from_solution(knights_board, 0):
    #     print("Koniec trasy! :)")
    pos = 1
    rand_x = random.randint(0,7)
    rand_y = random.randint(0,7)
    board[rand_x][rand_y] = 0
    if(knight_problem_2nd(board, rand_x, rand_y, move_x, move_y, pos)):
        print(draw_tab(board))
    else:
        print("Nie ma rozwiązania :(")

start()