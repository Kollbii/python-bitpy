# #Dana jest N-elementowa tablica zawierająca liczby naturalne. W tablicy możemy
# #przeskoczyć z pola o indeksie k o n pól w prawo jeżeli wartość n jest czynnikiem
# #pierwszym liczby tablica[k]. Napisać funkcję sprawdzającą czy jest możliwe
# #przejście z pierwszego pola tablicy na ostatnie pole.

# import random

# #generowanie losowej 30 elementowej tablicy w przedziale 10-100

# def gener30():
#     tab = []
#     for i in range (0, 30):
#         tab.append(random.randint(10, 100))

#     return tab

# #sprawdzenie czy liczba tab[k] ma czynniki pierwsze równe n

# def checkPrimes(tab, k, n):
#     a = tab[k]
#     b = primeFactors(a)   #tablica z czynnikami pierwszymi liczby tab[k]

#     for i in range (0, len(b)):
#         if b[i] == n:
#             return True
#             break

#     return False

# #zwraca czynniki pierwsze podanej liczby w tablicy

# def primeFactors(a):
#     factors = []
#     c = 2
#     while a != 1:
#         while a % c == 0:
#             a /= c
#             factors.append(c)
#         c += 1
#     return factors

# #wykonanie kroku o n jednostek w prawo
# #jeśli jest koniec tablicy wraca na początek

# def step(tab, k, n):
#     boolean = checkPrimes(tab, k, n)
#     if boolean: #step
        
#         a = k+n
#         if a < len(tab):
#             return f"Przejście liczby {tab[k]} o krok {n} wynosi {tab[a]} \n{n} zawiera się w czynnikach {primeFactors(tab[k])}\n\n"
#         else:
#             while a > len(tab)-1: #dzięki temu -1 działa przechodzenie na początek :))
#                 a = a - len(tab)
#                 a += k
#             return f"Przejście liczby {tab[k]} o krok {n} wynosi {tab[a-k]} \n{n} zawiera się w czynnikach {primeFactors(tab[k])}\n\n"

#     else: #do not step
#         return f"Nie można wykonać przejścia {tab[k]} o krok {n} \n{n} nie zawiera się w czynnikach {primeFactors(tab[k])}\n\n"

#     return boolean 

# #czy mozliwe przejscie z pierwszego pola na ostatnie

# def firstToLast(tab):
#     a = tab[0]
#     b = len(tab) - 1    #ile kroków potrzeba, żeby być na ostatnim miejscu
#     factors = primeFactors(a)
#     for i in range (0, len(factors)):
#         if factors[i] == b:
#             return f"Możliwe jest przejście z pierwszego pola na ostatnie \nPierwsze pole: {tab[0]} \nCzynniki: {factors} \nDługość tablicy: {b}\n\n"
#             break
#     return f"Nie jest możliwe przejście z pierwszego pola na ostatnie \nPierwsze pole: {tab[0]} \nCzynniki: {factors} \nDługość tablicy: {b}\n\n"

# #EXAMPLE TABS

# exTab = [80,129,57,30,63,119,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# exTab1 = [119,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
# exTab2 = [874,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

# #RANDOM TABS

# for i in range(0, 5):
#     tab = gener30()
#     print(tab)
#     x = random.randint(0, 29)
#     y = random.randint(1, 9)
#     print(step(tab, x, y))
#     print(firstToLast(tab))

# # print(firstToLast(exTab1))
# # print(firstToLast(exTab2))

# #TEST CASES
# # print(step(exTab1, 0, 17))
# # print(step(exTab, 0, 5))
# # print(step(exTab, 3, 7))
# # print(step(exTab, 2, 19))
# # print(step(exTab, 1, 43))
# # print(step(exTab, 5, 17))
# # print(step(exTab, 3, 9))
# # print(step(exTab, 20, 2))

import math

def is_prime(number):
    for i in range(2, math.floor(math.sqrt(number))+1):
        if number%i == 0:
            return False
    return True

k = [92, 6, 6, 18, 112, 972, 472, 512]

def does_path_exists(_list):
    visited = [5]
    end = len(_list)-1
    for index in visited:
        number = _list[index]
        print(index, "current index")
        for i in range(2, (number//2)+1):
            if is_prime(i) and number%i == 0 and i + index <= end:
                if index+i not in _list:
                    visited.append(index+i)
    if end in visited:
        return True
    return False

print(does_path_exists(k))