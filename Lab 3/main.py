import re

final = ''

#zwara indeksy gdzie znajduje się '0'

def indexesOf0(stringArr):
    indexes = []
    for i in range(0, len(stringArr)):
        if(stringArr[i] == '0'):
            indexes.append(i)
    return indexes

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


givenString  = str(input("Wprowadź dowolny ciąg znaków: "))

a = re.search(('0(.+?)0'),givenString).group(1)

if(a):
    stringArr = list(givenString)
    print(takeOut(givenString,stringArr))
else:
    print("Podano jedno lub żadnych zer")



# Test Cases
    #TODO