import re

final = ''

#zwaraca indeksy gdzie znajduje się '0'

def indexesOf0(stringArr):
    indexes = []
    for i in range(0, len(stringArr)):
        if(stringArr[i] == '0'):
            indexes.append(i)
    return indexes

#rekurencja i zebranie wszystkich słów pomiędzy '0'
#EDIT: Inspiracja ipv6 - usunięcie '0' pomiędzy '0' 29-33

def takeOut(givenString,stringArr): 
    takenOut = re.search(('0(.+?)0'),givenString)
    indexes = indexesOf0(stringArr)
    #print(indexes)

    if(takenOut != None):
        global final
        takenOut = re.search(('0(.+?)0'),givenString).group(1)
    
        #wrzucenie WSZYSTKICH zer pomiędzy 'zerami'

        for i in range (0,len(takenOut)):
            if(ord(takenOut[i]) == 48):                 
                newString = givenString[indexes[1]:]
                newArr = list(newString)
                return takeOut(newString,newArr)

        final += ''.join(takenOut)
        newString = givenString[indexes[1]:]
        newArr = list(newString)
        return takeOut(newString,newArr)
    else:
        return final

#zamiana na kody dziesiętne

def getDecFromString(givenString):
    decString = []
    stringArr = list(givenString)
    for i in range(0,len(givenString)):
        decString.append(ord(stringArr[i]))     #   wykorzystanie funkcji ord()
    return decString                            #   podanej w poleceniu

#Main

#givenString  = str(input("Wprowadź dowolny ciąg znaków: "))

def main(givenString):
    
    a = re.search(('0(.+?)0'),givenString)

    if(a):
        stringArr = list(givenString)
        print("String po odjęciu zer:", takeOut(givenString,stringArr))
        print("Kody ASCII:\n" + str(getDecFromString(final)))
        sortedFinalASCII = sorted(getDecFromString(final))
        my5th = list(set(sortedFinalASCII))
        print("5 co do wartości kod ASCII: " + str(my5th[4]))
        print(my5th)
    else:
        print("Podano jedno lub żadnych zer")


# Test Cases
#Zakładamy, że dane są poprawne i jest minimum 5 znaków

#print(main(givenString))           #USER

#TODO
    #Coś sortowanie w ostatnim przypadku nie działa

# print(main("00Siemaneczko000Duzo0Zer0000"))
# print(main("000000000434854719300"))
# print(main("przykladbezer"))
# print(main("wiecejnieko0mpletnego"))
# print(main("0standard0"))
print(main("Pominę0Parę000Wyrazów0BezZeraNaKoncuIPoczątku"))
