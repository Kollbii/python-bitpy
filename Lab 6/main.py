# Zadanie 3.
# Wykorzystując funkcje, napisz program tworzący plansze do sudoku. Plansze należy
# następnie zapisać do osobnych plików. Należy zapisać je w takiej formie, żeby były czytelne
# dla ludzkiego oka.
# Ponadto trzeba obsłużyć niezbędne wyjątki.


import random
from random import randint
from colorama import init
from termcolor import colored
init()

# prościej jest wygenerować tablicę 2 wymiarową 9x9         if item in my_list

def gener_tab():
    tab = [[0 for i in range(9)] for j in range(9)]
    nums = []
    for i in range(0, 9):
        for j in range(0, 9):
            rand = random.randint(1, 9)
            row_tab = tab_row(tab, i, j)
            col_tab = tab_col(tab, i, j)
            if(i == 0):
                if rand in nums:
                    while rand in nums:
                        rand = random.randint(1,9)
                    nums.append(rand)
                    tab[i][j] = rand
                else:
                    nums.append(rand)
                    tab[i][j] = rand

            else:
                while rand in row_tab and rand in col_tab:
                    rand = random.randint(1, 9)
                nums.append(rand)
                tab[i][j] = rand
            print(row_tab)
            print(col_tab)
        # print(nums)
        nums = []
    return tab

def check_col(tab, rand, i, j):
    for x in range (0, i):
        if(rand == tab[x][j]):
            print(rand, tab[x][j])
            return False
    return True

def tab_col(tab, i, j):
    tab_col = []
    for x in range (0, i):
        tab_col.append(tab[x][j])
    return tab_col

def tab_row(tab, i, j):
    tab_row = []
    for x in range (0, j):
        tab_row.append(tab[i][x])
    return tab_row


def draw_tab(tab):
    draw = ''    
    for i in range (0, len(tab)):
        for j in range (0, len(tab[i])):
            if(j == len(tab[i]) - 1):
                draw += ''.join(str(tab[i][j]))
                draw += ''.join("\n")
            else:
                draw += ''.join(str(tab[i][j]))
                draw += ''.join(", ")
    return draw





print(colored("Super tekst", "cyan"))

tab = draw_tab(gener_tab())
print(tab)


# zapisywanie do pliku

f = open("Lab 6\plansza.txt", "w")
f.write("this does now print in row unique elements!\n")
f.write(str(tab))
f.close()