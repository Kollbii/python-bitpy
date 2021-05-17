# Proszę napisać program wczytujący tablicę dwuwymiarową o ustalonym
# wymiarze n x n wypełnioną liczbami naturalnymi. Dla danej tablicy należy napisać
# funkcję, która zwraca liczbę par elementów, o określonym iloczynie, takich że
# elementy są odległe o jeden ruch skoczka szachowego.
# Wymiar tablicy powinien być definiowany przez użytkownika.

import random

# Randomowa tablica o rozmiarze nxn wypełniona losowymi liczbami z zakresu

def gener_tab(n):
    tab = [[random.randint(1,9) for x in range(n)] for y in range(n)]     #dwuwymiarowa tablica wypełniona zerami
    return tab

# Ładnie wypisze w formie "szachownicy"

def draw_tab(tab):
    draw = ''    
    for i in range (0, len(tab)):
        for j in range (0, len(tab[i])):
            if(j == len(tab[i]) - 1):
                draw += ''.join(str(tab[i][j]))
                draw += ''.join("\n")
            else:
                draw += ''.join(str(tab[i][j]))
                draw += ''.join(" | ")
    return draw

# Sprawdza czy iloczyn tych par jest równy zadanemu iloczynowi

def check_multiplication(tab, i, j, x, y, l):
    if(tab[i][j] * tab[i+x][j+y] == l):
        return True
    return False

# Wyszukuje WSZYSTKIE możliwe przeskoki
# Zwraca tablicę WSZYSTKICH możliwych przeskoków o zadanym iloczynie ale z POWTÓRZENIAMI

def find_possible_pairs(tab, l):
    possible_pairs = []
    
    if(len(tab) < 3):
        print("Za mała tablica! Skoczek nie ma gdzie skoczyć :)")
    else:
        for i in range (0, len(tab)):
            for j in range(0, len(tab[i])):
                for x, y in _moves:

                    if((i + x >= 0 and i + x < len(tab)) and (j + y >= 0 and j + y < len(tab))):
                        if(check_multiplication(tab, i, j, x, y, l)):
                            print(f"Start index: [{i}] [{j}] = {tab[i][j]} przejście o {x} {y} --> [{i+x}] [{j+y}] = {tab[i+x][j+y]}")
                            possible_pairs.append([tab[i][j], tab[i+x][j+y]])
                        
    print(f"\n{draw_tab(tab)}")
    return possible_pairs

# No to tutaj wyrzucam te duplikaty bo zwykły set() na 2D array'u nie chciał działać

def remove_duplicates(tab):
    seen = set()
    new_tab = []
    for x in tab:
        a = tuple(x)
        if a not in seen:
            new_tab.append(x)
            seen.add(a)
    return new_tab


work_array = [
    [2,3,6,3,6],
    [7,2,9,4,7],
    [1,4,3,2,6],
    [7,6,8,5,7],
    [2,3,6,3,2]
]

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

# n = int(input("Podaj rozmiar tablicy [n x n]:  "))
# l = int(input("Podaj iloczyn do szukania: "))

# print(remove_duplicates(find_possible_pairs(gener_tab(n), l)))

for i in range(0, 5):
    tab_size = random.randint(1,10)
    ilcz = random.randint(1,20)
    print(f"\n------------------------------\nIloczyn: {ilcz} | Rozmiar tablicy: {tab_size}")
    print(remove_duplicates(find_possible_pairs(gener_tab(tab_size), ilcz)))
    print(f"\n------------------------------\n")