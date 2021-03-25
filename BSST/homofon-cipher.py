import random
string = "jak  latwo  zauwazyc  szyfr  monoalfabetyczny  nie  jest  wcale  bezpieczny  poniewaz zdradza  charakterystyke  jezykowa  tekstu  zaszyfrowanego"

alphabetDict = {
    "a":[244,245,231,181,182,183,232,132],
    "b":[128,129,130],
    "c":[254,251,250],
    "d":[253,249,248,240],
    "e":[242,252,247,180,179,178],
    "f":[143,159,175],
    "g":[191,297,223],
    "h":[141,157,173],
    "i":[142,158,222,224,203,190],
    "j":[138,154,170],
    "k":[144,160,175],
    "l":[39,65],
    "m":[41,66],
    "n":[42,67],
    "o":[169,185,201,217,233,234],
    "p":[44,69],
    "r":[45,70],
    "s":[46,71],
    "t":[47,72],
    "u":[48,73],
    "w":[49,74],
    "x":[50,75],
    "y":[51,76],
    "z":[52,77],
    " ": [32]
}


def encrypt(string):
    encrypted = ""
    for char in string:
        if char == " ":
            encrypted += ''.join("  ")
        else:
            encrypted += ''.join(str(chr(alphabetDict[char][random.randint(0, 1)])))    
            encrypted += ''.join(" ")    
    return encrypted

def decrypt(string):
    pass

# print(alphabetDict["a"][2])
print(encrypt(string))