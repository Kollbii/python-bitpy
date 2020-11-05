# Proszę napisać program wczytujący tablicę dwuwymiarową o ustalonym
# wymiarze n x n wypełnioną liczbami naturalnymi. Dla danej tablicy należy napisać
# funkcję, która zwraca liczbę par elementów, o określonym iloczynie, takich że
# elementy są odległe o jeden ruch skoczka szachowego.
# Wymiar tablicy powinien być definiowany przez użytkownika.

import random

n = int(input("Podaj rozmiar tablicy [n x n]:  "))
# iloczyn = int(input("Podaj iloczyn do szukania: "))

def generTab(n):
    tab = [[0 for x in range(n)] for y in range(n)]     #dwuwymiarowa tablica wypełniona zerami
    for i in range (0, n):
        for j in range (0, n):
            tab[i][j] = random.randint(1,9)
    return tab

# Ładnie wypisze w formie "szachownicy"

def drawTab(tab):
    draw = ''    
    for i in range (0, len(tab)):
        for j in range (0, len(tab)):
            if(j == len(tab) - 1):
                draw += ''.join(str(tab[i][j]))
                draw += ''.join("\n")
            else:
                draw += ''.join(str(tab[i][j]))
                draw += ''.join(" | ")
    return draw


# print(generTab(n))
print(drawTab(generTab(n)))


# tabs = [[True]*3]*4
# print(tabs)
# print(tabs[1][0])
