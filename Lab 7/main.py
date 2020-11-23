# Zadanie 7.
# Na szachownicy o wymiarach 100 na 100 umieszczamy N skoczków (N<100).
# Położenie skoczków jest opisywane przez tablicę
# dane=[(w1 , k 1),(w2, k 2),(w3 , k 3), ...(wN , kN)].
# Proszę napisać funkcję, która zwróci położenie skoczków wzajemnie się
# szachujących. Do funkcji należy przekazać położenie skoczków.
# Należy zwizualizować rozkład skoczków na szachownicy.
# Testy:
# 1. Przypadek, w którym nie występuje szachowanie.
# 2. Szachują się dwa skoczki.
# 3. Szachuje się więcej niż dwa skoczki.

import random
from colorama import init
init()

def draw_tab(tab):
    draw = ''    
    for i in range (0, len(tab)):
        for j in range (0, len(tab)):
            if(j == len(tab[i]) - 1):
                draw += ''.join(str(tab[i][j]))
                draw += ''.join("\n")
            else:
                draw += ''.join(str(tab[i][j]))
                draw += ''.join(" ") # •
    return draw

def get_random_position_knights(board,k):   # k < 100
    placed_knights = [[False for f in range(len(board))] for g in range(len(board))]
    c = 0
    while c < k:
        x = random.randint(0, len(board) - 1)
        y = random.randint(0, len(board) - 1)
        if placed_knights[x][y] == False:
            board[x][y] = '\u001b[32m♞\u001b[0m'        # zielone skoczki :)))
            placed_knights[x][y] = True
            c += 1
        else:
            c -= 1
    return board

def does_check(board, i, j, x, y):
    if board[i][j] == board[i + x][j + y]:
        return True
    return False

def get_checked_knights(board):
    checked_knights  = 0

    for i in range (0, len(board)):
        for j in range (0, len(board[i])):

            if board[i][j] == '\u001b[32m♞\u001b[0m':  # sprawdza tylko zielone skoczki
                for x, y in _moves:
                    if ((i + x >= 0 and i + x < len(board)) and (j + y >= 0 and j + y < len(board))):
                        checked = does_check(board, i, j, x, y)
                        if checked == True:
                            board[i][j] = '\u001b[31m♞\u001b[0m'
                            board[i + x][j + y] = '\u001b[31m♞\u001b[0m'
                            print(f"♞ na [{i}][{j}]\t szachuje ♞ na [{i + x}][{j + y}]")
                            checked_knights += 2

    if checked_knights == 0:
        print(f"Żaden ♞  się nie szachuje.")
    elif checked_knights == 2:
        print(f"\nDokładnie jedna para ♞  się szachuje!")
    else:
        print(f"\nTotalna wojna ♞")
    return board

_moves = [
    [1,2],
    [2,1],  
    [-1,2],
    [-2,1],
    [-1,-2],
    [-2,-1],
    [1,-2],
    [2,-1]
]

def start():
    board = [['•' for i in range(30)] for j in range(30)]   # zmienić na 100 potem
    knights_number = random.randint(2,100)

    knights_board = get_random_position_knights(board, knights_number)
    checked_board = get_checked_knights(knights_board)
    print(draw_tab(checked_board))

start()