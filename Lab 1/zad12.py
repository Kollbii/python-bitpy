# Zadanie 12. Napisać program wyznaczający wartość do której zmierza iloraz dwóch kolejnych
# wyrazów ciągu Fibonacciego. Wyznaczyć ten iloraz dla różnych wartości początkowych wyrazów
# ciągu.

fibNumbers = []
x = 0
y = 1
c = 0
ilorazy = []
while(x < 100000):
    fibNumbers.append(x)
    next = x + y
    x = y 
    y = next

for i in range(0,len(fibNumbers)):
    # print(fibNumbers[i])
    if(i == len(fibNumbers) - 1):
        break
    else:
        ilorazy.append(fibNumbers[i]/fibNumbers[i+1])
        print(ilorazy[i])