import math

while True:
    try:
        n = int(input("Podaj przedział do którego chcesz wyznaczyc liczny pierwsze: ")) 
        n>0
        break
    except ValueError:
        print("Błędna liczba. Wprowadź liczbę naturalną.")
        continue 
    

# znajdujemy liczby pierwsze z przedziału [2, n]
def sito(n):
    pomocnicza =[1 for x in range (n+1)]
    for i in range (2, n+1):
        for j in range (i+1, n+1):
            if j%i == 0:
                pomocnicza[j] = 0

    liczbypierwsze = []
    for i in range (2, len(pomocnicza)):
        if pomocnicza[i] == 1:
            liczbypierwsze.append(i)

    return liczbypierwsze            


def ilorazliczbpierwszych(k):
    pierwsze = sito(k)
    i=0
    while(i < len(pierwsze)):
        if(i+1 == len(pierwsze)):
            print("Koniec")
            break
        else:
            a = pierwsze[i+1]//pierwsze[i] # iloraz całkowity 
            b = pierwsze[i+1] % pierwsze[i] # reszta z dzielenia 
            print(str(pierwsze[i+1]) + "/" + str(pierwsze[i]) + " = " + str(a) + " + r. " + str(b))
            i+=1

print(sito(n))
print (ilorazliczbpierwszych(n))

# s = str(input("Wprowadź znaki z * : "))
# ns = s.replace('*','')
# print("Nowy ciąg: ", ns)