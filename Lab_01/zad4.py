# Zadanie 4. Napisać program rozwiązujący równanie 𝑥^2 − 2 = 0 metodą bisekcji.
a = 1 # f(a)<0 b
b = 2 # f(b)>0 a
e = 0.000000001 #dokladnosc
def fn(x):
    return x*x - 2

while((b-a) >= e):
    c = (a+b)/2
    if( fn(c) > 0 ):
        b = c
    elif( fn(c) < 0):
        a = c
print(c)
