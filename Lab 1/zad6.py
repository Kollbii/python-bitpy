#Zadanie 6. Napisać program sprawdzający czy zadana liczba jest pierwsza

x = int(input("Wprowadź liczbę: "))
i = 1
counter = 0
while(i<x):
    if(x%i == 0):
        counter += 1
    i+=1
if(counter == 1):
    print("Jest l. pierwszą")
else:
    print("Nie jest l. pierwszą")