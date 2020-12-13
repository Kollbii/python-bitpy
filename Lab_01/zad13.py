# Zadanie 13. Zmodyfikować wzór Newtona aby program obliczał pierwiastek stopnia 3.
e = 0.00001 #dokładność
x = float(input("Wprowadź liczbę: "))
y=x/2
if(x > 0):
    while(abs((x/(y*y)) - y)  >= e):
        y = ((x/(y*y) + y))/2
    #print("Pierwiastek kwadratowy z " + str(x) + " wynosi: " + str(y))
    print(y)