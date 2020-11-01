import re
import random
# zwaraca indeksy gdzie znajduje się '0'

def indexesOf0(stringArr):
    indexes = []
    for i in range(0, len(stringArr)):
        if stringArr[i] == '0':
            indexes.append(i)
    return indexes

# rekurencja i zebranie wszystkich słów pomiędzy '0'
# usunięcie zer pomiędzy zerami

def takeOut(givenString, stringArr, g): 
    final = g
    takenOut = re.search(('0(.+?)0'), givenString)
    indexes = indexesOf0(stringArr)
    # print(indexes)

    if takenOut != None:
        takenOut = re.search(('0(.+?)0'), givenString).group(1)
    
        for i in range (0, len(takenOut)):
            if ord(takenOut[i]) == 48:
                newString = givenString[indexes[1]:]
                newArr = list(newString)
                return takeOut(newString, newArr, final)

        final += ''.join(takenOut)
        newString = givenString[indexes[1]:]
        newArr = list(newString)
        return takeOut(newString, newArr, final)
    else:
        return final

# zamiana na kody dziesiętne

def getDecFromString(givenString):
    decString = []
    stringArr = list(givenString)
    for i in range(0, len(givenString)):
        decString.append(ord(stringArr[i]))     # wykorzystanie funkcji ord()
    return decString                            # podanej w poleceniu


def main(givenString):
    
    a = re.search(('0(.+?)0'), givenString)

    if(a):
        stringArr = list(givenString)
        final = takeOut(givenString, stringArr, '')
        sortedFinalASCII = sorted(set(getDecFromString(final)))           # usunięcie duplikatów
        if len(sortedFinalASCII) < 5:
            return f"Jest mniej niż 5 kodów ASCII\n"
        else:
            return f"Podany string: \t\t\t{givenString} \nString po wycięciu z zer: \t{final} \nKody ASCII: \n{getDecFromString(final)} \n5 co do wartości kod ASCII: {sortedFinalASCII[4]}\n"
    else:
        return "Podano jedno lub żadnych zer\n"

# Test Case
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


# Random Case

# randomowy string o długości od 20 do 50 znaków
# ASCII od 48 do 122

def randomString():
    randString = ""
    a = random.randint(10, 50)

    for i in range (0, a):
        zeroChance = random.randint(1, 10)
        char = random.randint(48, 122)
        if zeroChance == 1:
            randString += ''.join('0')
        else:
            randString += ''.join(chr(char))

    return randString

# print(randomString())
# print(main(randomString()))
# print(main(randomString()))
# print(main(randomString()))
# print(main(randomString()))
# print(main(randomString()))