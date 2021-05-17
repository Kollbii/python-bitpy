# Zadanie 7. Napisać program wypisujący podzielniki liczby

x = int(input("Podaj liczbę: "))
i = 1
podzielniki = []
print("Podzielniki libczy " + str(x) + " to: ")
#print(isinstance((x/i),int))
for i in range(1,x+1):
    if(x%i == 0):
        podzielniki.append(i)

for i in range(0,len(podzielniki)):
    print(int(podzielniki[i]))
