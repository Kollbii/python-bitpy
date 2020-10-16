# Zadanie 11. Napisać program wyznaczający najmniejszą wspólną wielokrotność 3 zadanych liczb.
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
d = (x*y)/nwd(x,y) # A 
#print((x*y)/nwd(x,y)) # NWW dla a i b
print((d*z)/nwd(d,z))
