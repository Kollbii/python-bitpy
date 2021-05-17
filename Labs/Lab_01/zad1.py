# Zadanie 1. Napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona.
x = 0
y = 1
# 1 1 2 3 5 8 13...
while(x < 1000000):
    print(x)
    next = x + y
    x = y 
    y = next
print("Koniec")