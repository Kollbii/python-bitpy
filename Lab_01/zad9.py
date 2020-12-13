# Zadanie 9. Napisać program wyszukujący liczby zaprzyjaźnione mniejsze od miliona.

def sumDz(n):
    sum = 0
    for i in range(1,n):
        if(n%i == 0):
            sum+= i
    return sum


for i in range(1, 20000): # tutaj range dać do 1 mln i będzie dobrze ale coś powyżej tych 20k liczy i liczy :c
    x  = sumDz(i)
    if(i > x):
        if( i == sumDz(x)):
            print(str(i) + " i " + str(x))
