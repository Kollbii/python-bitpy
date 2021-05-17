# Zadanie 4a: Aby sprawdzić jakość wybranego generatora liczb losowych/pseudolosowych można skorzystać z twierdzenia 
# (przypisywane Ernesto Cesaro), że dwie losowo wybrane liczby całkowite są względnie pierwsze z prawdopodobieństwem:  
# 6/π2 ≈ 0,608

# Napisz zatem program, który będzie losował pary liczb całkowitych i obliczał odsetek tych, które są względnie pierwsze 
# (możesz użyć gotowych funkcji, które będą weryfikowały czy liczby są względnie pierwsze). Gdy wykonasz już dużą liczbę 
# losowań i obliczysz odsetek tych par, które są względnie pierwsze, wyznacz liczbę π, korzystając z twierdzenia Cesaro. 
# Jeśli wartość π będzie wynosiła ok. 3,14 to świetnie, ale jeśli będzie inna - zastanów się co może być tego przyczyną.

import random
from math import sqrt
counter = 0

def nwd(a, b): return nwd(b, a%b) if b else a

def generRandInts(n):
    arr = []
    for _ in range (n):
        arr.append(random.randint(10,1000))
    return arr

def generPairs():
    global counter
    pair = generRandInts(2)
    # print(pair, nwd(pair[0], pair[1]))
    if nwd(pair[0], pair[1]) == 1:
        counter += 1

if __name__ == '__main__':
    n = 100000

    for i in range(n):
        generPairs()
    print(counter)
    print("odsetek liczb pierwszych: ", counter/n)
    print("uzyskana liczba pi: ", sqrt(6/(counter/n)))