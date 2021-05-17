# Proszę napisać program wczytujący tablicę dwuwymiarową o ustalonym
# wymiarze n x n wypełnioną liczbami naturalnymi. Dla danej tablicy należy napisać
# funkcję, która zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz
# sumy elementów w kolumnie w którym leży element do sumy elementów wiersza
# w którym leży element jest największa.
# Wymiar tablicy powinien być definiowany przez użytkownika.

import random

n = int(input("Podaj n - stworzę randomową tablicę [n x n]: "))

# Najpierw tworzy Ci dwuwymiarową tablicę wypełnioną zerami [line 17]
# I dopiero w pętlach do konkretnego indeksu jest przypisywana randomowa liczba [line 20]
# Funkcja zwraca tablicę 2D o wymiarach n x n

def gener_tab(n):
    tab = [[0 for x in range(n)] for y in range(n)]
    for i in range (0, n):
        for j in range (0, n):
            tab[i][j] = random.randint(1,9)
    # print(tab)
    return tab

# Tutaj dla funu i wizualizacji napisałem pomocniczą funkcję, która wypisze mi tablicę w formie 
# kwadratu i każdy indeks i cyferka będzie na swoim miejscu
# Zachęcam do analizy ale nie powinien cię o to męczyć

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

# Te funkcje są identycznie - tylko w liczeniu sum kollumn "zamieniasz indeksy miejscami"
# Przyrównaj linijki 49 i 60. To jest zasaddnicza różnica pomiędzy tymi funkcjami.
# To dało się zapisać w jednej funkcji z jakimś prostym If'em albo zamienić parametry podane
# na wejściu ale w ten sposób prościej załapiesz idee
# Zwraca Ci tablicę z sumami elementów.

def sum_elements_row(tab):
    row_sum = []
    sum = 0
    for i in range (0, len(tab)):
        for j in range (0, len(tab)):
                sum += int(tab[i][j])
        row_sum.append(sum)
        sum = 0
    # print(row_sum)
    return row_sum

def sum_elements_collumn(tab):
    col_sum = []
    sum = 0
    for i in range (0, len(tab)):
        for j in range (0, len(tab)):
            sum += int(tab[j][i])
        col_sum.append(sum)
        sum = 0
    # print(coll_sum)
    return col_sum

# Tutaj wydaje mi się, że warto uważać z tym len(tab).
# Mamy doczynienia z kwadratową tablicą i długości tych tablic są takie same
# Warto mieć na uwadze, że może być to rozwiązane inaczej

# EDIT: Własnie usunąłem jeden parametr i też działa ;) jak coś to wcześniejsza wersja wyglądała tak:

# def compare(tab, sum_row, sum_col):
#     for i in range (0, len(tab)):
#         for j in range (0, len(tab)):

# Usuwamy to co nadmiarowe :) 

def compare(sum_row, sum_col):
    largest = 0
    row = 0
    col = 0
    for i in range (0, len(sum_col)):
        for j in range (0, len(sum_row)):
            current = round(sum_col[i]/sum_row[j], 4)
            print(f"{current} = {sum_col[i]} / {sum_row[j]}")   #To możesz usunąć albo zahaszować - służyło jako pomoc w celach weryfikacji. I dzięki temu widzisz jak pętle się iterują ^^
            if(current > largest): 
                largest = current
                col = i
                row = j
    return f"\nKolumna i wiersz: {col} , {row}\nNajwiększy iloraz sumy {largest}"

# Pozmieniaj sobie cyferki w tym arrayu bo przekopiowałem go ze swojego zadania XD
# Albo nawet usuń skoro masz funkcję która generuje Ci automatyczną tablicę

work_array = [
    [2,3,6,3,6],
    [7,2,9,4,7],
    [1,4,3,2,6],
    [7,6,8,5,7],
    [2,3,6,3,2]
]

# A tutaj już dzieje się cała magia

tab = gener_tab(n)
sum_row = sum_elements_row(tab)
sum_col = sum_elements_collumn(tab)

print(draw_tab(tab))
print(sum_col)
print(sum_row)
print(compare(sum_row, sum_col))