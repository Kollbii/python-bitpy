#   Import biblioteki głównie dla funkcji sqrt()
import math
#   Wprowadzenie danych przez użytkownika
# x = float((input("Podaj współczynnik a: ")))
# y = float((input("Podaj współczynnik b: ")))
# z = float((input("Podaj współczynnik c: ")))

def liniowa(x,y):
    return (-1*y)/x

def kwadratowa(a,b,c):
    d = float(b*b - 4*a*c)                              #Liczenie delty
    print("------------------------------")
    print("a:", a, " b:",b, " c:",c)
    print("Delta:",d)
    print("Rozwiązanie:")
    if(d > 0):                                          #Rozważanie przypadków
        if(a == 0 and c == 0):                          #Odpowiednie warunki, żeby np. nie dzielić przez 0
            print("x1 = 0")
        elif(a == 0):
            print("x1: ", liniowa(b,c))
        else:
            x1 = (-1*b - math.sqrt(d))/(2*a)
            x2 = (-1*b + math.sqrt(d))/(2*a)
            print('x1:', round(x1,2), 'x2:', round(x2,2))
    elif(d == 0):
        if(a == 0 and c == 0):
            print("x1: 0")
        elif(a == 0):
            print("x1: ", liniowa(b,c))
        else:
            x1 = float((-1*b)/(2*a))
            print("x1: ", round(x1,2))
    else:
        print("Program nie oblicza pierwiastków w płaszczyźnie zespolonej")

#   TEST CASES
print(kwadratowa(1,-2,1)) # delta = 0
print(kwadratowa(5,90,5)) # delta > 0
print(kwadratowa(-78,0,5))
print(kwadratowa(0,51,5))
print(kwadratowa(0,45,0))
print(kwadratowa(1,2,10))
print(kwadratowa(-88,-5,1))
print(kwadratowa(0,0,0))

#   USER CASE
# print(kwadratowa(x,y,z))

#a = 0 -> liniowa
#a = 0; b = 0 -> stała
#b = 0 -> pierwiastek
#b = 0 ; c = 0 - > 0
#a = 0 ; c = 0 -> 0
