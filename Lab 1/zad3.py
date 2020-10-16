# Zadanie 3. Napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona.
e = 0.000001 #dokładność
x = float(input("Wprowadź liczbę: "))
y=x/2
if(x > 0):
    while(abs(x/y - y)/2  >= e):
        y = (x/y + y)/2
    print("Pierwiastek kwadratowy z " + str(x) + " wynosi: " + str(y))
else:
    print("Wprowadź liczbę dodatnią")