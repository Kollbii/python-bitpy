import re
import random

class TestTakeOut:

    def testTakeOutString1(self):
        string = "0standard0"
        result = main(string)
        assert result == "standard"
    
    def testTakeOutString2(self):
        string = "przykladbezer"
        result = main(string)
        assert result == "Podano jedno lub żadnych zer\n"

    def testTakeOutString3(self):
        string = "aaa0Siemaneczko0Duzo0Zer0aaa"
        result = main(string)
        assert result == "SiemaneczkoDuzoZer"

    def testTakeOutString4(self):
        string = "000000000434854719300"
        result = main(string)
        assert result == "4348547193"

    def testTakeOutString5(self):
        string = "0standard0"
        result = main(string)
        assert result == "standard"

    def testTakeOutString6(self):
        string = "Pominę0Parę000Wyrazów00000BezZeraNaKoncuIPoczątku"
        result = main(string)
        assert result == "ParęWyrazów"

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
            #return f"Podany string: \t\t\t{givenString} \nString po wycięciu z zer: \t{final} \nKody ASCII: \n{getDecFromString(final)} \n5 co do wartości kod ASCII: {sortedFinalASCII[4]}\n"
    else:
        return "Podano jedno lub żadnych zer\n"

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

# print(main(randomString()))
# print(main(randomString()))
# print(main(randomString()))
# print(main(randomString()))
# print(main(randomString()))