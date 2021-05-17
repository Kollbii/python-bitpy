#   Import biblioteki głównie dla funkcji sqrt()
import math
#   Wprowadzenie danych przez użytkownika
x = float((input("Podaj współczynnik a: ")))
y = float((input("Podaj współczynnik b: ")))
z = float((input("Podaj współczynnik c: ")))

def liniowa(x, y):
    return (-1*y)/x

def kwadratowa(a , b , c):
    d = float(b*b - 4*a*c)                              #Liczenie delty
    if(d > 0):                                          #Rozważanie przypadków
        if(a == 0 and c == 0):                          #Odpowiednie warunki, żeby np. nie dzielić przez 0
            return "x1 = 0"
        elif(a == 0):
            print("x1: ", round(liniowa(b,c),4))
        else:
            x1 = (-1*b - math.sqrt(d))/(2*a)
            x2 = (-1*b + math.sqrt(d))/(2*a)
            print('x1:', round(x1,2), 'x2:', round(x2,2))
    elif(d == 0):
        if(a == 0 and c == 0):
            return "x1 = 0"
        elif(a == 0):
            print("x1: ", liniowa(b,c))
        else:
            x1 = float((-1*b)/(2*a))
            print("x1: ", round(x1,2))
    else:
        if(a == 0 and c == 0):
            return "x1 = 0"
        elif(a == 0):
            print("x1: ", liniowa(b,c))
        else:
            #obsługa liczb zespolonych (?)
            dzesp1 = math.sqrt(-1*d)       #+ "i"      #dla ładnego zapisu
            dzesp2 = -1*math.sqrt(-1*d)    #+ "i"       #części urojone
            x1 = str(-1*b/2*a) + " + " + str(round(dzesp1/(2*a),3)) + "i"
            x2 = str(-1*b/2*a) + " " + str(round(dzesp2/(2*a),3)) + "i"
            print("x1:", x1 ,"x2:", x2)

#   TEST CASES
# print(kwadratowa(1,-2,1)) # delta = 0
# print(kwadratowa(5,90,5)) # delta > 0
# print(kwadratowa(-78.31,0,5))
# print(kwadratowa(0,51,5))
# print(kwadratowa(0,-45,0))4
# print(kwadratowa(1,2,10))   # zespolone 
# print(kwadratowa(-88,-5,1))
# print(kwadratowa(1,0,50))   #zespolone
# print(kwadratowa(0,0,0))

#   USER CASE
print(kwadratowa(x,y,z))

#Try, Catch, Expect -> upgrade in future when i get better :))
#Also make code better to read