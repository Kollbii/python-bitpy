# Zadanie 3.
# Wykorzystując funkcje, napisz program tworzący plansze do sudoku.
# Plansze zapisać do osobnego pliku. Zapisać je w takiej formie, żeby były czytelne dla ludzkiego oka.
# Obsłużyć niezbędne wyjątki.

import random

# Baza całej tabeli
def first_row():
    mother_row = []
    nums =[]
    for i in range (0, 9):
        rand = random.randint(1, 9)
        if rand not in nums:
            mother_row.append(rand)
            nums.append(rand)
        else:
            while rand in nums:
                rand = random.randint(1, 9)
            mother_row.append(rand)
            nums.append(rand)
    return mother_row           # [1,2,3,6,7,8,4,5,9]

def gener_9x9():
    tab =[]
    mother_row = first_row()

    print(f"Mother row: {mother_row}\n")
    # To się na pewno dało lepiej ale spełnia swoją funkcję i jestem happy
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

    return tab

def swap_ints(tab):
    random_repetitions = random.randint(10,20)
    for x in range(random_repetitions):

        fle = random.randint(1, 5)
        sle = random.randint(6, 9)

        # print(f"{fle} zamieniam z {sle}")

        for i in range (0, len(tab)):
            for j in range (0, len(tab[i])):
                if(tab[i][j] == fle):
                    tab[i][j] = sle
                elif(tab[i][j] == sle):
                    tab[i][j] = fle

    return tab

def delete_random_positions(tab):
    counter = 0
    # for delete in range (0, random.randint(80)):
    while counter < 60:
        ri = random.randint(0, 8)
        rj = random.randint(0, 8)
        if(tab[ri][rj] != '•'):
            tab[ri][rj] = '•'
            counter += 1
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

def draw_nice(tab):
    draw = '┌─────────┬─────────┬─────────┐\n'    
    for i in range (0, len(tab)):
        if (i == 3 or i == 6):
            draw += ''.join("├─────────┼─────────┼─────────┤\n")
        for j in range (0, len(tab)):
            if(j == 2 or j ==5):
                draw += ''.join(str(tab[i][j]))
                draw += ''.join(" │ ")
            elif(j == 8):
                draw += ''.join(str(tab[i][j]))
                draw += ''.join(" │\n")
            elif(j == 0):
                draw += ''.join("│ ")
                draw += ''.join(str(tab[i][j]))
                draw += ''.join("  ")
            else:
                draw += ''.join(str(tab[i][j]))
                draw += ''.join("  ") # •
    draw += ''.join("└─────────┴─────────┴─────────┘\n")
            
    return draw


f = open("Lab 6/board.txt", 'w', encoding='utf-8')
f.write("")
f.close()
ans = open("Lab 6/base.txt", 'w', encoding='utf-8')
ans.write("")
ans.close()

for i in range (1, 6):
    tab = gener_9x9()
    randomized_tab = swap_ints(tab)
    a = draw_nice(randomized_tab)
    playable = delete_random_positions(randomized_tab)
    nice_board = draw_nice(playable)
    print(draw_nice(playable))

    f = open("Lab 6/board.txt", 'a', encoding='utf-8')
    f.write(f"Board no. {i}\n{nice_board}\n")
    f.close()

    ans = open("Lab 6/base.txt", 'a', encoding='utf-8')
    ans.write(f"Board {i} answer:\n{a}")
    ans.close()