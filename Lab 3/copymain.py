import re

def indexesOf0(stringArr):
    indexes = []
    for i in range(0, len(stringArr)):
        if(stringArr[i] == '0'):
            indexes.append(i)
    return indexes

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

def getDecFromString(givenString):
    decString = []
    stringArr = list(givenString)
    for i in range(0,len(givenString)):
        decString.append(ord(stringArr[i]))
    return decString

# givenString  = str(input("Wprowadź dowolny ciąg znaków: "))

def main(givenString):
    a = re.search(('0(.+?)0'),givenString)
    if(a):
        stringArr = list(givenString)
        final = takeOut(givenString,stringArr,'')
        sortedFinalASCII = sorted(set(getDecFromString(final)))
        print("String po odjęciu zer:" + str(final))
        print("Kody ASCII:\n" + str(getDecFromString(final)))
        print("5 co do wartości kod ASCII: " + str(sortedFinalASCII[4]))
    else:
        return "Podano jedno lub żadnych zer"

print(main("0standard0"))                                         # standard | 115
print(main("przykladbezer"))                                      # -
print(main("wiecejniek0mpletnego"))                               # -
print(main("aaa0Siemaneczko0Dużo0Zer0aaa"))                       # SiemaneczkoDuzoZer | 99
print(main("000000000434854719300"))                              # 4348547193 | 55
print(main("Pominę0Parę000Wyrazów00000BezZeraNaKoncuIPoczątku"))  # ParęWyrazów | 119
print(main("Losowy00CiągZnaków0Oddzielony0Zerami000"))            # CiągZnakówOddzielonyZerami | 100

# print(main(givenString))