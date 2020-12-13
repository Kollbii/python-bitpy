import re
import random

class TestTakeOut:
    def testTakeOutString(self):
        string1 = "0standard0"
        result1 = main(string1)
        assert result1 == "standard"

        string2 = "przykladbezer"
        result2 = main(string2)
        assert result2 == "Podano jedno lub żadnych zer\n"

        string3 = "aaa0Siemaneczko0Duzo0Zer0aaa"
        result3 = main(string3)
        assert result3 == "SiemaneczkoDuzoZer"

        string4 = "000000000434854719300"
        result4 = main(string4)
        assert result4 == "4348547193"


def indexesOf0(stringArr):
    indexes = []
    for i in range(0, len(stringArr)):
        if stringArr[i] == '0':
            indexes.append(i)
    return indexes

def takeOut(givenString, stringArr, g): 
    final = g
    takenOut = re.search(('0(.+?)0'), givenString)
    indexes = indexesOf0(stringArr)

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

def getDecFromString(givenString):
    decString = []
    stringArr = list(givenString)
    for i in range(0, len(givenString)):
        decString.append(ord(stringArr[i]))
    return decString


def main(givenString):
    a = re.search(('0(.+?)0'), givenString)
    if(a):
        stringArr = list(givenString)
        final = takeOut(givenString, stringArr, '')
        sortedFinalASCII = sorted(set(getDecFromString(final)))     # usunięcie duplikatów
        if len(sortedFinalASCII) < 5:
            return f"Jest mniej niż 5 kodów ASCII\n"
        else:
            return final
            # return f"Podany string: \t\t\t{givenString} \nString po wycięciu z zer: \t{final} \nKody ASCII: \n{getDecFromString(final)} \n5 co do wartości kod ASCII: {sortedFinalASCII[4]}\n"
    else:
        return "Podano jedno lub żadnych zer\n"

# Test Case
# Zakładamy, że dane są poprawne i jest minimum 5 znaków

# print(main("0standard0"))                                         # standard | 115
# print(main("przykladbezer"))                                      # -
# print(main("wiecejniek0mpletnego"))                               # -
# print(main("aaa0Siemaneczko0Dużo0Zer0aaa"))                       # SiemaneczkoDuzoZer | 99
# print(main("000000000434854719300"))                              # 4348547193 | 55
# print(main("Pominę0Parę000Wyrazów00000BezZeraNaKoncuIPoczątku"))  # ParęWyrazów | 119
# print(main("Losowy00CiągZnaków0Oddzielony0Zerami000"))            # CiągZnakówOddzielonyZerami | 100

# randomowy string o długości od 10 do 50 znaków
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

print(main(randomString()))
print(main(randomString()))
print(main(randomString()))
print(main(randomString()))
print(main(randomString()))