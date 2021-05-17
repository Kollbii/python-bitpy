# Zadanie 8. Napisać program wyszukujący liczby doskonałe mniejsze od miliona.

def czyDoskonala(x):
    podzielniki = []
    sm = 0
    for i in range(1,x):
        if(x%i == 0):
            podzielniki.append(i)
            #print(i)

    for i in range(0,len(podzielniki)):
        sm += podzielniki[i]

    #print("Suma: " + str(sm))
    if(sm == x):
        return True
        #print("Liczba jest liczbą doskonałą")
    else:
        return False
        #print("Liczba nie jest liczbą doskonałą")

#print(czyDoskonala(28)) 

for i in range(1,8129): # Kolejna l. doskonała to 33550336 więc dla oszczędzenia komputera wpisuje taki range
    if(czyDoskonala(i) == True):
        print(i)
