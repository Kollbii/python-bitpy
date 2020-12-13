#Zadanie 5. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
#liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.

fib1 = 0
fib2 = 1
x = int(input("Podaj liczbę: "))
final = False
while(fib1 < 1000000): # Tyle w zupełności wystarczy
    #print(fib1)
    next = fib1 + fib2
    fib1 = fib2 
    fib2 = next

    if(fib1*fib2 == x):
        final = True
        break

if(final):
    print("Jest iloczynem dwóch kolejnych wyrazów C.F.")
else:
    print("Nie jest iloczynem dwóch kolejnych wyrazów C.F.")