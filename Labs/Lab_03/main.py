import re

# zwaraca indeksy gdzie znajduje się '0'

def indexesOf0(stringArr):
    indexes = []
    for i in range(0, len(stringArr)):
        if(stringArr[i] == '0'):
            indexes.append(i)
    return indexes

# rekurencja i zebranie wszystkich słów pomiędzy '0'
# Usunięcie '0' pomiędzy '0' 24-28

def takeOut(givenString,stringArr,g): 
    final = g
    takenOut = re.search(('0(.+?)0'),givenString)
    indexes = indexesOf0(stringArr)
    # print(indexes)

    if(takenOut != None):
        takenOut = re.search(('0(.+?)0'),givenString).group(1)
    
        for i in range (0,len(takenOut)):
            if(ord(takenOut[i]) == 48):
                newString = givenString[indexes[1]:]
                newArr = list(newString)
                return takeOut(newString,newArr,final)

        final += ''.join(takenOut)
        newString = givenString[indexes[1]:]
        newArr = list(newString)
        return takeOut(newString,newArr,final)
    else:
        return final

# zamiana na kody dziesiętne

def getDecFromString(givenString):
    decString = []
    stringArr = list(givenString)
    for i in range(0,len(givenString)):
        decString.append(ord(stringArr[i]))     # wykorzystanie funkcji ord()
    return decString                            # podanej w poleceniu

def main(givenString):
    
    a = re.search(('0(.+?)0'),givenString)

    if(a):
        stringArr = list(givenString)
        final = takeOut(givenString,stringArr,'')
        sortedFinalASCII = sorted(set(getDecFromString(final)))           # usunięcie duplikatów
        ret = "String po odjeciu zer: " + str(final) + "\nKody ASCII: \n" + str(getDecFromString(final)) + "\n5 co do wartości kod ASCII: " + str(sortedFinalASCII[4]) + "\n"
        return ret
    else:
        return "Podano jedno lub żadnych zer\n"

# Test Cases
# Zakładamy, że dane są poprawne i jest minimum 5 znaków

print(main("0standard0"))                                         # standard | 115
print(main("przykladbezer"))                                      # -
print(main("wiecejniek0mpletnego"))                               # -
print(main("aaa0Siemaneczko0Dużo0Zer0aaa"))                       # SiemaneczkoDuzoZer | 99
print(main("000000000434854719300"))                              # 4348547193 | 55
print(main("Pominę0Parę000Wyrazów00000BezZeraNaKoncuIPoczątku"))  # ParęWyrazów | 119
print(main("Losowy00CiągZnaków0Oddzielony0Zerami000"))            # CiągZnakówOddzielonyZerami | 100

# User Case

# givenString  = str(input("Wprowadź dowolny ciąg znaków: "))
# print(main(givenString))