import re

final = ''
decString = []

#zwara indeksy gdzie znajduje się '0'

def indexesOf0(stringArr):
    indexes = []
    for i in range(0, len(stringArr)):
        if(stringArr[i] == '0'):
            indexes.append(i)
    return indexes

#rekurencja i zebranie wszystkich słów pomiędzy '0'

def takeOut(givenString,stringArr): 
    takenOut = re.search(('0(.+?)0'),givenString)
    indexes = indexesOf0(stringArr)
    print(indexes)
    if(takenOut != None):
        takenOut = re.search(('0(.+?)0'),givenString).group(1)
        global final
        final += ''.join(takenOut)
        newString = givenString[indexes[1]:]
        newArr = list(newString)
        # print('final:',final)
        # print('newString:', newString)
        # print('newArr', newArr)
        return takeOut(newString,newArr)
    else:
        return final

#zamiana na kody dziesiętne

def getDecFromString(givenString):
    global decString
    stringArr = list(givenString)
    for i in range(0,len(givenString)):
        decString.append(ord(stringArr[i]))     #   wykorzystanie funkcji ord()
    return decString                            #   podanej w poleceniu


#Main

givenString  = str(input("Wprowadź dowolny ciąg znaków: "))

a = re.search(('0(.+?)0'),givenString).group(1)

if(a):
    stringArr = list(givenString)
    print(takeOut(givenString,stringArr))
    print(getDecFromString(final))
else:
    print("Podano jedno lub żadnych zer")





# Test Cases

#Zakładamy, że dane są poprawne i jest minimum 5 znaków

#TODO