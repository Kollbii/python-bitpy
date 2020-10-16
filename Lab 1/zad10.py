# Zadanie 10. Napisać program wyznaczający największy wspólny dzielnik 3 zadanych liczb.
x = int(input("Podaj liczbe 1: "))
y = int(input("Podaj liczbe 2: "))
z = int(input("Podaj liczbe 3: "))

def nwd(a, b):
    while (b>0):
        temp = a
        a = b
        b = temp%b
    return a
#print(nwd(24, 36))
print(nwd(nwd(x,y),z))
