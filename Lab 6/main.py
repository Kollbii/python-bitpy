# Zadanie 3.
# Wykorzystując funkcje, napisz program tworzący plansze do sudoku. Plansze należy
# następnie zapisać do osobnych plików. Należy zapisać je w takiej formie, żeby były czytelne
# dla ludzkiego oka.
# Ponadto trzeba obsłużyć niezbędne wyjątki.

import random
from colorama import init
from termcolor import colored
init()

# mother row | baza 

def first_row():
    tab = []
    nums =[]
    for i in range (0, 9):
        rand = random.randint(1, 9)
        if rand not in nums:
            tab.append(rand)
            nums.append(rand)
        else:
            while rand in nums:
                rand = random.randint(1, 9)
            tab.append(rand)
            nums.append(rand)
    return tab

def gener_9x9():
    tab =[]
    mother_row = first_row()

    print(f"Mother row: {mother_row}\n")
    f = open("Lab 6\plansza.txt", "w")
    f.write(f"Mother row: {mother_row}\n")

    for row in range (0, 9):
        if row == 0:
            tab.append(mother_row)
        elif row == 1:
            tab.append(mother_row[3:] + mother_row[:3])
        elif row == 2:
            tab.append(mother_row[6:] + mother_row[:6])
        elif row == 3:
            tab.append(mother_row[1:] + mother_row[:1])
        elif row == 4:
            tab.append(mother_row[4:] + mother_row[:4])
        elif row == 5:
            tab.append(mother_row[7:] + mother_row[:7])
        elif row == 6:
            tab.append(mother_row[2:] + mother_row[:2])
        elif row == 7:
            tab.append(mother_row[5:] + mother_row[:5])
        else:
            tab.append(mother_row[8:] + mother_row[:8])

    drawed = draw_tab(tab)
    f.write(str(drawed))
    f.close()
    return tab

def draw_tab(tab):
    draw = ''    
    for i in range (0, len(tab)):
        for j in range (0, len(tab)):
            if(j == len(tab[i]) - 1):
                draw += ''.join(str(tab[i][j]))
                draw += ''.join("\n")
            else:
                draw += ''.join(str(tab[i][j]))
                draw += ''.join("  ") # •
    return draw

def randomize(tab):
    random_repetitions = random.randint(5,10)
    for x in range(random_repetitions):

        fle = random.randint(1, 5)
        sle = random.randint(6, 9)

        print(f"{fle} zamieniam z {sle}")

        for i in range (0, len(tab)):
            for j in range (0, len(tab[i])):
                if(tab[i][j] == fle):
                    tab[i][j] = sle
                elif(tab[i][j] == sle):
                    tab[i][j] = fle

    return tab

def delete_random(tab):
    for delete in range (0, random.randint(40,60)):
        # random_chance = random.randint(1,5)
        # if(random_chance == 1):
        ri = random.randint(0, 8)
        rj = random.randint(0, 8)
        if(tab[ri][rj] != '•'):
            tab[ri][rj] = '•'
                
    f = open("Lab 6\plansza.txt", "w", encoding='utf-8')
    f.write(f"Usunięte i zrandomizowane: \n {draw_tab(tab)}")
    f.close()
    return tab

def draw_nice(tab):
    draw = ''    
    for i in range (0, len(tab)):
        for j in range (0, len(tab)):
            if(j == 2 or j ==5):
                draw += ''.join(str(tab[i][j]))
                draw += ''.join("|")
                draw += ''.join("")
            elif(j == 8):
                draw += ''.join(str(tab[i][j]))
                draw += ''.join("|\n")
            else:
                draw += ''.join(str(tab[i][j]))
                draw += ''.join("  ") # •

    return draw

tab = gener_9x9()
print(draw_tab(tab))

randomized_tab = randomize(tab)
print(draw_tab(randomized_tab))

deleted_tab = delete_random(tab)
print(draw_tab(deleted_tab))
print(draw_nice(deleted_tab))

f = open("Lab 6\plansza.txt", "w", encoding='utf-8')
f.write(f"Usunięte i zrandomizowane:\n{draw_nice(deleted_tab)}")
f.close()